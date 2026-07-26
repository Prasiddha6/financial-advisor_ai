import pandas as pd
from sklearn.linear_model import LinearRegression


def train_forecast_model(df: pd.DataFrame):
    """
    Train a simple linear regression model using Year to predict Revenue.
    """

    yearly = (
        df.groupby("Year")["Totals.Revenue"]
        .sum()
        .reset_index()
        .sort_values("Year")
    )

    X = yearly[["Year"]]
    y = yearly["Totals.Revenue"]

    model = LinearRegression()
    model.fit(X, y)

    return model


def forecast_revenue(df: pd.DataFrame, years_ahead: int = 5):
    """
    Forecast revenue for the next N years.
    """

    yearly = (
        df.groupby("Year")["Totals.Revenue"]
        .sum()
        .reset_index()
        .sort_values("Year")
    )

    model = train_forecast_model(df)

    last_year = yearly["Year"].max()

    future_years = pd.DataFrame(
        {
            "Year": range(last_year + 1, last_year + years_ahead + 1)
        }
    )

    predictions = model.predict(future_years)

    forecast = future_years.copy()
    forecast["Predicted Revenue"] = predictions

    return forecast