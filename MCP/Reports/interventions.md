# Interventions log: EmployeeCatalogMCP

Interventions are fixes sent to Mentor after the first build, one prompt at a time, each with the exact prompt. Manual work in ODC Studio is logged here too. Numbered entries are spec interventions only.

## Interventions

### Manual intervention M-1: RunTimer screen added in ODC Studio to run BootstrapData by hand (2026-11-22)

| Item | Value |
|---|---|
| Type | Manual work in ODC Studio. Last resort, because the bootstrap could not run by timer. Not a Mentor prompt: no prompt file, no Mentor session, no run |
| Reason | Platform incident P-2. The Development stage's daily timer limit blocks `BootstrapTimer` (Run now failed with OS-TMR-42900 at 07:17 AEDT) until the reset, expected about 11:00 AEDT and not confirmed |
| Made by | The user, in ODC Studio |
| Published | Revision 4, 2026-11-21T21:01:27.066Z (2026-11-22 08:01:27 AEDT), deployed to Development 21:01:27.448Z, build key 8d56a5ae-2d78-2dfc-738d-57562fdced1c |
| Also in Studio | `Employee` was saved at 2026-11-21T20:13:51Z (07:13:51 AEDT). No property or attribute of it differs from revision 3: only the last-modified date and tool marker changed |
| What was added (from the published graph) | Screen `RunTimer` in `MainFlow`, login required, permission Staff only. One Button whose On Click runs the screen action `RunTimerOnClick`: Start, call server action `BootstrapData`, message "Employees Bootstrapped.", End. No menu link to it |
| Graph comparison | Revision 3 to revision 4: `MCP/Reports/graphdiff/3-to-4.diff`, `4.xre` SHA-256 5f810164e45c26b836f8ece75e60d764fc9aeca583d37f9ace51167200ecabd9. 38 nodes added, 0 removed, 2 changed (`MainFlow`, `Employee`, tool markers and dates only). Every added node belongs to the new screen. Nothing changed in `BootstrapData`, `BootstrapEmployee`, `BootstrapTimer`, `Employee_List`, `Employee_Detail`, the Staff role, the menu or the module's default screen |
| Run time and browser result | User report, browser, after the run: Employee_List shows 17 rows on one page, sorted by last name, with no Hugo, Maya or Quinn. Alice's detail shows five values, read-only, Active = Yes. Not provided (left as placeholders in the user's message): the click time, the message shown, the results of the searches "Alice", "Recruiter" and "Hugo", and whether the 07:13:51 save of `Employee` was the user's Studio session |
| Status | In place. **Kept by the user's decision (2026-11-22).** It will not be removed and no removal prompt is prepared. Recorded as deviation D-4 for the final report |

**Notes**

- `RunTimerOnClick` always shows "Employees Bootstrapped." after `BootstrapData` returns. `BootstrapData` ignores the output of `BootstrapEmployee`, so the message is the same whether 20 rows were inserted or the action skipped. Only Employee_List shows whether the data exists.
- Running the action from a button is not a timer run, so P-2 does not apply to it.
- This proves `BootstrapData` and `BootstrapEmployee` only. It does not prove that `BootstrapTimer` inserts on publish. With data present, a timer run would skip.
- D-2 re-check on revision 4: the only call to any Employee create, update or delete action is still the one `CreateEmployee` in `BootstrapEmployee`. `BootstrapData` is now called by `BootstrapTimer` and by `RunTimerOnClick`. See `MCP/Reports/check-2-2026-11-22.md`.

### Intervention I-1: Department record names did not match their Labels (add-department, 2026-11-22)

