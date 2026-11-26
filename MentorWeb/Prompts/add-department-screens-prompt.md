# add-department, task 5: screens prompt (prompt 2)
Status: sent to Mentor, run succeeded. Not published. Publish 2 is task 6 and needs its own confirmation.
- App: EmployeeCatalogMW (asset key 07a64c21-0c8c-8afb-28ee-5d8530d55cf8). No other app was referenced.
- Mentor session: f7e87282-b5af-e6bb-4393-9be764f3577f (new session, one session for this task)
- Run: a5c0336c-ae32-151b-81a1-176a0f06459b
- Sent as one single prompt, with the app key as the only asset reference. Wording: prompt 2 of design.md ("Task 2: screens prompt (then publish 2)"), word for word.
- Revision before sending: app_revisions showed revision 7 as the latest (2026-11-22T02:20:28Z, model digest 4ef9300f-41f9-c9e7-a19a-b66a2170f554), the revision saved in task 4 (Reports/graphdiff/rev7.txt). No newer revision, so no comparison was needed.
- The user confirmed the tenant write before anything was sent.
## Prompt sent (exact)
```
In the EmployeeCatalogMW app, show the Department on the Employees screen and the Employee_Details screen, and add a Department filter to the Employees screen. The Department static entity and the Employee.DepartmentId attribute already exist.

Employees screen:
1. In the GetEmployees aggregate, add the Department static entity as a source, joined to Employee on Employee.DepartmentId = Department.Id with a With or Without join, so that employees without a Department are still returned.
2. In the Table widget, add a column with the header Department as the last column, after Email. It shows Department.Label of the row. It is not sortable. Keep the four existing columns as they are.
3. Add a local variable SelectedDepartmentId to the screen. Its data type is Department Identifier and its default value is empty (the null identifier).
4. Add a Dropdown named DepartmentDropdown to the existing Filters container, next to the Search block. Bind it to SelectedDepartmentId. Its options are the records of the Department static entity, sorted by Label, with Label as the text and Id as the value. Add a first option with the text "All departments" and an empty value.
5. Add a screen action OnDepartmentChange and run it on the OnChange event of DepartmentDropdown. It sets StartIndex to 0 and refreshes GetEmployees, as OnSearch does.
6. In GetEmployees, add a new, separate filter condition: SelectedDepartmentId is empty, or Employee.DepartmentId = SelectedDepartmentId. Keep the existing search filter on SearchKeyword, the existing IsActive = True filter and the existing role-check filter exactly as they are, so that all of them apply together. An employee without a Department is returned when no department is chosen and is not returned when a department is chosen.

Employee_Details screen:
7. In the GetEmployeeById aggregate, add the Department static entity as a source, joined to Employee on Employee.DepartmentId = Department.Id with a With or Without join. Keep its two existing filters.
8. Show the department on the screen as a field with the label Department and the value Department.Label of the employee, in the same style and group as the other Employee fields. The value is empty when the employee has no Department.

Do not change anything else: not the other columns, the search, the sort, the pagination, the EmployeeStructure structure, the ImportData screen, any other screen, any role or any sample data action. Do NOT publish the app in this turn.
```
## Run result (before any publish)
- Run status: succeeded, after about 1 minute (Mentor: "Worked for 1m 0s"). Polled about every 40 seconds. No retry was needed and no second prompt was sent on this session.
- Asset facts for EmployeeCatalogMW: attemptedChange true, changeApplied true, validation 0 errors, 16 warnings (the same count as after the data prompt run). No first messages were returned.
- Pending model changes reported by Mentor (final list, one event):
  - Modified: screen Employees (IMobileScreen), screen Employee_Details (IMobileScreen).
  - Nothing else is listed. No server action, entity, role, timer, structure or module change is listed, and the sample data actions, ImportData, UploadEmployeeExcel and DownloadEmployeeExcel are not in the list. The list only says "Modified" for the two screens and does not say what changed inside them.
