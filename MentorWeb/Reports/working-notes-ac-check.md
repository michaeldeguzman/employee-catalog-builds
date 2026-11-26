# Working notes: AC-01 to AC-06 check against EmployeeCatalogMW

Task 4 of spec employee-catalog. These notes feed tasks 5 and 6. They are working notes, not the verification report.

## Basis

- Evidence: `Reports/working-notes-inspection.md` (task 3, read-only, app revision 1). No new tenant calls were made in task 4.
- Compared against: `.kiro/specs/employee-catalog/requirements.md` (unchanged) and `BRD/EmployeeCatalogMW-BRD.md` (unchanged).
- The per-AC detail sections below describe revision 1 (before task 5.1). The section "Task 5.1 re-check (revision 2)" at the end has the current result for AC-02 and AC-05.
- All results are **static**: they come from the stored app model, not from running the app. Nothing was run in a browser. A run-time check is still needed before the final report claims a pass. Exception: AC-06 was later checked by the user (see its section). Its first result, a pass, was wrong and has been corrected to Fail.
- The BRD asks for every behaviour the requirements ask for (IsActive filter, name-only search, View-only Staff, 20 records with 3 inactive, only two screens, exact lengths). So each deviation below is a deviation by Mentor from the BRD, not a gap in the BRD.

## Summary

| AC | Result | Mentor produced it? | Fallback needed |
|---|---|---|---|
| AC-01 list loads | Pass (static) | Yes | No |
| AC-02 search | Revision 1: Fail. After task 5.1 (revision 2): Pass (static), with a limit (see "Task 5.1 re-check") | Search existed, matched too much. Fixed by the 5.1 Mentor prompt | Yes, task 5.1 (done) |
| AC-03 inactive hidden | Revision 1 to 5: Fail. Revision 6 (after task 5.2): Pass, verified by hand by the user (browser) | No (filter missing). The 5.2 Mentor prompt added it | Yes, task 5.2 (done) |
| AC-04 detail screen | Pass (static) | Yes | No |
| AC-05 empty search result | Revision 1 and 2: Fail. Revision 6 (after tasks 5.1 and 5.2): Pass, verified by hand for "Hugo", static for other text | Search existed, matched too much. 5.1 fixed the name matching, 5.2 the IsActive filter | Yes, tasks 5.1 and 5.2 (done) |
| AC-06 sample data present | Revision 1 to 3: Fail. Revision 4 (after task 5.3): Pass, verified by hand by the user (browser). See "Task 5.3 browser check" and its follow-up | Mentor produced sample data that did not match the BRD. The 5.3 Mentor prompt replaced it | Yes, task 5.3 (done) |

## Per-AC detail

### AC-01 (list loads): Pass (static)
- Evidence: screen `Employees` has a table with 4 sortable columns in the order FirstName, LastName, JobTitle, Email. Aggregate `GetEmployees` loads from Employee at start. The screen is limited to Staff and Admin.
- Caveats:
  - "One row per Active_Employee" is met only partly while AC-03 fails, because inactive employees are also in the list. That defect is recorded under AC-03, not here.
  - The table pages 10 rows at a time (MaxRecords 10), so 17 active employees take 2 pages. The AC does not mention paging. I treat that as acceptable, not as a failure.
  - Needs data to exist (see AC-06) and a run-time look.
- Source: Mentor produced it. Fallback: none.

