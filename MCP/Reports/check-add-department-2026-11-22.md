# Check report: add-department on EmployeeCatalogMCP (2026-11-22)

Task 9 of `MCP/.kiro/specs/add-department/tasks.md`. Written 2026-11-22, about 12:15 AEDT (01:15 UTC). App: EmployeeCatalogMCP, app key debb6b49-7b59-ecf6-b2eb-50a5f78250f3, Development stage 8b036dbd-6d28-2b5c-c50a-77a6bc07d748, URL https://your-tenant-dev.outsystems.app/EmployeeCatalogMCP.

This report changes nothing in the app, in `employee-catalog/requirements.md` or in `spec.md`. Tenant calls made for it were read-only: `app_revisions`, `app_list`, `env_app`, `app_logs`, `context_graph`. New files: this report, `Reports/graphdiff/9.xre`, `8-to-9.diff`, `8-to-9-notes.md`. Sample data is made up.

**Updated (2026-11-22, later, task 9).** The report now holds your task 8 browser results and two decisions, all stated by you in chat: the revision 9 button is logged as U-3 and added to D-4, and the delete rule `Protect` is kept. No tenant call was made for this update. Files changed by it: this report and `MCP/Reports/interventions.md`.

**Updated again (2026-11-22, later, task 9 re-opened).** The remaining task 8 browser results are now recorded. Source for each: "user statement in chat, task 8 (remaining steps)". The user states they ran these steps on **revision 9** and that the results apply because revision 9 changed only `RunTimer`. This also settles the earlier "revision 8 or 9" label question: the report now says the user ran the steps on revision 9. No tenant call was made. Only this report was changed. `interventions.md` needed no change. Three items stay "No record found" because the user left a placeholder unfilled in the message: the five values of Alice Anderson's detail, the dropdown position, and the exact text of the empty option.

## 1. Summary

| Item | Result |
|---|---|
| Browser checks of task 8 (AC-07, AC-08, AC-01 to AC-06) | **Recorded as reported by the user, with three items still open.** Source: your statements in chat, task 8 (first statement, and "remaining steps"), Staff test user, revision 9. Kiro did not see the screens. Every step of AC-07 and AC-08 now has a reported result and none is reported as failing. AC-01 (columns and 17 rows), AC-02, AC-03 (Hugo only), AC-05 (no rows, message), AC-06 (as reported) are recorded. **Still "No record found":** the five values of Alice Anderson's detail (AC-04), the dropdown position, the exact text of the empty option (unfilled placeholders), plus the items in section 10. See section 3 |
| AC-07 (department shown) | **All four steps reported by the user as matching** (section 3). Open inside AC-07: the Human Resources count was not stated on its own (only the all-17-rows match), and Alice's five values (an AC-04 item) have no record. Kiro has not seen it, so this is a user-reported result, not a Kiro check |
| AC-08 (department filter) | **All five steps reported by the user as matching** (section 3). Open: whether the search was cleared in step 4 and the row count for Finance in step 1 were not stated. The dropdown position and the empty-option text are not part of AC-08 and have no record |
| Delete rule of DepartmentId | `Protect`. Graph and Mentor's summary agree. **Decision (user): keep `Protect`.** Not changed (section 5) |
| Assignment match (task 4) | Match. Seed and update both hold the 20 rows of the table and agree with each other. Hashes unchanged in revisions 5, 7, 8 and 9 (section 6) |
| D-2 | Holds in revision 9 (section 7) |
| (a) EmployeeCatalogMW unchanged at revision 6 | **Pass** |
| (b) No other app touched | **Pass** |
| (c) SDD Base unchanged | **Pass** |
| Revision 9 | **Revision 9** of EmployeeCatalogMCP (2026-11-22T01:00:56Z, 12:00:56 AEDT) adds a button "Run Employee Dept" and an empty action on the RunTimer screen. **Confirmed by you:** a Studio publish by you, a test you abandoned, not removed. Logged as U-3 in `interventions.md` (manual change, no functional effect) and added to D-4. The app and the requirements still disagree on the screen content (section 9) |

