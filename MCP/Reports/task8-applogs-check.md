# Task 8: app_logs check for EmployeeCatalogMCP (revision 1)

Run on 2026-11-22, 06:16 to 06:19 AEDT (2026-11-21 19:16 to 19:19 UTC). Read-only: `app_logs`, `app_traces`, `app_health`. No tenant write, no Mentor prompt, no publish. The Mentor session a899ca3b-0707-bf0e-b248-c03509ed6b00 was not used.

## Scope of the check

- App: EmployeeCatalogMCP, app_key debb6b49-7b59-ecf6-b2eb-50a5f78250f3. Stage: Development (key 8b036dbd-6d28-2b5c-c50a-77a6bc07d748).
- Task 8 (changed form): look for any error or warning from `BootstrapTimer`, `BootstrapData` or `BootstrapEmployee` written after the revision 1 publish finished.
- Revision 1 timing (from session.md): deployed 06:05:40 AEDT (19:05:40Z), publish run succeeded about 06:06:20 AEDT (19:06:20Z). The main window starts at 19:06:20Z. Wider windows (from 19:05:00Z, 19:00:00Z and 18:00:00Z) were also queried, because a "when published" timer can start at deployment, before the publish run reports success.

## Queries and results

All `app_logs` queries used severities Debug, Information, Warning, Error unless noted. Every result: `total` 0, no entries.

| # | App filter | Window start (UTC) | Search | Severity | Count |
|---|---|---|---|---|---|
| 1 | app_key | 19:06:20Z | none | all four | 0 |
| 2 | app_key | 19:06:20Z | "Bootstrap" | all four | 0 |
| 3 | app_key | 19:06:20Z | none | Warning, Error | 0 |
| 4 | app_key | 19:06:20Z | "BootstrapTimer" | all four | 0 |
| 5 | app_key | 19:06:20Z | "BootstrapData" | all four | 0 |
| 6 | app_key | 19:06:20Z | "BootstrapEmployee" | all four | 0 |
| 7 | name "EmployeeCatalogMCP" | 18:00:00Z | none | all four | 0 |
| 8 | all apps in stage | 19:00:00Z | "Bootstrap" | all four | 0 |
| 9 | app_key (re-check about 06:17:30 AEDT, after a 45 s wait) | 19:06:20Z | "Bootstrap" | Warning, Error | 0 |
| 10 | app_key (re-check) | 19:05:00Z | none | all four | 0 |

Other read-only calls:

- `app_traces` for the app_key, since 18:00:00Z, no filters: 0 traces.
- `app_health` for the app_key, last 2 hours (17:16Z to 19:16Z), Development: 0 rows, `noData` status `determined`: the app had no traffic in the window. The tool's own rule applies: that is not a statement that the app is healthy.

## Control check on the log source (other apps, counts and timestamps only)

- Stage-wide, last 24 hours, no filter: `total` 2036 entries. The newest returned entry is dated 2026-11-21T12:25:21Z (about 6 h 50 min before these queries). It is a timer-start line from another app in the stage.
- Stage-wide, since 19:00:00Z, no filter: 0 entries. Stage-wide since 12:26:00Z, no filter: 0 entries.
- So the Development stage shows no log entry of any app after 12:25:21Z. The log source returned nothing new for anyone, including the 06:05 to 06:19 AEDT period in which EmployeeCatalogMCP was published.

## Findings

- Errors or warnings from `BootstrapTimer`, `BootstrapData` or `BootstrapEmployee`: **none found**. Zero entries of any severity for the app after the publish.
- The "fix path" of task 8 (error or warning from a bootstrap element) is not triggered.

## What this does and does not prove

- It does not prove the data was inserted. `BootstrapEmployee` writes no "inserted N rows" log line (deviation D-1), so a log search cannot show it either way.
- It does not prove that `BootstrapTimer` ran. The other apps' timers show a "Timer <name>: starting execution" line in this log. No such line exists for `BootstrapTimer`, but the stage has no entries at all after 12:25:21Z, so the absence is not informative. Possible reasons that cannot be told apart from here: the log source is behind or not recording for the stage, the timer has not run yet, the timer ran and was not logged.
- It does not prove there was no error. With the log source silent for the whole stage for about 6 h 50 min, "no error found" means "no error was reported to this log source".
- The first real evidence of the data is the browser check after task 10 (20 rows, Hugo Brandt, Maya Petrov and Quinn Abara inactive, Alice active, values as in spec.md section 10), done with AC-06 in task 12.
- Risk to be aware of: if the timer did not run, that is found only after task 10. The Employee table would then be empty and AC-01 to AC-06 would fail until it is fixed.

## Not done

No ODC Studio, no data view, no ODC Portal check (task 8 no longer includes them). No fix prompt, no publish.
