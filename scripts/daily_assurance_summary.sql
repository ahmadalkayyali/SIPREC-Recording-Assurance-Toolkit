/*
Purpose:
Generate a daily recording assurance summary.

This query counts confirmed and missing recordings.
*/

DECLARE @StartDate DATETIME = '2026-07-07 00:00:00';
DECLARE @EndDate   DATETIME = '2026-07-08 00:00:00';

WITH RecordingCheck AS
(
    SELECT
        c.GlobalCallId,
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
)
SELECT
    RecordingAssuranceStatus,
    COUNT(*) AS CallCount
FROM
    RecordingCheck
GROUP BY
    RecordingAssuranceStatus
ORDER BY
    RecordingAssuranceStatus;