| Item | Value |
|---|---|
| Spec | `MCP/.kiro/specs/add-department/` (follows task 4, before task 5) |
| Reason | The record names did not match their Labels. Found by the graph check after publish 1 (finding F-1 in `MCP/Reports/graphdiff/4-to-5-notes.md`). Invisible in the browser |
| Found in | Revision 5 (publish 1, publication key 2419713c-d7ef-3106-f0c7-f2528dfb5698). By Id the Labels were right (1 Engineering, 2 Finance, 3 Human Resources, 4 Sales), but the record at position 0 was named Finance (Id 1, Label Engineering), position 1 HumanResources (Id 2, Finance), position 2 Engineering (Id 4, Sales), position 3 Sales (Id 3, Human Resources) |
| Mentor session | 2a37df04-4249-c799-44b7-22c99914b5c1 |
| Fix prompt | `MCP/Prompts/010-fix-department-record-names.md`. Confirmed by the user before sending. Sent unchanged |
| Fix run | 2c7fa05a-1824-3ae7-6ae3-40a20fb6b548, succeeded in 20 s. assetFacts: attemptedChange true, changeApplied true, 0 validation errors, 18 warnings. Result: `MCP/Reports/add-department/result-i1-fix-records.json`. Pending changes: four `IStaticEntityRecord` elements modified (one step used the temporary name "Engineering2") |
| Publish prompt | `MCP/Prompts/011-publish-fix-department-record-names.md`. Confirmed by the user before sending. Sent unchanged |
| Publish run | e495a911-fd93-1356-d402-5f29aaf99fd7, succeeded in 28 s. **Revision 7**, publication key 027d5b64-ff46-b1b9-b0c5-af6eaa7c5070, 2026-11-21T22:56:22Z, modelDigest 9bfe03ed-2029-7222-1490-579d50506088. Mentor auto-merged revision 6 (see U-2). Result: `MCP/Reports/add-department/result-publish-i1.json` |
| Graph comparison | `MCP/Reports/graphdiff/5-to-7.diff` and `5-to-7-notes.md`, `7.xre` SHA-256 99250cf08122d67a2e40b9daaecf5ddf907f2dacd76ade3ec57368ccb3c911fd. 0 nodes added, 0 removed, 7 changed. 0 edges differ |
| Result | **Names fixed; positions unchanged; handled by sorting the dropdown by Id.** The four record names now equal their Labels. Ids and Labels unchanged. Seed and update literal hashes unchanged (`808c85070a`, `ce1312410b`). The record positions are unchanged (Id 1, 2, 4, 3), so a dropdown in record order would read Engineering, Finance, Sales, Human Resources. Three further nodes of `BootstrapData` changed from revision 6 (U-2), not from I-1 |
| Decision (user, 2026-11-22) | No I-2. Accept the record positions as they are. Prompt B (design.md, item 3) is changed to sort the dropdown by Department Id ascending. That is a design change to an unsent prompt, not an intervention |
| Status | Closed. Names fixed in revision 7 |

## Deviations

Deviations are differences between what the skill or the prompt required and what Mentor built, where the user decided not to send a fix. They are not interventions and are not numbered in the Interventions list above.

### Deviation D-1: Deviation from the skill's own guardrail, bootstrap action does not log "inserted N rows" (decided 2026-11-22)

| Item | Value |
|---|---|
| Task | 5 (part 1 data), found in Mentor's summary; affects task 8 |
| Run | 6d9624d6-584a-4809-8474-56b53ea9ae28 (session a899ca3b-0707-bf0e-b248-c03509ed6b00) |
| Prompt file | MCP/Prompts/002-part1-data.md, constraint 7 |

**What the skill and the prompt required.** The skill's data guardrail (and constraint 7 of the prompt, sent unchanged) says each `Bootstrap<Entity>` logs one line: "Bootstrap<Entity>: inserted N rows" or "Bootstrap<Entity>: skipped, N present". The skill's Step 5, item 5 then checks the sample data by reading the app's runtime logs for that line.

**What Mentor built.** `BootstrapEmployee` returns the text "inserted N rows" as an output `Message` instead of writing it to the runtime log. Mentor's summary says it found no log action to call. No log line is written, so a search of `app_logs` for "Bootstrap" is not expected to find `BootstrapEmployee: inserted 20 rows`.

**Decision (user).** No fix prompt. The deviation is kept as built.

**Consequence.** Task 8 is changed from an `app_logs` check to a manual data check by the user (row count, the inactive records, an active Alice, values compared with spec.md section 10). Task 8 text in `.kiro/specs/employee-catalog/tasks.md` was edited accordingly. `design.md` still describes the `app_logs` check in build-flow item 7, in the AC-06 traceability row and in expected gap 5. It was not edited.

