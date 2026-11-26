# Mentor session and app facts

| Field | Value |
|---|---|
| App name | EmployeeCatalogMCP |
| app_key | debb6b49-7b59-ecf6-b2eb-50a5f78250f3 |
| sessionId | a899ca3b-0707-bf0e-b248-c03509ed6b00 |
| runId (creation turn) | 87be3c2f-be5b-5683-b3ac-90ac0e858268 |
| Mentor conversationId | 52bac87f-1324-eb15-58f1-a0c68804ee1d |
| Creation prompt | MCP/Prompts/001-create-app.md |
| Portfolio key | 2361d977-28e7-c828-d75b-302e87dcb460 (same as EmployeeCatalogMW; name not exposed) |
| Development env key | 8b036dbd-6d28-2b5c-c50a-77a6bc07d748 |

These are the IDs of the restarted attempt (2026-11-22). The IDs of the lost first attempt are in the incident section below.

## Creation turn result (task 4, restart)

- Local times (AEDT, 2026-11-22): pre-send `app_list` re-check and backup of the old result file 05:54:29; session opened just after; creation prompt sent 05:54:45; first poll `working`, no events; terminal `succeeded` seen on the second poll after a 20s pause, noted at 05:55:18 (the poll itself was a few seconds earlier). The run's own events say "Worked for 6s".
- Pre-send check: `app_list` (search "EmployeeCatalog") showed only EmployeeCatalogMW (07a64c21-0c8c-8afb-28ee-5d8530d55cf8, revision 6) and Employee Catalog (31b31b9c-c028-bfee-1811-c6b59aba4b5b). No app named EmployeeCatalogMCP.
- Status: succeeded. `hasMore: false`, no truncated events. A re-read from cursor 0 after the terminal poll returned the same run, so the session and run were still alive at that point.
- assetFacts: one asset, key debb6b49-7b59-ecf6-b2eb-50a5f78250f3. attemptedChange true, changeApplied true, validation errorCount 0, warningCount 18.
- Mentor's answer: created the web app EmployeeCatalogMCP in the given portfolio from the standard web app template, as a draft, not published, no other changes.
- Not published: Mentor said so, no publish was requested, and the app is not in `app_list`. `app_info` for the new key returns 404, the same as the first attempt before its first publish. The app's existence is therefore confirmed by the run's assetFacts only, until the first publish (task 6).
- Session left open on purpose. Task 5 sends the part 1 prompt in this session.
- Full run payload: `result-create.json` in this folder. The lost attempt's payload is `result-create-lost-attempt.json`.

## Lost first attempt: Part 1 data turn (task 5): run lost, outcome unknown

(Everything from here down describes the first attempt, session 29f880cb-69a8-3d38-93d2-bd0c1a879024, and is superseded.)


- Prompt: `MCP/Prompts/002-part1-data.md` (build-prompt --part data output, sent unchanged, asset ref app_key ee94947f-4977-cf9d-8863-0aedede9b3d7).
- Sent in session 29f880cb-69a8-3d38-93d2-bd0c1a879024. runId f12ee6f1-e814-ab30-2ae6-874edd4944b7.
- Polls 1 and 2 returned status `working`. Poll 2 (cursor 7) showed pendingModelChanges: Employee (Created), BootstrapEmployee (Created), BootstrapData (Created), WakeBootstrapTimer (Created), Staff role (Modified), the app module (Modified), Login screen (Modified). Mentor's last reasoning event said it was creating the bootstrap action to seed the 20 employees.
- Poll 3 and every later poll (including cursor 0) returned `status: not_found`, no events. The task 4 creation run d5f0a70b-d0a9-38ce-bdbf-92dcb2589e89 in the same session also returns `not_found` now.
- No terminal result and no completion signals were received. `result-data.json` was NOT written because there is nothing to save.
- App is still unpublished, so app_list (search EmployeeCatalogMCP) and context_entities (app_key) return nothing. They cannot show whether the session still holds the work.
- Nothing was published. No second prompt was sent. No new session was opened.

