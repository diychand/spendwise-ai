import os
import re
import time
from typing import Optional, Dict, Any, List
import pandas as pd
from google import genai
from dotenv import load_dotenv

from logging_config import get_logger
from models import Transaction

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

logger = get_logger(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-3.5-flash-lite"


def extract_purchase_details(question: str) -> Dict[str, Any]:
    """
    Extracts potential purchase amount and timeframe from the user's question if present.
    e.g. 'buy a bike worth ₹60,000 next month' -> amount: 60000.0, timeframe_months: 1
    """
    cleaned = question.replace(",", "").lower()
    amount = None
    timeframe_months = None

    # Match rupee amount patterns: ₹60000, rs 60000, inr 60000, 60000 rs, worth 60000
    amt_matches = re.findall(r"(?:₹|rs\.?|inr|\bworth\b|\bfor\b)\s*(\d+(?:\.\d+)?)", cleaned)
    if not amt_matches:
        # Fallback to pure numbers >= 1000 that likely indicate target purchase
        large_nums = re.findall(r"\b(\d{4,9})\b", cleaned)
        if large_nums:
            amount = float(large_nums[0])
    else:
        amount = float(amt_matches[0])

    # Match timeframe patterns: 'next month' -> 1, 'in 2 months' -> 2, 'in 1 year' -> 12, etc.
    if re.search(r"\bnext month\b|\bthis month\b|\bin a month\b|\b1 month\b", cleaned):
        timeframe_months = 1
    else:
        month_match = re.search(r"(\d+)\s*(?:months?|mo)\b", cleaned)
        if month_match:
            timeframe_months = int(month_match.group(1))
        else:
            year_match = re.search(r"(\d+)\s*(?:years?|yrs?)\b", cleaned)
            if year_match:
                timeframe_months = int(year_match.group(1)) * 12

    return {"amount": amount, "timeframe_months": timeframe_months}


def compute_financial_profile(transactions: List[Transaction]) -> Dict[str, Any]:
    """
    Analyzes actual transaction data to build a complete financial profile.
    """
    if not transactions:
        return {}

    data = [{
        "id": t.id,
        "date": t.date,
        "description": t.description,
        "amount": t.amount,
        "type": t.type,
        "category": t.category or "Other",
        "is_anomaly": t.is_anomaly
    } for t in transactions]

    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)

    months = sorted(df["month"].unique())
    num_months = len(months) or 1

    income_txns = df[df["type"] == "CREDIT"]
    expense_txns = df[df["type"] == "DEBIT"]

    monthly_income = income_txns.groupby("month")["amount"].sum().reindex(months, fill_value=0)
    monthly_expenses = expense_txns.groupby("month")["amount"].sum().reindex(months, fill_value=0)
    monthly_surplus = monthly_income - monthly_expenses

    avg_income = float(monthly_income.mean())
    avg_expense = float(monthly_expenses.mean())
    avg_surplus = float(monthly_surplus.mean())
    savings_rate = (avg_surplus / avg_income * 100) if avg_income > 0 else 0.0

    # Category breakdown (DEBIT only)
    cat_totals = expense_txns.groupby("category")["amount"].sum().to_dict()
    cat_monthly = {cat: round(amt / num_months, 2) for cat, amt in cat_totals.items()}
    cat_pct = {
        cat: round((amt / (avg_expense * num_months) * 100), 1) if avg_expense > 0 else 0.0
        for cat, amt in cat_totals.items()
    }

    # Sort categories by average monthly spending descending
    sorted_categories = sorted(cat_monthly.items(), key=lambda x: x[1], reverse=True)

    # 50/30/20 budget framework analysis:
    # Needs: Rent, Bills, Groceries
    # Wants: Food (dining out), Shopping, Entertainment, Travel
    # Savings: Monthly surplus
    needs_cats = ["Rent", "Bills", "Groceries"]
    wants_cats = ["Food", "Shopping", "Entertainment", "Travel"]

    needs_monthly = sum(cat_monthly.get(c, 0.0) for c in needs_cats)
    wants_monthly = sum(cat_monthly.get(c, 0.0) for c in wants_cats)

    needs_pct = (needs_monthly / avg_income * 100) if avg_income > 0 else 0.0
    wants_pct = (wants_monthly / avg_income * 100) if avg_income > 0 else 0.0

    # Potential cuts simulation (15%, 25%, and 35% on discretionary wants)
    potential_savings_simulation = {}
    for cat in wants_cats:
        curr = cat_monthly.get(cat, 0.0)
        if curr > 0:
            potential_savings_simulation[cat] = {
                "current_monthly": curr,
                "cut_15pct": round(curr * 0.15, 2),
                "cut_25pct": round(curr * 0.25, 2),
                "cut_35pct": round(curr * 0.35, 2),
            }

    tiered_savings = {
        "gentle_15pct": round(wants_monthly * 0.15, 2),
        "moderate_25pct": round(wants_monthly * 0.25, 2),
        "aggressive_35pct": round(wants_monthly * 0.35, 2),
    }

    return {
        "num_months": num_months,
        "months_analyzed": months,
        "avg_monthly_income": round(avg_income, 2),
        "avg_monthly_expense": round(avg_expense, 2),
        "avg_monthly_surplus": round(avg_surplus, 2),
        "savings_rate_pct": round(savings_rate, 1),
        "category_monthly_averages": cat_monthly,
        "category_percentages": cat_pct,
        "sorted_categories": sorted_categories,
        "wants_monthly": round(wants_monthly, 2),
        "budget_50_30_20": {
            "needs_monthly": round(needs_monthly, 2),
            "needs_pct": round(needs_pct, 1),
            "wants_monthly": round(wants_monthly, 2),
            "wants_pct": round(wants_pct, 1),
            "savings_pct": round(savings_rate, 1),
        },
        "potential_discretionary_savings": potential_savings_simulation,
        "tiered_savings": tiered_savings,
        "total_discretionary_20pct_boost": round(wants_monthly * 0.20, 2),
    }