**Update (2026-11-22, later).** Task 8 was changed again: it now only checks `app_logs` for errors or warnings from the bootstrap elements, and the manual data check moved to after task 10, in the browser, with AC-06 in task 12. `design.md` was then edited in those three places (build-flow item 7, the AC-06 traceability row, expected gap 5) to say the same. Result of the task 8 check: `MCP/Reports/task8-applogs-check.md`.

### Deviation D-3: Email length is 256, requirements say 250 (decided 2026-11-22)

D-2 (Staff has no View permission on Employee in the model) is recorded in `MCP/spec-driven-build/EmployeeCatalogMCP/session.md` and carried to task 9. It has no decision yet, so it has no entry here. D-3 is the next free id.

| Item | Value |
|---|---|
| Task | 5 (part 1 data), found in the task 6 graph baseline (finding F-1) |
| Run | 6d9624d6-584a-4809-8474-56b53ea9ae28 (session a899ca3b-0707-bf0e-b248-c03509ed6b00) |
| Published revision | 1 (publication key 5f1513df-48de-9153-26e3-cac40540a1aa) |
| Details | `MCP/Reports/graphdiff/1-baseline-notes.md`, finding F-1 |

**What was required.** requirements.md (Glossary) and spec.md section 3 say Email is of type Email with length 250. The prompt `MCP/Prompts/002-part1-data.md` carried that unchanged.

**What was built.** Mentor's summary said Email 250. The published graph (revision 1, `1.xre`) shows `Length: 256` for Employee.Email. The two other apps read read-only for comparison (EmployeeCatalogMW r6 and Employee Catalog r6) also show 256 for their Email attribute.

**Note.** Probably fixed by the platform for the Email type, not confirmed in the docs. The docs search (outsystems-docs, odc, synced 2026-10-28) returned no page on the Email length.

**Facts.** No AC tests the length. Nothing was changed. No fix prompt was sent.

**Decision (user).** Log it as a deviation, not an intervention, and do not fix it.

### Deviation D-4: Extra screen RunTimer, added by the user in ODC Studio, kept (decided 2026-11-22)

| Item | Value |
|---|---|
| Requirement | `requirements.md` and `spec.md` section 8 (out of scope): no screen other than Employee_List and Employee_Detail |
| What exists | Screen `RunTimer` in `MainFlow`, published in revision 4 (2026-11-21T21:01:27Z). Added by the user in ODC Studio, not by Mentor. Logged as manual intervention M-1. It is not in `requirements.md` or `spec.md` |
| Access | Login required, permission Staff only. Not in the menu. Reachable by its URL |
| Effect | A Staff user can trigger `BootstrapData` with one button. `BootstrapEmployee` inserts the 20 fixed records only when the Employee table is empty, and skips otherwise. No create, edit or delete of any other kind is reachable |
| D-2 | Stays resolved for create, edit and delete, with this note: the only call to an Employee create, update or delete action is still `CreateEmployee` in `BootstrapEmployee`. What changed is that a Staff user can now trigger that insert, not only the timer. Evidence: `MCP/Reports/check-2-2026-11-22.md`, `MCP/Reports/graphdiff/3-to-4.diff` |
| Revision 9 addition (2026-11-22, task 9 of add-department) | A second button "Run Employee Dept" on `RunTimer`, with an empty client action `RunEmployeeDeptOnClick` (Start and End only, no call). Added by the user in ODC Studio, revision 9. The user says it was a test that was abandoned. It was not removed. No functional effect: the button calls nothing and writes nothing. Logged as U-3. Evidence: `MCP/Reports/graphdiff/8-to-9.diff` and `8-to-9-notes.md` |
| App and requirements | They now disagree on the screen list. This is reported. `requirements.md` and `spec.md` are not changed |
**Decision (user).** Keep `RunTimer`. Do not remove it. No removal prompt is prepared. List it in the final report as an extra screen, added by the user, not by Mentor.

**Update (2026-11-22, task 9 of add-department).** D-4 now also covers the extra button "Run Employee Dept" and its empty action `RunEmployeeDeptOnClick` on `RunTimer` (U-3, revision 9). Stated by the user: a test the user abandoned. The button and action stay in the app, because the user did not ask to remove them, and no removal prompt is prepared. They add no write path, so the D-2 note above is unchanged. `RunTimerOnClick` (the first button, calls `BootstrapData`) is unchanged.

