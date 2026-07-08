import os
import pandas as pd
from datetime import datetime


RESULTS_FILE = "reports/sample_recording_assurance_results.csv"
SUMMARY_FILE = "reports/sample_recording_assurance_summary.csv"
REPORT_FILE = "reports/sample_daily_assurance_report.md"


def main():
    if not os.path.exists(RESULTS_FILE):
        print("Results file not found. Run reconcile_recordings.py first.")
        return

    results = pd.read_csv(RESULTS_FILE)

    total_calls = len(results)
    confirmed = len(results[results["RecordingAssuranceStatus"] == "RECORDED_CONFIRMED"])
    missing = len(results[results["RecordingAssuranceStatus"] == "MISSING_RECORDING"])

    assurance_score = round((confirmed / total_calls) * 100, 2) if total_calls > 0 else 0

    missing_calls = results[results["RecordingAssuranceStatus"] == "MISSING_RECORDING"]

    report_lines = []
    report_lines.append("# Sample Daily SIPREC Recording Assurance Report")
    report_lines.append("")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("")
    report_lines.append("## Executive Summary")
    report_lines.append("")
    report_lines.append(f"- Total expected recorded calls: {total_calls}")
    report_lines.append(f"- Confirmed recordings: {confirmed}")
    report_lines.append(f"- Missing recordings: {missing}")
    report_lines.append(f"- Recording assurance score: {assurance_score}%")
    report_lines.append("")
    report_lines.append("## Missing Recording Details")
    report_lines.append("")

    if missing_calls.empty:
        report_lines.append("No missing recordings found.")
    else:
        report_lines.append("| GlobalCallId | CallDateTime | CallingPartyNumber | CalledPartyNumber | AgentExtension |")
        report_lines.append("|---|---|---|---|---|")

        for _, row in missing_calls.iterrows():
            report_lines.append(
                f"| {row['GlobalCallId']} | {row['CallDateTime']} | {row['CallingPartyNumber']} | {row['CalledPartyNumber']} | {row['AgentExtension']} |"
            )

    report_lines.append("")
    report_lines.append("## Notes")
    report_lines.append("")
    report_lines.append("This report is generated from synthetic sample data and is intended to demonstrate a repeatable recording assurance method.")

    with open(REPORT_FILE, "w", encoding="utf-8") as report:
        report.write("\n".join(report_lines))

    print(f"Daily assurance report generated: {REPORT_FILE}")


if __name__ == "__main__":
    main()
