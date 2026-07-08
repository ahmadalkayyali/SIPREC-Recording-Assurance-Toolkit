/*
Purpose:
Find calls that should have been recorded but do not have matching recording evidence.

This query compares expected recorded calls against recorder export records.
*/

DECLARE @StartDate DATETIME = '2026-07-07 00:00:00';
DECLARE @EndDate   DATETIME = '2026-07-08 00:00:00';

SELECT
    c.GlobalCallId,
    c.CallDateTime,
    c.CallingPartyNumber,
    c.CalledPartyNumber,
    c.AgentExtension,
    c.DurationSeconds,
    r.RecordingId,
    r.RecordingStartTime,
    r.RecordingDurationSeconds,
    CASE
        WHEN r.RecordingId IS NULL THEN 'MISSING_RECORDING'
        ELSE 'RECORDED_CONFIRMED'
    END AS RecordingAssuranceStatus
FROM
    ExpectedRecordedCalls c
LEFT JOIN
    RecorderExport r
    ON c.GlobalCallId = r.GlobalCallId
WHERE
    c.CallDateTime >= @StartDate
    AND c.CallDateTime < @EndDate
    AND c.ShouldBeRecorded = 1
    AND r.RecordingId IS NULL;
