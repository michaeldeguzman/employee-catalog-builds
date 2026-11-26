# Check report: EmployeeCatalogMW against the add-department requirements

Task 9 of spec add-department (change to Build 1: Mentor Web).

## Basis
- App: EmployeeCatalogMW, asset key 07a64c21-0c8c-8afb-28ee-5d8530d55cf8, ODC Development environment (env key 8b036dbd-6d28-2b5c-c50a-77a6bc07d748). URL: https://your-tenant-dev.outsystems.app/EmployeeCatalogMW. Reactive Web. No other app was touched (see "Read-only checks").
- Last revision: revision 10 (2026-11-22T03:20:11Z, publication key 0a330d7b-8136-eb1e-f376-3832e5454d52). The browser checks of task 8 were made on revision 9. Only three detail pages were re-checked on revision 10 (see "What was checked on which revision").
- Checked against: `.kiro/specs/add-department/requirements.md` (AC-07, AC-08) and `.kiro/specs/employee-catalog/requirements.md` (AC-01 to AC-06, the AC text of the first build). Neither file was changed. The BRD was not changed.
- Docs sync date (outsystems-docs MCP, `last_updated`, called when this report was written, 2026-11-22T03:31Z): 2026-10-28T09:05:12.959543+00:00. design.md recorded 2026-10-28T09:05:12Z at design time. The docs have not been synced since the design, so the research notes and the design rest on the same docs.
- Source notes: `Prompts/add-department-data-prompt.md`, `Prompts/add-department-screens-prompt.md`, `Prompts/add-department-fix-department-field-prompt.md`, the graphs and comparisons in `Reports/graphdiff/` (rev6, rev7, rev9, rev10; compare-rev6-rev7, compare-rev7-rev9, compare-rev9-rev10), and the Notes section of tasks.md (the user's decisions after task 7 and the results of task 8 and I-1).

## How to read the evidence
- **By hand, through the user**: Claude in Chrome made the checks in the browser on the user's instruction (read-only, as the user's Staff test user). The user reviewed the report and the screenshots and gave the results to Kiro. Kiro did not see the screen or the data. This report states only what the user reported.
- **Static**: Kiro read the stored app model (context_graph) of the named revision. The app was not run. The read tools have no data query. The graph hides text literals inside aggregates and actions (it shows only their length and a hash). UI strings, labels and style classes are readable.
- Revision 8 has no graph. context_graph always serves the latest revision, so only revisions 7, 9 and 10 could be saved. Statements about revision 8 are inferences from revision 9 (see the revision history).

## Result per AC

