import os
import re
import pandas as pd


SIPREC_LOG_FILE = "data-samples/siprec_signaling_log_sample.txt"
OUTPUT_FILE = "reports/sample_siprec_signaling_summary.csv"


def extract_call_id(line):
    match = re.search(r"Call-ID:\s*(\S+)", line)
    if match:
        return match.group(1)
    return None


def main():
    os.makedirs("reports", exist_ok=True)

    records = []

    with open(SIPREC_LOG_FILE, "r", encoding="utf-8") as log_file:
        for line in log_file:
            call_id = extract_call_id(line)

            if call_id:
                records.append({
                    "GlobalCallId": call_id,
                    "HasInvite": "INVITE" in line,
                    "HasTrying": "100 Trying" in line,
                    "Has200Ok": "200 OK" in line,
                    "HasAck": "ACK" in line,
                    "RawLogLine": line.strip()
                })

    log_events = pd.DataFrame(records)

    if log_events.empty:
        print("No SIPREC records found.")
        return

    summary = log_events.groupby("GlobalCallId").agg({
        "HasInvite": "max",
        "HasTrying": "max",
        "Has200Ok": "max",
        "HasAck": "max"
    }).reset_index()

    summary["SiprecSignalingStatus"] = summary.apply(
        lambda row: "SIPREC_SESSION_FOUND"
        if row["HasInvite"] and row["Has200Ok"] and row["HasAck"]
        else "NEEDS_REVIEW",
        axis=1
    )

    summary.to_csv(OUTPUT_FILE, index=False)

    print("SIPREC log parsing completed.")
    print()
    print(summary.to_string(index=False))
    print()
    print(f"SIPREC summary saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