## Unplanned publishes
Publishes that were not part of the plan and not sent by Kiro. They are not interventions and are not numbered in the Interventions list.
### Unplanned Studio publish U-1: revision 3 (2026-11-22)
| Item | Value |
|---|---|
| App / revision | EmployeeCatalogMCP (debb6b49-7b59-ecf6-b2eb-50a5f78250f3), revision 3 |
| Published | 2026-11-21T19:46:08.134Z per `app_revisions` (2026-11-22 06:46:08 AEDT). Deployed to Development 19:46:08.771Z, build key e460d438-7ab0-83f7-82ac-f2432afdd5bf |
| Made by | The user, in ODC Studio. The revision user key is the same as for revisions 1 and 2. The graph marks the module `LastModifiedByTool` as ODCStudio |
| Time discrepancy | The user said the Studio session was opened at about 07:11. The recorded publish time is 06:46:08 AEDT. The recorded time is used here. No revision exists after 3 (checked 07:12 AEDT). To be confirmed by the user |
| Kiro / Mentor involvement | None. No prompt, no Mentor session |
| Functional change | None. Graph comparison revision 2 to 3 (`MCP/Reports/graphdiff/2-to-3.diff`, `3.xre` SHA-256 ceb8b3fce38d487ce17621805e57a5ca744a1f68f610bf57da290e8226d0b81d): 0 nodes removed, 5 added, 70 changed. All are reference entries or elements of referenced libraries, plus the module's tool marker. Nothing changed in Employee, the Staff role, any `Bootstrap*` element or either screen |
**Decision (user).** Log it as an unplanned Studio publish with no functional change. Not an intervention. The user states that build A had the same for its revisions 3 and 5 (stated by the user, not checked by Kiro).
**Consequence for the check.** The user's browser check was made after this publish, so the empty Employee_List was seen on revision 3, not revision 2. See `MCP/Reports/check-2-2026-11-22.md`.
### Unplanned Studio publish U-2: revision 6 (2026-11-22)
| Item | Value |
|---|---|
| App / revision | EmployeeCatalogMCP (debb6b49-7b59-ecf6-b2eb-50a5f78250f3), revision 6 |
| Published | 2026-11-21T22:49:05.120546Z per `app_revisions` (2026-11-22 09:49:05 AEDT), by "Developer" per Mentor's `publishAutoMerged` event. Between publish 1 (revision 5, 22:40:02Z) and the I-1 publish (revision 7, 22:56:22Z) |
| Made by | The user, in ODC Studio, at about 09:49 AEDT (confirmed by the user). Mentor's `publishAutoMerged` event names the publisher as Developer. ODC Studio is now closed |
| Kiro / Mentor involvement | None in revision 6. Mentor merged it automatically into the I-1 publish. Kiro did not know of it until the publish result |
| What changed (from the 5 -> 7 diff, the only comparison possible, because the graph service serves only the newest revision) | `BootstrapData`: tool marker and date (ODCStudio, 22:44:54), and the X and Y position of two nodes (the `UpdateEmployee` call and the first For Each). Layout only. No flow connection or value changed. Nothing else in the app changed beyond I-1 |
| Effect on numbering | The expected "6.xre" does not exist. The comparison file is `7.xre` |
**Confirmed by the user (2026-11-22).** Logged as an unplanned Studio publish, not an intervention. No functional change. ODC Studio is closed.
### Unplanned Studio publish U-3: revision 9 (2026-11-22)
| Item | Value |
|---|---|
| App / revision | EmployeeCatalogMCP (debb6b49-7b59-ecf6-b2eb-50a5f78250f3), revision 9 |
| Published | 2026-11-22T01:00:56.020536Z per `app_revisions` (2026-11-22 12:00:56 AEDT), modelDigest 89f31b38-ca52-171c-3a27-ebd1d86c934b, deployed to Development with build key 2218804b-eaea-362d-5ece-8f0407f005c9. After the add-department screens publish (revision 8, 23:09:10Z on 21 Nov) |
| Made by | The user, in ODC Studio (confirmed by the user, 2026-11-22). The graph markers agree: tool marker ODCStudio and the user's own user name |
| Type | Manual change in ODC Studio, with no functional effect. Not a Mentor prompt: no prompt file, no Mentor session, no run. Not a spec intervention |
| What changed (from the 8 -> 9 graph comparison) | On screen `RunTimer`: a new Button "Run Employee Dept" and a new client action `RunEmployeeDeptOnClick` with only Start and End and no call to any action. 14 nodes added, 0 removed, 3 changed (tool marker and last-modified dates of the module, `MainFlow` and `RunTimer`). Nothing else changed: data model, `BootstrapData`, `BootstrapEmployee`, `BootstrapTimer`, Staff role, menu, `Employee_List`, `Employee_Detail`. The seed and update literal hashes are the same as in revision 5 (`808c85070a`, `ce1312410b`) |
| Purpose | A test by the user, abandoned (stated by the user). The button and the action were not removed |
| Graph comparison | `MCP/Reports/graphdiff/8-to-9.diff`, `8-to-9-notes.md`, `9.xre` SHA-256 a50ceb4684487ee01a92684449e462e8d3d8f78beb4d6bce12679be48fac9fc3 |
| Status | In place, not removed. Part of deviation D-4 (extra content on the extra screen `RunTimer`) |
**Decision (user).** Log it as a manual change with no functional effect. Add it to D-4. Do not remove the button. Note: `8-to-9-notes.md` was written before this confirmation and still says "The user has not confirmed this one". It is a point-in-time file and was not edited.
## Platform incidents