## 2. Revisions of EmployeeCatalogMCP in this change

Source: `app_revisions` (read 2026-11-22 about 12:10 AEDT) and `env_app` (revision 9 deployed, build key 2218804b-eaea-362d-5ece-8f0407f005c9).

| Revision | Published (UTC) | What | Made by | Graph file |
|---|---|---|---|---|
| 4 | 2026-11-21T21:01:27Z | RunTimer screen (M-1). Baseline of this change | You, Studio | `4.xre` |
| 5 | 2026-11-21T22:40:02Z | Publish 1: data (task 3) | Kiro, through Mentor | `5.xre`, `4-to-5.diff`, `4-to-5-notes.md` |
| 6 | 2026-11-21T22:49:05Z | Layout only in `BootstrapData` (U-2) | You, Studio | no own file, merged into 7 |
| 7 | 2026-11-21T22:56:22Z | I-1: record names fixed | Kiro, through Mentor | `7.xre`, `5-to-7.diff`, `5-to-7-notes.md` |
| 8 | 2026-11-21T23:09:10Z | Publish 2: screens (task 6) | Kiro, through Mentor | `8.xre`, `7-to-8.diff`, `7-to-8-notes.md` |
| 9 | 2026-11-22T01:00:56Z | Button "Run Employee Dept" and an empty action on RunTimer (U-3) | You, Studio (confirmed by you) | `9.xre`, `8-to-9.diff`, `8-to-9-notes.md` (made for this report) |

Prompt files 006, 007, 008 and 009 are byte-identical to the four prompt blocks of the current `design.md` (checked with a script for this report). The old `design.md` copy (`Reports/add-department/design.md.before-i1`) differs only in prompt B, which is the recorded design change (dropdown sorted by Id). Prompts 010 and 011 belong to I-1.

## 3. Browser checks (task 8): results, AC-07, AC-08, AC-01 to AC-06

**Source of the results below:** two statements of yours in chat, both for task 8, run as your Staff test user: the first one (given after the first version of this report, labelled revision 8 at the time) and the later one, "user statement in chat, task 8 (remaining steps)". You state you ran these steps on **revision 9**, and that the results apply because revision 9 changed only `RunTimer` (see `8-to-9.diff`: no change to `Employee_List` or `Employee_Detail`). The revision label is as you state it. They are your reported browser results. Kiro did not see the screens and did not repeat the checks. They are recorded per step as you stated them. Where your statements do not cover a step, or you left a placeholder unfilled, the result stays "**No record found**" and the step is listed in section 10. Results without an explicit source label come from the first statement. Results labelled "remaining steps" come from the later one.

**Evidence searched earlier (unchanged):** `MCP/Reports/*.md`, `MCP/Reports/add-department/*` (result JSON files and the two `.before-i1` copies), `MCP/Reports/interventions.md`, `MCP/spec-driven-build/EmployeeCatalogMCP/session.md`. No file in `MCP/` held a task 8 result before this update. `tasks.meta.json` shows task 8 ran in chat session sess_d5444b37-ad02-2d6c-6469-9d9e37e7a3e9.

**How the departments were filled (your statement):** by "Run now" on `BootstrapTimer` in the ODC Portal at about 12:00 AEDT (trigger via the ODC Portal). This fits the stage log line `BootstrapTimer: starting execution` at 12:00:02 AEDT (app version 8, see the log table below).

The expected value comes from `requirements.md` of this spec (assignment table). The right column is what can be said without the browser (graph or log), and it is support, not a test result.

### AC-07 (department shown)

