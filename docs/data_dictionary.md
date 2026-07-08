# Data Dictionary

## expected_recorded_calls.csv

| Field | Description |
|---|---|
| GlobalCallId | Unique call identifier used for correlation |
| CallDateTime | Date and time when the call started |
| CallingPartyNumber | Caller ANI or originating number |
| CalledPartyNumber | DNIS, dialed number, or destination number |
| AgentExtension | Agent or device extension associated with the call |
| DurationSeconds | Call duration in seconds |
| ShouldBeRecorded | 1 means the call should be recorded; 0 means it should not |

## recorder_export.csv

| Field | Description |
|---|---|
| GlobalCallId | Unique call identifier from recorder metadata |
| RecordingId | Unique recording identifier |
| RecordingStartTime | Date and time when the recording started |
| RecordingDurationSeconds | Duration of the recording in seconds |
| RecorderStatus | Recording availability status |

## sample_recording_assurance_results.csv

| Field | Description |
|---|---|
| GlobalCallId | Unique call identifier |
| CallDateTime | Date and time when the call started |
| CallingPartyNumber | Caller ANI or originating number |
| CalledPartyNumber | DNIS, dialed number, or destination number |
| AgentExtension | Agent or device extension |
| DurationSeconds | Call duration in seconds |
| ShouldBeRecorded | Indicates whether the call should have been recorded |
| RecordingId | Matching recording identifier, if available |
| RecordingStartTime | Recording start time, if available |
| RecordingDurationSeconds | Recording duration, if available |
| RecorderStatus | Recorder export status |
| RecordingAssuranceStatus | Final toolkit classification |

## RecordingAssuranceStatus Values

| Status | Description |
|---|---|
| RECORDED_CONFIRMED | Matching recording evidence exists |
| MISSING_RECORDING | Expected recording was not found |
| NEEDS_REVIEW | Manual review is required |
| SIPREC_SESSION_FOUND | SIPREC signaling evidence was found |
