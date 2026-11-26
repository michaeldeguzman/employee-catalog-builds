# Implementation Plan: add-department
## Overview
This plan adds a Department to each employee of the existing app EmployeeCatalogMW, shows it on the Employees and Employee_Details screens, and adds a Department filter to the Employees screen. It follows design.md: two direct Mentor prompts through the OutSystems MCP, each followed by its own publish and its own graph check, then the browser checks by the user, a check report, and the last task.
All files created by these tasks are under MentorWeb/ (prompts in MentorWeb/Prompts/, graphs and comparisons in MentorWeb/Reports/graphdiff/, the report in MentorWeb/Reports/, the BRD in MentorWeb/BRD/). Nothing is written to SDD Base and nothing is written to /tmp. The only app touched is EmployeeCatalogMW. There is no custom code and there are no Playwright tests in this plan.
Tasks marked [CONFIRM] are tenant writes: Kiro asks the user first and sends nothing until the user says yes. Every Mentor send and every publish is a [CONFIRM] task.
Prompt 1 and prompt 2 are the code blocks in design.md ("Components and Interfaces"). They are sent word for word.
## Tasks
- [x] 1. USER STEP (gate): confirm the timer budget and that ODC Studio is closed
  - This is a user step and is not run by Kiro. Kiro starts no other task before the user confirms both points.
  - Confirm the timer budget: in the ODC Portal, the Run now action on the timer LoadSampleDataOnPublish (App EmployeeCatalogMW, Configurations, Timers) works, and does not fail with OS-TMR-42900.
  - Confirm that ODC Studio is closed, so no Studio publish can land between Kiro's turns.
  - Kiro cannot read the timer state or the data, so these are the user's statements.
  - _Requirements: AC-07_
- [x] 2. [CONFIRM] Send the data prompt (prompt 1) to Mentor
  - Before asking: read app_revisions for EmployeeCatalogMW (asset key 07a64c21-0c8c-8afb-28ee-5d8530d55cf8). The latest revision must be 6, the revision of `Reports/graphdiff/rev6.txt`. If it is newer, save its graph in `Reports/graphdiff/` and compare it with rev6 first (design.md, "Before each prompt and publish"), and tell the user.
  - Ask the user to confirm the tenant write. Send nothing before the answer is yes.
  - Open one new Mentor session for this task. Send prompt 1 from design.md, word for word, as one single prompt, with the app key as the only asset reference.
  - Poll the run until it is terminal. Read the asset facts for EmployeeCatalogMW (attemptedChange, changeApplied, validation errors and warnings) and the pending model changes. Report Mentor's summary as Mentor's own words, not verified.
  - If the run fails or times out, retry in the same session with a narrower prompt, never in a new app. Tell the user before any retry.
  - Do not publish in this task. Do not start another turn on this session until the run is terminal.
  - Save the exact prompt sent as one file in MentorWeb/Prompts/ (add-department-data-prompt.md), with the session id, the run id and the result.
  - _Requirements: AC-07_
- [x] 3. [CONFIRM] Publish 1
  - Before asking: the run of task 2 is terminal, app_revisions shows no publish newer than the one seen in task 2, and no other publish of this app is known to be running.
  - Ask the user to confirm the publish. Tell the user that publishing runs the timer LoadSampleDataOnPublish, which sets the Department of the 20 employees.
  - Send one publish turn in the same session as task 2, with the app key as the only asset reference and this note: "add-department 1: Department static entity, Employee.DepartmentId, one-time department update in LoadSampleData."
  - Poll until terminal. Read the publish outcome, the revision and the publication key. Check with publish_status and publish_logs, and with env_app that the revision is deployed in Development. A timed-out or indeterminate publish is never repeated: check it by its publication key first.
  - If the run reports a conflict or a merge with another revision, stop and ask the user.
  - Close the Mentor session after the publish has landed.
  - USER STEP inside this task: if the timer cannot run on publish (OS-TMR-42900 or the daily limit), the user clicks Run now on LoadSampleDataOnPublish in the ODC Portal. This is an operational step, not a model change. Kiro cannot see whether it ran.
  - _Requirements: AC-07_
