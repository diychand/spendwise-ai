import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SpendWise AI", page_icon="💰", layout="wide")

BACKEND_URL = "http://127.0.0.1:8000"

# ---------- Global styling: hide Streamlit chrome, clean landing look ----------
st.markdown(
    """
    <style>
    #MainMenu, footer, .stDeployButton,
    [data-testid="stToolbar"], [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
    }
    header[data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding-top: 2.5rem !important; }

    .hero {
        text-align: center;
        margin: 9vh 0 1.5rem 0;
    }
    .hero .hero-emoji { font-size: 56px; line-height: 1; margin-bottom: 8px; }
    .hero h1 {
        font-size: 3rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin: 0 0 6px 0;
        padding: 0;
    }
    .hero p { color: #7a756d; font-size: 1.1rem; margin: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)


def safe_get(endpoint, params=None):
    """GET request with basic error handling so a backend hiccup doesn't crash the app."""
    try:
        response = requests.get(f"{BACKEND_URL}{endpoint}", params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        st.warning(f"Couldn't load data from {endpoint} (status {response.status_code}).")
        return None
    except requests.exceptions.RequestException:
        st.error("Couldn't reach the server. Please try again in a moment.")
        return None


def clear_cached_views():
    for key in list(st.session_state.keys()):
        if (
            key.startswith("cat_data_")
            or key.startswith("flash_msg_")
            or key.startswith("corr_")
            or key == "advice_chat_history"
        ):
            del st.session_state[key]


# ---------- Session state setup ----------
if "data_ready" not in st.session_state:
    st.session_state["data_ready"] = False

# ===================== LANDING PAGE =====================
if not st.session_state["data_ready"]:
    _, mid, _ = st.columns([1, 2, 1])

    with mid:
        st.markdown(
            """
            <div class="hero">
                <div class="hero-emoji">💰</div>
                <h1>SpendWise AI</h1>
                <p>Your personal finance assistant</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        uploaded_file = st.file_uploader(
            "Upload your bank statement (CSV)",
            type="csv",
            label_visibility="collapsed",
            help=(
                "Accepted formats: (A) Date, Description, Amount, Type  or  "
                "(B) Date, Narration, Withdrawal (Debit), Deposit (Credit). "
                "Common header names like Txn Date, Particulars and Dr/Cr are detected automatically."
            ),
        )

        if uploaded_file is not None:
            if st.button("Continue", type="primary", use_container_width=True):
                try:
                    with st.spinner("Preparing your dashboard..."):
                        files = {"file": (uploaded_file.name, uploaded_file, "text/csv")}
                        upload_response = requests.post(
                            f"{BACKEND_URL}/transactions/upload", files=files, timeout=30
                        )

                        upload_ok = upload_response.status_code == 200

                        if upload_ok:
                            requests.post(f"{BACKEND_URL}/categorize/rules", timeout=30)
                            requests.post(f"{BACKEND_URL}/categorize/train-ml", timeout=60)
                            ml_res = requests.post(f"{BACKEND_URL}/categorize/ml", timeout=30)

                            uncat_remaining = True
                            try:
                                ml_data = ml_res.json()
                                uncat_remaining = (
                                    ml_data.get("still_uncategorized", 1) > 0 or "error" in ml_data
                                )
                            except Exception:
                                uncat_remaining = True

                            if uncat_remaining:
                                requests.post(f"{BACKEND_URL}/categorize/llm", timeout=60)

                            requests.post(f"{BACKEND_URL}/anomaly/detect", timeout=30)

                    if not upload_ok:
                        error_msg = "We couldn't read that file."
                        missing_fields = []
                        detected_headers = []
                        tip = ""

                        try:
                            err_data = upload_response.json()
                            detail = err_data.get("detail", {})
                            if isinstance(detail, dict):
                                error_msg = detail.get("message") or detail.get("error") or error_msg
                                missing_fields = detail.get("missing_required_fields", [])
                                detected_headers = detail.get("detected_headers", [])
                                tip = detail.get("suggestion", "")
                            elif isinstance(detail, str):
                                error_msg = detail
                        except Exception:
                            error_msg = upload_response.text or f"HTTP {upload_response.status_code} Error"

                        st.error(f"❌ {error_msg}")

                        if missing_fields:
                            st.markdown("**Required columns missing:**")
                            for mf in missing_fields:
                                st.markdown(f"- ⚠️ **{mf}**")

                        if detected_headers:
                            st.markdown(f"**Columns found in your file ({len(detected_headers)}):**")
                            st.code(", ".join(f"'{h}'" for h in detected_headers), language="text")

                        if tip:
                            st.info(f"💡 {tip}")

                        st.stop()

                except requests.exceptions.RequestException:
                    st.error("❌ Couldn't connect to the server. Please try again in a moment.")
                    st.stop()

                clear_cached_views()
                st.session_state["data_ready"] = True
                st.rerun()

    st.stop()  # Nothing below is shown until data is ready

# ---------- Fetch data once ----------
transactions = safe_get("/transactions/") or []
df = pd.DataFrame(transactions)

REQUIRED_COLUMNS = {"id", "date", "description", "amount", "category", "type", "is_anomaly"}
data_ok = (not df.empty) and REQUIRED_COLUMNS.issubset(df.columns)

# Baseline numbers used by the sidebar and the chat tab
avg_inc = avg_exp = avg_surp = s_rate = 0.0
if data_ok:
    _debit = df[df["type"] == "DEBIT"]
    _credit = df[df["type"] == "CREDIT"]
    months_count = len(df["date"].str[:7].unique()) or 1
    avg_inc = _credit["amount"].sum() / months_count
    avg_exp = _debit["amount"].sum() / months_count
    avg_surp = avg_inc - avg_exp
    s_rate = (avg_surp / avg_inc * 100) if avg_inc > 0 else 0

# ---------- Sidebar ----------
with st.sidebar:
    st.header("💰 SpendWise AI")
    st.write("Your finances, understood.")

    if data_ok:
        st.divider()
        st.caption(f"💰 **Monthly surplus**: ₹{avg_surp:,.0f}")
        st.caption(f"📈 **Savings rate**: {s_rate:.1f}%")
        st.divider()

    if st.button("Upload a different statement", use_container_width=True):
        clear_cached_views()
        st.session_state["data_ready"] = False
        st.rerun()

# ---------- Tabs ----------
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "💳 Transactions",
    "💬 AI Financial Chat",
    "🎯 Can I afford it?"
])

# ===================== TAB 1: OVERVIEW =====================
with tab1:
    if data_ok:
        debit_df = df[df["type"] == "DEBIT"]
        credit_df = df[df["type"] == "CREDIT"]

        total_spent = debit_df["amount"].sum()
        total_income = credit_df["amount"].sum()
        anomaly_count = int(df["is_anomaly"].sum())

        # ---- Row 1: key numbers ----
        k1, k2, k3, k4 = st.columns(4)
        with k1.container(border=True):
            st.metric("Total spent", f"₹{total_spent:,.0f}")
        with k2.container(border=True):
            st.metric("Total income", f"₹{total_income:,.0f}")
        with k3.container(border=True):
            st.metric("Net balance", f"₹{total_income - total_spent:,.0f}")
        with k4.container(border=True):
            st.metric("Unusual transactions", anomaly_count)

        # ---- Row 2: two equal charts side by side ----
        left, right = st.columns(2, gap="medium")

        with left:
            with st.container(border=True):
                st.subheader("Spending by category")
                category_totals = debit_df.groupby("category")["amount"].sum().reset_index()
                fig_pie = px.pie(category_totals, names="category", values="amount", hole=0.45)
                fig_pie.update_traces(textposition="inside", textinfo="percent")
                fig_pie.update_layout(
                    height=380,
                    margin=dict(t=10, b=10, l=10, r=10),
                    legend=dict(orientation="h", yanchor="top", y=-0.02, xanchor="center", x=0.5),
                )
                st.plotly_chart(fig_pie, use_container_width=True)

        with right:
            with st.container(border=True):
                st.subheader("Spending over time")
                trend_data = safe_get("/analysis/monthly-trend")
                if trend_data:
                    trend_df = pd.DataFrame(trend_data)
                    fig_line = px.line(trend_df, x="month", y="amount", markers=True)
                    fig_line.update_layout(
                        height=380,
                        margin=dict(t=10, b=10, l=10, r=10),
                        yaxis_title="Amount (₹)",
                        xaxis_title=None,
                    )
                    st.plotly_chart(fig_line, use_container_width=True)
                else:
                    st.info("Not enough data to show a trend yet.")

        # ---- Row 3: full-width monthly category chart ----
        category_data = safe_get("/analysis/monthly-category")
        if category_data:
            cat_df = pd.DataFrame(category_data)

            with st.container(border=True):
                st.subheader("Spending by category, month over month")
                fig_bar = px.bar(cat_df, x="month", y="amount", color="category", barmode="stack")
                fig_bar.update_layout(
                    height=420,
                    margin=dict(t=10, b=10, l=10, r=10),
                    yaxis_title="Amount (₹)",
                    xaxis_title=None,
                    legend_title_text="",
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
                )
                st.plotly_chart(fig_bar, use_container_width=True)

            # ---- Row 4: month picker on the left, table on the right ----
            with st.container(border=True):
                st.subheader("Category breakdown by month")
                available_months = sorted(cat_df["month"].unique(), reverse=True)

                pick_col, table_col = st.columns([1, 2], gap="large")
                with pick_col:
                    selected_month = st.selectbox("Select month", available_months, key="overview_month")
                    summary = safe_get("/analysis/category-summary", params={"month": selected_month})
                    if summary:
                        st.metric(f"Total spent in {selected_month}", f"₹{summary['total_spent']:,.0f}")

                with table_col:
                    if summary:
                        summary_df = pd.DataFrame(summary["categories"])
                        summary_df.columns = ["Category", "Amount (₹)"]
                        st.dataframe(summary_df, use_container_width=True, hide_index=True)

        # ---- Row 5: flagged transactions ----
        if anomaly_count > 0:
            flagged = safe_get("/anomaly/flagged")
            if flagged:
                with st.container(border=True):
                    st.subheader("⚠️ Transactions worth a look")
                    flagged_df = pd.DataFrame(flagged)[["date", "description", "amount", "category"]]
                    flagged_df.columns = ["Date", "Description", "Amount", "Category"]
                    st.dataframe(flagged_df, use_container_width=True, hide_index=True)
    else:
        st.info("No transaction data available.")


# ===================== TAB 2: TRANSACTIONS =====================
@st.fragment
def render_category_section(month: str, category_name: str, initial_data: dict, all_categories: list):
    cache_key = f"cat_data_{month}_{category_name}"
    flash_key = f"flash_msg_{month}_{category_name}"

    if cache_key not in st.session_state:
        st.session_state[cache_key] = initial_data

    current_data = st.session_state[cache_key]
    subtotal = current_data.get("subtotal", 0.0)
    txns = current_data.get("transactions", [])

    st.markdown(f"#### 🏷️ **{category_name}** — ₹{subtotal:,.2f}  *({len(txns)} transactions)*")

    if flash_key in st.session_state:
        st.success(st.session_state.pop(flash_key))

    if txns:
        df_cat = pd.DataFrame([
            {
                "ID": t["id"],
                "Date": t["date"],
                "Description": t["description"],
                "Amount": f"₹{t['amount']:,.2f}",
                "Category": t["category"],
            }
            for t in txns
        ])
        st.dataframe(df_cat, use_container_width=True, hide_index=True)

        txn_options = {
            f"#{t['id']} | {t['date']} | {t['description']} — ₹{t['amount']:,.2f}": t["id"]
            for t in txns
        }

        col1, col2, col3 = st.columns([5, 3, 2], vertical_alignment="bottom")
        with col1:
            selected_label = st.selectbox(
                f"Pick transaction from {category_name}",
                options=list(txn_options.keys()),
                key=f"corr_txn_{month}_{category_name}",
            )
            selected_id = txn_options[selected_label]
        with col2:
            cat_choices = [c for c in all_categories if c != category_name] + [category_name]
            new_category = st.selectbox(
                f"Correct category for #{selected_id}",
                options=cat_choices,
                key=f"corr_cat_{month}_{category_name}",
            )
        with col3:
            if st.button("Save Correction", key=f"corr_btn_{month}_{category_name}", type="primary", use_container_width=True):
                try:
                    res = requests.patch(
                        f"{BACKEND_URL}/transactions/{selected_id}/correct",
                        json={"category": new_category},
                        timeout=10,
                    )
                    if res.status_code == 200:
                        refetched = safe_get(
                            "/analysis/monthly-breakdown",
                            params={"month": month, "category": category_name, "type": "DEBIT"},
                        )
                        if refetched and len(refetched) > 0:
                            st.session_state[cache_key] = refetched[0]
                        else:
                            st.session_state[cache_key] = {"category": category_name, "subtotal": 0.0, "transactions": []}

                        target_key = f"cat_data_{month}_{new_category}"
                        if target_key in st.session_state:
                            del st.session_state[target_key]

                        st.session_state[flash_key] = f"✅ Transaction #{selected_id} moved to '{new_category}'."
                        st.rerun(scope="fragment")
                    else:
                        st.error(f"Couldn't save the change (status {res.status_code}).")
                except requests.exceptions.RequestException:
                    st.error("Couldn't connect to the server.")
    else:
        st.info(f"No transactions in {category_name} for {month}.")

    st.divider()


with tab2:
    st.subheader("Monthly Spending by Category")
    st.caption("Browse transactions grouped by category for any month and fix any that look wrong.")

    if data_ok:
        backend_months = safe_get("/analysis/months")
        if backend_months and isinstance(backend_months, list):
            available_months = backend_months
        else:
            available_months = sorted(df["date"].str[:7].unique(), reverse=True)

        if not available_months:
            st.info("No transaction months available.")
        else:
            col_m1, col_m2, col_m3 = st.columns([3, 3, 2], vertical_alignment="bottom")
            with col_m1:
                selected_month = st.selectbox("Select month", available_months, key="selected_breakdown_month")

            breakdown_data = safe_get("/analysis/monthly-breakdown", params={"month": selected_month, "type": "DEBIT"})
            if breakdown_data is None:
                breakdown_data = []

            total_month_spent = sum(g.get("subtotal", 0.0) for g in breakdown_data)

            with col_m2:
                st.metric(f"Total spent in {selected_month}", f"₹{total_month_spent:,.2f}")

            with col_m3:
                if st.button("🔄 Refresh Month", use_container_width=True):
                    for k in list(st.session_state.keys()):
                        if k.startswith(f"cat_data_{selected_month}_") or k.startswith(f"flash_msg_{selected_month}_"):
                            del st.session_state[k]
                    st.rerun()

            st.divider()

            standard_cats = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Groceries", "Salary", "Rent", "Other"]
            existing_cats = [c for c in df["category"].dropna().unique().tolist() if c]
            all_categories = sorted(list(set(standard_cats + existing_cats)))

            if breakdown_data:
                for group in breakdown_data:
                    render_category_section(
                        month=selected_month,
                        category_name=group["category"],
                        initial_data=group,
                        all_categories=all_categories,
                    )
            else:
                st.info(f"No spending found for {selected_month}.")

            with st.expander("📋 View all transactions", expanded=False):
                filter_col1, filter_col2 = st.columns(2)
                with filter_col1:
                    categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
                    selected_category = st.selectbox("Filter by category", categories, key="flat_filter_cat")
                with filter_col2:
                    selected_type = st.selectbox("Filter by type", ["All", "DEBIT", "CREDIT"], key="flat_filter_type")

                filtered_df = df.copy()
                if selected_category != "All":
                    filtered_df = filtered_df[filtered_df["category"] == selected_category]
                if selected_type != "All":
                    filtered_df = filtered_df[filtered_df["type"] == selected_type]

                display_df = filtered_df[["date", "description", "amount", "category", "type"]].copy()
                display_df.columns = ["Date", "Description", "Amount", "Category", "Type"]
                st.dataframe(display_df, use_container_width=True, hide_index=True)
    else:
        st.info("No transactions to show.")


# ===================== TAB 3: AI FINANCIAL CHAT =====================
def trigger_autoscroll():
    components.html(
        """
        <script>
        function scrollChat() {
            try {
                const el = window.parent.document.getElementById('chat-bottom-anchor');
                if (el) {
                    el.scrollIntoView({ behavior: 'smooth', block: 'end' });
                } else {
                    const main = window.parent.document.querySelector('section.main');
                    if (main) {
                        main.scrollTo({ top: main.scrollHeight, behavior: 'smooth' });
                    }
                }
            } catch(e) {}
        }
        setTimeout(scrollChat, 60);
        setTimeout(scrollChat, 260);
        </script>
        """,
        height=0,
        width=0,
    )


def render_sources(evidence):
    """Compact 'Sources' dropdown under an answer."""
    if not evidence:
        return
    txns = evidence.get("transactions", [])
    guidelines = evidence.get("guidelines", [])
    if not txns and not guidelines:
        return
    with st.expander(f"Sources ({len(txns) + len(guidelines)})", expanded=False):
        if guidelines:
            st.markdown("**Benchmarks used:**")
            for g in guidelines:
                st.markdown(f"* **{g['title']}** — {g['summary']}")
        if txns:
            st.markdown("**From your statement:**")
            for t in txns:
                st.markdown(f"* `{t['date']}` **₹{t['amount']:,.2f}** ({t['category']}) — *{t['description']}*")


with tab3:
    st.markdown("""
    <style>
    div[data-testid="stChatMessage"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0.75rem 0.25rem !important;
        max-width: 820px !important;
        margin: 0 auto !important;
    }

    div[data-testid="stTabContent"]:nth-of-type(3) div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #EBE7DF !important;
        border-radius: 16px !important;
        background-color: #FAF9F5 !important;
        padding: 14px 18px !important;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.02) !important;
    }

    /* User message */
    div[data-testid="stChatMessage"]:has([aria-label="Chat message from user"]),
    div[data-testid="stChatMessage"]:has([data-testid*="AvatarUser"]) {
        flex-direction: row-reverse !important;
        justify-content: flex-start !important;
        padding-top: 0.4rem !important;
        padding-bottom: 0.4rem !important;
        max-width: 820px !important;
        margin: 0 auto !important;
    }
    div[data-testid="stChatMessage"]:has([aria-label="Chat message from user"]) [data-testid="stChatMessageContent"],
    div[data-testid="stChatMessage"]:has([data-testid*="AvatarUser"]) [data-testid="stChatMessageContent"] {
        background-color: #F0EFEA !important;
        color: #1F1E1D !important;
        border-radius: 18px 18px 4px 18px !important;
        padding: 11px 18px !important;
        margin-left: auto !important;
        margin-right: 0 !important;
        max-width: 78% !important;
        border: 1px solid rgba(0, 0, 0, 0.04) !important;
        box-shadow: none !important;
        line-height: 1.6 !important;
        font-size: 15px !important;
        text-align: left !important;
    }
    div[data-testid="stChatMessage"]:has([aria-label="Chat message from user"]) [data-testid^="stChatMessageAvatar"],
    div[data-testid="stChatMessage"]:has([data-testid*="AvatarUser"]) [data-testid^="stChatMessageAvatar"] {
        margin-left: 10px !important;
        margin-right: 0 !important;
        background-color: #E6E3DB !important;
        border: 1px solid #DCD8CF !important;
        color: #4D4A45 !important;
        border-radius: 50% !important;
        width: 30px !important;
        height: 30px !important;
        min-width: 30px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 13px !important;
        font-weight: 600 !important;
    }

    /* Assistant message */
    div[data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]),
    div[data-testid="stChatMessage"]:has([data-testid*="AvatarAssistant"]) {
        background: transparent !important;
        padding-top: 0.6rem !important;
        padding-bottom: 0.6rem !important;
        max-width: 820px !important;
        margin: 0 auto !important;
    }
    div[data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) [data-testid="stChatMessageContent"],
    div[data-testid="stChatMessage"]:has([data-testid*="AvatarAssistant"]) [data-testid="stChatMessageContent"] {
        background: transparent !important;
        color: #1F1E1D !important;
        padding: 2px 4px !important;
        max-width: 100% !important;
        border: none !important;
        box-shadow: none !important;
        line-height: 1.72 !important;
        font-size: 15.5px !important;
    }
    div[data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) [data-testid^="stChatMessageAvatar"],
    div[data-testid="stChatMessage"]:has([data-testid*="AvatarAssistant"]) [data-testid^="stChatMessageAvatar"] {
        margin-right: 14px !important;
        background-color: #FAF0EB !important;
        border: 1px solid #F3DDD3 !important;
        color: #CC785C !important;
        border-radius: 8px !important;
        width: 30px !important;
        height: 30px !important;
        min-width: 30px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 14px !important;
        font-weight: 700 !important;
    }
    div[data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) [data-testid^="stChatMessageAvatar"] span,
    div[data-testid="stChatMessage"]:has([data-testid*="AvatarAssistant"]) [data-testid^="stChatMessageAvatar"] span {
        font-size: 0 !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    div[data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) [data-testid^="stChatMessageAvatar"] span::after,
    div[data-testid="stChatMessage"]:has([data-testid*="AvatarAssistant"]) [data-testid^="stChatMessageAvatar"] span::after {
        content: "✦" !important;
        font-size: 15px !important;
        color: #CC785C !important;
        font-weight: 700 !important;
    }

    /* Typography */
    [data-testid="stChatMessageContent"] p {
        margin-bottom: 0.85rem !important;
        line-height: 1.72 !important;
        color: #242220 !important;
    }
    [data-testid="stChatMessageContent"] h1,
    [data-testid="stChatMessageContent"] h2,
    [data-testid="stChatMessageContent"] h3,
    [data-testid="stChatMessageContent"] h4 {
        color: #171615 !important;
        font-weight: 600 !important;
        margin-top: 1.25rem !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.01em !important;
    }
    [data-testid="stChatMessageContent"] h3 {
        font-size: 1.15rem !important;
        border-bottom: 1px solid #ECE9E2 !important;
        padding-bottom: 0.3rem !important;
    }
    [data-testid="stChatMessageContent"] ul,
    [data-testid="stChatMessageContent"] ol {
        margin-left: 1.25rem !important;
        margin-bottom: 0.85rem !important;
        line-height: 1.7 !important;
    }
    [data-testid="stChatMessageContent"] li {
        margin-bottom: 0.3rem !important;
        color: #2B2927 !important;
    }
    [data-testid="stChatMessageContent"] strong {
        color: #141312 !important;
        font-weight: 600 !important;
    }
    [data-testid="stChatMessageContent"] hr {
        border: none !important;
        border-top: 1px solid #ECE9E2 !important;
        margin: 1.1rem 0 !important;
    }
    [data-testid="stChatMessageContent"] blockquote {
        border-left: 3px solid #CC785C !important;
        background: #FAF8F5 !important;
        padding: 8px 14px !important;
        margin: 0.8rem 0 !important;
        border-radius: 0 6px 6px 0 !important;
        color: #55524E !important;
    }

    /* Input bar */
    div[data-testid="stTabContent"]:nth-of-type(3) div[data-testid="stChatInput"] {
        position: sticky !important;
        bottom: 0 !important;
        z-index: 100 !important;
        margin-top: 8px !important;
        border-radius: 24px !important;
        border: 1px solid #D8D4CC !important;
        background: #FFFFFF !important;
        box-shadow: 0 2px 14px rgba(0, 0, 0, 0.05) !important;
        padding: 3px 8px !important;
        transition: all 0.2s ease !important;
    }
    div[data-testid="stTabContent"]:nth-of-type(3) div[data-testid="stChatInput"]:focus-within {
        border-color: #CC785C !important;
        box-shadow: 0 0 0 3px rgba(204, 120, 92, 0.15), 0 4px 16px rgba(0, 0, 0, 0.06) !important;
    }
    div[data-testid="stTabContent"]:nth-of-type(3) [data-testid="stChatInput"] textarea {
        color: #1F1E1D !important;
        font-size: 15px !important;
        line-height: 1.5 !important;
    }
    div[data-testid="stTabContent"]:nth-of-type(3) [data-testid="stChatInput"] textarea::placeholder {
        color: #8C877E !important;
    }
    div[data-testid="stTabContent"]:nth-of-type(3) [data-testid="stChatInputSubmitButton"] button {
        background-color: #CC785C !important;
        color: #FFFFFF !important;
        border-radius: 50% !important;
        border: none !important;
        width: 32px !important;
        height: 32px !important;
        min-height: 32px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: transform 0.15s ease, background-color 0.15s ease !important;
    }
    div[data-testid="stTabContent"]:nth-of-type(3) [data-testid="stChatInputSubmitButton"] button:hover {
        background-color: #B8654A !important;
        transform: scale(1.05) !important;
    }

    /* Prompt starter buttons */
    .prompt-col .stButton > button {
        background-color: #FFFFFF !important;
        color: #33312E !important;
        border: 1px solid #E5E2DA !important;
        border-radius: 12px !important;
        padding: 10px 14px !important;
        text-align: left !important;
        font-size: 13.5px !important;
        font-weight: 500 !important;
        transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02) !important;
        height: auto !important;
        min-height: 48px !important;
        width: 100% !important;
    }
    .prompt-col .stButton > button:hover {
        border-color: #CC785C !important;
        background-color: #FAF8F5 !important;
        color: #171615 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 3px 8px rgba(204, 120, 92, 0.08) !important;
    }

    /* Thinking indicator */
    @keyframes thinkingPulse {
        0%, 80%, 100% { opacity: 0.25; transform: scale(0.85); }
        40% { opacity: 1; transform: scale(1.15); }
    }
    .thinking-container {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 4px;
        margin: 6px 0 10px 0;
    }
    .thinking-avatar {
        width: 30px;
        height: 30px;
        background: #FAF0EB;
        border: 1px solid #F3DDD3;
        color: #CC785C;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        font-weight: 700;
    }
    .thinking-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #FAF8F5;
        border: 1px solid #EAE7E0;
        padding: 5px 14px;
        border-radius: 20px;
    }
    .thinking-text { font-size: 13px; color: #706B63; font-weight: 500; }
    .thinking-dots { display: inline-flex; gap: 4px; align-items: center; }
    .thinking-dots span {
        width: 4px;
        height: 4px;
        background-color: #CC785C;
        border-radius: 50%;
        display: inline-block;
        animation: thinkingPulse 1.4s infinite ease-in-out both;
    }
    .thinking-dots span:nth-child(1) { animation-delay: -0.32s; }
    .thinking-dots span:nth-child(2) { animation-delay: -0.16s; }
    .thinking-dots span:nth-child(3) { animation-delay: 0s; }

    /* New conversation button */
    .clear-container .stButton > button {
        background: transparent !important;
        border: 1px solid #E0DDD5 !important;
        color: #7A756D !important;
        border-radius: 18px !important;
        font-size: 13px !important;
        padding: 5px 14px !important;
        transition: all 0.2s ease !important;
    }
    .clear-container .stButton > button:hover {
        border-color: #CC785C !important;
        color: #CC785C !important;
        background: #FAF8F5 !important;
    }

    /* Sources dropdown */
    .stChatMessage [data-testid="stExpander"] {
        border: 1px solid #ECE7DF !important;
        border-radius: 8px !important;
        background: #FAF8F5 !important;
        margin-top: 12px !important;
        margin-bottom: 4px !important;
    }
    .stChatMessage [data-testid="stExpander"] summary {
        font-size: 0.83rem !important;
        color: #79716B !important;
        font-weight: 500 !important;
    }
    .stChatMessage [data-testid="stExpander"] summary:hover { color: #CC785C !important; }
    .stChatMessage [data-testid="stExpander"] [data-testid="stExpanderDetails"] {
        padding: 10px 14px !important;
        font-size: 0.85rem !important;
        color: #37352F !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    hcol1, hcol2 = st.columns([6, 2], vertical_alignment="center")
    with hcol1:
        st.subheader("💬 Financial Advisor")
        st.caption("Savings plans, expense cuts, purchase roadmaps and budget reviews.")
    with hcol2:
        if st.session_state.get("advice_chat_history"):
            st.markdown('<div class="clear-container">', unsafe_allow_html=True)
            if st.button("🔄 New conversation", key="clear_advisor_chat"):
                st.session_state["advice_chat_history"] = []
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    if "advice_chat_history" not in st.session_state:
        st.session_state["advice_chat_history"] = []

    chat_container = st.container(height=580)
    with chat_container:
        if not st.session_state["advice_chat_history"]:
            with st.chat_message("assistant", avatar="assistant"):
                st.markdown(f"""
### 👋 Hi, I'm your financial advisor

Ask me anything about your money and I'll answer using your own numbers.

**Your monthly snapshot:**
* 💵 **Income**: ₹{avg_inc:,.0f}
* 💳 **Expenses**: ₹{avg_exp:,.0f}
* 📈 **Surplus**: **₹{avg_surp:,.0f}** ({s_rate:.1f}% savings rate)

---
#### Try asking:
""")
            qcol1, qcol2 = st.columns(2)
            with qcol1:
                st.markdown('<div class="prompt-col">', unsafe_allow_html=True)
                if st.button("💡 How can I cut expenses to save more?", key="qp_cut", use_container_width=True):
                    st.session_state["pending_prompt"] = "How can I cut my expenses to save more?"
                    st.rerun()
                if st.button("🏍️ Plan to buy a bike worth ₹60,000", key="qp_bike", use_container_width=True):
                    st.session_state["pending_prompt"] = "Give me a plan so I can save enough to buy a bike worth ₹60,000 next month."
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

            with qcol2:
                st.markdown('<div class="prompt-col">', unsafe_allow_html=True)
                if st.button("🚗 Can I afford a ₹6,00,000 car?", key="qp_car600k", use_container_width=True):
                    st.session_state["pending_prompt"] = "I want to buy a car worth ₹6,00,000. At what month will I be able to buy it and how should I cut expenses to afford the EMI?"
                    st.rerun()
                if st.button("📊 Where am I overspending?", key="qp_budget", use_container_width=True):
                    st.session_state["pending_prompt"] = "Where am I overspending compared to a typical budget?"
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

        for msg in st.session_state["advice_chat_history"]:
            if msg["role"] == "user":
                with st.chat_message("user", avatar="user"):
                    st.markdown(msg["content"])
            else:
                with st.chat_message("assistant", avatar="assistant"):
                    st.markdown(msg["content"])
                    if msg.get("evidence"):
                        render_sources(msg["evidence"])

        active_turn_placeholder = st.empty()
        st.markdown('<div id="chat-bottom-anchor"></div>', unsafe_allow_html=True)

    chat_prompt = st.chat_input("Ask anything, e.g. 'How can I save ₹60,000 for a bike?'", key="financial_advisor_chat_input")
    if "pending_prompt" in st.session_state and st.session_state["pending_prompt"]:
        chat_prompt = st.session_state.pop("pending_prompt")

    if chat_prompt:
        st.session_state["advice_chat_history"].append({"role": "user", "content": chat_prompt})
        with active_turn_placeholder.container():
            with st.chat_message("user", avatar="user"):
                st.markdown(chat_prompt)

            thinking_box = st.empty()
            thinking_box.markdown(
                """
                <div class="thinking-container">
                    <div class="thinking-avatar">✦</div>
                    <div class="thinking-pill">
                        <span class="thinking-text">Thinking</span>
                        <span class="thinking-dots"><span></span><span></span><span></span></span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            trigger_autoscroll()

            try:
                res = requests.post(
                    f"{BACKEND_URL}/agent/advice",
                    json={
                        "question": chat_prompt,
                        "chat_history": [
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state["advice_chat_history"]
                        ],
                    },
                    timeout=45,
                )
                thinking_box.empty()
                if res.status_code == 200:
                    res_data = res.json()
                    advice_text = res_data.get("advice", "I couldn't come up with an answer just now. Please try again.")
                    evidence = res_data.get("retrieved_evidence")
                    with st.chat_message("assistant", avatar="assistant"):
                        st.markdown(advice_text)
                        if evidence:
                            render_sources(evidence)
                    st.session_state["advice_chat_history"].append({
                        "role": "assistant",
                        "content": advice_text,
                        "evidence": evidence,
                    })
                else:
                    err_msg = "Something went wrong. Please try again."
                    with st.chat_message("assistant", avatar="assistant"):
                        st.error(err_msg)
                    st.session_state["advice_chat_history"].append({"role": "assistant", "content": err_msg})
            except requests.exceptions.RequestException:
                thinking_box.empty()
                err_msg = "Couldn't connect to the server. Please try again in a moment."
                with st.chat_message("assistant", avatar="assistant"):
                    st.error(err_msg)
                st.session_state["advice_chat_history"].append({"role": "assistant", "content": err_msg})

        st.rerun()

# ===================== TAB 4: AFFORDABILITY =====================
with tab4:
    st.subheader("Can I afford this?")
    st.caption("Tell us what you're planning to buy and we'll check it against your spending habits.")

    purchase_amount = st.number_input("Purchase amount (₹)", min_value=0.0, step=500.0, value=10000.0)

    if st.button("Check affordability", type="primary"):
        result = safe_get("/analysis/affordability", params={"purchase_amount": purchase_amount})
        if result:
            if "error" in result:
                st.warning(result["error"])
            else:
                verdict = result["verdict"]
                if verdict == "Easily affordable":
                    st.success(f"✅ {verdict}")
                elif verdict == "Affordable with planning":
                    st.info(f"🟡 {verdict}")
                else:
                    st.warning(f"🔴 {verdict}")
                st.write(result["explanation"])