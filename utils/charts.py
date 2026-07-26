import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def revenue_trend(df: pd.DataFrame):
    revenue = (
        df.groupby("Year")["Totals.Revenue"]
        .sum()
        .reset_index()
        .sort_values("Year")
    )

    fig = px.line(
        revenue,
        x="Year",
        y="Totals.Revenue",
        markers=True,
        title="Revenue Trend"
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        xaxis_title="Year",
        yaxis_title="Revenue"
    )

    return fig


def expenditure_trend(df: pd.DataFrame):
    expenditure = (
        df.groupby("Year")["Totals.Expenditure"]
        .sum()
        .reset_index()
        .sort_values("Year")
    )

    fig = px.line(
        expenditure,
        x="Year",
        y="Totals.Expenditure",
        markers=True,
        title="Expenditure Trend"
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        xaxis_title="Year",
        yaxis_title="Expenditure"
    )

    return fig


def revenue_vs_expenditure(df: pd.DataFrame):

    comparison = (
        df.groupby("Year")[[
            "Totals.Revenue",
            "Totals.Expenditure"
        ]]
        .sum()
        .reset_index()
        .sort_values("Year")
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=comparison["Year"],
            y=comparison["Totals.Revenue"],
            name="Revenue"
        )
    )

    fig.add_trace(
        go.Bar(
            x=comparison["Year"],
            y=comparison["Totals.Expenditure"],
            name="Expenditure"
        )
    )

    fig.update_layout(
        barmode="group",
        template="plotly_white",
        height=500,
        title="Revenue vs Expenditure"
    )

    return fig


def debt_trend(df: pd.DataFrame):

    debt = (
        df.groupby("Year")[
            "Totals.Debt at end of fiscal year"
        ]
        .sum()
        .reset_index()
        .sort_values("Year")
    )

    fig = px.area(
        debt,
        x="Year",
        y="Totals.Debt at end of fiscal year",
        title="Debt Trend"
    )

    fig.update_layout(
        template="plotly_white",
        height=420
    )

    return fig


def top_states(df: pd.DataFrame):

    states = (
        df.groupby("State")["Totals.Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        states,
        x="Totals.Revenue",
        y="State",
        orientation="h",
        title="Top 10 States by Revenue"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def tax_revenue(df: pd.DataFrame):

    tax = (
        df.groupby("Year")["Totals.Tax"]
        .sum()
        .reset_index()
        .sort_values("Year")
    )

    fig = px.bar(
        tax,
        x="Year",
        y="Totals.Tax",
        title="Tax Revenue"
    )

    fig.update_layout(
        template="plotly_white",
        height=420
    )

    return fig


def expenditure_distribution(df: pd.DataFrame):

    categories = {
        "Education": df["Details.Expenditure.Education"].sum(),
        "Health": df["Details.Expenditure.Health"].sum(),
        "Police": df["Details.Expenditure.Police protection"].sum(),
        "Highways": df["Details.Expenditure.Highways"].sum(),
        "Corrections": df["Details.Expenditure.Correction"].sum()
    }

    fig = px.pie(
        names=list(categories.keys()),
        values=list(categories.values()),
        hole=0.45,
        title="Major Expenditure Categories"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def correlation_heatmap(df: pd.DataFrame):

    numeric = df.select_dtypes(include="number")

    corr = numeric.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        title="Correlation Matrix"
    )

    fig.update_layout(
        height=700
    )

    return fig