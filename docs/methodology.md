# Methodology

## Overview

The SIPREC Recording Assurance Toolkit uses a simple reconciliation method to determine whether calls expected to be recorded have matching recording evidence.

The method is based on comparing three types of evidence:

1. Expected recorded calls
2. Recorder export records
3. SIPREC signaling logs

## Step 1: Identify Expected Recorded Calls

The first step is to identify calls that should have been recorded. These records may come from CDR, UCCE, CUIC, contact center reporting, or another call detail source.

Minimum useful fields:

- GlobalCallId
- CallDateTime
- CallingPartyNumber
- CalledPartyNumber
- AgentExtension
- DurationSeconds
- ShouldBeRecorded

## Step 2: Load Recorder Export

The second step is to load the recording platform export. This file should contain the recordings that were actually available in the recorder.

Minimum useful fields:

- GlobalCallId
- RecordingId
- RecordingStartTime
- RecordingDurationSeconds
- RecorderStatus

## Step 3: Reconcile Calls and Recordings

The toolkit compares the expected call list against the recorder export.

Primary match field:

- GlobalCallId

Fallback matching can be added later using:

- AgentExtension
- CallingPartyNumber
- CalledPartyNumber
- Time window

## Step 4: Classify Recording Status

Each call receives a recording assurance status.

| Status | Meaning |
|---|---|
| RECORDED_CONFIRMED | Matching recording evidence exists |
| MISSING_RECORDING | No matching recording was found |
| NEEDS_REVIEW | The record requires manual review |

## Step 5: Generate Daily Report

The toolkit generates a daily summary showing:

- Total expected recorded calls
- Confirmed recordings
- Missing recordings
- Recording assurance score
- Missing call details

## Future Enhancements

Future versions can add:

- Time-window matching
- SIPREC failure code extraction
- Short or silent recording detection
- Recorder API integration
- Dashboard output
- Email alerting