| AC | Result | Evidence | Mentor produced it? | Fallback |
|---|---|---|---|---|
| AC-07 department shown | Pass | By hand, through the user (revision 9): all 17 rows show the department from the assignment table, none wrong or empty. Detail pages: Alice Anderson (EmployeeId 14) Engineering, Grace Lindholm (20) Human Resources, Liam Oduya (25) Sales. The 3 inactive employees opened by Id: Hugo Brandt (21) Finance, Maya Petrov (26) Engineering, Quinn Abara (30) Finance. All equal to the table. By hand, through the user (revision 10): Department shown on the detail pages of EmployeeId 14 (Engineering), 21 (Finance) and 25 (Sales). Static (revision 10): GetEmployees and GetEmployeeById have the Department source with a left join ("Employee with or without Department"); the table has 5 header cells and 5 row cells; the update SetEmployeeDepartments in LoadSampleData (revision 7, unchanged since) matches 20 of 20 emails to the table | Yes. The data prompt, the screens prompt and the publishes did it. The update route (an update inside the bootstrap) came from design.md, because Mentor is not documented to update existing records | None for AC-07. One follow-up prompt (I-1) fixed the position of the field on Employee_Details, see Interventions |
| AC-08 department filter | Pass | By hand, through the user (revision 9): Finance shows Elena Novak and Kara Whitfield. Finance and search "Kara" shows Kara Whitfield. Finance and search "Alice" shows no items. Engineering 7 rows, Human Resources 3, Sales 5, "All departments" 17. Dropdown beside the search box, to its right, with the empty option "All departments", then Engineering, Finance, Human Resources, Sales. Static (revision 10): GetEmployees has 4 filter conditions. The 3 existing ones are structurally identical to revision 7 (and revision 6: only a stamp changed on GetEmployees in revision 7). The new one reads `SelectedDepartmentId = <call> or Employee.DepartmentId = SelectedDepartmentId`. Local variable SelectedDepartmentId, DepartmentDropdown with an On Change event, and a new client action with an assignment and a refresh of data exist | Yes. Flagged in the research (dropdown with search and the active-only rule not documented for Mentor). Mentor built it from the prompt, with no fallback | None |
| AC-01 list loads | Pass | By hand, through the user (revision 9): columns First Name, Last Name, Job Title, Email, Department (the four AC columns plus Department). 17 rows over 2 pages. Department has no sort icon | Yes (first build) | None in this change |
| AC-02 search | Pass | By hand, through the user (revision 9): "Alice" shows Alice Anderson. Static: the search condition has the same structure in revision 7 and revision 10 | Yes (the first build needed fallback 5.1; unchanged by this change) | None in this change |
| AC-03 inactive hidden | Pass | By hand, through the user (revision 9): none of Hugo Brandt, Maya Petrov, Quinn Abara is in the list. Static: the condition Employee.IsActive = True is unchanged | Yes (first build fallback 5.2; unchanged by this change) | None in this change |
| AC-04 detail screen | Pass, partial coverage | By hand, through the user (revision 9): the detail shows the employee name, Job Title, Department, Is Active and Email. No editable fields and no Save or Delete buttons. Revision 10, three employees: Job Title, Department and Is Active shown | Yes (first build) | None in this change |
| AC-05 empty search result | Pass | By hand, through the user (revision 9): "Hugo" shows no items. Also Finance with "Alice" shows no items | Yes (first build fallbacks 5.1 and 5.2; unchanged by this change) | None in this change |
| AC-06 sample data present | Pass, partial coverage | By hand, through the user (revision 9): 17 rows in the list plus 3 inactive employees opened by Id (21, 26, 30) make 20. Alice is active (Is Active Yes on revision 10, EmployeeId 14) | Yes (first build fallback 5.3; unchanged by this change) | None in this change |

Summary: 8 of 8 ACs pass on the evidence below. No AC failed. AC-07 and AC-08 were produced by Mentor from two direct prompts, with no fallback prompt. One follow-up prompt (I-1) was needed for a layout defect on Employee_Details, which was not an AC failure. The AC-01 to AC-06 re-check found no regression on revision 9 (browser) and no change to their elements in the graph (revision 7 to 10).

