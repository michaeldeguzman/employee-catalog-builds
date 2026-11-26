# Timers in the Development stage and the daily timer limit
Read-only, 2026-11-22 (AEDT). Stage: Development, key 8b036dbd-6d28-2b5c-c50a-77a6bc07d748. Sources: `app_logs` (stage-wide, all apps), `env_apps` (50 deployed apps), `context_graph` for the apps that logged timer runs, and the saved build A graph `Reports/graphdiff/reference/EmployeeCatalogMW-r6.xre`. No tenant write.
Related: platform incident P-2 in `Reports/interventions.md`.

## What the graph can and cannot show
- The model graph of a timer holds the name, timeout, priority and, for "run when published", the schedule value `WhenPublished`.
- A recurring schedule is not in the graph: `Schedule` is empty for every recurring timer below. The effective schedule is the one in the ODC Portal for the stage. The cadence below is therefore taken from the log lines, not from the model.
- The docs search (outsystems-docs, ODC, synced 2026-10-28) returned no page for OS-TMR-42900 or for the Personal Edition timer limit.

## Timers that executed on 2026-11-20 and 2026-11-21 (UTC), from the logs
Run counts are "starting execution" lines. Duration is my estimate: the time from the start line to the "executed successfully" line of the same trace, summed. It is not the platform's own measure.
| App (asset key, revision) | Timer | Schedule in graph | Observed cadence | Runs 20 Nov (00:00Z to 13:00:26Z) | Runs 21 Nov (00:00Z to 12:25:21Z) | Estimated seconds 20 Nov / 21 Nov |
|---|---|---|---|---|---|---|
| RAG Knowledge Base (eb6ab730-cbdc-eba3-8851-897d66e0ca57, r72) | RecomputeBM25Stats | none | about every 5 min (median gap 300 s). Its description says every 30 minutes | 157 | 150 | 974.4 / 1001.6 |
| CloneOfRAGKnowledgeBase (f5cf9dac-58ed-7cd9-ac9e-6a84470247eb, r2) | RecomputeBM25Stats | none | about every 5 min | 157 | 150 | 246.6 / 226.1 |
| Clone2OfRAGKnowledgeBase (9c076567-6b41-6fa6-5a81-2af9a3c8bf5a, r1) | RecomputeBM25Stats | none | about every 5 min | 157 | 150 | 222.8 / 219.3 |
| OKF Store (9a21ae93-ccfb-b227-5b1f-ec6127e1d08a, r140) | IngestBatch | none | about every 5 min | 157 | 150 | 211.4 / 208.6 |
| OKF Store | LinkResolution | none | about every 5 min | 157 | 150 | 204.1 / 198.5 |
| EmployeeCatalogV2 (8fd59c69-8e31-b9a4-53c1-4db19b34b2e8, version 31) | DailyJobTimer | not readable | about hourly | 14 | 13 | 16.7 / 14.9 |
| EmployeeCatalogMW (07a64c21-0c8c-8afb-28ee-5d8530d55cf8, r6) | LoadSampleDataOnPublish | `WhenPublished` (saved r6 graph) | on each publish | 0 | 7 | 0 / 9.1 |
| **Total** | | | | **799** | **770** | **1875.9 / 1877.9** |
- The five timers that run every 5 minutes account for about 99% of the estimated time on both days.
- EmployeeCatalogV2 is not in the `env_apps` list of 50 deployed apps and `context_graph` returns OS-APPS-40401 (asset not found) for its key, yet its timer still logs. Its use is small (about 15 to 17 s a day).

## Timers that exist but did not run on those two days
- OKF Store: `ResetData`.
- RAG Knowledge Base, CloneOfRAGKnowledgeBase, Clone2OfRAGKnowledgeBase: `ResetData` and `CleanupCache` in each.
- EmployeeCatalogMCP: `BootstrapTimer` (`WhenPublished`, 20 minutes). Portal: Last run "-".

## When the limit was reached
- 2026-11-20: last timer log line 13:00:26.332Z (00:00 AEDT on 21 Nov). The first line of the next day is 2026-11-21T00:00:25.703Z, so the stage went quiet for 11.0 h and recovered at 00:00 UTC.
- 2026-11-21: last timer log line 12:25:21.387Z (23:25 AEDT). No timer logs since, until at least 20:12Z.
- The two days total almost the same estimated time (1875.9 s and 1877.9 s, about 31 minutes). That fits a cap on execution duration, as the error text says. The actual cap and how the platform measures it are not confirmed.
- One observed reset, at 00:00 UTC (11:00 AEDT). The reset time is not confirmed in the docs.

## Not covered
- The other 44 deployed apps were not scanned. Any timer that did not run on 20 or 21 November used none of the limit on those days, and would not appear in the logs. Say so if a full scan of all 50 graphs is wanted.
- Before 2026-11-20T00:00Z was not examined.

## Environment change made by the user (not part of build B)
- The user will slow down or deactivate the five timers that run about every 5 minutes (RecomputeBM25Stats in RAG Knowledge Base, CloneOfRAGKnowledgeBase and Clone2OfRAGKnowledgeBase; IngestBatch and LinkResolution in OKF Store) in the ODC Portal, in the apps that own them.
- This is the user's own change to the Development stage, made by the user. It is not part of build B, not an intervention, and not made by Kiro or Mentor. Kiro does not touch any other app.
- Status when recorded: announced, not yet made. What was changed, when, and the new schedules are to be added when the user reports them.
- Effect on the reset signal: Kiro's poll looks for any timer line in the stage logs after 2026-11-21T12:25:21Z. If those timers are deactivated or slowed, the first signal may come from a slower timer (the hourly EmployeeCatalogV2 DailyJobTimer last ran at the top of the hour) and may arrive later than the reset itself.

