# Verification report: EmployeeCatalogMW against the employee-catalog requirements

Task 6 of spec employee-catalog (Build 1: Mentor Web).

## Basis
- App: EmployeeCatalogMW, asset key 07a64c21-0c8c-8afb-28ee-5d8530d55cf8, ODC Development environment (env key 8b036dbd-6d28-2b5c-c50a-77a6bc07d748). No other app was touched.
- Final revision checked: revision 6. URL: https://your-tenant-dev.outsystems.app/EmployeeCatalogMW
- Checked against: `.kiro/specs/employee-catalog/requirements.md` (AC-01 to AC-06) and `BRD/EmployeeCatalogMW-BRD.md`. Neither file was changed.
- Docs sync date (task 1): outsystems-docs MCP, source "odc", last_updated 2026-10-28T09:05:12Z (sync date 2026-10-28).
- Source notes: `Reports/working-notes-inspection.md` (task 3, revision 1), `Reports/working-notes-ac-check.md` (tasks 4 and 5, with the revision comparisons), and the three prompt files in `Prompts/`.

## How to read the evidence
- **Hand**: the user checked it in the browser on the stated revision. Kiro did not see the data and relies on what the user reported.
- **Static**: Kiro read the stored app model (context_graph). The app was not run. The read tools have no data query, and the graph hides text literals (it shows only their length and a hash).
- A pass below says which of the two supports it, and what was not checked.

## Result per AC

| AC | Result | Evidence | Mentor produced it? | Fallback |
|---|---|---|---|---|
| AC-01 list loads | Pass | Static: table with FirstName, LastName, JobTitle, Email, loaded by GetEmployees. Hand (revision 6): 17 rows across all pages, equal to the 17 active records | Yes | None |
| AC-02 search | Pass | Static (revision 2 to 6): the filter matches FirstName or LastName only, and an empty search returns all rows. Hand (revision 6): "Alice" shows Alice Anderson | Search existed but matched too much (JobTitle and Email too). Fixed by a fallback | Task 5.1 |
| AC-03 inactive hidden | Pass | Hand (revision 6): 17 rows, none of Hugo Brandt, Maya Petrov or Quinn Abara. Static: filter Employee.IsActive = True on GetEmployees | No (no filter was generated) | Task 5.2 |
| AC-04 detail screen | Pass | Static: the FirstName cell links to Employee_Details with the Id, and the screen shows FirstName, LastName, JobTitle, Email and IsActive. Hand (revision 6): Hugo's detail page shows Hugo and IsActive false | Yes | None |
| AC-05 empty search result | Pass | Hand (revision 6): "Hugo" (matches only an inactive name) returns no rows. Static: name-only search plus the IsActive filter | The filter existed but matched too much | Tasks 5.1 and 5.2 |
| AC-06 sample data present | Pass | Hand (revision 4): 20 rows; Alice Anderson active; Hugo Brandt, Maya Petrov and Quinn Abara inactive | Mentor produced sample data, but 13 records with other names | Task 5.3 |

Summary: 6 of 6 ACs pass. 2 (AC-01, AC-04) were produced by Mentor as generated. 4 (AC-02, AC-03, AC-05, AC-06) needed a fallback Mentor prompt. No fallback needed manual work in ODC Studio.

### What was not checked, per AC
- AC-01: the four columns and their order by hand. The 10-rows-per-page paging is not mentioned in the AC and is not treated as a failure.
- AC-02: whether rows other than Alice Anderson were shown for "Alice" (not reported). Case sensitivity of the Like operator.
- AC-03: the names of the other 17 rows (only the count and the three inactive names were checked).
- AC-04: opening a detail page through a row link (the user used a URL). The other attributes on Employee_Details (not reported).
- AC-05: text that matches only a job title or an email, and text that matches nothing. Both are covered by the model, not by hand.
- AC-06: only 4 of the 20 names were read by name (Alice, Hugo, Maya, Quinn) plus the count of 20. The other 16 names, jobs and emails were not read, and the user did not look for the 13 old names. The count of 20 rules out the old rows staying. After task 5.2 the list shows only active rows, so the total of 20 was not re-counted on revision 6. Hugo's record still exists there.

## Interventions
Every fallback used was a Mentor prompt sent through the OutSystems MCP, one single prompt per task, in its own Mentor session, after the user confirmed the tenant write and again the publish. There was no manual fallback in ODC Studio. Each prompt is saved as a file in `Prompts/`.

### Intervention 1: task 5.1, AC-02 and AC-05 (search), published as revision 2
- Mentor session 5f50fb46-a93b-5959-c66e-ca8f32b9cf7f. Edit run c0c0da77-381f-99da-43c1-c2a8f67f15e1. Publish run 6323c443-bfce-f7ac-c48b-bf3d776842e4, publication key 69dfbaf1-1325-ebd7-baae-7338bf50d767.
- What was done: the existing search filter in GetEmployees was changed to match only FirstName or LastName.
- Differs from design.md: it uses the real screen, aggregate and variable names, and says to change the existing filter, not add a second one.
- Exact prompt (file `Prompts/5.1-fallback-search.md`):
```
In the Employees screen, change the existing search filter in the GetEmployees aggregate so SearchKeyword matches only FirstName or LastName. Remove the JobTitle and Email conditions. Do not add a second filter. Change nothing else.
```
- Verification: graph comparison of revision 1 and 2. Content changed only in the search filter of GetEmployees. Metadata stamps also changed on MainFlow and the module.

