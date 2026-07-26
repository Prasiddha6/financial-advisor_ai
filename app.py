from utils.data_loader import DataLoader
from utils.analytics import calculate_dataset_metrics
import streamlit as st

st.set_page_config(
    page_title="Financial Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Financial Analytics Dashboard")

st.sidebar.header("Data Source")

uploaded_file = st.sidebar.file_uploader(
    "Upload Financial Dataset",
    type=["csv"],
)

if uploaded_file is not None:
    try:
        # Load dataset
        df = DataLoader.load_csv(uploaded_file)

        # Validate dataset
        errors = DataLoader.validate_dataframe(df)

        if errors:
            for error in errors:
                st.error(error)
            st.stop()

        # Clean dataset
        df = DataLoader.clean_dataframe(df)

        # Calculate metrics
        metrics = calculate_dataset_metrics(df)

        st.success("Dataset loaded successfully.")

        st.subheader("Dataset Preview")
        st.dataframe(df, use_container_width=True)

        st.subheader("Dataset Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", metrics["rows"])

        with col2:
            st.metric("Columns", metrics["columns"])

        with col3:
            st.metric("Missing Values", metrics["missing_values"])

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric("Numeric Columns", metrics["numeric_columns"])

        with col5:
            st.metric(
                "Total Numeric Value",
                f"{metrics['total_value']:,.2f}",
            )

        with col6:
            st.metric(
                "Average Numeric Value",
                f"{metrics['average_value']:,.2f}",
            )

    except Exception as e:
        st.error(f"Error loading dataset: {e}")

else:
    st.info("Please upload a CSV file to begin analysis.")