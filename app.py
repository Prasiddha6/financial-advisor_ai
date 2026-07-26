import streamlit as st

st.set_page_config(
    page_title="AI Financial Advisor",
    page_icon="💰",
    layout="wide"
)

st.title("AI Financial Advisor")

st.markdown("""
## Welcome!

This application helps you:

- Analyze expenses
- Predict future spending
- Track savings
- Get AI-powered financial advice

Built using:

- Streamlit
- Pandas
- Plotly
- Scikit-Learn
- Google Gemini
""")