| Step | Expected | Result | Support without the browser |
|---|---|---|---|
| 1 | Employee_List shows a Department column and 17 rows | **Recorded (user, task 8):** the Department column matched the assignment table for all 17 rows. 17 rows (AC-01 re-check) | Revision 8 graph: new last column, header "Department", cell `GetEmployees.List.Current.Department.Label` (`7-to-8-notes.md`). Unchanged in revision 9 (`8-to-9.diff`) |
| 2 | Rows match the table: Engineering 7, Finance 2, Human Resources 3, Sales 5 | **Recorded (user, task 8):** "matched the assignment table for all 17 rows: yes". Separate counts were stated for Engineering (7, AC-08 step 5), Finance (Elena and Kara, AC-08 step 1) and, in the later statement, Sales (5 rows, AC-08 step 5, revision 9). Engineering and Sales equal the table. The count for Human Resources was not stated on its own | Seed and update literals match the table (section 6). Timer log below |
| 3 | Detail of Alice Anderson (Engineering), Grace Lindholm (Human Resources), Liam Oduya (Sales) shows the department | **Recorded (user statement in chat, task 8 (remaining steps), revision 9):** Alice Anderson = Engineering. Grace Lindholm = Human Resources. Liam Oduya = Sales. All three equal the assignment table. **No record found** for the five values of Alice's detail: the user left the placeholder "[values]" unfilled (see AC-04) | New last field "Department" on `DetailCard` (revision 8 graph, unchanged in revision 9) |
| 4 | EmployeeId 8 Hugo Brandt, Finance. 13 Maya Petrov, Engineering. 17 Quinn Abara, Finance | **Recorded (user, task 8):** EmployeeId 8 Hugo = Finance, 13 Maya = Engineering, 17 Quinn = Finance. **Recorded again (user statement in chat, task 8 (remaining steps), revision 9):** EmployeeId 13 Maya: Active No, Department Engineering. EmployeeId 17 Quinn: Active No, Department Finance. The two statements agree | The join is Left ("With or Without") with Employee as left source, as the graph shows |

AC-07 verdict: **all four steps have a reported result that matches `requirements.md`, none is reported as failing.** This is the user's report, not a Kiro check. Not stated and so still open inside AC-07: the Human Resources count on its own (step 2; the all-17-rows match implies 3, per the table) and Alice's five values (AC-04, below). Maya's and Quinn's Active = No is recorded (AC-06); Hugo's Active value was not stated in the later message.

### AC-08 (department filter)

| Step | Expected | Result | Support without the browser |
|---|---|---|---|
| 1 | Finance shows only Elena Novak and Kara Whitfield | **Recorded (user, task 8):** Finance shows Elena and Kara. No row count was given for Finance, so "no other row" is not stated. The later statement (step 2 below) shows Kara with Finance chosen, which agrees | `GetEmployees` has three filter conditions in AND: `Employee.IsActive` (index 0), the search (1), `SelectedDepartmentId = NullIdentifier() Or Employee.DepartmentId = SelectedDepartmentId` (2, new). IsActive and search nodes unchanged from revision 7 |
| 2 | Finance with search "Kara" shows only Kara Whitfield | **Recorded (user statement in chat, task 8 (remaining steps), revision 9):** Finance + "Kara" shows Kara Whitfield. Matches. Related, from the first statement: Finance with search "Elena" shows Elena | Same filters, combined by AND |
| 3 | Finance with search "Alice" shows no rows | **Recorded (user statement in chat, task 8 (remaining steps), revision 9):** Finance + "Alice" shows no rows. Matches | Same filters, combined by AND |
| 4 | "All departments" with the search cleared shows the 17 rows | **Recorded (user, task 8):** All departments shows 17 rows. Whether the search was cleared is not stated | Empty option "All departments" is the default. The third condition is true when `SelectedDepartmentId` is empty |
| 5 | Sales shows 5 rows, Engineering 7 | **Recorded:** Engineering shows 7 rows (user, task 8). Sales shows 5 rows (user statement in chat, task 8 (remaining steps), revision 9). Both equal the active totals in `requirements.md` (Engineering 7, Sales 5) | None beyond the table totals |

AC-08 verdict: **all five steps have a reported result that matches `requirements.md`, none is reported as failing.** This is the user's report, not a Kiro check. Not stated and so still open: whether the search was cleared in step 4, and the Finance row count in step 1 (the later statement shows Kara but gives no count).