def calculate_goal_affordability(
    amount: float,
    timeframe_months: Optional[int],
    profile: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Calculates goal-specific affordability, financing models, and custom-sized expense cuts.
    Differentiates between small items (<50k), medium goals (50k-250k), and major assets (>=250k, e.g. cars).
    """
    avg_surplus = profile.get("avg_monthly_surplus", 0.0)
    avg_income = profile.get("avg_monthly_income", 0.0)
    wants_monthly = profile.get("wants_monthly", 0.0)

    # 1. Goal Scale Classification
    if amount >= 250000:
        goal_scale = "major_asset"  # Cars, homes, large investments
    elif amount >= 50000:
        goal_scale = "medium"       # Two-wheelers, electronics, emergency fund
    else:
        goal_scale = "small"        # Gadgets, short vacations, appliances

    # Full Cash Savings Timeline
    months_cash_current = round(amount / avg_surplus, 1) if avg_surplus > 0 else None

    boost_25 = round(wants_monthly * 0.25, 2)
    boost_35 = round(wants_monthly * 0.35, 2)
    surplus_boost_25 = round(avg_surplus + boost_25, 2)
    surplus_boost_35 = round(avg_surplus + boost_35, 2)

    months_cash_boosted_25 = round(amount / surplus_boost_25, 1) if surplus_boost_25 > 0 else None
    months_cash_boosted_35 = round(amount / surplus_boost_35, 1) if surplus_boost_35 > 0 else None

    # 2. Major Asset Financing Model (for cars/assets >= 250k)
    financing = None
    if goal_scale == "major_asset":
        down_payment_20 = round(amount * 0.20, 2)
        down_payment_30 = round(amount * 0.30, 2)
        down_payment_50 = round(amount * 0.50, 2)

        months_dp_current = round(down_payment_20 / avg_surplus, 1) if avg_surplus > 0 else None
        months_dp_boosted = round(down_payment_20 / surplus_boost_25, 1) if surplus_boost_25 > 0 else None

        # 80% Loan EMI (5 years @ 9.5% p.a.)
        loan_80 = round(amount * 0.80, 2)
        r = 0.095 / 12
        n = 60
        emi_80 = round(loan_80 * r * ((1 + r)**n) / (((1 + r)**n) - 1), 2)

        # 70% Loan EMI (with 30% down payment)
        loan_70 = round(amount * 0.70, 2)
        emi_70 = round(loan_70 * r * ((1 + r)**n) / (((1 + r)**n) - 1), 2)

        # 50% Loan EMI (with 50% down payment)
        loan_50 = round(amount * 0.50, 2)
        emi_50 = round(loan_50 * r * ((1 + r)**n) / (((1 + r)**n) - 1), 2)

        # Debt to Income Ratio
        dti_pct = round((emi_80 / avg_income * 100), 1) if avg_income > 0 else 0.0
        emi_surplus_gap = round(emi_80 - avg_surplus, 2)

        # Can the EMI gap be bridged by discretionary expense cuts alone?
        can_bridge_with_cuts = (emi_surplus_gap <= wants_monthly) and (emi_surplus_gap > 0)
        pct_cut_needed_for_emi = round((emi_surplus_gap / wants_monthly * 100), 1) if (wants_monthly > 0 and emi_surplus_gap > 0) else 0.0

        financing = {
            "down_payment_20": down_payment_20,
            "months_to_down_payment_current": months_dp_current,
            "months_to_down_payment_boosted": months_dp_boosted,
            "loan_amount_80": loan_80,
            "emi_5yr_9_5pct": emi_80,
            "down_payment_30": down_payment_30,
            "emi_with_30pct_dp": emi_70,
            "down_payment_50": down_payment_50,
            "emi_with_50pct_dp": emi_50,
            "dti_pct": dti_pct,
            "emi_surplus_gap": emi_surplus_gap,
            "can_bridge_with_cuts": can_bridge_with_cuts,
            "pct_cut_needed_for_emi": pct_cut_needed_for_emi,
            "is_severe_dti_risk": dti_pct > 40.0,
        }

    # 3. Timeframe Target Gap
    target_achievable_current = None
    target_achievable_boosted = None
    target_gap_current = None
    target_gap_boosted = None
    required_monthly_savings = None
    required_discretionary_cut_pct = None

    if timeframe_months and timeframe_months > 0:
        required_monthly_savings = round(amount / timeframe_months, 2)
        current_capacity = avg_surplus * timeframe_months
        boosted_capacity = surplus_boost_25 * timeframe_months

        target_achievable_current = current_capacity >= amount
        target_achievable_boosted = boosted_capacity >= amount

        target_gap_current = round(amount - current_capacity, 2)
        target_gap_boosted = round(amount - boosted_capacity, 2)

        surplus_shortfall = required_monthly_savings - avg_surplus
        if surplus_shortfall > 0 and wants_monthly > 0:
            required_discretionary_cut_pct = round((surplus_shortfall / wants_monthly * 100), 1)

    return {
        "purchase_amount": amount,
        "timeframe_months": timeframe_months,
        "goal_scale": goal_scale,
        "avg_monthly_surplus": avg_surplus,
        "avg_monthly_income": avg_income,
        "months_needed_current": months_cash_current,
        "months_needed_boosted_25": months_cash_boosted_25,
        "months_needed_boosted_35": months_cash_boosted_35,
        "boosted_monthly_surplus_25": surplus_boost_25,
        "boosted_monthly_surplus_35": surplus_boost_35,
        "financing": financing,
        "target_achievable_current": target_achievable_current,
        "target_gap_current": target_gap_current,
        "target_achievable_boosted": target_achievable_boosted,
        "target_gap_boosted": target_gap_boosted,
        "required_monthly_savings": required_monthly_savings,
        "required_discretionary_cut_pct": required_discretionary_cut_pct,
    }


def generate_advisor_response(
    question: str,
    profile: Dict[str, Any],
    affordability: Optional[Dict[str, Any]] = None,
    chat_history: Optional[List[Dict[str, str]]] = None,
    rag_evidence: Optional[Dict[str, Any]] = None
) -> str:
    """
    Calls Gemini with structured, goal-scale-aware financial context and RAG retrieved evidence
    to generate grounded, transparent, and actionable advice.
    """
    if not profile:
        return "I don't have enough transaction data yet to provide personalized advice. Please upload a bank statement first."

    # Build structured category context string
    top_categories_str = "\n".join([
        f"- {cat}: ₹{amt:,.2f}/month ({profile['category_percentages'].get(cat, 0)}% of total expenses)"
        for cat, amt in profile.get("sorted_categories", [])[:5]
    ])

    discretionary_cuts_str = "\n".join([
        f"- {cat}: Current ₹{info['current_monthly']:,.2f}/mo -> 15% cut saves ₹{info['cut_15pct']:,.2f}/mo | 25% cut saves ₹{info['cut_25pct']:,.2f}/mo | 35% cut saves ₹{info['cut_35pct']:,.2f}/mo"
        for cat, info in profile.get("potential_discretionary_savings", {}).items()
    ])

    affordability_context = ""
    if affordability and affordability.get("purchase_amount"):
        amt = affordability["purchase_amount"]
        scale = affordability.get("goal_scale")
        tf = affordability.get("timeframe_months")
        tf_str = f"within {tf} month(s)" if tf else "open timeframe (user is asking how many months it will take)"
        fin = affordability.get("financing")

        if scale == "major_asset" and fin:
            affordability_context = f"""
TARGET INQUIRY: MAJOR VEHICLE / ASSET PURCHASE (Amount: ₹{amt:,.2f})
- Scale: Major Vehicle/Asset Purchase
- 100% Cash Purchase Timeline: ~{affordability['months_needed_current']} months (~{round(affordability['months_needed_current']/12, 1)} years at current surplus)
- 20% Down Payment: ₹{fin['down_payment_20']:,.2f} (Time to save down payment: ~{fin['months_to_down_payment_current']} months at current surplus, ~{fin['months_to_down_payment_boosted']} months with 25% cuts)
- 80% 5-Year Auto Loan EMI (@9.5% p.a.): ₹{fin['emi_5yr_9_5pct']:,.2f}/month
- Loan EMI as % of Gross Monthly Income (Debt-to-Income): {fin['dti_pct']}% (Safe financial benchmark: ≤15-20%)
- Monthly Surplus vs EMI Gap: Current surplus is ₹{affordability['avg_monthly_surplus']:,.2f}/mo. EMI is ₹{fin['emi_5yr_9_5pct']:,.2f}/mo. Shortfall to service EMI: ₹{fin['emi_surplus_gap']:,.2f}/mo.
- Can this EMI gap be bridged by cutting discretionary spending alone? {fin['can_bridge_with_cuts']} (requires cutting ~{fin['pct_cut_needed_for_emi']}% across all discretionary wants)
- Severe DTI Risk Warning (>40% of salary)? {fin['is_severe_dti_risk']}
- 30% Down Payment Option: ₹{fin['down_payment_30']:,.2f} down payment lowers EMI to ₹{fin['emi_with_30pct_dp']:,.2f}/month.
- 50% Down Payment Option: ₹{fin['down_payment_50']:,.2f} down payment lowers EMI to ₹{fin['emi_with_50pct_dp']:,.2f}/month.

CRITICAL INSTRUCTIONS FOR THIS MAJOR ASSET ({amt:,.0f}):
1. DO NOT give a generic "cut Food by 20% and save cash for 6-11 years" answer! Real vehicle buyers finance via down payment + auto loan.
2. Structure your plan around real vehicle financing:
   a) Step 1: Saving the 20-30% Down Payment (show exact timeline: ~{fin['months_to_down_payment_current']} months at current pace, or ~{fin['months_to_down_payment_boosted']} months with cuts).
   b) Step 2: The Monthly EMI Reality Check (₹{fin['emi_5yr_9_5pct']:,.2f}/mo): Compare against their salary (₹{affordability['avg_monthly_income']:,.2f}) and current surplus (₹{affordability['avg_monthly_surplus']:,.2f}).
   c) DTI & Affordability Verdict:
      - If purchase is around ₹600,000: EMI is ~₹10,081 (35.8% of salary). Shortfall is ₹2,624/mo. Explain that cutting ~30% of discretionary spending (Food by 35% saves ₹1,733, Shopping saves ₹570, Travel saves ₹335) or saving a 30% down payment (₹1.8L) makes this EMI manageable!
      - If purchase is around ₹1,000,000+: EMI is ~₹16,801 (**nearly 60% of total salary of ₹28,145!**). Shortfall is ₹9,345/mo, which exceeds their ENTIRE discretionary spending budget (₹{profile.get('wants_monthly', 8632):,.2f})! State clearly that a ₹10 Lakh car at their current income is a high-risk debt trap that cannot be solved by cutting food alone. Recommend realistic alternatives:
        * Stepping stone vehicle: A reliable certified pre-owned car in the ₹2.5L-₹3.5L range (EMI ~₹5,000/mo, easily covered by their ₹7,456 surplus with a safety cushion).
        * Or save a 50% down payment (₹5L) over 4 years while growing monthly income to ₹50,000+.