- Mentor's summary (its own words, not verified against the model), paraphrased closely:
  - Employees screen: GetEmployees now includes the Department static entity, joined on Employee.DepartmentId = Department.Id with a With or Without join. The table has a new last column, Department, after Email. It shows Department.Label and is not sortable. The local variable SelectedDepartmentId has type Department Identifier and an empty default. DepartmentDropdown is in the Filters container next to the search, bound to SelectedDepartmentId. Its options come from a new GetDepartments aggregate sorted by Label, with Label as the text and Id as the value. The first option is "All departments" with an empty value. OnDepartmentChange runs on the dropdown's OnChange, sets StartIndex to 0 and refreshes GetEmployees, as OnSearch does. GetEmployees has a new, separate filter: SelectedDepartmentId = NullIdentifier() or Employee.DepartmentId = SelectedDepartmentId. The search, IsActive = True and role-check filters are unchanged, so all four apply together.
  - Employee_Details screen: GetEmployeeById also joins Department on Employee.DepartmentId = Department.Id with a With or Without join. Its two existing filters are unchanged. A new Department field sits in the Employment Details group, between Job Title and Is Active, styled like the other fields, showing Department.Label (empty when the employee has no department).
  - Mentor says it changed nothing else, that validation shows no errors (only warnings that were already there), and that it did not publish. It asks the user to check in the browser how the dropdown looks next to the search.
- Notes for the graph check of task 7 (not findings yet):
  - The new aggregate GetDepartments is not named in prompt 2. The prompt asked for dropdown options from the records of the Department static entity, and Mentor built them with a separate aggregate. It is a new element on the Employees screen. It is checked in the graph and reported in task 7. Nothing was changed by Kiro.
  - Mentor placed the new Employee_Details field between Job Title and Is Active. The prompt said "in the same style and group as the other Employee fields" and did not name a position.
  - The model is not read by Kiro yet. The three existing GetEmployees filters, the With or Without joins, OnSearch, OnSort and OnPaginationNavigate are checked in the graph after publish 2 (task 7). The browser behaviour is checked by the user in task 8.
- The session f7e87282-b5af-e6bb-4393-9be764f3577f has not been closed. Publish 2 (task 6) uses this same session.

## Publish 2 (task 6)
Status: published. Revision 8 is deployed in Development. The Mentor session is closed.
- The user confirmed the publish before anything was sent.
- Before asking: the task 5 run a5c0336c-ae32-151b-81a1-176a0f06459b was read again with mentor_get_run: status succeeded, changeApplied true, 0 validation errors, 16 warnings. app_revisions showed revision 7 as the latest (no newer publish).
- Publish turn: sent in the same session f7e87282-b5af-e6bb-4393-9be764f3577f, with the app key 07a64c21-0c8c-8afb-28ee-5d8530d55cf8 as the only asset reference. No other app was referenced.
- Publish run: e164c94b-6a17-13e7-996b-c540742bb131. Sent once, not repeated.
- Publish note: "add-department 2: Department column and filter on Employees, Department on Employee_Details."
- Prompt text sent (one turn): Publish the EmployeeCatalogMW app now. Publish note: "add-department 2: Department column and filter on Employees, Department on Employee_Details." Do not change anything else in the app.
- Revision: 8 (revisionDateTime 2026-11-22T02:45:05Z, model digest f62c880f-bdf7-347c-d49f-6937251afab5).
- Publication key: fd32cd29-4e06-a6f6-69f9-2418d2ce835d.
- Outcome: success.
  - Run events: publishStarted, publishAccepted (revision 8), publishSucceeded (revision 8). The run ended succeeded after about 22 seconds. Its pending model changes list was empty (the screen changes of task 5 were already pending in the session and are part of this revision). No conflict and no merge with another revision was reported.
  - publish_status: Finished, outcome success, applicationRevision 8.
  - publish_logs: Info messages only (OS-DPL-20012, 20002, 20003, 20004, 20019, 20005, 20007). No errors, no warnings, no OS-* error codes.
  - env_app (Development, env key 8b036dbd-6d28-2b5c-c50a-77a6bc07d748): revision 8, build key 1c6611b5-51a5-7b7a-588c-b3834d83c9d2, deployment key fd32cd29-4e06-a6f6-69f9-2418d2ce835d, deployed 2026-11-22T02:45:05Z. URL: https://your-tenant-dev.outsystems.app/EmployeeCatalogMW
  - app_revisions after the publish: revision 8 is the latest, revision 7 is the one before it. No other revision appeared in between.
- Mentor session f7e87282-b5af-e6bb-4393-9be764f3577f closed after the publish landed (closed: true).
- Timer: publishing runs LoadSampleDataOnPublish again. Kiro cannot see the timer state or the data. The update is safe to run again. If the department update did not run after publish 1 and did not run now, the user clicks Run now on LoadSampleDataOnPublish in the ODC Portal (USER STEP of task 6). Not confirmed by the user at the time of this record.
- Next: task 7 (graph check of revision 8, saved as Reports/graphdiff/rev8.txt and compared with rev7). Not started.