### Dropdown order, position and empty option (user, task 8)

Reported order of the dropdown: All Departments, Engineering, Finance, Human Resources, Sales (first statement).

**Dropdown position (below or beside the search input): No record found.** In the later statement the user left the placeholder "[below / beside]" unfilled. **Exact text of the empty option: No record found.** The user left the placeholder "[exact text]" unfilled. The only label on record is "All Departments", from the earlier chat statement, which may only be how it was typed. Prompt 008 says "All departments". The label question stays open.

- Against `requirements.md`: the Glossary lists the records in the order Engineering, Finance, Human Resources, Sales, and AC-08 states no order for the dropdown. The reported order follows the Glossary after the empty option. No AC is affected.
- Against prompt 008 (item 3): the prompt asks for the records sorted by Department Id ascending (Engineering, Finance, Human Resources, Sales) and one empty option labelled "All departments", which is the default. The reported order matches. Your statement writes the empty option as "All Departments" (capital D). Whether that is the label in the app or only how it was typed in chat is not stated. The label is not part of any AC. Not checked against the graph.
- This also fits the I-1 decision (record positions accepted, dropdown sorted by Id), as the user sees it in the browser.
- Mentor-vs-prompt position note (section 9): Mentor's summary says the dropdown is below `Input_Search` on its own line, while prompt 008 says "next to" it. **Still not covered:** the position placeholder was unfilled in the user's message. No record found.

### Short re-check of AC-01 to AC-06

| AC | Expected | Result | Support without the browser |
|---|---|---|---|
| AC-01 | First name, Last name, Job title, Email, Department. 17 rows | **Recorded:** 17 rows and the Department column (user, task 8). Columns: First name, Last name, Job title, Email, Department (user statement in chat, task 8 (remaining steps), revision 9). Matches the four existing columns plus Department. Column order and header spelling are as the user listed them | The four existing columns are unchanged in revision 8 (no existing widget, header or cell node changed) |
| AC-02 | "Alice" shows only Alice Anderson | **Recorded (user, task 8):** searching "Alice" finds Alice. That no other row appeared is not stated | Search condition node unchanged |
| AC-03 | Hugo Brandt, Maya Petrov, Quinn Abara not listed | **Partly recorded (user, task 8):** "Hugo is not listed". Mapped to AC-03 because AC-03 says no row is shown for any Employee with IsActive false, and Hugo Brandt is inactive in the assignment table. **No record found** for Maya Petrov and Quinn Abara on their own. The 17 rows reported are consistent with the three being hidden (20 minus 3), but that is an inference, not a record | `Employee.IsActive` filter node unchanged |
| AC-04 | Detail of Alice Anderson shows five values and Department, read-only | **Partly recorded.** Read-only (user, task 8; whose detail was opened is not stated). Department of Alice Anderson = Engineering (user statement in chat, task 8 (remaining steps), revision 9). **No record found** for the five values (First name, Last name, Email, Job title, Active): the user left the placeholder "[values]" unfilled. Related: the detail of EmployeeId 8, 13 and 17 showed the departments (AC-07 step 4) | Existing five fields unchanged, Department added last |
| AC-05 | "zzzz" shows no rows and "No employees found." | **Recorded (user statement in chat, task 8 (remaining steps), revision 9):** "zzzz" shows no rows, message "No employees found". The user wrote it without a final full stop, so **the full stop is not stated**. Consistency note: `employee-catalog/requirements.md` AC-05 requires only "the table shows no rows" and names no message. The text "No employees found." comes from this spec's `design.md` check list, `tasks.md` task 8 and prompt 008 (which tells Mentor to keep that text). `build-report.md` records the message as "No employees found" with no full stop. The no-rows part of AC-05 is recorded. The full stop is not covered by any requirement | The text node and the sort are unchanged |
| AC-06 | 17 visible + EmployeeId 8, 13, 17 (Active = No) = 20 records, 3 inactive, Alice active | **Recorded as reported (user statement in chat, task 8 (remaining steps), revision 9):** 17 active rows, unchanged by this change. Hugo, Maya and Quinn open by Id (as the user wrote it). Active = No is stated for Maya (13) and Quinn (17). Not stated: Active = No for Hugo (8), the total of 20 and Alice's Active value. The seed literal holds the 20 records with the table's `IsActive` values (section 6), so 17 + 3 = 20 is consistent with `requirements.md`, but the user did not report the total | The seed literal holds 20 records with the `IsActive` values of the table (section 6) |