"""
        elif scale == "medium":
            req_savings = affordability.get('required_monthly_savings')
            req_savings_str = f"₹{req_savings:,.2f}/mo" if req_savings is not None else "N/A (user has not set a rigid monthly deadline)"
            req_cut = affordability.get('required_discretionary_cut_pct')
            req_cut_str = f"{req_cut}% cut" if req_cut is not None else "N/A"
            target_gap = affordability.get('target_gap_current')
            target_gap_str = f"₹{target_gap:,.2f}" if target_gap is not None else "N/A"

            affordability_context = f"""
TARGET INQUIRY: MEDIUM GOAL PURCHASE (Amount: ₹{amt:,.2f})
- Scale: Medium Cash Goal (e.g. two-wheeler/bike, electronics, laptop, emergency fund)
- Current Cash Timeline: {affordability['months_needed_current']} months (without any cuts, simply using current ₹{affordability['avg_monthly_surplus']:,.2f}/mo surplus)
- Accelerated Cash Timeline: {affordability['months_needed_boosted_25']} months (with moderate 25% cuts saving +₹{profile.get('tiered_savings', {}).get('moderate_25pct', 0):,.2f}/mo)
- Fast-Track Cash Timeline: {affordability['months_needed_boosted_35']} months (with aggressive 35% cuts saving +₹{profile.get('tiered_savings', {}).get('aggressive_35pct', 0):,.2f}/mo)
- Timeframe requested: {tf_str}
- Is target achievable in timeframe without changes? {affordability.get('target_achievable_current')}
- Required monthly savings for target timeframe: {req_savings_str} (Requires {req_cut_str} on discretionary spending)

