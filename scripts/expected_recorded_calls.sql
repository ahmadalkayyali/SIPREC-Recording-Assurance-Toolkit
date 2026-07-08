/*
Purpose:
Identify calls that are expected to be recorded.

This is a generic SQL example. Table and column names should be adjusted
to match the actual CDR, UCCE, CUIC, or recorder export database schema.

Logic:
- Include calls that should be recorded
- Exclude short test calls if needed
- Include useful call correlation fields
*/

DECLARE @StartDate DATETIME = '2026-07-07 00:00:00';
DECLARE @EndDate   DATETIME = '2026-07-08 00:00:00';

SELECT
    GlobalCallId,
    CallDateTime,
    CallingPartyNumber,
    CalledPartyNumber,
    AgentExtension,
    DurationSeconds,
    ShouldBeRecorded
FROM
    ExpectedRecordedCalls
WHERE
    CallDateTime >= @StartDate
    AND CallDateTime < @EndDate
    AND ShouldBeRecorded = 1;