Platform incidents are failures of the platform that cost work. They are not numbered, are not interventions, and have no fix prompt.

### Incident P-1: Mentor session lost, EmployeeCatalogMCP gone (2026-11-22)

| Item | Value |
|---|---|
| Task | 4 (creation) and 5 (part 1 data) of `.kiro/specs/employee-catalog/tasks.md` |
| Lost Mentor session | 29f880cb-69a8-3d38-93d2-bd0c1a879024 |
| Creation run (task 4) | d5f0a70b-d0a9-38ce-bdbf-92dcb2589e89 |
| Part 1 run (task 5) | f12ee6f1-e814-ab30-2ae6-874edd4944b7 |
| app_key of the lost app | ee94947f-4977-cf9d-8863-0aedede9b3d7 |
| Creation prompt file | MCP/Prompts/001-create-app.md |
| Part 1 prompt file | MCP/Prompts/002-part1-data.md |
| Details and per-step record | MCP/spec-driven-build/EmployeeCatalogMCP/session.md, last section |

**Times** (local AEDT, UTC+11, 2026-11-22). The runs and polls carried no recorded timestamps, so those are "not recorded". Known: the creation turn took 6 s ("Worked for 6s" in its events). File modification times: `scope-baseline.md` 05:42:06, `001-create-app.md` 05:42:07, `result-create.json` 05:43:13, `002-part1-data.md` 05:45:41, the session.md lost-run section 05:49:59. Part 1 run sent: not recorded (after 05:45:41). First `not_found` poll: not recorded. User's ODC Studio check: not recorded (after 05:49:59).

**Symptoms**

- The part 1 run returned `working` on poll 1 and poll 2, then `not_found` on every later poll, including cursor 0.
- The creation run in the same session also returned `not_found`, although it had succeeded earlier and its result was saved.
- No terminal status and no completion signals for the part 1 run.

**Checks after the incident**

- The user checked ODC Studio: EmployeeCatalogMCP does not exist.
- Kiro, read-only: `app_list` search "EmployeeCatalog" returns only EmployeeCatalogMW and `Employee Catalog`. `app_info` for the lost app_key returns 404.

**Lost**

- The unpublished EmployeeCatalogMCP app created in task 4.
- The in-flight part 1 changes: Employee, BootstrapEmployee, BootstrapData, the WakeBootstrapTimer signature, the Staff role change, the Login screen change (and the app module change).
- No `result-data.json` exists.

**Not lost**

- `spec.md`, `requirements.md`, `design.md`, `tasks.md`, `Reports/scope-baseline.md`.
- The prompt files `001-create-app.md` and `002-part1-data.md`, and `result-create.json`.

