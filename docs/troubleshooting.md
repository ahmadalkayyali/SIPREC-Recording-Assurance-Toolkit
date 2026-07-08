# Troubleshooting Guide

## Problem: Missing Recording

### Meaning

A call was expected to be recorded, but no matching recording was found in the recorder export.

### Possible Causes

- SIPREC session was never created
- Recorder did not ingest the recording
- Metadata mismatch between call system and recorder
- Recording export was incomplete
- Call was excluded by recording policy
- Recorder service issue
- SIP trunk or media forking issue

### What to Check

- Confirm the call should have been recorded
- Check SIPREC signaling logs for the GlobalCallId
- Confirm SIP INVITE, 200 OK, and ACK exist
- Check recorder ingestion logs
- Confirm recorder export timing
- Validate agent, device, and recording policy

---

## Problem: SIPREC Session Missing

### Meaning

The expected call exists, but there is no SIPREC signaling evidence.

### Possible Causes

- Recording profile not assigned
- SIP trunk issue
- Device not configured for recording
- Built-in bridge disabled
- Recording CSS or route pattern issue
- Recorder unreachable

### What to Check

- Device recording configuration
- Recording profile
- SIP trunk status
- Recorder destination
- SIPREC route pattern
- CUCM or CUBE logs

---

## Problem: Recording Duration Mismatch

### Meaning

A recording exists, but the recording duration does not match the call duration.

### Possible Causes

- Late recording start
- Early recording stop
- Media failure
- Recorder processing issue
- Transfer or conference scenario
- Metadata correlation issue

### What to Check

- Call start and end time
- Recording start and end time
- SIPREC BYE messages
- RTP media flow
- Recorder logs

---

## Problem: Script Does Not Run

### Possible Causes

- pandas is not installed
- Script is being run from the wrong folder
- CSV files are missing
- File path is incorrect

### Fix

Install requirements:

```bash
pip install -r requirements.txt
