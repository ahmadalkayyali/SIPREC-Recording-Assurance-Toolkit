import os
import pandas as pd


EXPECTED_CALLS_FILE = "data-samples/expected_recorded_calls.csv"
RECORDER_EXPORT_FILE = "data-samples/recorder_export.csv"

RESULTS_FILE = "reports/sample_recording_assurance_results.csv"
SUMMARY_FILE = "reports/sample_recording_assurance_summary.csv"


def main():
    os.makedirs("reports", exist_ok=True)

    expected_calls = pd.read_csv(EXPECTED_CALLS_FILE)
    recorder_export = pd.read_csv(RECORDER_EXPORT_FILE)

    expected_calls = expected_calls[expected_calls["ShouldBeRecorded"] == 1]

    results = expected_calls.merge(
        recorder_export,
        how="left",
        on="GlobalCallId"
    )

    results["RecordingStatus"] = results["RecordingId"].apply(
        lambda value: "RECORDED_CONFIRMED" if pd.notna(value) else "MISSING_RECORDING"
    )

    summary = (
        results["RecordingStatus"]
        .value_counts()
        .reset_index()
    )

    summary.columns = ["RecordingStatus", "Count"]

    results.to_csv(RESULTS_FILE, index=False)
    summary.to_csv(SUMMARY_FILE, index=False)

    print("Recording assurance check completed.")
    print()
    print(summary.to_string(index=False))
    print()
    print(f"Results saved to: {RESULTS_FILE}")
    print(f"Summary saved to: {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
