import pandas as pd

class DataValidator:
    def check_nulls(self, df):
        return df.isnull().sum()

    def check_column_types(self, df):
        return df.dtypes

    def check_unique_labels(self, df, label_col):
        return df[label_col].nunique()

