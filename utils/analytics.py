import pandas as pd


def calculate_dataset_metrics(df: pd.DataFrame) -> dict:
    """
    Calculate summary metrics for the uploaded dataset.
    """

    numeric_df = df.select_dtypes(include="number")

    metrics = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "numeric_columns": len(numeric_df.columns),
        "total_value": float(numeric_df.sum().sum()),
        "average_value": float(numeric_df.mean().mean())
        if not numeric_df.empty
        else 0.0,
    }

    return metrics