### Intervention 2: task 5.3, AC-06 (sample data), published as revision 4
- Mentor session a6e89e56-6e78-6c13-b75e-e4009cfc25e9. Edit run 37affd32-77a0-35bd-4fd8-1ce37cae608d. Publish run c161932e-1026-c3d5-81a0-2bb1d3788938, publication key d079e233-cd8d-0718-3e3d-04fd8e2d1a2d.
- What was done: the sample data was replaced with the 20 BRD records in LoadSampleDataForEmployee, and LoadSampleData got a one-time cleanup. If no Employee has the email alice.anderson@example.com, it deletes all Employee records, reads the table again, and loads the 20 records. If Alice exists, it deletes nothing.
- The user was told before the publish that it deletes the 13 existing records.
- Differs from design.md: the design prompt only asked for 20 records. The user adapted it to quote all 20 BRD records, to name the real bootstrap elements, and to add the one-time cleanup, because the bootstrap only runs when the table is empty.
- Mentor's offers to remove the development-stage condition and to delete the unused Employee.json resource were declined. No follow-up prompt was sent.
- Exact prompt (file `Prompts/5.3-fallback-sample-data.md`):
```
In the EmployeeCatalogMW app, replace the Employee sample data loaded by the sample data bootstrap (server actions LoadSampleData and LoadSampleDataForEmployee, and timer LoadSampleDataOnPublish) with exactly the 20 records below. The bootstrap only runs when the Employee table is empty. Add a one-time cleanup: if no Employee record has the email alice.anderson@example.com, delete all existing Employee records, then load these 20. If that record already exists, delete nothing. Run this cleanup before the existing empty-table check, so the 20 records then load into the empty table. This way the cleanup runs once and never on later publishes. All records are fictional and every email is on example.com. Each record is: FirstName LastName, JobTitle, Email, IsActive.

1. Alice Anderson, Software Engineer, alice.anderson@example.com, true
2. Bruno Castillo, Product Manager, bruno.castillo@example.com, true
3. Carla Dubois, UX Designer, carla.dubois@example.com, true
4. Devon Marsh, QA Analyst, devon.marsh@example.com, true
5. Elena Novak, Data Analyst, elena.novak@example.com, true
6. Felix Okafor, DevOps Engineer, felix.okafor@example.com, true
7. Grace Lindholm, HR Specialist, grace.lindholm@example.com, true
8. Hugo Brandt, Finance Analyst, hugo.brandt@example.com, false
9. Irene Takeda, Marketing Manager, irene.takeda@example.com, true
10. Jonas Ferreira, Support Agent, jonas.ferreira@example.com, true
11. Kara Whitfield, Project Manager, kara.whitfield@example.com, true
12. Liam Oduya, Sales Representative, liam.oduya@example.com, true
13. Maya Petrov, Technical Writer, maya.petrov@example.com, false
14. Nolan Reyes, Software Engineer, nolan.reyes@example.com, true
15. Olivia Sandoval, Office Manager, olivia.sandoval@example.com, true
16. Pavel Hartmann, Security Analyst, pavel.hartmann@example.com, true
17. Quinn Abara, Business Analyst, quinn.abara@example.com, false
18. Rosa Lindqvist, Recruiter, rosa.lindqvist@example.com, true
19. Samir Haddad, Solutions Architect, samir.haddad@example.com, true
20. Tessa Moreau, Customer Success Manager, tessa.moreau@example.com, true

17 records have IsActive true. 3 records have IsActive false: Hugo Brandt, Maya Petrov and Quinn Abara. Do not change any Employee attribute or attribute length, the Picture attribute, any screen (including the ImportData screen), any role or any filter. Change nothing else.
```
- Verification: graph comparison of revision 3 and 4. Content changed only inside LoadSampleData (21 nodes added, layout shifts) and LoadSampleDataForEmployee (the JSON source became a text literal). The flow was read: Alice check, delete, read again, empty check, load. Module stamps and stored validation messages also changed. The Employee entity and attributes are identical.

### Intervention 3: task 5.2, AC-03 (inactive hidden), published as revision 6
- Mentor session dc137568-65af-56c9-b4a1-9f81626e45e5. Edit run d37fef1f-cac5-0433-417c-49aa622e00c1. Publish run f1b1ff2c-d714-6f5c-6234-11101b17393a, publication key 54d13cb0-0fb9-3a77-32df-59ccb42cb1fd.
- What was done: a new, separate filter condition Employee.IsActive = True was added to GetEmployees.
- Differs from design.md: it uses the real screen and aggregate names and says to keep the search and role filters as they are.
- Exact prompt (file `Prompts/5.2-fallback-isactive-filter.md`):
```
In the Employees screen, add a new, separate filter condition to the existing GetEmployees aggregate so that it returns only the Employee records whose IsActive is True. Keep the existing search filter and the existing role-check filter exactly as they are. Do not change the Employees table columns or any other screen. Change nothing else.
```
- Verification: graph comparison of revision 5 and 6. Content changed only in GetEmployees: 5 nodes added for the new condition. The search filter and role filter are unchanged. Metadata stamps changed on the Employees screen, GetEmployees, MainFlow and the module, and stored validation messages were reordered.