- [x] 4. Graph check after publish 1
  - Read the full stored graph of the new revision with context_graph (no root, all pages). Retry after about a minute on graph_pending. Save it as `MentorWeb/Reports/graphdiff/rev<N>.txt`.
  - Compare it with the previous saved revision (rev6, or the interim revision from task 2) with scope.py and diff.py from `Reports/graphdiff/`. Save the output as `compare-rev<A>-rev<B>.txt` in the same folder. Read the flow of LoadSampleData and LoadSampleDataForEmployee with flow.py.
  - Check the intended scope in design.md ("Graph comparison after each publish", publish 1): the Department static entity and its 4 records, Employee.DepartmentId, the entity actions that follow from it, LoadSampleData, LoadSampleDataForEmployee and the module stamps.
  - Check that the update in LoadSampleData sets only empty DepartmentId, matches by Email, runs on every path to End, and sits under IsInDevStage(), as far as the graph shows. Text literals are hidden in the graph, so the Email and Department values are not readable. Say so.
  - Report every change outside the intended scope (existing filters, roles and permissions, the timer, ImportData, EmployeeStructure, the Excel actions, any stateflow elements, other attributes). Do not fix anything. Stop and tell the user before task 5.
  - _Requirements: AC-07_
- [x] 5. [CONFIRM] Send the screens prompt (prompt 2) to Mentor
  - Before asking: publish 1 is finished and the graph check of task 4 is reported. Read app_revisions: the latest revision must be the revision saved in task 4. If it is newer, save and compare it first.
  - Ask the user to confirm the tenant write. Send nothing before the answer is yes.
  - Open one new Mentor session for this task. It starts from the published revision of publish 1. Send prompt 2 from design.md, word for word, as one single prompt, with the app key as the only asset reference.
  - Poll until terminal. Read the asset facts, the pending model changes and Mentor's summary, as in task 2.
  - If the run fails or times out, retry in the same session with a narrower prompt, never in a new app. Tell the user before any retry.
  - Do not publish in this task.
  - Save the exact prompt sent as one file in MentorWeb/Prompts/ (add-department-screens-prompt.md), with the session id, the run id and the result.
  - _Requirements: AC-07, AC-08_
- [x] 6. [CONFIRM] Publish 2
  - Before asking: the run of task 5 is terminal and app_revisions shows no publish newer than the one seen in task 5.
  - Ask the user to confirm the publish. Tell the user that publishing runs the timer again, and that the update is safe to run again.
  - Send one publish turn in the same session as task 5, with the app key as the only asset reference and this note: "add-department 2: Department column and filter on Employees, Department on Employee_Details."
  - Poll until terminal and check the outcome, the revision and the publication key as in task 3. Never repeat a publish. Stop and ask on a conflict or a merge.
  - Close the Mentor session after the publish has landed.
  - USER STEP inside this task: if the department update did not run after publish 1 and does not run now, the user clicks Run now on LoadSampleDataOnPublish in the ODC Portal.
  - _Requirements: AC-07, AC-08_
- [x] 7. Graph check after publish 2
  - Read the full stored graph of the new revision, save it as `Reports/graphdiff/rev<N>.txt`, and compare it with the revision saved in task 4, as in task 4. Save the comparison output in the same folder.
  - Check the intended scope in design.md (publish 2): the Employees screen (GetEmployees with the new source and one new filter condition, one new column, DepartmentDropdown, SelectedDepartmentId, OnDepartmentChange), the Employee_Details screen (GetEmployeeById with the new source, one new field) and the module stamps.
  - Check that both joins are With or Without, that the existing three filters of GetEmployees are unchanged, and that OnSearch, OnSort and OnPaginationNavigate are unchanged.
  - Report every change outside the intended scope. Do not fix anything. Stop and tell the user before task 8.
  - _Requirements: AC-07, AC-08_
- [x] 8. USER STEP: browser checks
  - This is a user step. The user checks at https://your-tenant-dev.outsystems.app/EmployeeCatalogMW as a Staff user, without ODC Studio, and reports what is seen. Kiro does not see the data.
  - AC-07: scan the 17 rows (2 pages) against the Department assignment table. Open Alice Anderson (Engineering), Grace Lindholm (Human Resources) and Liam Oduya (Sales) and check the detail screen.
  - AC-08: choose Finance and see only Elena Novak and Kara Whitfield. With Finance chosen, search "Kara" shows only Kara Whitfield, and search "Alice" shows no rows. Choose Engineering (7 rows), Human Resources (3 rows) and Sales (5 rows), then "All departments" (17 rows).
  - Inactive employees: the user gives Kiro the EmployeeIds of Hugo Brandt, Maya Petrov and Quinn Abara after publish 2. The user opens Employee_Details with each EmployeeId and reports the Department: Finance, Engineering and Finance.
  - Short re-check of AC-01 to AC-06: AC-01 17 active rows with FirstName, LastName, JobTitle, Email (and Department). AC-02 "Alice" shows Alice Anderson. AC-03 Hugo Brandt, Maya Petrov and Quinn Abara are not in the list. AC-04 one row opens a detail with FirstName, LastName, Email, JobTitle and IsActive. AC-05 "Hugo" shows no rows. AC-06 17 rows plus the 3 inactive employees opened by Id make 20, and Alice is active.
  - If every Department cell is empty, the update has not run: the user clicks Run now on the timer, reloads, and checks again. No model change.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06, AC-07, AC-08_