### What the runtime logs show about the data update (read-only `app_logs`, since 2026-11-21T22:00Z)

| Time (UTC) | Time (AEDT) | Stage log line | App version |
|---|---|---|---|
| 2026-11-21T22:40Z (publish 1) and 23:09Z (publish 2) | 09:40 and 10:09 | No `BootstrapTimer` line at either publish | 5, 8 |
| 2026-11-22T01:00:02.984Z | 12:00:02 | `Timer BootstrapTimer: starting execution` | 8 |
| 01:00:21.927Z | 12:00:21 | `finished successfully in 18094 milliseconds`, then `executed successfully` | 8 |
| 01:01:26.090Z | 12:01:26 | `starting execution` | 9 |
| 01:01:29.065Z | 12:01:29 | `finished successfully in 2166 milliseconds`, then `executed successfully` | 9 |
| 01:03:40.5Z | 12:03:40 | `New application version detected, starting upgrade` | 9 |

Reading: the publish-time timer runs of revisions 5 and 8 left no log line, which fits incident P-2 (the logs were empty for the whole stage earlier, `task8-applogs-check.md`). The first timer line is at 12:00:02 AEDT, after the expected reset at 11:00 AEDT. The log does not say how that run started. **You state it was "Run now" on `BootstrapTimer` in the ODC Portal at about 12:00**, which matches the log time. The log does not say what the run wrote. The second run, started by the publish of revision 9 ("When published"), took 2.2 s against 18.1 s for the first, which is consistent with a first run that did the update and a second that found nothing to do. That is an inference. `BootstrapData` shows the same message whether or not it changed data (M-1), so the browser decides, and your results in this section are the browser record.

**Revision label (resolved by you).** The first statement was labelled revision 8. You now state that you ran the steps on revision 9, and that the results apply because revision 9 changed only `RunTimer`. The log fits this: the Run now finished at 12:00:21 AEDT on version 8, revision 9 was published at 12:00:56 AEDT, the first timer run on version 9 was at 12:01:26 and the upgrade line at 12:03:40. A browser check after about 12:03 AEDT runs on revision 9. The report uses your label (revision 9). The log gives the order of events but not the time of your browser steps, so the label is as you stated it. `8-to-9.diff` shows no change to `Employee_List` or `Employee_Detail`, which supports that the results apply to both revisions.