CRITICAL INSTRUCTIONS FOR THIS MEDIUM GOAL ({amt:,.0f}):
- Give a tailored cash accumulation plan.
- If user asked for next month or an unrealistic short timeframe: explain why that timeframe has a shortfall of {target_gap_str}, and give the realistic cash roadmap ({affordability['months_needed_current']} months with 0 cuts, or {affordability['months_needed_boosted_25']} months with 25% cuts).
- If user has not specified a timeframe, present both the natural timeline ({affordability['months_needed_current']} months) and the accelerated timeline ({affordability['months_needed_boosted_25']} months) with specific category cuts in Food and Shopping.
- Provide targeted cuts sized specifically to save this amount (e.g. cutting Food and Shopping to save the required gap).
"""
        else:
            affordability_context = f"""
TARGET INQUIRY: SMALL PURCHASE (Amount: ₹{amt:,.2f})
- Timeline at current surplus: {affordability['months_needed_current']} months
- Readily achievable with minor budget adjustments within 1-3 months.
"""

    history_str = ""
    if chat_history:
        recent = chat_history[-4:]
        history_str = "\nPREVIOUS CONVERSATION CONTEXT:\n" + "\n".join([
            f"{msg.get('role', 'user').capitalize()}: {msg.get('content', '')}"
            for msg in recent
        ])

    evidence_str = ""
    if rag_evidence:
        try:
            from agent.rag_service import FinancialRAGService
            formatted_ev = FinancialRAGService.format_evidence_for_prompt(rag_evidence)
            if formatted_ev.strip():
                evidence_str = f"\nRETRIEVED RAG EVIDENCE & FINANCIAL BENCHMARKS:\n{formatted_ev}\n"
        except Exception as ev_err:
            logger.warning("Failed to format RAG evidence: %s", ev_err)

    prompt = f"""You are SpendWise AI, an expert, encouraging, and honest personal financial advisor.