### What was checked on which revision
- Browser checks, all AC (task 8): revision 9 (revision 8 plus the user's Studio publish, see the history).
- Browser re-check after I-1: revision 10, EmployeeId 14, 21 and 25, the detail page only.
- Graph: revision 7 (task 4), revision 9 (task 7, read as revision 8 plus stamps), revision 10 (I-1, and this task: the Delete Rule and the joins and filters of the two aggregates, read again from rev10.txt with inline Python, no script saved).

### What was not checked, per AC
- AC-07
  - The Department on the detail page of the 14 employees not opened (6 were opened on revision 9, 3 of them also on revision 10).
  - The Employees screen on revision 10. The graph shows it unchanged between revisions 9 and 10, but the list was not looked at again in the browser.
  - An employee with no Department (all 20 have one). Static only: the left join and the filter condition.
  - The timer run itself. Kiro cannot read the timer state or the data. The user read the Last run of LoadSampleDataOnPublish in the ODC Portal (see Interventions, "Timer"), so the run after publish 1 is the user's statement. Whether it ran after revisions 8 and 10 is not known (the Portal reading was not tied to a time).
  - The text literals in the update (emails, and the mapping to labels) are hashed in the graph. The mapping was checked in task 4 by matching the hashes (20 of 20), and the SQL text itself is readable in the graph.
- AC-08
  - The dropdown behaviour on revision 10 (the browser checks were on revision 9; the graph shows the Employees screen unchanged in revision 10).
  - Paging with a department chosen, changing the page and then the department, and the dropdown with sorting. Only the combinations listed in the table were tried.
  - Searches other than "Kara" and "Alice" with a department chosen.
  - A user without the Staff role.
  - An employee without a Department, with a department chosen (not shown) and with none chosen (shown). Static only.
  - The sorted order of the dropdown options is the reported order of the browser. The graph shows GetDepartments sorted by Label ascending, MaxRecords 50.
- AC-01: the column order by hand beyond the reported list. The paging (10 rows per page) is not in the AC and is not treated as a failure.
- AC-02: whether rows other than Alice Anderson were shown for "Alice". The user reported "Alice shows Alice Anderson". Case sensitivity of the Like operator. Which attributes the search matches is not readable from the graph (the identifiers were not read in this task); the structure is the same as in revisions 6 and 7.
- AC-03: only the three inactive names were checked, plus the count of 17.
- AC-04: the detail was reported as "the employee name", so FirstName and LastName as two separate fields are not confirmed. IsActive was shown as Is Active (Yes or No). Email was reported on revision 9 and not on the revision 10 re-check. Whether the detail pages were opened through a row link is not stated (the inactive employees were opened by Id).
- AC-05: only "Hugo" and "Alice" with Finance. Text matching only a job title or an email, and text matching nothing at all, were not tried.
- AC-06: the count of 20 is 17 + 3. It is not a count of the table. The other 14 names were read by the user against the assignment table (AC-07 scan) but Kiro did not see them. No check for extra records outside EmployeeId 14 to 30.

## Delete Rule of Employee.DepartmentId
- Value: **Protect** (stored graph, revision 10, attribute DepartmentId of the entity Employee, key 7skC5R_8TVsV6FYAotkxDn*MJzFZgOQZaN5yZ6w8irhwY). It was already Protect in revision 7. Read only, not changed.
- The prompt did not state a Delete Rule (requirements.md of this spec, Research notes Q2). Departments are static records, so no Department is deleted while the app runs. No decision is asked.
- Other DepartmentId facts read from the graph: Department Identifier, Foreign Key to Department, IsMandatory false, IsAutoNumber No, label "Department".

## Interventions
Each prompt below was sent through the OutSystems MCP as one single prompt, in its own Mentor session, with the app key as the only asset reference, after the user confirmed the tenant write. Each publish was a separate turn in the same session after the user confirmed it. No publish was repeated. Each Mentor session was closed after its publish landed. Each prompt is saved in `Prompts/`. Revision 9 is not in this list (see the revision history).

### Intervention 1: data prompt and publish 1 (task 2 and 3), AC-07
- Mentor session 9bd7d0f9-cdd1-c740-5138-5f7a236f5f88. Prompt run 4396579a-668b-5825-2a49-15149cc73ef9 (succeeded, about 2 minutes, no retry). Publish run d195b4f5-269f-b3ed-9f70-1fba90df885a (succeeded, about 24 seconds).
- Publish 1: revision 7, 2026-11-22T02:20:28Z, publication key ebf70064-658c-e43c-51fb-44e4fe3e5894. publish_status Finished, outcome success. publish_logs: Info messages only. No conflict and no merge was reported.
- Wording: prompt 1 of design.md, word for word (file `Prompts/add-department-data-prompt.md`).
- Mentor's run facts: attemptedChange true, changeApplied true, 0 validation errors, 16 warnings. Pending changes listed as Modified outside the named scope: screens Employees and Employee_Details, actions UploadEmployeeExcel and DownloadEmployeeExcel. See the graph findings for what changed in them.
- Mentor reported one deviation: it could not make the Department Id auto-number, so the 4 records have Ids 1 to 4 set by hand. The graph confirms it (IsAutoNumber No on Department.Id).
- Exact prompt:
```
In the EmployeeCatalogMW app, make these data changes.
1. Add a static entity named Department with only the default static entity attributes and no others. Give it exactly 4 records, with the labels Engineering, Finance, Human Resources and Sales. Department is a plain lookup list. Do not create a stateflow, state transitions or any status logic for it.
2. Add an attribute DepartmentId to the Employee entity. It is an Identifier and a Foreign Key to the Department static entity, and it is not mandatory. Do not change any other Employee attribute, any attribute length or the Picture attribute.
3. In the sample data bootstrap (server actions LoadSampleData and LoadSampleDataForEmployee, and timer LoadSampleDataOnPublish), add a one-time update that sets Employee.DepartmentId on the 20 existing sample employees. Match each employee by Email to the table below, and set DepartmentId to the Department record with that label. Set DepartmentId only on an Employee whose DepartmentId is empty. Never overwrite a DepartmentId that is already set, and change no other attribute, so that running the update again changes nothing. The update covers all 20 employees, including the 3 with IsActive false (Hugo Brandt, Maya Petrov and Quinn Abara). Add it in LoadSampleData so that it runs on every execution, on every path that reaches the End node, after the existing GetAliceRecord check, the cleanup and the empty-table check and load, under the same IsInDevStage() condition that LoadSampleData already uses. Refer to the Department records through the Department static entity, never by a hard-coded numeric Id. Keep the timer schedule as it is (WhenPublished), and keep the GetAliceRecord check, DeleteAllEmployees and the empty-table check as they are.
4. In LoadSampleDataForEmployee, add the department to the 20 sample records, using the same table, so that when the Employee table is empty and the 20 records are loaded, each record is created with its DepartmentId already set.
Email, Department:
alice.anderson@example.com, Engineering
bruno.castillo@example.com, Engineering
carla.dubois@example.com, Engineering
devon.marsh@example.com, Engineering
elena.novak@example.com, Finance
felix.okafor@example.com, Engineering
grace.lindholm@example.com, Human Resources
hugo.brandt@example.com, Finance
irene.takeda@example.com, Sales
jonas.ferreira@example.com, Sales
kara.whitfield@example.com, Finance
liam.oduya@example.com, Sales
maya.petrov@example.com, Engineering
nolan.reyes@example.com, Engineering
olivia.sandoval@example.com, Human Resources
pavel.hartmann@example.com, Engineering
quinn.abara@example.com, Finance
rosa.lindqvist@example.com, Human Resources
samir.haddad@example.com, Sales
tessa.moreau@example.com, Sales
Do not change anything else: not the other Employee data (names, job titles, emails, IsActive), the EmployeeStructure structure, the ImportData screen, the actions UploadEmployeeExcel and DownloadEmployeeExcel, any other screen, any aggregate or filter, or any role. Do NOT publish the app in this turn.
```
- Publish turn text: `Publish the app EmployeeCatalogMW now. Publish note: add-department 1: Department static entity, Employee.DepartmentId, one-time department update in LoadSampleData.`

### Intervention 2: screens prompt and publish 2 (task 5 and 6), AC-07 and AC-08
- Mentor session f7e87282-b5af-e6bb-4393-9be764f3577f. Prompt run a5c0336c-ae32-151b-81a1-176a0f06459b (succeeded, about 1 minute, no retry). Publish run e164c94b-6a17-13e7-996b-c540742bb131 (succeeded, about 22 seconds).
- Publish 2: revision 8, 2026-11-22T02:45:05Z, publication key fd32cd29-4e06-a6f6-69f9-2418d2ce835d. publish_status Finished, outcome success. publish_logs: Info messages only. No conflict and no merge was reported.
- Wording: prompt 2 of design.md, word for word (file `Prompts/add-department-screens-prompt.md`).
- Mentor's run facts: attemptedChange true, changeApplied true, 0 validation errors, 16 warnings. Pending changes: Modified screens Employees and Employee_Details, nothing else.
- Exact prompt:
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
- Publish turn text: `Publish the EmployeeCatalogMW app now. Publish note: "add-department 2: Department column and filter on Employees, Department on Employee_Details." Do not change anything else in the app.`

### Timer Run now steps by the user
- No Run now was used in this change. The user said so after task 9, and tasks 3 and 6 recorded none.
- Timer reading by the user (ODC Portal, after task 9, reported by the user; Kiro did not see it): LoadSampleDataOnPublish shows Last run 22 Nov 2026 13:20:58 AEDT (02:20:58Z), about 30 seconds after publish 1 (revision 7, 02:20:28Z). So the department update ran by the timer on publish, not by a Run now. This is the user's reading of the Portal. It shows that the timer ran. It does not show by itself what the update changed. The Department values seen in the browser on revision 9 (17 rows plus 3 inactive employees opened by Id) are consistent with it.
- Open point: the Portal showed only that one Last run. The user did not say when the Portal was read. If it was read after publish 2 (revision 8, about 13:45 AEDT) and after I-1 (revision 10, about 14:20 AEDT), the timer did not run after those two publishes, although the design expected it to run on each publish. Kiro does not know the reading time and cannot read the timer. This does not affect the result: the update is safe to run again and the values were present, and neither later publish changed the update (revision 10 changed only Employee_Details, revision 8 changed only the two screens).
- The update is safe to run again.

### Follow-up prompt: I-1, Department field on Employee_Details (after task 8), AC-07 and AC-04 (layout)
- Reason: task 7 finding 1 and the browser check of task 8 (a layout defect on every employee checked): on Employee_Details the Department label and value sat between the "Job Title" label and its value, because the Department field Container was nested inside the Job Title field Container. Mentor had said it placed the field between Job Title and Is Active. The user decided on the fix and confirmed the exact text before it was sent.
- Mentor session 8bee7696-2c22-cbc8-e5be-d6f84475dacc. Prompt run ace55c12-b0ec-aec3-d8ea-9491ffb941ff (succeeded, about 1 minute, no retry). Publish run 7c62b380-4f40-e2aa-76b4-ebd861669364 (succeeded, about 21 seconds).
- Publish: revision 10, 2026-11-22T03:20:11Z, publication key 0a330d7b-8136-eb1e-f376-3832e5454d52. Publish note: "add-department I-1: Department field on Employee_Details moved out of the Job Title field." publish_status Finished, outcome success. publish_logs: Info messages only. env_app: revision 10 deployed in Development.
- Mentor's run facts: attemptedChange true, changeApplied true, 0 validation errors, 16 warnings. Pending changes: Modified screen Employee_Details and the module stamp. Mentor said the Department field Container was recreated, not moved, with the same label, value and styles.
- Exact prompt (file `Prompts/add-department-fix-department-field-prompt.md`):
```
In the EmployeeCatalogMW app, on the Employee_Details screen, fix the position of the Department field. Do not change anything else.

Today, in the Employment Details group (the Column2 placeholder of the Columns3 block, with the title text "Employment Details"), the Container of the Department field is nested inside the Container of the Job Title field. It sits between the Label with the text "Job Title" and the Expression that shows GetEmployeeById.List.Current.Employee.JobTitle. So on the screen the Department label and value appear between the Job Title label and the Job Title value.

Change it as follows:
1. Move the Container of the Department field (the Label with the text "Department" and the Expression that shows GetEmployeeById.List.Current.Department.Label) out of the Container of the Job Title field. It becomes a direct child of the Container that holds the three field Containers of the Employment Details group, as its own field.
2. In that group the order of the fields is: Job Title, Department, Is Active.
3. The Container of the Job Title field again holds only its Label with the text "Job Title" followed by its Expression for GetEmployeeById.List.Current.Employee.JobTitle.
4. Keep the Department Label text, the Department value expression and the styles of both as they are. The Is Active field, the Personal Information group, the Contact Information group and the title text of the group stay as they are.

Do not change anything else: not the Employees screen, GetEmployeeById, any other aggregate, action, structure, role, screen or sample data action. Do NOT publish the app in this turn.
```
- Publish turn text: `Publish the EmployeeCatalogMW app now. Publish note: "add-department I-1: Department field on Employee_Details moved out of the Job Title field." Do not change anything else in the app.`
- Result: fixed and verified in the browser for three employees (by hand, through the user, Claude in Chrome, three screenshots reviewed by the user, revision 10): EmployeeId 14 Alice Anderson (Job Title Software Engineer, Department Engineering, Is Active Yes), EmployeeId 21 Hugo Brandt (Finance Analyst, Finance, Is Active No), EmployeeId 25 Liam Oduya (Sales Representative, Sales, Is Active Yes). On all three, Department is its own field after Job Title and before Is Active. No editable fields and no Save or Delete buttons. Finding 1 is closed.
- Not re-checked on revision 10: the other 17 of the 20 employees on Employee_Details, the Employees screen (list, department column, dropdown, search), and the dropdown behaviour. The graph shows only Employee_Details changed in revision 10 and the Employees screen unchanged.

## Revision history

| Revision | When (UTC, 2026-11-22) | Made by | What |
|---|---|---|---|
| 7 | 02:20:28 | Kiro, MCP publish (publication key ebf70064-658c-e43c-51fb-44e4fe3e5894) | Publish 1, Intervention 1 |
| 8 | 02:45:05 | Kiro, MCP publish (publication key fd32cd29-4e06-a6f6-69f9-2418d2ce835d) | Publish 2, Intervention 2 |
| 9 | 02:48:33 | the user, ODC Studio | Unplanned. No functional change. Reason not stated |
| 10 | 03:20:11 | Kiro, MCP publish (publication key 0a330d7b-8136-eb1e-f376-3832e5454d52) | I-1, follow-up prompt |

Revisions 1 to 6 are in `Reports/EmployeeCatalogMW-verification-report.md`. Revision 7 followed revision 6 (2026-11-21T10:56:49Z) directly.

- Revision 9 versus revision 7 (graph comparison, `Reports/graphdiff/compare-rev7-rev9.txt`): stamps only on top of the content of publish 2. The nodes stamped after revision 8 are the module EmployeeCatalogMW and the entity Employee (02:48:26Z, both with LastModifiedByTool ODCStudio), and their other fields are unchanged. The other content nodes added or changed (Employees, Employee_Details, GetEmployees, GetEmployeeById) carry the Mentor session date 02:40:16, before revision 8. Regenerated validation messages: 11 nodes changed, the same 16 messages as in revision 7. Layout X/Y shifts: 0.
- A build comparison should count them as unplanned, with no functional change.
- No revision 8 graph exists, because context_graph returns only the latest revision. The graph check of task 7 therefore read revision 9 as revision 8 plus stamps. That is an inference, supported by the stamp dates above, not an observation of revision 8.
- Revision 9 was already the latest revision when the I-1 prompt was sent (app_revisions, read before sending). The comparison baseline for I-1 was revision 9, not revision 8.
- The revision user key in app_revisions is the same on revisions 5 to 10 (the user's key), so it does not tell a Studio publish from an MCP publish. The publication keys, the Mentor run events and the LastModifiedByTool stamps in the graph (ODCStudio or AgentExperience) do.

## Graph comparison findings
Scripts and outputs are in `Reports/graphdiff/`. Metadata stamps, regenerated validation messages and layout X/Y shifts are counted and named, not treated as findings (first build). Text literals inside aggregates and actions are hidden in the graph.

### Publish 1: revision 6 to revision 7 (`compare-rev6-rev7.txt`, task 4)
In scope, as found:
- Static entity Department: 61 nodes added. 4 records (hash-checked labels): Engineering Id 1, Finance Id 2, Human Resources Id 3 (record identifier "HumanResources"), Sales Id 4. Attributes Id, Label, Order, Is_Active only. Order 1 to 4, Is_Active True. Id has IsAutoNumber No. No state, transition or stateflow node type exists in revisions 6 or 10.
- Employee: one attribute added, DepartmentId (Department Identifier, Foreign Key to Department, not mandatory, Delete Rule Protect). The 7 other attributes are unchanged. The entity node itself carries new stamps.
- LoadSampleData: flow read with flow.py. Start, GetAliceRecord, If (GetAliceRecord empty and IsInDevStage()), DeleteAllEmployees (True) then GetEmployeeRecords, If (GetEmployeeRecords empty and IsInDevStage()), LoadSampleDataForEmployee (True), then both paths reach If IsInDevStage()? and, when True, SetEmployeeDepartments (Advanced SQL) then End. One End node (revision 6 had two). The SQL is readable: UPDATE Employee SET DepartmentId = CASE on LOWER(Email) in the 20 emails, WHERE DepartmentId is null or 0 and LOWER(Email) in the 20 emails. It matches by Email, sets only an empty DepartmentId, covers all 20 including the 3 inactive, and its four parameters are bound to the static records, not to numbers. The CASE mapping equals the assignment table (20 of 20). The existing checks and DeleteAllEmployees are kept.
- LoadSampleDataForEmployee: the CreateEmployee source gained a DepartmentId field (a nested If chain on the email, 20 of 20 emails matched by hash, final else NullIdentifier()). The six other field assignments were deleted and recreated (new keys, same sources): 281 nodes added, 38 removed.
- Module: stamps. Library elements added because of the new types: 9 nodes in the Integer Identifier library group and 1 for NullIdentifier (built-in function).

Outside the intended scope (reported, nothing fixed):
- UploadEmployeeExcel: its TypeConversion gained an 8th AttributeMapping with TargetValue Employee.DepartmentId and no SourceValue (4 nodes added). An Excel import therefore still creates employees without a Department. DownloadEmployeeExcel: stamps only. Both actions also carry new LastModifiedBy and tool stamps. The prompt said not to change them. Mentor listed both as Modified.
- Employees (GetEmployees) and Employee_Details (GetEmployeeById): stamps only in revision 7, no content change. Mentor listed both screens as Modified.
- MainFlow: stamp only.
- One layout shift (counted, not a finding): the End node X/Y in LoadSampleData.
- The unchanged items from the not-in-scope list in design.md: existing filters, roles, the timer (still WhenPublished), ImportData, EmployeeStructure and the Employee attributes other than DepartmentId, no node added, removed or changed beyond the items above.

### Publish 2: revision 7 to revision 8, read as revision 7 to revision 9 (`compare-rev7-rev9.txt`, task 7)
In scope, as found:
- Employees: new local variable SelectedDepartmentId; GetEmployees with Department as a second source, a left join ("Employee.DepartmentId = Department.Id (Employee with or without Department)") and a fourth filter condition; a new last column Department (header and row cell, not sortable); DepartmentDropdown in the Filters container, with an On Change event; the client action OnDepartmentChange (assignment StartIndex = 0, then a refresh of GetEmployees). 95 nodes added.
- Employee_Details: GetEmployeeById with the Department source and a left join, and the Department field (a Container with a Label "Department" and an Expression GetEmployeeById.List.Current.Department.Label). 31 nodes added.
- Accepted by the user after task 7, listed here as in scope with that acceptance as the reason:
  - Finding 2: the new aggregate GetDepartments (source Department, MaxRecords 50, sorted by Label ascending) that feeds the dropdown. The prompt did not name it.
  - Finding 3: one extra Container (3 columns) around DepartmentDropdown in Filters.
- Checked in task 7 and read again on revision 10 in this task: both joins are With or Without (left). The three existing GetEmployees filters (search, role check, IsActive = True) have the same structure as in revision 7. GetEmployeeById keeps its two filters. OnSearch, OnSort and OnPaginationNavigate: no node changed or removed between revision 7 and revision 10. The filter condition new in GetEmployees is `SelectedDepartmentId = <call> or Employee.DepartmentId = SelectedDepartmentId` (the call is NullIdentifier() according to Mentor; its name is not read in this task).
- Stamps and the like (counted): module, Employee entity, Employees, Employee_Details, GetEmployees, GetEmployeeById; 11 regenerated validation messages (the same 16 messages); 0 layout shifts. The two attributes of the join record "Department, Employee Record" are counted by the script under the module.

Finding outside the scope, at the time:
- Finding 1: on Employee_Details the Department field Container was nested inside the Job Title field Container (between the Job Title label and its value). It was a layout defect, confirmed in the browser in task 8, and fixed by I-1 (revision 10).

### I-1: revision 9 to revision 10 (`compare-rev9-rev10.txt`)
- Only Employee_Details changed. Node counts are equal (11,590 nodes, 21,471 edges). 22 nodes and 52 edges were removed (the old Department field Container and its subtree) and the same 22 nodes and 52 edges added under new keys, of the same types.
- The Department Container, its Label "Department", its Expression, the Visible value and the styles are identical before and after. In revision 10 the Employment Details group Container has four direct children in this order: the title Container, Job Title, Department, Is Active. The Job Title Container holds only its Label and its Expression. The Is Active Container, the group title and the rest of the screen are identical.
- Counted, not findings: the module stamp (LastModifiedByTool back from ODCStudio to AgentExperience), the screen stamp, 11 regenerated validation messages (the same 16 messages), 0 layout shifts.
- Net, revision 7 to revision 10 (scope.py): the module (2 attribute nodes), the Employee entity (stamp), Employees (2 stamps, 95 added), Employee_Details (2 stamps, 31 added), library nodes (15 added). No other container has a node added, removed or changed.

## Read-only checks (this task)
- Latest revision: app_revisions for EmployeeCatalogMW (2026-11-22T03:31Z) shows revision 10 (2026-11-22T03:20:11Z, model digest 4be3b537-95f1-5761-3d3e-997d80fc39b7) as the latest, then 9, 8 and 7 (2026-11-22T02:20:28Z, model digest 4ef9300f-41f9-c9e7-a19a-b66a2170f554), then 6. Total 10 revisions. No revision newer than the I-1 publish.
- No other app touched: every prompt of this change referenced only the app key 07a64c21-0c8c-8afb-28ee-5d8530d55cf8 (the prompt files). app_list (117 assets, read in full) shows no other asset with a revision dated after 2026-11-22T01:00:56Z. The closest, EmployeeCatalogMCP, has revision 9 at 2026-11-22T01:00:56Z, before the first publish of this change (02:20:28Z). This shows published revisions only. It does not show unpublished edits.
- SDD Base unchanged: `find` found no file in SDD Base newer than `.kiro/specs/add-department/tasks.md` (14:25:59 AEDT) or newer than the add-department `requirements.md` (12:47:02 AEDT), .DS_Store files included. This relies on file modification times and cannot show a deleted file. Nothing was written to SDD Base or to /tmp by this task.
- Tenant: read-only calls only (app_revisions, app_list, last_updated). No Mentor prompt and no publish was sent in this task.

## Disagreements between the app and the requirements
Nothing was changed. These stay report-only.
1. `employee-catalog/requirements.md` still says "Departments (no Department entity in this version)" under Out of scope, and its AC-01 and AC-04 do not name Department. The app has Department, as the add-department spec describes. Task 10 is to update that file, so this is expected until then.
2. Screen names are Employees and Employee_Details, not Employee_List and Employee_Detail (carried from the first build, item 1). The prompts used the app names.
3. The update that sets DepartmentId runs only under IsInDevStage() (the decision recorded in design.md, not in the requirements). In a stage where IsInDevStage() is false, no Department is set on the existing employees, and AC-07 would not hold there. The requirements do not name a stage.
4. The Department static entity has hand-set Ids 1 to 4 (IsAutoNumber No). The requirements say "default static entity attributes only", and the attributes Id, Label, Order and Is_Active are the defaults. The prompt did not ask for hand-set Ids, and Mentor reported it as a deviation.
5. DepartmentId has Delete Rule Protect. The requirements do not state a rule.
6. An Excel import (ImportData, UploadEmployeeExcel) now has a DepartmentId mapping with no source, so imported employees have no Department, and the export has no Department column. This is outside the requirements of this change. It adds to the carried-over items 2 and 3 (an extra ImportData screen that creates employees).
7. Items 3 to 10 of the first build report are carried over and were not re-read in this check: extra role Admin (the roles in revision 10 are still Admin and Staff), Staff Edit and Create rights, attribute lengths 200/200/200/256, the Picture attribute and image, the bootstrap that runs only in the development stage with its cleanup (the cleanup deletes all employees when Alice is missing), the unused Employee.json resource, and the landing screen not determined. The graph comparisons in this change show no change to them, except for the items in the findings above.

## Findings for the comparison with a second build
- Both direct prompts worked as written, with no fallback prompt. Mentor changed more than the prompt named in two places that the graph shows: the Excel import mapping and stamps on four elements (publish 1), and a new GetDepartments aggregate and an extra Container (publish 2).
- The one defect was the position of the Department field on Employee_Details. Mentor's summary said it was between Job Title and Is Active. The graph and the browser showed it inside the Job Title field. The summary was not reliable here. Only the graph and the browser were.
- The update route was the design's, not Mentor's, because the docs do not describe Mentor updating existing records. Mentor built it as an Advanced SQL update in the bootstrap, and the graph shows the CASE mapping equal to the table.
- A graph of each publish can be lost: context_graph serves only the latest revision, so a Studio publish between the planned publishes (revision 9) left no graph of revision 8. Reading the graph right after each publish, before any other publish, avoids it.
- The user published revision 9 from ODC Studio between the planned publishes, as in the first build (revisions 3 and 5). A build comparison should count them as unplanned, with no functional change.