## Platform incident: Mentor session lost, EmployeeCatalogMCP gone (logged 2026-11-22)

This was a platform incident, not a spec intervention and not a fix. Full entry: `MCP/Reports/interventions.md`, section "Platform incidents". Every value in the first table of this file (app_key, sessionId, runId, conversationId) and the two sections above describe the lost attempt and are superseded once the app is created again.

### Facts

| Item | Value |
|---|---|
| Lost session | 29f880cb-69a8-3d38-93d2-bd0c1a879024 |
| Creation run (task 4) | d5f0a70b-d0a9-38ce-bdbf-92dcb2589e89 |
| Part 1 run (task 5) | f12ee6f1-e814-ab30-2ae6-874edd4944b7 |
| app_key of the lost app | ee94947f-4977-cf9d-8863-0aedede9b3d7 |
| Part 1 prompt file | MCP/Prompts/002-part1-data.md (7860 bytes) |
| Creation prompt file | MCP/Prompts/001-create-app.md |

### Times

Times below are local (AEDT, UTC+11) on 2026-11-22. The MCP responses carried no timestamps that were recorded, so the exact send time of each run and of each poll is not recorded. The only recorded durations and times are these:

| Event | Time |
|---|---|
| Creation turn duration (from the run's events) | "Worked for 6s" |
| `Reports/scope-baseline.md` last written (read-only checks before the creation turn) | 05:42:06 |
| `Prompts/001-create-app.md` last written | 05:42:07 |
| `result-create.json` written (creation run result saved) | 05:43:13 |
| `Prompts/002-part1-data.md` last written | 05:45:41 |
| Part 1 run sent | not recorded (after 05:45:41) |
| Poll 1 and poll 2 (`working`) | not recorded |
| First poll that returned `not_found` | not recorded |
| This file's lost-run section last written | 05:49:59 |
| User's check in ODC Studio | not recorded (after 05:49:59) |
| Re-check of the tenant for this log (`app_list`, `app_info`) | 2026-11-22, during the incident logging invocation of task 4 (restart) |

### Symptoms

- Part 1 run: poll 1 `working`, poll 2 `working` (cursor 7, with pendingModelChanges listed in the section above), then `not_found` on poll 3 and on every later poll, including cursor 0, with no events.
- The task 4 creation run in the same session also returned `not_found`, although it had succeeded and its result was saved to `result-create.json`.
- No terminal status and no completion signals were ever received for the part 1 run.

### Checks after the incident

- User check in ODC Studio: EmployeeCatalogMCP does not exist.
- Kiro check, read-only: `app_list` with search "EmployeeCatalog" returns only `EmployeeCatalogMW` (07a64c21-0c8c-8afb-28ee-5d8530d55cf8) and `Employee Catalog` (31b31b9c-c028-bfee-1811-c6b59aba4b5b). `app_info` for ee94947f-4977-cf9d-8863-0aedede9b3d7 returns 404 Not Found.

### What was lost

- The unpublished EmployeeCatalogMCP app created in task 4, with its app_key.
- The in-flight part 1 changes that were pending in the session: Employee, BootstrapEmployee, BootstrapData, the WakeBootstrapTimer signature, the Staff role change, and the Login screen change (plus the app module change).
- There is no `result-data.json`, because the run never produced a result.

### What was not lost

- `spec.md`, `requirements.md`, `design.md`, `tasks.md`.
- The prompt files `Prompts/001-create-app.md` and `Prompts/002-part1-data.md`.
- `result-create.json` (a record of the lost creation run), `Reports/scope-baseline.md`.

### State

- Nothing was published. No revision of EmployeeCatalogMCP exists on the tenant.
- EmployeeCatalogMW was not touched. Its latest revision is still 6 (checked again after the incident).
- `Prompts/002-part1-data.md` stays on disk as the record of the lost turn. The new send of the same text is not saved again. If the text of a new send differs, it is saved under the next free number; otherwise the reuse is noted here.
- Task 4 restarts from the beginning: a new session, a new creation turn, a new app_key. Nothing from the lost session is reused.

## Part 1 data turn, re-run (task 5, restart attempt, session a899ca3b-0707-bf0e-b248-c03509ed6b00)

- Prompt: reused `MCP/Prompts/002-part1-data.md`. `build-prompt --part data` was run again on the current spec.md and its output (7860 bytes, kept as `MCP/Reports/scratch/part1-data.rerun.md`) is byte-identical to that file (`cmp`), so no new numbered prompt file was saved.
- Sent unchanged in session a899ca3b-0707-bf0e-b248-c03509ed6b00, asset ref app_key debb6b49-7b59-ecf6-b2eb-50a5f78250f3. Covered by the go/no-go of task 3 and the user's confirmation to go straight into task 5.
- Sent at 2026-11-22 05:57:04 AEDT (time noted just before the send call).
- **runId: 6d9624d6-584a-4809-8474-56b53ea9ae28** (written before polling). `pollIntervalMs` advertised: 1000.
- Poll log (local AEDT):
  - Poll 1, right after the send (about 05:57:10, exact time not noted): `working`, cursor 3, reasoning events only.
  - Poll 2, 05:58:12: `working`, cursor 8. pendingModelChanges: Employee (Created), BootstrapEmployee (Created), BootstrapData (Created), WakeBootstrapTimer (Created, IActionSignature, key suffix `#WakeTimer`), Staff (Modified, IAppRole), EmployeeCatalogMCP module (Modified), Login (Modified, IMobileScreen).
  - Poll 3, 05:58:51: **`succeeded`**. "Worked for 55s" in the run's own events. No `not_found` at any point (no P-2).
  - Replay from cursor 0, 05:59:02: same terminal result. Saved as `result-data.json` in this folder (5 pendingModelChanges snapshots are repeats of the same 7 changes).
- Completion signals: assetFacts for debb6b49-7b59-ecf6-b2eb-50a5f78250f3: attemptedChange true, changeApplied true, validation errorCount 0, warningCount 18, no turn-level error.
- Report: `render-report --label data` run, exit 0 ("Landed: yes (succeeded, no validation errors)"). Written to `build-report.md` in this folder (05:59:44 AEDT). It will be re-rendered with later turns.
- Mentor did not publish: no publication key or "published" message in the events, Mentor's answer says "It isn't published", and `app_list` (search "EmployeeCatalog") still shows only EmployeeCatalogMW (revision 6, unchanged) and Employee Catalog (revision 6). The new app is still not listed, as expected for an unpublished draft. `context_entities` for the app_key returns 0 rows for the same reason, so the model cannot be read back from the tenant until the task 6 publish.
- Session left open (used again in tasks 6 to 10).

### Task 5 check against spec.md and the part 1 prompt (from Mentor's summary and the pendingModelChanges; the tenant cannot be read back before publish)

| Check | Result | Evidence |
|---|---|---|
| Employee: FirstName Text 50, LastName Text 50, Email Email 250, JobTitle Text 100, IsActive Boolean, automatic Id Long Integer | Matches | Mentor summary lists exactly these; Employee (Created) in pendingModelChanges |
| Staff is the only role | Matches | Mentor renamed the template's default role to Staff (IAppRole Modified, not Created); 1 role |
| BootstrapEmployee once | Matches | One IServerAction Created |
| BootstrapData once | Matches | One IServerAction Created |
| BootstrapTimer once | Not confirmed independently | Timers do not appear as an element type in pendingModelChanges. Mentor says it created BootstrapTimer. The WakeBootstrapTimer signature (key suffix `#WakeTimer`) is the timer's companion element and supports that one timer exists. Confirm in the task 6 graph |
| Nothing else added | Two points below | Module (Modified) is expected; Login screen (Modified) is not asked for |
| 20 sample rows, values as given | Per Mentor's summary only | Cannot be read back until publish; task 8 and task 12 check them |

Judgement of the elements seen in the first attempt:

- WakeBootstrapTimer (IActionSignature, Created): not named in spec.md or the prompt. The `#WakeTimer` key suffix marks it as the wake signature ODC creates with a timer, so it follows from the BootstrapTimer the prompt asks for. Treated as expected, to be confirmed in the task 6 graph.
- Login screen (Modified): the prompt says no screens, screen logic, navigation or menu entries. Mentor modified the template Login screen without saying so in its summary, and no part of spec.md asks for it. Likely a side effect of renaming the template's role to Staff, but it is unverified. Deviation reported to the user. The task 6 graph baseline and the task 10 comparison will show what actually differs.

### Deviations from the prompt found in Mentor's summary

- D-1: the "Bootstrap<Entity>: inserted N rows / skipped, N present" line is returned as an output `Message` of BootstrapEmployee, not written to the runtime log ("I found no log action to call"). The prompt (constraint 7) asks each Bootstrap<Entity> to log the line. Task 8 searches app_logs for `BootstrapEmployee: inserted 20 rows`, so unless something writes that line to the log, task 8 will find nothing.
- D-2: Staff has no View permission on Employee in the model (Mentor: "I set up no permission on Employee for Staff"). spec.md section 2 says Staff has View access to Employee. The prompt's data constraints do not name entity permissions explicitly, and task 9 checks "Staff has View access to Employee only", so this is carried to part 2.

## Publish part 1 (task 6)

- Confirmed by the user ("Yes, publish") for this one publish: publish the data model of EmployeeCatalogMCP to its development environment, from session a899ca3b-0707-bf0e-b248-c03509ed6b00.
- Prompt: `MCP/Prompts/003-publish-part1.md`, asset ref app_key debb6b49-7b59-ecf6-b2eb-50a5f78250f3.
- Sent at 2026-11-22 06:05:4x AEDT (file written 06:05:29, send call right after).
- **runId (publish turn): d2ff1b12-ee3b-9672-5d3d-a41270e6f6cf** (written before polling). `pollIntervalMs` advertised: 1000.
- Poll 1 (about 06:05:50 AEDT): `working`, cursor 4. Events: publishStarted, then **publishAccepted: revision 1, publicationKey 5f1513df-48de-9153-26e3-cac40540a1aa**. Not yet terminal. No second publish will be sent.
- publish_status (publication key 5f1513df-48de-9153-26e3-cac40540a1aa), about 06:05:55: `Running`, `in_progress`.
- Poll 2 of the run, about 06:06:20 AEDT (after a 20s pause): **`succeeded`**. Events: `publishSucceeded` revision 1; "Worked for 40s"; Mentor: revision 1 is live in development with the note, no other changes, data not checked. assetFacts: attemptedChange false, changeApplied false (expected for a publish-only turn); pendingModelChanges empty; no validation block.
- publish_status, about 06:06:20: status `Finished`, **outcome `success`**, applicationRevision 1. Not indeterminate.
- env_app (Development, 06:06:30): revision 1 deployed, buildKey 911af749-44d0-ea58-f118-bea927ba80e2, deploymentKey 5f1513df-48de-9153-26e3-cac40540a1aa, deploymentDateTime 2026-11-21T19:05:40.681Z (06:05:40 AEDT). Revision matches the publication. URL: https://your-tenant-dev.outsystems.app/EmployeeCatalogMCP
- app_revisions: one revision, 1, revisionDateTime 2026-11-21T19:05:40.552Z, modelDigest 13198b24-fbd6-794c-8f89-397e465092af.
- Only one publish turn was sent. Result saved as `result-publish-part1.json` in this folder.
- Mentor session a899ca3b-0707-bf0e-b248-c03509ed6b00 is left open for tasks 9 and 10.
- Open item for task 9 (D-2): Staff has no View permission on Employee in the model (Mentor's summary). To be checked in task 9, not an intervention.
- Graph verification (about 06:07 to 06:12 AEDT): whole-app graph read in one page (`has_more` false), header revision 1 = published revision. Saved as `MCP/Reports/graphdiff/1.xre` (baseline). Notes, findings and the Login analysis: `MCP/Reports/graphdiff/1-baseline-notes.md`. Read-only reference copies of EmployeeCatalogMW r6 and "Employee Catalog" r6 graphs are in `MCP/Reports/graphdiff/reference/`.
- Roles lookup (task 7 pre-step), first call 06:06 returned 0 rows (index not yet updated); calls at about 06:10 returned **Staff, key f9f3f634-4449-ffea-b5c8-bae77af37d07**, total 1, index timestamp 2026-11-21T19:07:17Z (06:07:17 AEDT). The Staff role exists on the tenant.
- EmployeeCatalogMW re-checked read-only at 06:12:11 AEDT: latest revision still 6, modelDigest 35873f58-1351-11c1-6d2d-9ad864ae3a67 (unchanged from `Reports/scope-baseline.md`).
- Findings carried to the orchestrator: F-1 Email length 256 vs 250; F-2 Staff permission on all six template screens and a CheckStaffRole step in Login; F-3 BootstrapEmployee seeds from one JSON literal (hash matches the spec's 20 records). Details in `1-baseline-notes.md`.

## User decisions on the task 6 findings (2026-11-22)

- **F-1 Email length 256 vs 250: logged as deviation D-3** in `MCP/Reports/interventions.md` (Deviations section), not as an intervention. Facts: Mentor's summary said 250; the published graph (revision 1) shows 256; the two other apps read read-only (EmployeeCatalogMW r6 and Employee Catalog r6) also show 256 for Email; no AC tests the length; nothing was changed. Note: probably fixed by the platform for the Email type, not confirmed in the docs. The user decided to log it and not fix it.
- **F-2 (Staff permission on the six template screens, CheckStaffRole step in Login): accepted by the user.**
- **F-3 (BootstrapEmployee seeds from one JSON literal): accepted by the user.**
- Task 7 (assign Staff to the test user) is being done by the user. Not marked or edited here.
- D-2 (Staff has no View permission on Employee) is still open and goes to task 9.

## Rule: reference graphs are for checking only

The graphs in `MCP/Reports/graphdiff/reference/` (EmployeeCatalogMW r6 and Employee Catalog r6) are read-only references for checking. Nothing from them is ever used in a Mentor prompt. Recorded also in `MCP/Reports/graphdiff/1-baseline-notes.md`.

Check of the existing prompts (`MCP/Prompts/001-create-app.md`, `002-part1-data.md`, `003-publish-part1.md`, 2026-11-22): none uses content from the reference files. 001 and 003 contain only the app name, the portfolio key, the app_key and the publish note. 002 is the `build-prompt --part data` output built from spec.md. A search of the three files for the names, keys and element names of the reference apps (EmployeeCatalogMW, xxxxxxxx, xxxxxxxx, `reference/`, graphdiff) found only the product name "Employee Catalog" in spec.md's own text. The 20 sample records in 002 come from build A's BRD through spec.md section 10, as the design says. They were not taken from the graph files.

## Task 8 (changed form): app_logs check, 2026-11-22 06:16 to 06:19 AEDT

- Task 8 now only checks `app_logs` for errors or warnings from BootstrapTimer, BootstrapData and BootstrapEmployee after the revision 1 publish finished. The manual data check (20 rows, Hugo Brandt, Maya Petrov and Quinn Abara inactive, Alice active, values as in spec.md section 10) moved to after task 10, in the browser, with AC-06 in task 12.
- Result: no log entry of any severity for EmployeeCatalogMCP in Development since 19:06:20Z (publish finished) or since 18:00Z; no error or warning from the bootstrap elements. `app_traces` 0, `app_health` no traffic. The stage's log source itself shows no entry newer than 2026-11-21T12:25:21Z for any app, so the empty result does not show whether the timer ran or the data was inserted. Details: `MCP/Reports/task8-applogs-check.md`.
- No tenant write, no Mentor prompt, no publish. The Mentor session stays open.

## Task 7 done and task 8 outcome (2026-11-22)

- Task 7 done: user assigned Staff to the test user (reported by the user). Kiro did not check this on the tenant.
- The `app_logs` check (task 8) was inconclusive: the Development log source was silent for all apps (no entry newer than 2026-11-21T12:25:21Z), so it does not show whether BootstrapTimer ran. The data check in the browser after task 10 (with AC-06 in task 12) decides whether BootstrapTimer ran and the 20 rows were inserted.

## Mentor part 2: screens (task 9)

- Prompt: `MCP/Prompts/004-part2-screens.md` (`build-prompt --part screens` output, 7483 bytes, saved before sending). Sent unchanged in session a899ca3b-0707-bf0e-b248-c03509ed6b00 (checked valid by a read of publish run 59946488 from cursor 0, status succeeded), asset ref app_key debb6b49-7b59-ecf6-b2eb-50a5f78250f3.
- Confirmed by the user ("Yes, send it") for this one turn, which does not publish.
- Sent at 2026-11-22 about 06:25 AEDT (date noted at 06:24:15 just before the send).
- **runId: 52f44c49-aeb3-fc4b-176b-ed3352ff7571** (written before polling). `pollIntervalMs` advertised: 1000.
- Poll log (local AEDT, approximate): poll 1 right after the send, `working`, cursor 3; poll 2 about 40s later, `working`, cursor 8, pendingModelChanges listed (see below) and a reasoning event that said the agent hit a compilation error and was inspecting the app structure; poll 3 about 45s later, **`succeeded`**, "Worked for 54s". No `not_found` at any point.
- Replay from cursor 0 saved as `result-screens.json` in this folder (valid JSON). Completion signals for debb6b49-7b59-ecf6-b2eb-50a5f78250f3: attemptedChange true, changeApplied true, validation errorCount 0, warningCount 18 (same count as part 1; Mentor says the warnings are the template's font URLs in the stylesheet), no turn-level error.
- Report: `render-report --label data --label screens` run, exit 0, "Landed: yes (succeeded, no validation errors)" for both turns. Written to `build-report.md` in this folder. The report lists the build turns only (data, screens). The publish turn of task 6 and the platform incident are not in it, as the skill specifies. No fix turn exists so far.
- Mentor did not publish: no publishStarted, publishAccepted or publicationKey event in the run, Mentor says "I haven't published". Tenant check after the turn: `app_revisions` for the app_key still shows one revision (1, modelDigest 13198b24-fbd6-794c-8f89-397e465092af); `app_list` shows EmployeeCatalogMCP revision 1, EmployeeCatalogMW revision 6 and Employee Catalog revision 6, all unchanged.
- pendingModelChanges of the run (the only source for what changed, because the app is unpublished and the lookups only see published revisions): Employee_List (Created, IMobileScreen), Employee_Detail (Created, IMobileScreen), EmployeeCatalogMCP module (Modified), Menu (Modified, IMobileBlock). Nothing else. No role, entity, Bootstrap* action, timer or Login change.

### Task 9 check against spec.md

| Check | Result | Evidence |
|---|---|---|
| Only Employee_List and Employee_Detail created | Matches | Exactly two Created entries, both screens. Menu block and module are Modified, which is the menu entry (Mentor: one `Employees` link to Employee_List) and the module's own change. One screen action `Search` is part of Employee_List. |
| Both screens require Staff | Per Mentor's summary only | "both in MainFlow and restricted to the Staff role". Not confirmed independently: the roles and screens lookups cannot see an unpublished app. Task 10 graph and task 11 lookups settle it. |
| Staff has View access to Employee only | Not met as a model setting, and cannot be (open, see D-2) | No role change in this turn. In turn 1 Mentor said it set no permission on Employee for Staff. The ODC docs found (outsystems-docs, odc, synced 2026-10-28T09:05:12Z) describe access control through screen roles and role checks, and entity-level View/Edit access only as a notation in the requirement document for Mentor Web. No doc found for an entity-level permission setting in the model. In practice Staff can only read Employee through the two Staff-only screens, and no screen or action creates, edits or deletes. No fix turn sent: the spec asks for something no model element is known to express. Decision for the user. |
| Bootstrap elements unchanged | Matches | No Bootstrap* or timer entry in pendingModelChanges; Mentor says "The bootstrap actions and timer are unchanged". Task 10 graph comparison against `1.xre` confirms. |

Other points from Mentor's summary, for the task 10 comparison and task 12 browser check:
- Employee_List lists only IsActive = true, sorted by last name then first name; the search input filters first or last name as the user types; "No employees found" shows when nothing matches; the first name in each row opens Employee_Detail (AC-01, AC-02, AC-03, AC-05). Mentor did not open the screens in a browser.
- Employee_Detail takes an `EmployeeId` input, shows the five attributes in a card with a link back, read-only (AC-04).
- No default landing screen is set. The user opens Employee_List from the menu or by its URL.
- Mentor reported a compilation error in the middle of the turn and recovered; the final validation is 0 errors.
- The Search action refreshes the list from the search input. Whether it matches FirstName OR LastName only (not JobTitle or Email) is checked in the browser (AC-02) and in the task 10 graph.
## Decisions before task 10 (user, 2026-11-22). Recorded only; no task started, no tenant write.
1. **D-2 is not a deviation.** ODC has no entity-level View setting, so D-2 is not logged as a deviation (this overrides the "decision for the user" wording in the task 9 check table). The requirement "Staff has View access to Employee only" is met if both screens (Employee_List, Employee_Detail) require Staff and the app has no way to create, edit or delete Employee records. After the task 10 publish, check both points from the published graph (screen roles on the two screens, and no create/update/delete of Employee in any screen, screen action, server action or timer other than BootstrapData's insert of the 20 sample rows). Record D-2 as **resolved** or **failed**.
2. **Mentor's extras from part 2** are recorded as extras for the final report. They are not interventions and no fix turn is sent: sort by last name then first name, the "No employees found" message, and the link back to the list on Employee_Detail.
3. **Stop after the task 10 graph check.** When the graph comparison and the D-2 check are done, stop and give the user the app URL for the browser check. Do not start task 11 or 12 before the user replies.

## Publish part 2 (task 10)

- Pre-check (read-only, about 06:33 AEDT): `app_revisions` shows one revision (1); session a899ca3b-0707-bf0e-b248-c03509ed6b00 alive (cursor-0 read of screens run ffc555e2 returned the same terminal result).
- Confirmed by the user ("Yes, publish") for this one publish: publish the screens of EmployeeCatalogMCP to its development environment.
- Prompt: `MCP/Prompts/005-publish-part2.md`, asset ref app_key debb6b49-7b59-ecf6-b2eb-50a5f78250f3.
- Sent at 2026-11-22 about 06:34:25 AEDT (date noted at 06:34:21 just before the send).
- **runId (publish turn): a05ef96c-b747-bf05-2cd6-087be9ab10eb** (written before polling). `pollIntervalMs` advertised: 1000.
- Poll 1 (about 06:34:30): `working`, cursor 4. Events: publishStarted, then **publishAccepted: revision 2, publicationKey 92338f80-b230-44fb-b754-d8e75c2db824**. No second publish was sent.
- Poll 2 (after a 30s pause, about 06:35:10): **`succeeded`**. Events: pendingModelChanges empty, `publishSucceeded` revision 2, "Worked for 28s". Mentor: revision 2 is live in development with the note, no other changes. assetFacts: attemptedChange false, changeApplied false (expected for a publish-only turn).
- publish_status (92338f80-b230-44fb-b754-d8e75c2db824): status `Finished`, **outcome `success`**, applicationRevision 2. Not indeterminate.
- env_app (Development): revision 2 deployed, buildKey da5bdf11-e30c-cecd-2a51-609710a4da06, deploymentKey 92338f80-b230-44fb-b754-d8e75c2db824, deploymentDateTime 2026-11-21T19:34:40.088Z (06:34:40 AEDT). URL: https://your-tenant-dev.outsystems.app/EmployeeCatalogMCP
- app_revisions: revisions 2 (modelDigest 254db6a1-38f4-e63a-e64e-93d993ab2d2f) and 1. Result saved as `result-publish-part2.json` in this folder (condensed copy of two polls).
- Graph verification: whole-app graph read in one page (`has_more` false), header revision 2 = published revision. Saved as `MCP/Reports/graphdiff/2.xre`. Diff: `MCP/Reports/graphdiff/1-to-2.diff`. Notes and D-2 check: `MCP/Reports/graphdiff/2-notes.md`.
- Result: 0 nodes and 0 edges removed; 367 nodes and 754 edges added, all part of the two screens and the menu link; 2 nodes changed (MainFlow and Menu, metadata only). Employee attributes, Staff role, Bootstrap* elements, the six template screens: unchanged. Out of scope: O-1, the module's DefaultScreen is now Employee_List (Mentor said it set none).
- D-2: resolved (both screens require Staff; the only call to an Employee create, update or delete action is CreateEmployee in BootstrapEmployee).
- Mentor session a899ca3b-0707-bf0e-b248-c03509ed6b00 is left open for task 11 (release it there).
- Per the user's decision, work stops after the task 10 graph check.

## Change add-department: Prompt A (task 2)

- Spec: `MCP/.kiro/specs/add-department/`. Prompt: `MCP/Prompts/006-add-department-data.md` (design.md "Prompt A", saved unchanged). Baseline: revision 4, `MCP/Reports/graphdiff/4.xre`.
- New Mentor session: **2a37df04-4249-c799-44b7-22c99914b5c1**. Data turn runId: **c4c8018a-f525-4e6c-9098-2dd150e34e66** (2m 21s). Result saved as `MCP/Reports/add-department/result-data.json`. Left open for tasks 3, 5 and 6.
- Result: attemptedChange true, changeApplied true, validation errors 0 (18 warnings), no turn-level error. Not published: no publication key, `app_revisions` still shows revision 4 as the latest. No fix turn.
- Mentor's summary: Department (static, not public, attributes Id and Label, 4 records: Engineering, Finance, Human Resources, Sales); Employee.DepartmentId (Department Identifier, not mandatory, delete rule **Protect**, the default); the one-time update in BootstrapData after the BootstrapEmployee call (fetches employees with an empty DepartmentId, matches by Email from one JSON literal, saves with UpdateEmployee, no SQL, a second run changes nothing); DepartmentId on each of the 20 seed records in BootstrapEmployee. The model cannot be read back before publish, so task 4 settles these.

### DepartmentSeed (user decision)

- Mentor also created the structure `DepartmentSeed` (attributes `Email` and `Department`). It is a helper structure that the update needs to deserialize the JSON table into a list. Prompt A did not name it.
- **Decision: keep it. Not a deviation.** Recorded by the user's reasoning: Prompt A only excluded new server actions, timers and Bootstrap elements, and a structure is none of those. Mentor named it in its summary, as the prompt's last constraint asks.
- For task 4: list `DepartmentSeed` as an expected helper structure, not as a change outside the intended scope. Task 4 still compares the full graph and reports anything else that is new.
- Also for task 4: the change events list Employee_List and Employee_Detail as "Modified" although no screen was changed. Probably the derived update of the Employee references; the graph diff decides.

### Timing note (P-2), from the user

- Prompt A was sent at about 09:30 AEDT, before the daily timer limit reset (P-2).
- BootstrapTimer will be blocked on publish 1 and on publish 2, so DepartmentId will **not** be filled after those publishes.
- After 11:00 AEDT the user clicks **Run now** on BootstrapTimer in the ODC Portal. That runs the update through the timer itself, not through RunTimer.
- The browser check in task 8 waits until then. Empty Department values before that point are expected and are not a failure.