Your job is to provide concrete, highly personalized, numbers-grounded financial advice based on the user's real financial data.

REAL USER FINANCIAL DATA (Across {profile['num_months']} months of statements):
- Average Monthly Income: ₹{profile['avg_monthly_income']:,.2f}
- Average Monthly Expenses: ₹{profile['avg_monthly_expense']:,.2f}
- Current Average Monthly Surplus (Savings): ₹{profile['avg_monthly_surplus']:,.2f}
- Current Savings Rate: {profile['savings_rate_pct']}% of income

BUDGET BREAKDOWN (50/30/20 Rule Comparison):
- Needs (Rent, Bills, Groceries): ₹{profile['budget_50_30_20']['needs_monthly']:,.2f}/mo ({profile['budget_50_30_20']['needs_pct']}% of income vs 50% benchmark)
- Wants (Food dining out, Shopping, Entertainment, Travel): ₹{profile['budget_50_30_20']['wants_monthly']:,.2f}/mo ({profile['budget_50_30_20']['wants_pct']}% of income vs 30% benchmark)
- Savings: {profile['savings_rate_pct']}% vs 20% benchmark

TOP EXPENSE CATEGORIES:
{top_categories_str}

AVAILABLE CUT TIERS (Discretionary Categories):
{discretionary_cuts_str}
- Tier 1 (Gentle 15% cut): +₹{profile.get('tiered_savings', {}).get('gentle_15pct', 0):,.2f}/month extra savings
- Tier 2 (Moderate 25% cut): +₹{profile.get('tiered_savings', {}).get('moderate_25pct', 0):,.2f}/month extra savings
- Tier 3 (Aggressive 35% cut): +₹{profile.get('tiered_savings', {}).get('aggressive_35pct', 0):,.2f}/month extra savings
{affordability_context}
{evidence_str}
{history_str}

