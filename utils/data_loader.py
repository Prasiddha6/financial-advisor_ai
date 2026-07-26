import pandas as pd


class DataLoader:
    """
    Handles loading and validating uploaded datasets.
    """

    @staticmethod
    def load_csv(uploaded_file):
        df = pd.read_csv(uploaded_file)
        return df

    @staticmethod
    def validate_dataframe(df):
        errors = []

        if df.empty:
            errors.append("The uploaded dataset is empty.")

        if df.columns.duplicated().any():
            errors.append("Duplicate column names were found.")

        return errors

    @staticmethod
    def clean_dataframe(df):
        cleaned_df = df.copy()

        cleaned_df = cleaned_df.drop_duplicates()

        for column in cleaned_df.select_dtypes(include="number").columns:
            cleaned_df[column] = cleaned_df[column].fillna(
                cleaned_df[column].median()
            )

        return cleaned_df