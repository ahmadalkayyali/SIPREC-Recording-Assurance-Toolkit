# SIPREC Recording Assurance Toolkit

The SIPREC Recording Assurance Toolkit is a simple open-source project designed to help voice and contact center engineers validate whether calls that should be recorded actually have matching recording evidence.

In many enterprise environments, call recording is assumed to be working if the recorder platform is online. In reality, a successful recording depends on multiple layers: call signaling, SIPREC session creation, media forking, recorder ingestion, metadata correlation, and final recording availability.

This toolkit provides a repeatable method to compare expected recorded calls against recorder exports and SIPREC signaling logs.

## Purpose

This project helps identify:

- Calls that should have been recorded
- Calls that have confirmed recording evidence
- Calls missing from the recorder export
- SIPREC sessions found in signaling logs
- Basic recording assurance results and daily reporting

## Simple Assurance Logic

Expected recorded call  
→ Match against recorder export  
→ Check SIPREC signaling evidence  
→ Classify the call status  
→ Generate a report  

## Status Types

| Status | Meaning |
|---|---|
| `RECORDED_CONFIRMED` | The call has matching recording evidence |
| `MISSING_RECORDING` | The call was expected to be recorded but no recording was found |
| `SIPREC_SESSION_FOUND` | SIPREC signaling evidence was found in logs |
| `NEEDS_REVIEW` | The call needs manual review |

## Repository Structure

```text
SIPREC-Recording-Assurance-Toolkit/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── data-samples/
│   ├── expected_recorded_calls.csv
│   ├── recorder_export.csv
│   └── siprec_signaling_log_sample.txt
│
├── scripts/
│   ├── reconcile_recordings.py
│   ├── parse_siprec_logs.py
│   └── generate_report.py
│
├── sql/
│   ├── expected_recorded_calls.sql
│   ├── missing_recordings.sql
│   └── daily_assurance_summary.sql
│
├── reports/
│   ├── sample_recording_assurance_results.csv
│   └── sample_daily_assurance_report.md
│
└── docs/
    ├── methodology.md
    ├── data_dictionary.md
    └── troubleshooting.md