**State**

- Nothing was published. EmployeeCatalogMW was not touched; its latest revision is still 6.
- `002-part1-data.md` stays on disk as the record of the lost turn. The re-send is saved as a new numbered prompt file only if its text differs from the file; otherwise the reuse is noted in session.md.
- Remedy: task 4 restarts from the beginning (new session, new creation turn, new app_key).
- No fix prompt. Not a spec intervention.
### Incident P-2: Development stage daily timer execution limit reached, Personal Edition (opened 2026-11-22, cause found 2026-11-22)
| Item | Value |
|---|---|
| Stage | Development, key 8b036dbd-6d28-2b5c-c50a-77a6bc07d748 |
| Cause (user, from the ODC Portal) | The Personal Edition daily timer execution limit for the Development stage. The limit is shared by all apps in the stage. Not a build or spec fault |
| Exact error text | `Couldn't run BootstrapTimer because the timer execution duration subscription has exceeded the daily limit in the Development stage. (OS-TMR-42900)` |
| Run now | Failed at 07:17 AEDT on 2026-11-22 (2026-11-21T20:17Z), with the error above |
| BootstrapTimer in the Portal | Last run "-" (never ran), Schedule "When published", Timeout 20 minutes (user report) |
| Last timer line in the stage logs | 2026-11-21T12:25:21.387Z (2026-11-21 23:25:21 AEDT) |
| Status | Open. Waiting for the daily limit to reset |
| Details | `MCP/Reports/dev-stage-timers-2026-11-22.md`, `MCP/Reports/check-2-2026-11-22.md` |
**What the logs show (Kiro, read-only)**
- Stage-wide timer starts: 799 on 2026-11-20 (until 13:00:26Z) and 770 on 2026-11-21 (until 12:25:21Z). Five timers that run about every 5 minutes account for about 99% of the estimated execution time. Their owners: RAG Knowledge Base, CloneOfRAGKnowledgeBase, Clone2OfRAGKnowledgeBase (each RecomputeBM25Stats) and OKF Store (IngestBatch, LinkResolution).
- Estimated execution time (start line to "executed successfully" line): 1875.9 s on 20 Nov and 1877.9 s on 21 Nov, almost equal. That fits a cap on execution duration. The cap value and the platform's own measure are not confirmed.
- After the first stop the stage was quiet for 11.0 h (2026-11-20T13:00:26Z to 2026-11-21T00:00:25Z) and timers resumed at 00:00 UTC.
- The docs search (outsystems-docs, ODC, synced 2026-10-28) has no page on OS-TMR-42900 or this limit.
**Impact on this project**
- The publish-time run of `BootstrapTimer` never executed for revisions 1 (19:05:40Z), 2 (19:34:39Z) and 3 (19:46:08Z). All fall after 12:25:21Z.
- The Employee table is empty. AC-01 and AC-06 stay failing, blocked by P-2.
- `BootstrapEmployee` has not run yet, so the action itself is untested. The model is correct on paper.
**Plan (user decision)**
- No publish before the limit resets. No Mentor prompt, no fix prompt.
- The user retries Run now for `BootstrapTimer` after the reset. The expected reset is 00:00 UTC (11:00 AEDT). Not confirmed. One reset was observed at 00:00 UTC.
- Kiro can poll `app_logs` for the first stage-wide timer line after 12:25:21Z on 2026-11-21 as the reset signal, on request.
**Note for the build A and build B comparison (user).** Build A ran while the stage still had timer budget. Build B's bootstrap was blocked because the budget was used up by other apps' timers. The outcome depends on the time of day, not on the build method.
**Environment change by the user.** The user will slow down or deactivate the five 5-minute timers in other apps in the ODC Portal. It is recorded in `MCP/Reports/dev-stage-timers-2026-11-22.md` as the user's own change, not part of build B.
**Open point.** The empty traces stay open. Not investigated further for now (user decision).
**Task 11.** Not started until the user has clicked Run now on `BootstrapTimer` after the reset and reported back.
**Classification.** Platform incident, by user decision. No fix prompt. Not a spec intervention.
