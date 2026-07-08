# SIPREC Recording Assurance Toolkit

The SIPREC Recording Assurance Toolkit is a simple open-source project for validating whether calls that should be recorded actually have matching recording evidence.

Many enterprise voice and contact center environments depend on SIPREC-based recording. A recording platform may appear healthy, but individual calls can still be missed because of signaling issues, metadata mismatches, recorder ingestion problems, or missing exports.

This toolkit uses a basic reconciliation method:

1. Load a list of calls expected to be recorded.
2. Load a recorder export.
3. Match both files using GlobalCallId.
4. Mark each call as recorded or missing.
5. Generate a result file and summary file.

## Simple Logic

Expected recorded call  
→ Match against recorder export  
→ If recording exists: RECORDED_CONFIRMED  
→ If no recording exists: MISSING_RECORDING  

## Files

| File | Purpose |
|---|---|
| `data-samples/expected_recorded_calls.csv` | Sample list of calls that should have been recorded |
| `data-samples/recorder_export.csv` | Sample list of recordings exported from a recording platform |
| `scripts/reconcile_recordings.py` | Python script that compares expected calls with recorder export |
| `reports/sample_recording_assurance_results.csv` | Sample output showing recording status |
| `reports/sample_recording_assurance_summary.csv` | Sample summary count by status |

## How to Run

Install requirements:

```bash
pip install -r requirements.txt