**Still missing:** the items marked "No record found" above (Alice's five values, dropdown position, exact empty-option text, and the items in section 10), and whether the Department column was empty before the Run now. Section 10 lists them.

## 4. Interventions and unplanned publishes in this change

| Id | What | Evidence | Status |
|---|---|---|---|
| I-1 | Fix of the record names of Department (prompt 010, publish prompt 011). Confirmed by you before each send. Session 2a37df04-4249-c799-44b7-22c99914b5c1, fix run 2c7fa05a-1824-3ae7-6ae3-40a20fb6b548, publish run e495a911-fd93-1356-d402-5f29aaf99fd7, revision 7 | `interventions.md`, `result-i1-fix-records.json`, `result-publish-i1.json`, `5-to-7-notes.md`. Read again in the revision 7, 8 and 9 graphs: the record names are Engineering, Finance, Sales, HumanResources (in that position order). The Labels were checked in `5-to-7-notes.md`, not re-read for revisions 8 and 9 | Closed. Names fixed. The request to order the records by Id did not change their positions. You decided to accept the positions and sort the dropdown by Id (prompt B changed before sending) |
| No I-2 or later | No fix prompt was sent after I-1 | `interventions.md` has no later entry; `Prompts/` ends at 011 | The log has no entry for a fix after task 8. The recorded browser results (section 3) report no wrong value and no step that needed a fix. The unrecorded items (section 10) are open |
| M-1 (earlier) | RunTimer screen, Studio, revision 4 | `interventions.md` | Kept (D-4) |
| U-2 | Studio publish revision 6, layout of `BootstrapData` | `interventions.md`, `5-to-7-notes.md` | Logged, no functional change |
| U-3 | Studio publish revision 9: button "Run Employee Dept" and empty action `RunEmployeeDeptOnClick` on RunTimer. A test you abandoned, not removed. Manual change, no functional effect | `8-to-9.diff`, `8-to-9-notes.md`, `app_revisions`, `interventions.md` | **Logged** in `interventions.md` (2026-11-22, on your confirmation) and added to D-4 |

Manual work in ODC Studio in this change: design.md says ODC Studio is not opened in this change. Revisions 6 and 9 were published from Studio by you. Both are logged (U-2 and U-3).

## 5. Delete rule of DepartmentId

**Found: `Protect`.** Not changed. **Decision (user, 2026-11-22): keep `Protect`.**

| Source | Value |
|---|---|
| Mentor's summary of task 2 (`result-data.json`, event 21) | "Its delete rule is `Protect`, the default." |
| Graph of revision 5 (`5.xre`, node `...*xZ7EwVxgT7_ycieZVJTDwj`, `Employee.DepartmentId`, `DeleteRule`) | `Protect`. `IsMandatory` false |
| Graphs of revisions 7, 8 and 9 (same node, read again for this report) | `Protect`. Same node key |

The two sources agree. The prompt did not ask for a particular rule. Requirements decision 2 says the rule is checked after the build and not changed without a decision. In ODC, `Protect` stops deleting a Department record while an Employee refers to it. Department has no write action in the app and no screen deletes anything, so the rule has no effect in the current app. You decided to keep `Protect` (requirements decision 2, taken after the build). No prompt is prepared and nothing is sent.

## 6. Assignment match of task 4

Source: `MCP/Reports/graphdiff/4-to-5-notes.md`, section "Assignment match". The graph stores each JSON literal as a length and a 10-character SHA-1 prefix, not as text. Task 4 rebuilt both literals from the table in `requirements.md` and the emails of spec.md, and compared length and hash.

| Literal | Where | Length, hash in graph | Rebuilt from the table | Match |
|---|---|---|---|---|
| Seed, revision 5 | `BootstrapEmployee`, `DeserializeEmployees` | 2,806, `808c85070a` | 20 records in spec.md order, plus `"DepartmentId":N` (1 Engineering, 2 Finance, 3 Human Resources, 4 Sales) | Yes |
| Update, revision 5 | `BootstrapData`, `DeserializeDepartments` | 1,256, `ce1312410b` | 20 objects `{"Email","Department"}` in table order | Yes |

- 20 of 20 rows agree with the table in prompt 006 by Email. The seed and the update agree with each other.
- Checked again for this report: both literal nodes have the same length and hash in revisions 5, 7, 8 and 9. The match therefore holds for the live app (revision 9).
- Id to Label of Department: 1 Engineering, 2 Finance, 3 Human Resources, 4 Sales (task 4, from the Label hashes).
- Limit: a match by length and a 40-bit hash prefix, not a reading of the text. The stored data was not read (section 3).

## 7. D-2 note

D-2 (Staff has no View permission on Employee) was resolved on the basis that the only call to an Employee create, update or delete action is `CreateEmployee` in `BootstrapEmployee`. Re-check on revision 9 (call nodes and entity-action edges from `9.xre`):

| Entity action | Called from |
|---|---|
| `CreateEmployee` | `BootstrapEmployee` (one call node) |
| `UpdateEmployee` | `BootstrapData` (one call node) |
| `CreateOrUpdateEmployee`, `CreateOrUpdateSomeEmployees`, `DeleteEmployee`, `DeleteAllEmployees`, `GetEmployee`, `GetEmployeeForUpdate` | no caller |
| `GetDepartment` (Department entity action) | no caller. The update uses an aggregate, not this action |

Result: **holds.** Note under D-2 (design decision 7): `UpdateEmployee` in `BootstrapData` is a second allowed write path, next to `CreateEmployee`. It is run by `BootstrapTimer` (on publish and by Run now) or by the RunTimer button `RunTimerOnClick`. It writes only DepartmentId, and only where it is empty (as built; seen in the flow of 4-to-5-notes, not run in a test). Users have no create, edit or delete path. The new revision 9 action `RunEmployeeDeptOnClick` calls nothing, so it adds no write path.

## 8. Read-only checks

### (a) EmployeeCatalogMW unchanged: **PASS**
- `app_revisions` for 07a64c21-0c8c-8afb-28ee-5d8530d55cf8 (2026-11-22, about 12:10 AEDT): latest revision 6, 2026-11-21T10:56:49.208634Z, modelDigest 35873f58-1351-11c1-6d2d-9ad864ae3a67. Six revisions in total, nothing newer.
- Baseline in `Reports/scope-baseline.md`: revision 6, same time, same digest. `env_app` for Development: revision 6, build key 298fc5bd-cadd-5ca4-d36c-a03d7d603cf1, deployed 2026-11-21T10:56:49.317Z, the same as the baseline.

### (b) No other app touched by this change: **PASS** (with the limit below)
- `app_list` for the whole tenant (117 assets, not truncated): the only asset with a revision date on or after 2026-11-20 is EmployeeCatalogMCP (revision 9, 2026-11-22T01:00:56Z), apart from EmployeeCatalogMW (2026-11-21T10:56:49Z, before this change started at about 22:30Z, and unchanged from the baseline). The next newest are Test Grep Agent and Grep Agent (2026-11-19T20:18Z) and AgentFileInspector (2026-11-19T10:13Z), all before the change.
- `Employee Catalog` (31b31b9c-c028-bfee-1811-c6b59aba4b5b): revision 6, 2026-11-11T01:38:32Z, the same revision as in the baseline.
- Every Mentor turn of this change named only the app key debb6b49-7b59-ecf6-b2eb-50a5f78250f3 (result files, session 2a37df04-4249-c799-44b7-22c99914b5c1, released after publish 2).
- Limit: this shows no new published revision elsewhere. It cannot show unpublished changes or a change to data or settings in another app. The timers of other apps that you slowed or switched off (`dev-stage-timers-2026-11-22.md`) are your own environment change, not part of this change.

### (c) SDD Base unchanged: **PASS**
- `find . -newer <tasks.md>` in `/Users/<user>/Development/SDD Base`: no file. `tasks.md` was last written 2026-11-22 12:08:51 AEDT, so this covers only the time since task 9 started.
- Wider check, because that window is short: `find . -newer` the add-department `requirements.md` (2026-11-22 08:38:59 AEDT, the start of the change): no file. The newest files in SDD Base outside `vendor/` are `.kiro/steering/outsystems-ui.md` and `mentor-standards.md` (2026-11-21 17:56:45), `workspace-layout.md` (17:43:35) and two `.DS_Store` files (2026-11-21 16:28, 16:27). The newest in `vendor/` is the git index of three vendored repositories, 2026-11-22 04:45:27, before the change.
- SDD Base is not a git repository, so there is no `git status` to add.

## 9. Deviations, and where the app and the requirements disagree

| Id | Item | App | Requirements | Status |
|---|---|---|---|---|
| D-1 | Bootstrap action returns a message and writes no log line | As built | prompt 002, constraint 7 | Decided, kept (first build) |
| D-3 | Email length | 256 | 250 | Decided, kept (first build) |
| D-4 | Extra screen `RunTimer`, now with a second button "Run Employee Dept" and an empty action `RunEmployeeDeptOnClick` (revision 9, U-3) | Exists, Staff only, not in the menu. The second button calls nothing and writes nothing | Both `requirements.md` files: no screen other than Employee_List and Employee_Detail | Decided, kept. Extended by U-3 on your decision (2026-11-22): a test you abandoned, not removed. Updated in `interventions.md` |
| Observation | Department record positions: Engineering, Finance, Sales, HumanResources. Requirements list: Engineering, Finance, Human Resources, Sales | Ids and Labels are right (1 to 4). The dropdown is sorted by Id, so users see the required order | `requirements.md` Glossary | Decided with I-1: positions accepted, dropdown sorted by Id |
| Observation | Elements not named in the prompts: structure `DepartmentSeed` (task 2), aggregate `GetDepartments` on Employee_List (prompt B), anonymous structure `Department, Employee Record` and its list type (derived) | In the app | Not in `requirements.md` | `DepartmentSeed`: you decided to keep, not a deviation. `GetDepartments`: inside the intended scope (the dropdown needs it). The derived types follow from the two-source aggregates |
| Observation | Dropdown position | Mentor's summary says "below `Input_Search` on its own line". The 7 to 8 graph notes say a new container in the same parent as `Input_Search` | Prompt B item 3 says "next to" | No AC covers the position. Not decided. Your task 8 statements give the dropdown order but not its position (the placeholder "[below / beside]" was left unfilled), so this item is still **not covered** (section 3) |
| Pending | `employee-catalog/requirements.md` still lists "Departments" as out of scope and has no AC-07 or AC-08 | `spec.md` the same | This spec | Task 10 updates both, as planned. Not a fault |

Elements outside the scope of the two publishes, from the graph comparisons: none in revisions 5 (findings F-1 to F-5 in `4-to-5-notes.md`, F-1 fixed by I-1), 7 and 8. Revision 9 is the only change outside the plan (U-3, logged, added to D-4).

## 10. Open items for the user

Settled by you on 2026-11-22: revision 9 (confirmed, logged as U-3, added to D-4, button not removed) and the delete rule (`Protect` kept).

1. **Items still without a record** (the user left a placeholder unfilled, or the statements do not cover them):
   - AC-04 (and the Alice part of AC-07 step 3): the five values of Alice Anderson's detail (First name, Last name, Email, Job title, Active). Placeholder "[values]" unfilled.
   - Dropdown position, below or beside the search input (Mentor's "below" against the prompt's "next to"). Placeholder "[below / beside]" unfilled.
   - Exact text of the empty option. Placeholder "[exact text]" unfilled. The label question "All Departments" (chat) against "All departments" (prompt 008) stays open.
   - AC-03: Maya Petrov and Quinn Abara not listed. The user reported only that Hugo is not listed (first statement) and that Maya and Quinn open by Id.
   - AC-06: Active = No for Hugo (8), the total of 20 records, and Alice's Active value. Maya's and Quinn's Active = No is recorded.
   - Smaller gaps inside recorded steps: the Human Resources count on its own (AC-07 step 2), whether the search was cleared (AC-08 step 4), the Finance row count (AC-08 step 1), and the full stop of "No employees found." (AC-05, not required by `requirements.md`).
2. **Small points to confirm:** whether the empty option label is "All Departments" or "All departments". The revision label is settled: revision 9, as you state.
3. **Consistency check against `requirements.md`:** every reported value agrees with the assignment table and its totals (Engineering 7 active, Sales 5 active, Finance Elena and Kara, Maya Engineering and inactive, Quinn Finance and inactive). No reported result disagrees with a requirement. One wording point: `employee-catalog/requirements.md` AC-05 requires only no rows, while the message text and its full stop come from this spec's `design.md`, `tasks.md` and prompt 008.
4. **Task 10.** It runs "after tasks 8 and 9 passed, or after you accept the reported failures". AC-07 and AC-08 have a reported result for every step, and no failure is reported. The items in item 1 have no record, so either supply them or accept them as unrecorded before task 10 starts. Task 10 was not started.
