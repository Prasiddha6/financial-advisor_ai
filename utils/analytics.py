import pandas as pd


def calculate_dataset_metrics(df: pd.DataFrame) -> dict:
    """
    Calculate key financial metrics for the dashboard.
    """

    total_revenue = df["Totals.Revenue"].sum()
    total_expenditure = df["Totals.Expenditure"].sum()
    total_tax = df["Totals.Tax"].sum()
    total_debt = df["Totals.Debt at end of fiscal year"].sum()
    capital_outlay = df["Totals.Capital outlay"].sum()

    net_balance = total_revenue - total_expenditure

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "states": df["State"].nunique(),
        "years": df["Year"].nunique(),
        "missing_values": int(df.isnull().sum().sum()),
        "revenue": total_revenue,
        "expenditure": total_expenditure,
        "tax": total_tax,
        "debt": total_debt,
        "capital_outlay": capital_outlay,
        "net_balance": net_balance,
    }


def yearly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate financial metrics by year.
    """

    return (
        df.groupby("Year")
        .agg(
            Revenue=("Totals.Revenue", "sum"),
            Expenditure=("Totals.Expenditure", "sum"),
            Tax=("Totals.Tax", "sum"),
            Debt=("Totals.Debt at end of fiscal year", "sum"),
        )
        .reset_index()
    )


def state_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate financial metrics by state.
    """

    return (
        df.groupby("State")
        .agg(
            Revenue=("Totals.Revenue", "sum"),
            Expenditure=("Totals.Expenditure", "sum"),
            Tax=("Totals.Tax", "sum"),
            Debt=("Totals.Debt at end of fiscal year", "sum"),
        )
        .sort_values("Revenue", ascending=False)
        .reset_index()
    )


def financial_ratios(df: pd.DataFrame) -> dict:
    """
    Calculate basic financial ratios.
    """

    revenue = df["Totals.Revenue"].sum()
    expenditure = df["Totals.Expenditure"].sum()
    debt = df["Totals.Debt at end of fiscal year"].sum()

    return {
        "expense_ratio": expenditure / revenue if revenue else 0,
        "debt_ratio": debt / revenue if revenue else 0,
        "surplus_ratio": (revenue - expenditure) / revenue if revenue else 0,
    }