### AC-02 (search): Fail
- Evidence: `GetEmployees` has a search filter bound to SearchKeyword and matches FirstName, LastName, **JobTitle and Email** with a "%" wildcard (the wildcard literal's hash equals "%"; the literal text is not readable). An empty SearchKeyword returns all rows.
- Why it fails:
  - The AC says the table shows only rows whose FirstName or LastName matches. The filter also matches JobTitle and Email, so a row can show for a reason other than the name.
  - No IsActive filter, so an inactive employee named Alice would also show (see AC-03).
- What works: a search input and a filter exist and "Alice" should find Alice Anderson. The failure is about precision, not about a missing feature.
- Source: Mentor produced a search (the docs flag said it might not). Fallback needed: yes (5.1).
- Note for 5.1: the app variable is `SearchKeyword`, not `SearchText`, and the screen is `Employees`, not `Employee_List`. The prompt in design.md uses both names. The user must decide how to word the prompt (see "Decisions for the user").

### AC-03 (inactive employees hidden): Fail
- Evidence: neither `GetEmployees` nor `GetEmployeeById` filters on Employee.IsActive. The only IsActive uses are in the entity, EmployeeStructure, the Excel download, the sample-data records and one display on Employee_Details. The list does not show an IsActive column.
- Source: Mentor did not produce it. Fallback needed: yes (5.2). Aggregate name for the prompt: `GetEmployees`.

### AC-04 (detail screen): Pass (static)
- Evidence: the FirstName cell on `Employees` links to screen `Employee_Details` with EmployeeId = row Id. `Employee_Details` loads `GetEmployeeById` and shows FirstName, LastName, JobTitle, Email and IsActive (plus Picture).
- Caveats: the link is on the FirstName cell, not the whole row. How IsActive is rendered (text, checkbox or icon) was not determined. The screen is named `Employee_Details`, not `Employee_Detail`.
- Source: Mentor produced it. Fallback: none.

### AC-05 (empty search result): Fail
- Evidence: same filter as AC-02. Search text that matches no FirstName or LastName but does match a JobTitle or Email (for example part of a job title) still returns rows, so the AC's "shows no rows" does not hold. Inactive rows are also not excluded.
- Source: Mentor produced the filter; it does not meet the AC. Fallback needed: yes (5.1, together with AC-02).

### AC-06 (sample data present): Fail (checked by the user through Mentor in ODC)
- Correction: this section first said Pass, verified by hand. That was wrong. The user reported that there is no employee named Alice in the data, and then relayed a check made by Mentor in ODC Studio. This section now has that result.
- Requirement (BRD): 20 fictional records, at least 2 with IsActive false, one active employee with FirstName Alice. The BRD names are: inactive Hugo Brandt, Maya Petrov, Quinn Abara; active Alice Anderson plus 16 others.
- Evidence (the user's relay of Mentor's answer in ODC, not a Kiro check). Mentor compared the **13 records in the app's sample-data file** with the BRD's 20:
  - Record count: BRD 20, app sample data 13 (7 short).
  - Inactive records: BRD 3 (Hugo Brandt, Maya Petrov, Quinn Abara). App 4 (Nina Patel, Owen Reed, Sophia Wells, Logan Price). This meets the minimum of 2, but the names differ.
  - Active Alice: BRD Alice Anderson. App: none. Missing.
  - Missing BRD names, all 20. Active (17): Alice Anderson, Bruno Castillo, Carla Dubois, Devon Marsh, Elena Novak, Felix Okafor, Grace Lindholm, Irene Takeda, Jonas Ferreira, Kara Whitfield, Liam Oduya, Nolan Reyes, Olivia Sandoval, Pavel Hartmann, Rosa Lindqvist, Samir Haddad, Tessa Moreau. Inactive (3): Hugo Brandt, Maya Petrov, Quinn Abara.
  - Extra names, all 13 in the app. Active (9): Evelyn Harper, Marcus Lindstrom, Lucas Morrison, Amelia Foster, Chloe Bennett, Ethan Griffin, Mason Cole, Isabella Hayes, Mia Turner. Inactive (4): Nina Patel, Owen Reed, Sophia Wells, Logan Price.
- Limit of the evidence: Mentor says it could not read the live Employee table. The 13 records are from the sample-data file, and the live table may differ. The user's own observation that there is no Alice in the data supports the result, but the live record count and the live inactive names are not independently confirmed. The user's first report (20 records, three named inactive, Alice active) is withdrawn and is not used as evidence.
- Static evidence from task 3 (unchanged): `LoadSampleData`, `LoadSampleDataForEmployee` and timer `LoadSampleDataOnPublish` exist. The sample-data JSON is a hidden text literal that the read-only tools can't read.
- Source: Mentor produced sample data, but not the BRD's data. Fallback needed: yes, task 5.3 (reopened, not started).
- Mentor also said the sample data loads only when the table is empty, so existing rows would need clearing first. This matters for the 5.3 prompt and the user must decide how to handle it.
- Other differences that Mentor reported in the same answer are already in the list below (screen names, ImportData and the Excel actions, Picture, attribute lengths). Mentor said it had not checked the Staff role. Kiro had checked it in task 3.

## Disagreements between the app and requirements.md
Nothing was changed. All are for the report.

1. Screen names: `Employees` and `Employee_Details` instead of `Employee_List` and `Employee_Detail`.
2. Extra screen `ImportData` (requirements: only two screens; out of scope: any other screen). It also provides upload and download of Employee Excel files, which writes data.
3. Extra role `Admin` (requirements: Staff is the only role).
4. Staff can read, edit and create Employee (`EmployeeCanEdit`, `EmployeeCanCreate`), not View only. The requirements and BRD say View only, no Edit.
5. Attribute lengths: FirstName and LastName 200 (50), JobTitle 200 (100), Email 256 (250). These are ODC defaults, so Mentor ignored the stated lengths.
6. Extra attribute `Picture` (Photos are out of scope) and a Picture image on `Employee_Details`.
7. Search matches JobTitle and Email as well (AC-02, AC-05).
8. No IsActive filter on the list (AC-03).
9. Which screen is the landing screen was not determined. The requirements say Employee_List.
10. The screen requires login (`AccessibleBy: False` in the stored model, not confirmed in ODC Studio).

Items 2, 3, 4, 5 and 6 are not covered by any AC. They break statements in the requirements (Glossary, Out of scope) but not an AC. They do not trigger a fallback in task 5, because task 5 covers only AC-02, AC-03, AC-05 and AC-06.

## Decisions for the user (before task 5)

- Task 5.1/5.2 prompts use "Employee_List" and "SearchText". The real names are `Employees` and `SearchKeyword`. The design says to replace only the aggregate words. Confirm whether to also replace the screen name, and whether the 5.1 prompt should say that the existing filter is changed to match only FirstName and LastName (otherwise Mentor may add a second filter next to the one that matches JobTitle and Email).
- Open: AC-06 failed (corrected result), so 5.3 is needed. The sample data loads only when the table is empty. Decide how the existing rows are handled before the 5.3 prompt is written.
- Items 2 to 6 in the disagreement list are outside the six ACs. Decide whether to have them reported only, or to cover them in a later change spec.
- Task 5 is in the order 5.1, 5.2, 5.3, each after the user confirms the tenant write and the publish. 5.1 and 5.2 both change `GetEmployees`, so the second prompt must wait until the first publish is finished.

---

## Task 5.1 re-check (revision 2)

Task 5.1 (fallback for AC-02 and AC-05, search). All checks are **static**, from the stored app model (context_graph, revision 2). The app was not run. No runtime pass is claimed.

### Intervention (for the report's "Interventions" section)

- ACs: AC-02 and AC-05.
- Kind: Mentor prompt through the OutSystems MCP (not a manual step in ODC Studio).
- Mentor session: 5f50fb46-a93b-5959-c66e-ca8f32b9cf7f. Edit run: c0c0da77-381f-99da-43c1-c2a8f67f15e1 (succeeded, changeApplied true, 0 validation errors, 2 warnings).
- Exact prompt (saved in `Prompts/5.1-fallback-search.md`):

```
In the Employees screen, change the existing search filter in the GetEmployees aggregate so SearchKeyword matches only FirstName or LastName. Remove the JobTitle and Email conditions. Do not add a second filter. Change nothing else.
```

- The prompt differs from the design.md wording. The user adapted it: real screen name (Employees), real aggregate (GetEmployees), real variable (SearchKeyword), and "change the existing filter, do not add a second one".
- Publish: after the user confirmed, one publish turn in the same session (run 6323c443-bfce-f7ac-c48b-bf3d776842e4). Revision 2, publication key 69dfbaf1-1325-ebd7-baae-7338bf50d767. publish_status: Finished, outcome success. env_app shows revision 2 deployed in Development. No retry.

### GetEmployees search filter in revision 2 (quoted from the model)

The model has exactly two filter conditions on the Employee source of GetEmployees.

Search filter (condition node KjuvQJDUwhZLwEXDT6ms2l), as read from the graph:

```
(SearchKeyword = "")
or (Employee.FirstName like ("%" + SearchKeyword + "%"))
or (Employee.LastName  like ("%" + SearchKeyword + "%"))
```

Revision 1 had two more `or` branches: `Employee.JobTitle like (...)` and `Employee.Email like (...)`. Both are gone in revision 2.

- Matches SearchKeyword against FirstName or LastName only: yes.
- Empty SearchKeyword returns all records: yes, through the `SearchKeyword = ""` branch (the empty-string literal has length 0 and hash da39a3ee5e, which is the SHA-1 prefix of the empty string).
- Only one search filter: yes. The other filter is the role check.
- Limit: the graph hides text literal values. The wildcard literals show only length 1 and hash 4345cb1fa2. I checked that this hash equals the SHA-1 prefix of "%", so they are "%", but the text itself is not shown.
- Not checked: the Like operator's case sensitivity at run time, and the screen's OnSearch action wiring (not traced in task 3 either).

### Role-based filter unchanged

Second filter (condition node KTCoXQwOhDaa8LHdTGx20E): `CheckStaffRole(UserId) or CheckStaffRole(UserId) or CheckAdminRole(UserId)`. All nodes and edges of this filter are identical in revision 1 and revision 2, and the structure matches the task 3 notes in `working-notes-inspection.md`. The graph shows the calls and their targets, not the argument expressions, so "(UserId)" is taken from the task 3 notes and not re-read. The doubled CheckStaffRole was already in revision 1.

### Comparison of revision 1 and revision 2

Method: I saved the full stored graph of revision 1 before the publish, fetched the full stored graph of revision 2 after it, and compared them node by node (11085 nodes before, 11067 after) and edge by edge (20215 before, 20173 after). Both graphs come from the same source (the stored model graph), so this is a like-for-like comparison.

Content changes (all inside one filter of one aggregate):
- GetEmployees aggregate, on screen Employees, search filter condition (KjuvQJDUwhZLwEXDT6ms2l): 18 expression nodes removed, 17 expression nodes changed (the tree was renumbered), 0 added. 72 edges removed and 30 added, all owned by this condition. Node types lost: 4 Identifier, 8 BinaryOperation, 4 Text, 2 CompoundIdentifier.

Metadata-only changes (no content change; modified-by stamps):
- GetEmployees aggregate (IScreenAggregate)
- Employees screen (IMobileScreen)
- MainFlow (IMobileFlow). Mentor's pending-changes list for the edit did not list MainFlow. Only the stamp changed.
- EmployeeCatalogMW module (IESpace)
- The stamps are the signed-in user as LastModifiedBy, LastModifiedDate 2026-11-21T10:12:04, tool AgentExperience and agent "node odc-mcp-remote". Not every element carries all of them: the module has no user and no date, and the aggregate has only user and date.

Nothing else differs in the whole graph (also covers roles, entities, structures, themes, actions, other screens, references and the role filter). No top-level graph field differs.

Result: nothing other than the Employees screen and the GetEmployees aggregate changed in content. The only extra change is the metadata stamp on MainFlow and on the module. I do not treat either as a problem, but I report them.

What the context_* lookups could and could not do:
- After the publish, I called context_screens, context_actions, context_entities, context_roles, context_structures, context_themes and context_connections for the app. They returned the same rows as before the publish (7 screens, 17 actions, 1 entity with 7 attributes, 2 roles, 1 structure, 2 themes, 0 AI connections), with the same index timestamp 2026-11-21T09:52:06Z. That timestamp is earlier than the publish (10:15Z), so these lookups had not been reindexed for revision 2 when I read them. I cannot use them as evidence about revision 2. They also do not carry filter expressions.
- context_graph did serve revision 2 (header: revision 2, latest_revision 2), so the comparison above rests on it.
- app_revisions lists revisions 1 and 2. app_info shows revision 2, modelDigest be460d49-f659-809a-6270-471b16d72e17 (revision 1: f7ae6599-4b8e-1aeb-c177-ad6f41532660).
- Not compared: the Employee data (the read tools have no data query). The data was not edited, but it was not re-read after the publish. Not compared: runtime behaviour.

### Validation warnings (2)

Not visible. The edit run reported warningCount 2 and an empty firstMessages list. The publish turn's result has no validation block. publish_logs and deploy_messages for the publication key hold 8 messages, all severity Info, with no warning or error. publish_status carries no messages. The release and debug builds finished, and the security audit lists no vulnerabilities. So the two warnings are in Mentor's validation of the session model, and their text is not exposed through the MCP. They can be read in ODC Studio.

### AC-02 (search): Pass (static), with a limit

- Requirement: when the user enters "Alice", the table shows only Active_Employee rows whose FirstName or LastName matches "Alice".
- Evidence: the search filter matches FirstName or LastName only (quoted above). With the BRD sample data (hand-checked by the user for AC-06), only Alice Anderson contains "Alice", and she is active. The three inactive employees (Hugo Brandt, Maya Petrov, Quinn Abara) do not contain "Alice".
- Correction (AC-06): the sentence above that uses the BRD sample data is withdrawn. The app has no Alice Anderson, so the "Alice" example does not apply to the current data. The model-based result still stands: the filter matches FirstName or LastName only.
- Limit: the "only Active_Employee" part is not enforced by the model, because GetEmployees has no IsActive filter (AC-03 still fails). The result holds for this sample data. It would not hold for an inactive employee named Alice.
- Verified: statically, from the model. Not run in the app. Whether Like is case-insensitive at run time is not checked.

### AC-05 (empty search result): Fail (static)

- Requirement: search text that matches no Active_Employee FirstName or LastName shows no rows.
- Evidence: the name-only matching is fixed (a job title or an email no longer returns rows). But there is still no IsActive filter, so text that matches only an inactive employee's name still returns that row. Example: with the BRD data, "Hugo" matches no active employee but returns Hugo Brandt (IsActive false). Correction (AC-06): the app has no Hugo Brandt. The app's inactive names are Nina Patel, Owen Reed, Sophia Wells and Logan Price (from Mentor's check of the sample-data file), so the same example with, say, "Nina" applies. The AC says no rows.
- Same cause as AC-03. The IsActive filter (task 5.2) is what closes it. After task 5.2, AC-05 needs a re-check.
- Verified: statically, from the model. Not run in the app.

### Finding

Before publishing, the unpublished Mentor change could not be verified from the app model, only from Mentor's summary and the pending-changes list. context_graph and the context_* lookups read the published revision (revision 1 at that point), so the edit in the session was invisible to them. The check of the filter became possible only after the publish, which means the publish had to happen before the change could be verified, not after.

Second finding: the context_* lookups were not reindexed after the publish (same 09:52:06Z timestamp). Only context_graph reflected revision 2.

---

## Task 5.2 (not started)

Superseded. This was true after revision 2. Task 5.2 was done later: see "Task 5.2 (fallback for AC-03, inactive hidden), published as revision 6" at the end.

## Task 5.3

Superseded. The earlier line "Not needed: AC-06 passed, verified by hand." was withdrawn, and 5.3 was reopened. It was done later: see "Task 5.3 (fallback for AC-06, sample data), published as revision 4".

---

## Deviations from the BRD (running list for the final report)

Found so far, from revision 1 and the revision 2 comparison. Nothing was fixed except item 8, which was fixed by the task 5.1 intervention. "Requirement" is the part of requirements.md that the deviation breaks. The BRD states the same thing in each case.

1. Screen names are Employees and Employee_Details, not Employee_List and Employee_Detail. Breaks: Glossary (Employee_List, Employee_Detail), and the names used in AC-01 to AC-05. Open.
2. Extra screen ImportData (Excel upload and download for Employee). Breaks: Out of scope, "Any screen other than Employee_List and Employee_Detail". BRD: "exactly two screens". Open.
3. ImportData and its actions (UploadEmployeeExcel) create Employee records. Breaks: Out of scope, "Creating, editing or deleting employees"; Introduction, "read-only". Open.
4. Extra role Admin, on all three MainFlow screens and in the permission actions. Breaks: Glossary, "Staff: The only role". Open.
5. Staff can read, edit and create Employee (EmployeeCanEdit, EmployeeCanCreate), not View only. Breaks: Glossary, "Staff ... has View access to Employee"; Out of scope, "Creating, editing or deleting employees". BRD: "No role has Edit access to any entity." Open.
6. Attribute lengths: FirstName 200 (50), LastName 200 (50), JobTitle 200 (100), Email 256 (250). Breaks: Glossary, Employee attributes. Open.
7. Extra attribute Picture (and a Picture image on Employee_Details). Breaks: Out of scope, "Photos"; Glossary, Employee attribute list. Open.
8. Search also matched JobTitle and Email. Breaks: AC-02, AC-05, Requirement 2. Fixed in revision 2 by the task 5.1 intervention.
9. No IsActive filter on GetEmployees (and none on GetEmployeeById). Breaks: AC-03 (Requirement 3). Also leaves AC-05 failing, and the "Active_Employee" part of AC-01 and AC-02 unenforced. Fixed in revision 6 by the task 5.2 intervention (hand-verified by the user).
10. The list pages at 10 rows (MaxRecords 10), so 17 active employees take 2 pages. AC-01 says one row per Active_Employee and does not mention paging. I did not treat this as a failure. Listed for completeness.

Not determined (not deviations yet): which screen is the landing screen (BRD: Employee_List); whether the screens need login in ODC Studio (the model says AccessibleBy False; AC-01 assumes a signed-in Staff user, so this is consistent).

11. Sample data does not match the BRD (added after the AC-06 correction). The app's sample-data file has 13 records, not 20. Its inactive records are Nina Patel, Owen Reed, Sophia Wells and Logan Price, not Hugo Brandt, Maya Petrov and Quinn Abara. There is no active Alice Anderson. Breaks: AC-06 (Requirement 6). Open (task 5.3, reopened, not started). Source: Mentor's check in ODC, relayed by the user, of the sample-data file only. Resolved in revision 4 by the task 5.3 intervention (hand-verified by the user).

Revision 2 added no new deviation.

---

## Finding: first AC-06 result

The first AC-06 result (Pass, verified by hand) was recorded without checking each named record against the data. The user's evidence named Alice Anderson, Hugo Brandt, Maya Petrov and Quinn Abara, and none of them is in the app's sample data. Kiro recorded that evidence as given and did not ask for a record-by-record check. The AC-06 Pass was withdrawn after the user corrected it. Task 5.3 was marked completed ("Not needed") and has been reopened. Two statements written in the 5.1 re-check relied on that wrong evidence (the Alice example in AC-02 and the Hugo example in AC-05). They now carry correction notes.

## Task 5.3 (fallback for AC-06, sample data), published as revision 4
All checks below are **static**, from the stored app model (context_graph, revision 4). The app was not run and the Employee table was not read. No runtime pass is claimed in this section. The user's browser check of the live table followed and is recorded below (AC-06: Pass).

### Intervention (for the report's "Interventions" section)
- AC: AC-06.
- Kind: Mentor prompt through the OutSystems MCP (not a manual step in ODC Studio).
- Mentor session: a6e89e56-6e78-6c13-b75e-e4009cfc25e9. Edit run: 37affd32-77a0-35bd-4fd8-1ce37cae608d (succeeded, changeApplied true, 0 validation errors, 16 warnings).
- Exact prompt: saved in `Prompts/5.3-fallback-sample-data.md` (all 20 BRD records, a one-time cleanup keyed on alice.anderson@example.com, and "Change nothing else.").
- The prompt differs from the design.md wording. The user adapted it: real action and timer names, all 20 records quoted, and the one-time cleanup that deletes the existing records.
- Mentor's offers to remove the development-stage condition on the cleanup and to delete the unused Employee.json resource were declined. No follow-up prompt was sent. Other deviations stay report-only.
- Publish: after the user confirmed, and after Kiro told the user that the publish deletes the 13 existing records, one publish turn in the same session (run c161932e-1026-c3d5-81a0-2bb1d3788938). Revision 4, publication key d079e233-cd8d-0718-3e3d-04fd8e2d1a2d. publish_status: Finished, outcome success. env_app shows revision 4 deployed in Development. No retry.

### Revision 3: unplanned publish from ODC Studio, no functional change
- Found before the 5.3 publish. Revision 3 was published at 2026-11-21T10:22:39Z by the user's own account (revisionUserKey a513133f-6c77-359f-302f-ce0c241608a7, not "ide-service"), through ODC Studio (changed nodes carry the tool "ODCStudio"). Kiro did not make it and no task asked for it. Source and reason: not stated.
- Comparison of revision 2 and revision 3 (full stored graphs, node by node and edge by edge): 11067 nodes and 20173 edges before, 11077 nodes and 20194 edges after.
  - No change to any action, screen, aggregate, filter, role, entity attribute, structure or theme.
  - Differences: stored validation messages regenerated (13 added, 1 changed; the ones read are "Non Existing Icon" warnings and a hidden security warning); modified-by stamps on the module, the Employee entity (stamp only, attributes identical), the Employees screen, MainFlow and three references; stamps on 43 library images and 2 library flows; the OutSystemsMaps reference no longer lists its ShapeType entity (3 nodes, 8 edges).
  - Result: no functional change. It matters for the comparisons because the baseline for 5.3 is revision 3, not revision 2.

### Check 1: LoadSampleData flow in revision 4
Control flow, from the graph connectors:
- Start, then GetAliceRecord (Employee source, filter `Employee.Email = <text>`, max 1 record).
- If `GetAliceRecord.List.Empty and IsInDevStage()`:
  - True: DeleteAllEmployees (the Employee entity action DeleteAllEmployees), then GetEmployeeRecords.
  - False: GetEmployeeRecords.
- GetEmployeeRecords (reads Employee again, max 1 record), then If `GetEmployeeRecords.List.Empty and IsInDevStage()`: True runs LoadSampleDataForEmployee, then End. False goes to End.
Findings:
- The empty-table check runs after the delete and reads the table again: yes. The delete node connects to GetEmployeeRecords, and GetEmployeeRecords is the aggregate that the empty check uses. There is one GetEmployeeRecords node, so both branches read after the delete or after the Alice check.
- The Alice filter's text literal has length 26 and hash f3d93a85c7. I checked that the hash equals the SHA-1 prefix of "alice.anderson@example.com" (26 characters). The literal text itself is not shown by the graph.
- The delete is guarded by IsInDevStage(), as in the load check.
- Timer LoadSampleDataOnPublish: its Action edge points to server action LoadSampleData, and it has the timer action WakeLoadSampleDataOnPublish. Yes, it calls LoadSampleData.
- Not read: the timer's Schedule and whether it fires on its own after a publish (the graph shows property names only). Mentor said it runs on publish. This is not confirmed.
- Not read: the content of the sample-data JSON. In revision 3 the JSON argument of JSONDeserializeEmployeeList was a Call (the Employee.json resource). In revision 4 it is a text literal of length 2466, hash 2e83c0b72a. The records, the count and the IsActive values can't be read from the graph.

### Comparison of revision 3 and revision 4
Method: the full stored graph of revision 3 (fetched before the publish) against the full stored graph of revision 4 (fetched after it), node by node and edge by edge: 11077 nodes and 20194 edges before, 11096 nodes and 20235 edges after. Every difference was assigned to its containing element.
Content changes, all inside the two named actions:
- LoadSampleData: 21 nodes added (the GetAliceRecord aggregate with its source and filter, the If node, the DeleteAllEmployees call, and their expressions), 7 nodes with only a layout position (X, Y) shifted, 1 node with changed stamps (the action itself).
- LoadSampleDataForEmployee: the JSON argument of JSONDeserializeEmployeeList changed from a Call to the text literal (1 node changed, 3 removed: an Argument, a CompoundIdentifier and an Identifier), plus the stamps on the action.
Outside the two actions:
- Module EmployeeCatalogMW: modified-by stamps only (last modified by tool ODCStudio, now AgentExperience, agent "node odc-mcp-remote").
- Stored validation messages: 4 changed and 1 added. They now include "Resource 'Employee.json' is never used" (UnusedResource) and the "caret-left", "caret-right", "cloud-arrow-down" and "cloud-arrow-up" icon warnings. These are validation text, not model logic. The count went from 15 to 16, which matches the 16 warnings in the edit run.
- Nothing else differs. The Employee entity and all its attributes are identical in revisions 3 and 4 (lengths and the Picture attribute unchanged). Screens (including ImportData), roles, filters (including the GetEmployees search filter and the role filter), structures, themes, the timer, the other actions and all references are unchanged.
Result: nothing outside LoadSampleData and LoadSampleDataForEmployee changed in content. The only extra changes are the module stamps and the stored validation messages.
- Not compared: the Employee data (the read tools have no data query), the timer's run time behaviour, and the text of the validation warnings beyond the ones listed above.

### Not yet known (user's browser check)
- Whether the 13 old records were deleted and the 20 BRD records loaded. The user will report the count and names.
- AC-06 was undecided until the user's browser check. Result: Pass on revision 4 (see "Task 5.3 browser check" below).
- If the data did not reload, Kiro sends no fix and reports it (user's instruction).

## Task 5.3 browser check (revision 4, done by the user by hand)
Evidence as the user reported it, not a Kiro check:
- Total Employee rows: 20.
- Alice Anderson: present. Her IsActive value was not reported.
- Hugo Brandt: present. IsActive on the detail screen: false.
- Maya Petrov: present. IsActive not reported.
- Quinn Abara: present. IsActive not reported.
- Old records (Nina Patel, Owen Reed, Sophia Wells, Logan Price and the other 9 old names): the user was not sure what the "old record" was, so nothing was checked by name.
AC-06 criteria against this evidence:
- 20 Employee records: met (20 rows).
- One active employee with first name Alice: Alice Anderson is present, but her IsActive was not reported. Open.
- At least 2 records with IsActive false: only Hugo Brandt is confirmed false. Maya Petrov and Quinn Abara were not checked for IsActive. Open.
- Fictional: the 4 names checked are BRD names, and the sample data was written from the BRD list. The other 16 rows were not read by name.
Inference, not a check: before 5.3 the table held 13 rows with none of the BRD names. A count of 20 with Alice, Hugo, Maya and Quinn present is what a full reload gives (the cleanup deletes all or nothing, and the load inserts the whole list). If the 13 old rows had stayed, the count would be 33. The old names were not read directly.
Decision: AC-06 is not recorded as Pass yet. The first AC-06 Pass was withdrawn because named records were not checked one by one (see "Finding: first AC-06 result"). Two checks are needed to close it: Alice Anderson's IsActive on her detail screen (expect true), and the IsActive of Maya Petrov or Quinn Abara (expect false). Task 5.3 is not ticked until then.

### Follow-up: detail screen checks on revision 4 (by the user, by hand)
- Alice Anderson: IsActive true.
- Maya Petrov: IsActive false.
- Quinn Abara: IsActive false.
- With the earlier check, Hugo Brandt is also false. All three inactive BRD names are confirmed false by hand.
### AC-06 result: Pass (verified by hand, revision 4)
- 20 Employee records: yes (20 rows, reported by the user).
- At least 2 with IsActive false: yes, 3 confirmed (Hugo Brandt, Maya Petrov, Quinn Abara).
- One active employee with first name Alice: yes (Alice Anderson, IsActive true).
- Fictional: the names checked are BRD names, and the data was written from the BRD list with example.com emails.
- Source: Mentor produced sample data (not the BRD data), and the task 5.3 fallback prompt fixed it. Fallback needed: yes.
- Limits: the user read 4 of the 20 names (Alice, Hugo, Maya, Quinn) and the count. The other 16 names, jobs and emails were not read, and the user did not look for the 13 old names. The count of 20 rules out the old rows staying. The evidence comes from the user's browser check, not from a Kiro check or from the model. Kiro's own checks of revision 4 are static and show the flow only (see "Check 1").
- Consequence for earlier text: the AC-02 and AC-05 examples that were withdrawn after the AC-06 correction (the "Alice" and "Hugo" examples) now apply again to revision 4 data, but they were not re-checked here.

## Revision 5: second unplanned publish from ODC Studio, no functional change
- Found while checking the 5.2 Mentor edit, before any 5.2 publish. Revision 5 was published at 2026-11-21T10:47:43Z by the user's own account (revisionUserKey a513133f-6c77-359f-302f-ce0c241608a7), through ODC Studio. It was made five minutes after Kiro's revision 4 publish. Kiro did not make it and no task asked for it. Source and reason: not stated.
- Comparison of revision 4 and revision 5 (full stored graphs, node by node and edge by edge): 11096 nodes and 20235 edges in both.
  - LoadSampleData: the GetAliceRecord aggregate's source and filter were re-saved with new internal keys (8 nodes removed, 8 added, same types). The text literal is unchanged (length 26, hash f3d93a85c7). The control flow is identical, edge by edge.
  - Stamps: module and the two sample-data actions (modified-by agent and tool), and the Employee entity LastModifiedDate (10:26:38). All 7 Employee attribute nodes are identical.
  - Stored validation messages reordered (11 changed, same texts).
  - GetEmployees, the Employees screen, roles, other actions and references: identical.
- Result: no functional change. Logged as an unplanned publish. The baseline for the task 5.2 comparison is revision 5.
- Not compared: the Employee data (the read tools have no data query).

## Task 5.2 (fallback for AC-03, inactive hidden), published as revision 6
All checks below are **static**, from the stored app model (context_graph, revision 6). The app was not run and the Employee table was not read. No runtime pass is claimed. The browser check is with the user.

### Intervention (for the report's "Interventions" section)
- AC: AC-03. Consequence for AC-05: its earlier failure came from the missing IsActive filter, which is now in the model. AC-05 is not re-evaluated here.
- Kind: Mentor prompt through the OutSystems MCP (not a manual step in ODC Studio).
- Mentor session: dc137568-65af-56c9-b4a1-9f81626e45e5. Edit run: d37fef1f-cac5-0433-417c-49aa622e00c1 (succeeded, changeApplied true, 0 validation errors, 16 warnings).
- Exact prompt (saved in `Prompts/5.2-fallback-isactive-filter.md`):
```
In the Employees screen, add a new, separate filter condition to the existing GetEmployees aggregate so that it returns only the Employee records whose IsActive is True. Keep the existing search filter and the existing role-check filter exactly as they are. Do not change the Employees table columns or any other screen. Change nothing else.
```
- The prompt differs from the design.md wording. The user adapted it: real screen (Employees) and aggregate (GetEmployees), the filter as a separate condition, and "Change nothing else.".
- Publish: after the user confirmed, one publish turn in the same session (run f1b1ff2c-d714-6f5c-6234-11101b17393a). Revision 6, publication key 54d13cb0-0fb9-3a77-32df-59ccb42cb1fd. publish_status: Finished, outcome success. env_app shows revision 6 deployed in Development. No retry.

### GetEmployees filters in revision 6 (read from the graph)
The aggregate has three filter conditions on the Employee source (revision 5 had two):
- Index 0, search filter (KjuvQJDUwhZLwEXDT6ms2l): unchanged. `SearchKeyword = "" or Employee.FirstName like ... or Employee.LastName like ...`.
- Index 1, role filter (KTCoXQwOhDaa8LHdTGx20E): unchanged. `CheckStaffRole(...) or CheckStaffRole(...) or CheckAdminRole(...)`.
- Index 2, new (GC1hy5gbVKCxnlkQDv7J9S): `Employee.IsActive = True` (a Boolean literal True, not text).
- Filter conditions of one aggregate are combined with AND in ODC (platform behaviour, not shown by the graph). The search and role conditions are the same nodes as in revision 5.
- Not checked: that the Employees table runs the aggregate with the filters applied at run time, and the table paging. GetEmployeeById is unchanged (no IsActive filter), so the detail screen still opens an inactive employee by Id.

### Comparison of revision 5 and revision 6
Method: the full stored graph of revision 5 (fetched before the publish, as the baseline) against the full stored graph of revision 6 (fetched after it), node by node and edge by edge: 11096 nodes and 20235 edges before, 11101 nodes and 20247 edges after. Every difference was assigned to its containing element.
Content change, all inside GetEmployees on Employees: 5 nodes added (the condition expression: Eq, Employee.IsActive compound identifier, its identifier, the Boolean True) and 12 edges added. Nothing removed.
Outside the new filter, metadata only:
- Employees screen and the GetEmployees aggregate: new LastModifiedDate stamp (2026-11-21T10:54:32) and modified-by agent.
- MainFlow: modified-by stamps only (Mentor's pending-changes list did not list it, as in task 5.1).
- Module EmployeeCatalogMW: modified-by stamps only (last tool AgentExperience).
- Stored validation messages: 11 changed, count unchanged at 16 (same texts, order changed). Revision 5 and 6 both have 16.
Nothing else differs: LoadSampleData and LoadSampleDataForEmployee, the Employee entity and its attributes, ImportData and the other screens, roles, structures, themes, the timer and all references are identical in revisions 5 and 6.
Result: nothing outside GetEmployees on Employees changed in content. The only extra changes are the stamps on MainFlow and the module and the stored validation messages.
- Not compared: the Employee data (the read tools have no data query), and run time behaviour.

### Not yet known (user's browser check)
- Whether the list hides Hugo Brandt, Maya Petrov and Quinn Abara at run time, and whether search still finds Alice and returns no rows for "Hugo".
- Whether the table still holds the 20 records (the list now shows only active rows, so the total of 20 can't be read from the list).
- AC-03 stays "static Pass, not hand-verified" and task 5.2 is not ticked until then.

## Task 5.2 browser check (revision 6, done by the user by hand)
Evidence as the user reported it, not a Kiro check:
- List rows across all pages: 17. Hugo Brandt, Maya Petrov and Quinn Abara in the list: none.
- Search "Hugo": no rows.
- Search "Alice": Alice Anderson shown. The user did not say whether other rows were also shown.
- Hugo's detail page, opened through its earlier URL: shows Hugo, IsActive false.

### AC-03 result: Pass (verified by hand, revision 6)
- Requirement: no row is shown for any Employee with IsActive false.
- Evidence: 17 rows across all pages, which equals the 17 active BRD records, and none of the three inactive names is in the list. Hugo's record still exists (detail page), so the rows are hidden, not deleted.
- Model evidence (static): `GetEmployees` has the filter `Employee.IsActive = True` (revision 6).
- Source: Mentor did not produce it. Fallback needed: yes (task 5.2).
- Limit: the list was read by the user as a count and by the three names. The names of the other 17 rows were not reported.

### AC-05 result: Pass (verified by hand for "Hugo", static for other text)
- Requirement: search text that matches no Active_Employee FirstName or LastName shows no rows.
- Evidence by hand: "Hugo" matches only an inactive employee's name. It returned no rows. This is the case that failed in revisions 1 and 2.
- Model evidence (static): the search filter matches FirstName or LastName only (task 5.1), and the IsActive filter is a separate condition (task 5.2).
- Source: Mentor produced the filter, but it matched too much. Fallback needed: yes (tasks 5.1 and 5.2).
- Limits: not tried by hand, text that matches only a job title or an email, and text that matches nothing at all.

### Effect on AC-01, AC-02 and AC-04 (hand evidence added, status unchanged)
- AC-01: 17 rows across all pages matches the 17 active records (hand). The four columns were not reported by hand.
- AC-02: "Alice" shows Alice Anderson (hand). Whether other rows appeared was not reported.
- AC-04: Hugo's detail page shows Hugo and IsActive false (hand). It was opened through a URL, not through a row link, and the other attributes were not reported.

## Task 7 scope check (not ticked: two points need the user)
1. Nothing outside EmployeeCatalogMW was touched: no finding against it. Every tenant call in this session used the app key 07a64c21-0c8c-8afb-28ee-5d8530d55cf8 (app_info, app_revisions, context_graph, env_app, publish status and logs, and the three Mentor sessions, whose asset facts list only this app). The task 3 notes say the app search used the name "EmployeeCatalogMW" only. Limit: Kiro has no call that lists all tenant writes, so this rests on the calls Kiro made.
2. No file written outside MentorWeb/: NOT met. Kiro wrote scratch files in /tmp/graphdiff for the graph comparisons: rev2.txt to rev6.txt (the full stored graphs, about 3 MB each) and the scripts diff.py, flow.py and scope.py. The prompt file 5.3 and these notes mention that folder. Open: the user decides whether to delete them, or keep them. Kiro's own tool-output copies under ~/.kiro/sessions are managed by Kiro. The folders "Development/" and ".history/" in the Employee Catalog root hold the user's prompt files and exported session zips, not files from these tasks (as far as this session can tell).
3. SDD Base unchanged: cannot be proven. SDD Base is not a git repository, so there is no diff. Three files there have a modified time on 2026-11-21 before the spec and BRD work: .kiro/steering/workspace-layout.md (17:43:35), .kiro/steering/mentor-standards.md and .kiro/steering/outsystems-ui.md (both 17:56:45). The spec was created at 18:03 and the BRD at 18:23. This session wrote nothing there. Earlier sessions: the write calls Kiro could find in their logs were all inside MentorWeb/, but that search is not conclusive. Open: the user confirms whether those three edits were theirs (project setup).
