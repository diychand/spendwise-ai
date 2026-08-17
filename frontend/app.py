import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SpendWise AI", page_icon="💰", layout="wide")

BACKEND_URL = "http://127.0.0.1:8000"

# ---------- Session state setup ----------
if "data_ready" not in st.session_state:
    st.session_state["data_ready"] = False

# ---------- Header ----------
st.title("💰 SpendWise AI")
st.caption("Your personal finance assistant — upload a statement and get instant insights")

# ---------- Upload section ----------
if not st.session_state["data_ready"]:
    st.subheader("Get started")
    st.write("Upload your bank statement (CSV) to see where your money is going.")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv", label_visibility="collapsed")

    if uploaded_file is not None:
        if st.button("Analyze my spending", type="primary"):
            with st.status("Analyzing your statement...", expanded=True) as status:
                st.write("Reading transactions...")
                files = {"file": (uploaded_file.name, uploaded_file, "text/csv")}
                upload_response = requests.post(f"{BACKEND_URL}/transactions/upload", files=files)

                if upload_response.status_code != 200:
                    status.update(label="Something went wrong. Please try again.", state="error")
                    st.stop()

                st.write("Understanding your transactions...")
                requests.post(f"{BACKEND_URL}/categorize/rules")
                requests.post(f"{BACKEND_URL}/categorize/train-ml")
                ml_result = requests.post(f"{BACKEND_URL}/categorize/ml").json()

                if ml_result.get("still_uncategorized", 0) > 0:
                    st.write("Double-checking a few unusual transactions...")
                    requests.post(f"{BACKEND_URL}/categorize/llm")

                st.write("Scanning for unusual activity...")
                requests.post(f"{BACKEND_URL}/anomaly/detect")

                status.update(label="All done!", state="complete")

            st.session_state["data_ready"] = True
            st.rerun()

    st.stop()  # Don't show anything below until data is ready

# ---------- Reset option ----------
with st.sidebar:
    st.header("SpendWise AI")
    st.write("Your finances, understood.")
    if st.button("Upload a different statement"):
        st.session_state["data_ready"] = False
        st.rerun()

# ---------- Fetch data once ----------
transactions_response = requests.get(f"{BACKEND_URL}/transactions/")
transactions = transactions_response.json() if transactions_response.status_code == 200 else []
df = pd.DataFrame(transactions)

# ---------- Tabs for a real app feel ----------
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "💳 Transactions", "🤖 Ask a question", "🎯 Can I afford it?"])

# ===================== TAB 1: OVERVIEW =====================
with tab1:
    if not df.empty:
        debit_df = df[df["type"] == "DEBIT"]
        credit_df = df[df["type"] == "CREDIT"]

        total_spent = debit_df["amount"].sum()
        total_income = credit_df["amount"].sum()
        anomaly_count = int(df["is_anomaly"].sum())

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total spent", f"₹{total_spent:,.0f}")
        col2.metric("Total income", f"₹{total_income:,.0f}")
        col3.metric("Net balance", f"₹{total_income - total_spent:,.0f}")
        col4.metric("Unusual transactions", anomaly_count)

        st.divider()

        # Charts
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.subheader("Spending by category")
            category_totals = debit_df.groupby("category")["amount"].sum().reset_index()
            fig_pie = px.pie(category_totals, names="category", values="amount", hole=0.4)
            fig_pie.update_layout(margin=dict(t=10, b=10, l=10, r=10))
            st.plotly_chart(fig_pie, use_container_width=True)

        with chart_col2:
            st.subheader("Spending over time")
            trend_response = requests.get(f"{BACKEND_URL}/analysis/monthly-trend")
            if trend_response.status_code == 200:
                trend_data = trend_response.json()
                if trend_data:
                    trend_df = pd.DataFrame(trend_data)
                    fig_line = px.line(trend_df, x="month", y="amount", markers=True)
                    fig_line.update_layout(margin=dict(t=10, b=10, l=10, r=10), yaxis_title="Amount (₹)")
                    st.plotly_chart(fig_line, use_container_width=True)

        st.subheader("Spending by category, month over month")
        category_response = requests.get(f"{BACKEND_URL}/analysis/monthly-category")
        if category_response.status_code == 200:
            category_data = category_response.json()
            if category_data:
                cat_df = pd.DataFrame(category_data)
                fig_bar = px.bar(cat_df, x="month", y="amount", color="category", barmode="group")
                fig_bar.update_layout(yaxis_title="Amount (₹)")
                st.plotly_chart(fig_bar, use_container_width=True)

        if anomaly_count > 0:
            st.divider()
            st.subheader("⚠️ Unusual transactions worth a look")
            flagged_response = requests.get(f"{BACKEND_URL}/anomaly/flagged")
            if flagged_response.status_code == 200:
                flagged = flagged_response.json()
                flagged_df = pd.DataFrame(flagged)[["date", "description", "amount", "category"]]
                flagged_df.columns = ["Date", "Description", "Amount", "Category"]
                st.dataframe(flagged_df, use_container_width=True, hide_index=True)
    else:
        st.info("No transaction data available.")

