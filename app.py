import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financial Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Financial Analytics Dashboard")

st.sidebar.header("Data Source")

uploaded_file = st.sidebar.file_uploader(
    "Upload Financial Dataset",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.success("Dataset loaded successfully.")

        st.subheader("Dataset Preview")
        st.dataframe(df, use_container_width=True)

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        with col3:
            st.metric("Missing Values", df.isnull().sum().sum())

    except Exception as e:
        st.error(f"Error loading dataset: {e}")

else:
    st.info("Please upload a CSV file to begin analysis.")