## Revision history

| Revision | When (UTC, 2026-11-21) | Made by | What |
|---|---|---|---|
| 1 | 09:50:55 | the user, Mentor Web generation (task 2) | The generated app |
| 2 | 10:15:51 | Kiro, MCP publish | Task 5.1 |
| 3 | 10:22:39 | the user, ODC Studio | Unplanned. No functional change. Reason not stated |
| 4 | 10:42:58 | Kiro, MCP publish | Task 5.3 |
| 5 | 10:47:43 | the user, ODC Studio | Unplanned. No functional change. Reason not stated |
| 6 | 10:56:49 | Kiro, MCP publish | Task 5.2 |

- Revision 3 versus revision 2 (full graph comparison): no change to any action, screen, aggregate, filter, role or entity attribute. Only stamps, regenerated validation messages, and the OutSystemsMaps reference no longer lists its ShapeType entity.
- Revision 5 versus revision 4: no functional change. The GetAliceRecord filter in LoadSampleData was re-saved with new internal keys (same text literal hash, identical control flow). Stamps and validation message order changed.
- Revision 6 shows the user's key as the revision user, not "ide-service" as revisions 2 and 4 do. Its publication key matches the publish Kiro sent. The reason is not known.
- Each Kiro publish was compared against the latest revision at the time, not only against the revision before it. This mattered for revisions 3 and 5.

## Disagreements between the app and requirements.md
Nothing was changed. These stay report-only. Items 1 to 7 are from revision 1 and are still present in revision 6, as far as the graph comparisons show (none of the three fallback prompts touched them). Items 8 to 10 are new findings from tasks 5.3 and 5.2.
1. Screen names are Employees and Employee_Details, not Employee_List and Employee_Detail.
2. Extra screen ImportData (Excel upload and download for Employee). Requirements: exactly two screens.
3. ImportData and its UploadEmployeeExcel action create Employee records. Requirements: read-only, no creating, editing or deleting employees.
4. Extra role Admin. Requirements: Staff is the only role.
5. Staff can read, edit and create Employee (EmployeeCanEdit, EmployeeCanCreate), not View only. Requirements: no role has Edit access.
6. Attribute lengths are FirstName 200, LastName 200, JobTitle 200 and Email 256, not 50, 50, 100 and 250.
7. Extra attribute Picture, and a Picture image on Employee_Details. Requirements: no photos.
8. The sample-data bootstrap runs only in the development stage, and now includes a one-time cleanup that deletes all Employee records when no record has the email alice.anderson@example.com. If someone deletes Alice in a development environment, the next run of LoadSampleData deletes everything and reloads the 20 records. This is a side effect of intervention 2 that the requirements do not describe.
9. The old Employee.json resource is still in the app and gives an "unused resource" warning. Mentor offered to delete it, and the offer was declined.
10. Which screen is the landing screen was not determined (requirements: Employee_List).
- Fixed by the interventions: the search matching JobTitle and Email (5.1), the missing IsActive filter (5.2), and the sample data that did not match the BRD (5.3).
- Stored validation messages: 2 in revision 2, 15 in revision 3 (regenerated when the user published from ODC Studio) and 16 from revision 4 (adds "Employee.json is never used"). The ones read are "Non Existing Icon" warnings and a hidden security warning (a server action in a screen accessible by everyone). Their full text is not exposed through the MCP.

## Findings for the comparison with a second build
- Mentor Web did not follow the BRD on: screen names, the number of screens, the number of roles, Staff access, attribute lengths, the Picture attribute, the sample data (13 records with other names), the name-only search, and the IsActive filter. It did follow the list columns, the detail screen and the existence of a search.
- All three fallback prompts worked the first time. Each changed only the intended element, as shown by the graph comparisons. This depended on writing the prompt with the real names and "Change nothing else.".
- A Mentor edit cannot be verified from the model before it is published, because the read tools show only published revisions. Publishing came before verification each time.
- The publish turn of a Mentor session reported an empty pending-changes list and attemptedChange false for tasks 5.3 and 5.2. The edits were already in the session from the edit run. The publish facts alone would have suggested nothing was published.
- The context_* lookups were not reindexed after the task 5.1 publish. Only context_graph showed the new revision.
- The first AC-06 result (Pass, by hand) was wrong, because named records were not checked one by one. It was withdrawn after the user corrected it. Two statements in the 5.1 notes relied on it and carry correction notes.
- Mentor could not read the live Employee table. All data checks came from the user in the browser.
- The user published revisions 3 and 5 from ODC Studio between the planned publishes. A build comparison should count them as unplanned, with no functional change.
