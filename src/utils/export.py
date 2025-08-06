import json
import pandas as pd

def export_classification_report(report, filepath):
    with open(filepath, 'w') as f:
        json.dump(report, f, indent=4)

def export_df_to_csv(df, filepath):
    df.to_csv(filepath, index=False)