- [x] 9. Read the delete rule and write the check report
  - Read the Delete Rule of Employee.DepartmentId in the graph of the last revision saved in task 7. Report the value. Do not change it.
  - Write the report as one file in MentorWeb/Reports/.
  - Per AC (AC-07 and AC-08, and the re-check of AC-01 to AC-06): pass or fail, the evidence (hand, with the revision, or static, from the graph), what was not checked, and whether Mentor produced it or a fallback was needed.
  - Include an "Interventions" section: each prompt sent (exact text), the session and run ids, each publish with its revision and publication key, the timer Run now steps by the user, and any follow-up prompt.
  - Include the graph comparison findings for both publishes, with every change outside the intended scope, and the docs sync date (last_updated).
  - List any disagreement between the app and the requirements, without changing either one.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06, AC-07, AC-08_
- [x] 10. Last task: update employee-catalog requirements.md and regenerate the BRD
  - Use only this workspace, the outsystems-docs MCP and the tenant (read-only). Do not read the MCP folder. Do not touch the tenant except read-only lookups.
  - Start only after task 9, and only if the report has no failed AC. If an AC failed, ask the user first.
  - Update `MentorWeb/.kiro/specs/employee-catalog/requirements.md` as listed in this spec's requirements.md ("Changes to the employee-catalog requirements.md"): add Department and DepartmentId to the Glossary, add Requirements 6 and 7 with AC-07 and AC-08, add Department to the columns named in AC-01 and to the attributes named in AC-04, remove "Departments (no Department entity in this version)" from Out of scope, and add Department_Assignment to the sample data. Change nothing else in the file.
  - Copy the current `MentorWeb/BRD/EmployeeCatalogMW-BRD.md` to `MentorWeb/Reports/scratch/EmployeeCatalogMW-BRD.before-add-department.md`.
  - Regenerate the BRD in `MentorWeb/BRD/` from the updated requirements.md, in Mentor format. Follow the mentor-standards steering file in SDD Base (read only) and check the format with the outsystems-docs MCP (search_docs, source "odc"), reporting the last_updated sync date. Save the generation prompt as one file in `MentorWeb/Prompts/`.
  - Never edit the BRD by hand. Do not upload it to Mentor Web. Do not change the app.
  - _Requirements: AC-07, AC-08_
## Notes
- Tasks 1 and 8, and the Run now steps inside tasks 3 and 6, are user steps. Kiro does not run them.
- Tasks 2, 3, 5 and 6 are [CONFIRM] tasks. No Mentor prompt and no publish is sent without the user's yes for that task.
- One Mentor session per prompt task (2 and 5). The publish of tasks 3 and 6 is a separate turn in the same session. A session runs one turn at a time. A publish is never retried.
- Tasks 4 and 7 end by reporting to the user. Kiro does not start the next task before that.
- The graph scripts and the baseline rev6.txt are already in `MentorWeb/Reports/graphdiff/`. Nothing is written to /tmp.
- BRD files are generated and never edited by hand.
- Decisions after task 7 (user, for task 9):
  - Revision 9 is an unplanned ODC Studio publish by the user at about 13:48 AEDT (02:48:33Z), after publish 2 (revision 8, 02:45:05Z, publication key fd32cd29-4e06-a6f6-69f9-2418d2ce835d). Log it in the report's revision history table, as in `Reports/EmployeeCatalogMW-verification-report.md` (revisions 3 and 5): Made by "the user, ODC Studio", What "Unplanned. No functional change. Reason not stated". List it separately from the Interventions section, which holds only the Mentor prompts and publishes Kiro sent. Add a comparison line for it (stamps only, evidence in `Reports/graphdiff/compare-rev7-rev9.txt`) and the sentence "A build comparison should count them as unplanned, with no functional change". No revision 8 graph exists, because context_graph returns only the latest revision. The graph check of task 7 therefore read revision 9 as revision 8 plus stamps, which is an inference. Say so in the report.
  - Task 7 findings 2 and 3 are accepted as part of the dropdown: the new aggregate `GetDepartments` (MaxRecords 50, sorted by Label ascending) and the extra Container (3 col) around `DepartmentDropdown` in Filters. In the report, list them as in scope, with the user's acceptance as the reason.
  - Task 7 finding 1 stays open until task 8: the Department field on Employee_Details is nested inside the Job Title field's container (between the Job Title label and value), while Mentor said it placed the field between Job Title and Is Active. The user checks the rendering in the browser in task 8. In the report, record the user's result, and do not fix it without a decision.