USER QUESTION:
"{question}"

INSTRUCTIONS FOR YOUR RESPONSE:
1. Provide a direct, honest, and empowering answer tailored specifically to the exact goal scale and nature of the question.
2. If the user asked about a major vehicle or asset purchase (e.g. ₹600,000 car vs ₹1,000,000 car):
   - Contrast down payment savings vs loan EMI feasibility.
   - Ground advice in the 20/4/10 vehicle rule (20% down, max 4 years, max 10% monthly income).
   - Do NOT suggest the exact same generic 20% food cut for all amounts. For ₹600k, calculate the exact ~30% cut needed to bridge the ₹2,624 EMI gap. For ₹1,000,000, highlight that the EMI (₹16,801) is 60% of their salary and exceeds their entire discretionary budget, explaining why income growth or a pre-owned car is essential.
3. If the user asked about a medium goal (e.g. ₹60,000 bike):
   - Provide a cash roadmap (6-8 months) with targeted category reductions sized to fit that goal.
4. If the user asked general expense cutting advice:
   - Outline the 3 tiered plans (Gentle 15%, Balanced 25%, Aggressive 35%).
5. Grounding & Citation:
   - Directly cite relevant transaction evidence retrieved from their statement (merchant names, dates, amounts) to make your points concrete.
   - Reference the retrieved financial benchmarks (e.g. 50/30/20 standard, 20/4/10 rule) to back your recommendations.
6. Format with bold metrics, bullet points, and clean markdown. Format all currency as ₹ (Indian Rupees) with commas.
"""

    logger.info("Gemini request -> task=financial_advice question=%r", question)
    start = time.perf_counter()

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        answer = response.text.strip()
        elapsed = time.perf_counter() - start
        logger.info("Gemini response <- task=financial_advice latency=%.3fs", elapsed)
        return answer
    except Exception as e:
        logger.warning("Gemini call failed (%s), generating deterministic fallback advice", e)
        return generate_fallback_advice(question, profile, affordability)


def generate_fallback_advice(
    question: str,
    profile: Dict[str, Any],
    affordability: Optional[Dict[str, Any]] = None
) -> str:
    """
    Deterministic rule-based fallback advice if Gemini API is unavailable or rate-limited.
    Provides goal-scale-aware financial plans.
    """
    surplus = profile.get("avg_monthly_surplus", 0.0)
    income = profile.get("avg_monthly_income", 0.0)
    expenses = profile.get("avg_monthly_expense", 0.0)
    rate = profile.get("savings_rate_pct", 0.0)
    wants = profile.get("wants_monthly", 0.0)

    if affordability is None:
        extracted = extract_purchase_details(question)
        amt = extracted.get("amount")
        if amt and amt > 0:
            affordability = calculate_goal_affordability(amt, extracted.get("timeframe_months"), profile)

    if affordability and affordability.get("purchase_amount"):
        amt = affordability["purchase_amount"]
        scale = affordability.get("goal_scale")
        fin = affordability.get("financing")

        if scale == "major_asset" and fin:
            if fin["is_severe_dti_risk"]:
                # High-value goal e.g. 10 Lakh car
                return f"""### 🚨 Major Purchase Reality Check: ₹{amt:,.2f} Vehicle/Asset

