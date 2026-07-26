import streamlit as st
import pandas as pd
from utils.predictor import forecast_revenue
from utils.data_loader import DataLoader
from utils.analytics import calculate_dataset_metrics
from utils.charts import (
    revenue_trend,
    expenditure_trend,
    revenue_vs_expenditure,
    top_states,
    tax_revenue,
    debt_trend,
    expenditure_distribution,
    correlation_heatmap,
)

st.set_page_config(
    page_title="Financial Analytics Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Financial Analytics Dashboard")
st.caption("Government Finance Dataset Analysis")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV Dataset",
    type=["csv"],
)

if uploaded_file is None:
    st.info("Upload a CSV file to begin analysis.")
    st.stop()

try:

    df = DataLoader.load_csv(uploaded_file)

    errors = DataLoader.validate_dataframe(df)

    if errors:
        for error in errors:
            st.error(error)
        st.stop()

    df = DataLoader.clean_dataframe(df)

except Exception as e:
    st.error(str(e))
    st.stop()

st.sidebar.header("Filters")

years = sorted(df["Year"].unique())

selected_years = st.sidebar.multiselect(
    "Year",
    years,
    default=years,
)

states = sorted(df["State"].unique())

selected_states = st.sidebar.multiselect(
    "State",
    states,
    default=states,
)

filtered_df = df[
    (df["Year"].isin(selected_years))
    &
    (df["State"].isin(selected_states))
]

metrics = calculate_dataset_metrics(filtered_df)

total_revenue = filtered_df["Totals.Revenue"].sum()

total_expenditure = filtered_df["Totals.Expenditure"].sum()

total_tax = filtered_df["Totals.Tax"].sum()

total_debt = filtered_df[
    "Totals.Debt at end of fiscal year"
].sum()

balance = total_revenue - total_expenditure

st.subheader("Key Performance Indicators")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric(
        "Revenue",
        f"{total_revenue:,.0f}",
    )

with c2:
    st.metric(
        "Expenditure",
        f"{total_expenditure:,.0f}",
    )

with c3:
    st.metric(
        "Net Balance",
        f"{balance:,.0f}",
    )

with c4:
    st.metric(
        "Tax Revenue",
        f"{total_tax:,.0f}",
    )

with c5:
    st.metric(
        "Outstanding Debt",
        f"{total_debt:,.0f}",
    )

st.divider()

left, right = st.columns(2)

with left:
    st.plotly_chart(
        revenue_trend(filtered_df),
        use_container_width=True,
    )

with right:
    st.plotly_chart(
        expenditure_trend(filtered_df),
        use_container_width=True,
    )

st.plotly_chart(
    revenue_vs_expenditure(filtered_df),
    use_container_width=True,
)

left, right = st.columns(2)

with left:
    st.plotly_chart(
        top_states(filtered_df),
        use_container_width=True,
    )

with right:
    st.plotly_chart(
        tax_revenue(filtered_df),
        use_container_width=True,
    )
    with right:
    st.plotly_chart(
        tax_revenue(filtered_df),
        use_container_width=True,
    )
    st.divider()

left, right = st.columns(2)

with left:
    st.plotly_chart(
        debt_trend(filtered_df),
        use_container_width=True,
    )

with right:
    st.plotly_chart(
        expenditure_distribution(filtered_df),
        use_container_width=True,
    )

st.divider()

st.subheader("Correlation Analysis")

st.plotly_chart(
    correlation_heatmap(filtered_df),
    use_container_width=True,
)

st.divider()

st.subheader("Dataset Summary")

summary = filtered_df.describe()

st.dataframe(
    summary,
    use_container_width=True,
)

st.divider()

st.subheader("Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Dataset",
    data=csv,
    file_name="filtered_financial_data.csv",
    mime="text/csv",
)

st.divider()

st.caption(
    "Financial Analytics Dashboard | Built with Streamlit and Plotly"
)
st.divider()

st.header("Revenue Forecast")

forecast_df = forecast_revenue(filtered_df)

st.dataframe(
    forecast_df,
    use_container_width=True,
)

forecast_chart = (
    forecast_df.set_index("Year")
)

st.line_chart(forecast_chart)