# ===================== TAB 2: TRANSACTIONS =====================
with tab2:
    st.subheader("All transactions")

    if not df.empty:
        # Filters
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
            selected_category = st.selectbox("Filter by category", categories)
        with filter_col2:
            selected_type = st.selectbox("Filter by type", ["All", "DEBIT", "CREDIT"])

        filtered_df = df.copy()
        if selected_category != "All":
            filtered_df = filtered_df[filtered_df["category"] == selected_category]
        if selected_type != "All":
            filtered_df = filtered_df[filtered_df["type"] == selected_type]

        display_df = filtered_df[["date", "description", "amount", "category", "type"]].copy()
        display_df.columns = ["Date", "Description", "Amount", "Category", "Type"]

        # Let the user fix a wrong category, right from the table
        st.caption("Spotted a mistake? You can correct any transaction's category below.")
        st.dataframe(display_df, use_container_width=True, hide_index=True)

        with st.expander("Correct a transaction's category"):
            txn_options = {
                f"{row['description']} — ₹{row['amount']}": row["id"]
                for _, row in filtered_df.iterrows()
            }
            if txn_options:
                selected_txn_label = st.selectbox("Select a transaction", list(txn_options.keys()))
                new_category = st.selectbox(
                    "Correct category",
                    ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Groceries", "Salary", "Rent", "Other"]
                )
                if st.button("Save correction"):
                    txn_id = txn_options[selected_txn_label]
                    correction_response = requests.patch(
                        f"{BACKEND_URL}/transactions/{txn_id}/correct",
                        json={"category": new_category}
                    )
                    if correction_response.status_code == 200:
                        st.success("Updated! Refresh to see the change.")
                        st.rerun()
    else:
        st.info("No transactions to show.")

# ===================== TAB 3: ASK A QUESTION =====================
with tab3:
    st.subheader("Ask anything about your finances")
    st.caption("e.g. \"How much did I spend on food last month?\" or \"What's my biggest expense category?\"")

    question = st.text_input("Your question", label_visibility="collapsed", placeholder="Type your question here...")

    if st.button("Ask", type="primary") and question:
        with st.spinner("Thinking..."):
            response = requests.post(f"{BACKEND_URL}/agent/query", json={"question": question})

        if response.status_code == 200:
            result = response.json()
            if "error" in result:
                st.warning("I couldn't quite answer that — try rephrasing your question.")
            else:
                st.success(result["answer"])
                with st.expander("See how this was calculated"):
                    st.code(result["generated_code"], language="python")
        else:
            st.error("Something went wrong. Please try again.")

# ===================== TAB 4: AFFORDABILITY =====================
with tab4:
    st.subheader("Can I afford this?")
    st.caption("Tell us what you're planning to buy, and we'll check it against your spending habits.")

    purchase_amount = st.number_input("Purchase amount (₹)", min_value=0.0, step=500.0, value=10000.0)

    if st.button("Check affordability", type="primary"):
        response = requests.get(f"{BACKEND_URL}/analysis/affordability", params={"purchase_amount": purchase_amount})
        if response.status_code == 200:
            result = response.json()
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