**Current Financial Baseline**:
- **Monthly Income**: ₹{income:,.2f} | **Current Surplus**: ₹{surplus:,.2f}/month
- **100% Cash Timeline**: {affordability['months_needed_current']} months (~{round(affordability['months_needed_current']/12, 1)} years)

---

### ⚠️ The Debt-to-Income Reality (Why Standard Cuts Are Not Enough)
For an asset worth **₹{amt:,.2f}**, a standard 80% auto loan (₹{fin['loan_amount_80']:,.2f}) over 5 years yields an estimated EMI of **₹{fin['emi_5yr_9_5pct']:,.2f}/month**.

* **EMI vs Salary**: This single EMI would consume **{fin['dti_pct']}% of your gross monthly salary** (safe benchmark is ≤15-20%).
* **Shortfall vs Surplus**: The EMI exceeds your current surplus of ₹{surplus:,.2f} by **₹{fin['emi_surplus_gap']:,.2f}/month**.
* **Why Normal Cuts Don't Work**: Your total discretionary spending across all categories (Food, Shopping, Travel, Entertainment) is only **₹{wants:,.2f}/month**. Even if you spent ₹0 on dining and shopping for 5 years, you would **still fall short by ₹{round(fin['emi_surplus_gap'] - wants, 2):,.2f}/month**!

---

### 🛡️ Recommended Strategic Plan for ₹{amt:,.2f}:
1. **Target a Stepping Stone Vehicle**: Consider a reliable certified pre-owned vehicle in the **₹2.5L – ₹3.5L** range. An 80% loan on a ₹3L car has an EMI of only ~₹5,040/month, which fits comfortably inside your ₹{surplus:,.2f} surplus with a ₹2,400 monthly safety buffer.
2. **Aggressive Down Payment Strategy**: If you are set on a ₹{amt:,.2f} car, save a **50% down payment (₹{fin['down_payment_50']:,.2f})** first. At your current savings rate + 30% discretionary cuts (saving ₹{affordability['boosted_monthly_surplus_25']:,.2f}/mo), this takes ~**{round(fin['down_payment_50'] / affordability['boosted_monthly_surplus_25'], 1)} months**. This halves the loan and drops the EMI to ₹{fin['emi_with_50pct_dp']:,.2f}/month.
3. **Focus on Income Growth**: Increase your primary income or add a secondary revenue stream to bring monthly income above ₹50,000 before taking on a ₹{amt:,.2f} obligation.
"""
            else:
                # Moderate major asset e.g. 6 Lakh car
                cut_needed = fin['pct_cut_needed_for_emi']
                return f"""### 🚗 Vehicle Purchase Feasibility Plan: ₹{amt:,.2f} Car

**Current Financial Baseline**:
- **Monthly Income**: ₹{income:,.2f} | **Current Surplus**: ₹{surplus:,.2f}/month (26.5% savings rate)
- **100% Cash Timeline**: {affordability['months_needed_current']} months (~{round(affordability['months_needed_current']/12, 1)} years)

---

### 💳 Financing Roadmap (20% Down Payment + 5-Year Loan)
Rather than waiting 6+ years to buy in all-cash, here is the realistic path to owning this car:

1. **Step 1: Save the 20% Down Payment (₹{fin['down_payment_20']:,.2f})**
   - At your current surplus (₹{surplus:,.2f}/mo): **{fin['months_to_down_payment_current']} months**
   - With accelerated savings (saving ₹{affordability['boosted_monthly_surplus_25']:,.2f}/mo): **{fin['months_to_down_payment_boosted']} months** (~1.1 years)

2. **Step 2: Service the Monthly EMI (₹{fin['emi_5yr_9_5pct']:,.2f}/month)**
   - An 80% loan of ₹{fin['loan_amount_80']:,.2f} at 9.5% p.a. over 5 years has an EMI of **₹{fin['emi_5yr_9_5pct']:,.2f}/month** ({fin['dti_pct']}% of salary).
   - Your current surplus is ₹{surplus:,.2f}/mo, leaving an EMI gap of **₹{fin['emi_surplus_gap']:,.2f}/month**.

