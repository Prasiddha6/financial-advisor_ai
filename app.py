import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financial Advisor AI",
    layout="wide"
)

st.title("Financial Advisor AI")
st.write("Upload a transaction dataset to generate financial insights.")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Transactions")
    st.dataframe(df, use_container_width=True)

    income = df.loc[df["Type"] == "Income", "Amount"].sum()
    expenses = df.loc[df["Type"] == "Expense", "Amount"].sum()

    savings = income - expenses

    savings_rate = 0
    if income > 0:
        savings_rate = (savings / income) * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Income", f"₹{income:,.2f}")
    col2.metric("Total Expenses", f"₹{expenses:,.2f}")
    col3.metric("Net Savings", f"₹{savings:,.2f}")
    col4.metric("Savings Rate", f"{savings_rate:.2f}%")