- Intervention I-1 (user decision after task 8): a fix prompt moved the Department field on Employee_Details out of the Job Title field's container. Prompt, session 8bee7696-2c22-cbc8-e5be-d6f84475dacc, run ace55c12-b0ec-aec3-d8ea-9491ffb941ff and the result are in `Prompts/add-department-fix-department-field-prompt.md`. Publish: revision 10, publication key 0a330d7b-8136-eb1e-f376-3832e5454d52, 2026-11-22T03:20:11Z, note "add-department I-1: Department field on Employee_Details moved out of the Job Title field." Graph check: `Reports/graphdiff/rev10.txt` and `compare-rev9-rev10.txt` (only Employee_Details changed, only the Department field moved, Job Title holds only its label and value). In the task 9 report, list I-1 in the Interventions section as a follow-up prompt, with the revision and publication key. This is the reason for finding 1. The user's browser re-check of the detail page after revision 10 is recorded in the report when the user reports it. The report's graph findings for both publishes read the last revision, 10, for the delete rule in task 9.
- Task 8 results (reported by the user; the checks were done in the browser by Claude in Chrome on the user's instruction, read-only, and the user reviewed the report and the screenshots; app EmployeeCatalogMW, revision 9, the user's Staff test user):
  - Columns: First Name, Last Name, Job Title, Email, Department. Department has no sort icon. 17 rows over 2 pages.
  - AC-07: all 17 rows show the department from the assignment table, none wrong or empty. Detail pages: Alice Anderson (EmployeeId 14) Engineering, Grace Lindholm (20) Human Resources, Liam Oduya (25) Sales.
  - Inactive employees opened by Id: Hugo Brandt 21 (Active No, Finance), Maya Petrov 26 (Active No, Engineering), Quinn Abara 30 (Active No, Finance). None of the three appears in the list.
  - AC-08: Finance = Elena Novak and Kara Whitfield. Finance + "Kara" = Kara Whitfield. Finance + "Alice" = no items. Engineering 7 rows, Human Resources 3, Sales 5, All departments 17.
  - Dropdown: beside the search box, to its right. Empty option "All departments". Order: All departments, Engineering, Finance, Human Resources, Sales.
  - Re-check of AC-01 to AC-06: "Alice" = Alice Anderson. "Hugo" = no items. The detail shows the employee name, Job Title, Department, Is Active and Email. No editable fields and no Save or Delete buttons.
  - Finding 1 confirmed as a layout defect on every employee checked (Department label and value between the "Job Title" label and its value). The user decided to fix it as I-1.
- I-1 browser re-check on revision 10 (reported by the user; done by Claude in Chrome on the user's instruction, read-only, and the user reviewed three screenshots): EmployeeId 14 Alice Anderson (Job Title Software Engineer, Department Engineering, Is Active Yes), EmployeeId 21 Hugo Brandt (Finance Analyst, Finance, Is Active No), EmployeeId 25 Liam Oduya (Sales Representative, Sales, Is Active Yes). On all three, Department is its own field after Job Title and before Is Active. No editable fields and no Save or Delete buttons. Record I-1 as fixed and verified in the browser, for those three employees. Finding 1 is closed.
- Evidence labels for the task 9 report: the browser results above are "by hand, through the user" (Claude in Chrome, reviewed by the user). Kiro did not see the data. The Department values per employee are not checked by Kiro beyond what the user reported. The timer Run now steps: the user did not report one in task 8, so the report says "not reported".
## Task Dependency Graph
```json
{
  "waves": [
    { "id": 0, "tasks": ["1"] },
    { "id": 1, "tasks": ["2"] },
    { "id": 2, "tasks": ["3"] },
    { "id": 3, "tasks": ["4"] },
    { "id": 4, "tasks": ["5"] },
    { "id": 5, "tasks": ["6"] },
    { "id": 6, "tasks": ["7"] },
    { "id": 7, "tasks": ["8"] },
    { "id": 8, "tasks": ["9"] },
    { "id": 9, "tasks": ["10"] }
  ]
}
```