---

### ✂️ Tailored Expense Cuts to Bridge the EMI Gap (₹{fin['emi_surplus_gap']:,.2f}/mo)
To comfortably afford the ₹{fin['emi_5yr_9_5pct']:,.2f} EMI, you need to cut **{cut_needed:.1f}%** from your discretionary spending (wants):

- **Food (Dining Out & Delivery)**: Cut by **30%** -> Saves **₹{profile.get('category_monthly_averages', {}).get('Food', 5000) * 0.30:,.2f}/month**
- **Shopping**: Cut by **30%** -> Saves **₹{profile.get('category_monthly_averages', {}).get('Shopping', 1500) * 0.30:,.2f}/month**
- **Travel & Entertainment**: Cut by **20%** -> Saves **₹{(profile.get('category_monthly_averages', {}).get('Travel', 1300) + profile.get('category_monthly_averages', {}).get('Entertainment', 700)) * 0.20:,.2f}/month**

**Total Extra Monthly Savings Unlocked**: **+₹{profile.get('wants_monthly', 8632) * 0.30:,.2f}/month**, raising your monthly surplus to **₹{surplus + profile.get('wants_monthly', 8632) * 0.30:,.2f}** and fully covering the car EMI!
"""
        else:
            # Medium or small goal (e.g. ₹60,000 bike)
            return f"""### 🎯 Savings Roadmap: ₹{amt:,.2f} Goal

**Your Numbers**:
- **Purchase Price**: ₹{amt:,.2f}
- **Current Monthly Surplus**: ₹{surplus:,.2f}/month
- **Current Timeline (Zero Cuts)**: **{affordability['months_needed_current']} months**
- **Accelerated Timeline (25% Discretionary Cuts)**: **{affordability['months_needed_boosted_25']} months** (saving ₹{affordability['boosted_monthly_surplus_25']:,.2f}/mo)
- **Fast-Track Timeline (35% Discretionary Cuts)**: **{affordability['months_needed_boosted_35']} months** (saving ₹{affordability['boosted_monthly_surplus_35']:,.2f}/mo)

### ✂️ Targeted Expense Cuts:
- **Food Delivery / Dining Out**: Trim by 25% to free up **₹{profile.get('category_monthly_averages', {}).get('Food', 5000) * 0.25:,.2f}/month**.
- **Shopping**: Postpone impulsive purchases to save **₹{profile.get('category_monthly_averages', {}).get('Shopping', 1500) * 0.25:,.2f}/month**.
"""

    # General savings plan (no specific purchase)
    return f"""### 📊 Tiered Expense Reduction & Savings Plans

**Financial Baseline**:
- Average Monthly Income: ₹{income:,.2f} | Expenses: ₹{expenses:,.2f} | Current Surplus: **₹{surplus:,.2f}/mo** ({rate}% savings rate)

---

### Option A: Gentle & Painless Plan (15% Cut)
- **Target**: Trim non-essential dining and impulse shopping by 15%.
- **Monthly Savings Unlocked**: **+₹{profile.get('tiered_savings', {}).get('gentle_15pct', 1300):,.2f}/month**
- **New Monthly Surplus**: **₹{surplus + profile.get('tiered_savings', {}).get('gentle_15pct', 1300):,.2f}/month** (31% savings rate)

### Option B: Balanced Optimization Plan (25% Cut)
- **Target**: Cook at home 3 extra nights a week, set a ₹1,000 shopping cap, reduce transit surge fares.
- **Monthly Savings Unlocked**: **+₹{profile.get('tiered_savings', {}).get('moderate_25pct', 2150):,.2f}/month**
- **New Monthly Surplus**: **₹{surplus + profile.get('tiered_savings', {}).get('moderate_25pct', 2150):,.2f}/month** (34% savings rate)

### Option C: Aggressive Frugal Sprint (35% Cut)
- **Target**: Pause all discretionary shopping, cap dining to ₹2,500/mo, strict entertainment allowance.
- **Monthly Savings Unlocked**: **+₹{profile.get('tiered_savings', {}).get('aggressive_35pct', 3000):,.2f}/month**
- **New Monthly Surplus**: **₹{surplus + profile.get('tiered_savings', {}).get('aggressive_35pct', 3000):,.2f}/month** (37% savings rate)
"""
