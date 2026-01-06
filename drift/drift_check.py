import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

def check_drift(reference_df: pd.DataFrame, current_df: pd.DataFrame):
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference_df, current_data=current_df)

    result = report.as_dict()

    dataset_drift = result["metrics"][0]["result"]["dataset_drift"]
    drift_share = result["metrics"][0]["result"]["drift_share"]

    return {
        "drift_detected": dataset_drift,
        "drift_score": drift_share
    }
