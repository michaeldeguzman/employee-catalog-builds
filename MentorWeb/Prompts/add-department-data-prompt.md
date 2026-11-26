# add-department, task 2: data prompt (prompt 1)
Status: sent to Mentor, run succeeded. Not published. Publish 1 is task 3 and needs its own confirmation.
- App: EmployeeCatalogMW (asset key 07a64c21-0c8c-8afb-28ee-5d8530d55cf8). No other app was referenced.
- Mentor session: 9bd7d0f9-cdd1-c740-5138-5f7a236f5f88 (new session, one session for this task)
- Run: 4396579a-668b-5825-2a49-15149cc73ef9
- Sent as one single prompt, with the app key as the only asset reference. Wording: prompt 1 of design.md ("Task 1: data prompt (then publish 1)"), word for word.
- Revision before sending: app_revisions showed revision 6 as the latest (2026-11-21T10:56:49Z), the revision of Reports/graphdiff/rev6.txt. No newer revision, so no comparison was needed.
- The user confirmed the tenant write before anything was sent.
## Prompt sent (exact)
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
## Run result (before any publish)
- Run status: succeeded, after about 2 minutes (Mentor: "Worked for 1m 55s"). Polled about every 30 to 45 seconds. No retry was needed and no second prompt was sent on this session.
- Asset facts for EmployeeCatalogMW: attemptedChange true, changeApplied true, validation 0 errors, 16 warnings (the same count as after the first build's edit runs). No first messages were returned.
- Pending model changes reported by Mentor (final list):
  - Created: Department (IStaticEntity).
  - Modified: Employee (IServerEntity), LoadSampleData (IServerAction), LoadSampleDataForEmployee (IServerAction), module EmployeeCatalogMW (IESpace).
  - Modified, outside the named scope of the prompt: screen Employees, screen Employee_Details, server action UploadEmployeeExcel, server action DownloadEmployeeExcel. The prompt said not to change these. The list only says "Modified". It does not say what changed. These four elements use the Employee entity, so a change in the entity can mark them as modified without a change by Mentor. This is not verified. It is checked in the graph comparison of task 4, after publish 1. Nothing was changed by Kiro to fix it.
  - The timer LoadSampleDataOnPublish is not in the list (consistent with "timer unchanged").
- Mentor's summary (its own words, not verified against the model), paraphrased closely:
  - Department: new static entity with 4 records (Engineering, Finance, Human Resources, Sales), only the default static entity attributes, no stateflow or status logic.
  - Employee: added DepartmentId, an optional foreign key to Department. No other attribute changed, Picture included.
  - LoadSampleData: both paths that previously went to the End node (the empty-table load and the skip path) now pass through an IsInDevStage() check. In dev they run a new update named SetEmployeeDepartments before the End node. It matches the 20 employees by email, including the 3 inactive ones, and sets DepartmentId only where it is empty. The department values come from the Department static entity, not hard-coded Ids. Running it again changes nothing. GetAliceRecord, DeleteAllEmployees and the empty-table check were kept.
  - LoadSampleDataForEmployee: each of the 20 records is created with its DepartmentId set from the table.
  - Timer: LoadSampleDataOnPublish unchanged, still runs when published.
  - Deviation reported by Mentor: it could not make the Department Id auto-number in this version, so the 4 records have Ids 1 to 4, set by hand. The run's events show it first tried auto-number, then reworked the entity setup. The prompt did not ask for hand-set Ids. The Ids are those of static entity records, and the sample data refers to the records through the entity, as the prompt asked. This is reported to the user and is checked in the graph after publish 1.
  - Mentor says it did not publish.
- Not verified by Kiro (only Mentor's own words so far): the logic of SetEmployeeDepartments (match by Email, only empty DepartmentId, both paths to End, IsInDevStage condition), the Delete Rule of DepartmentId, the absence of stateflow elements, and that the four out-of-scope elements above are only knock-on changes. Text literals (the emails and labels) are not readable in the stored graph.
- The session 9bd7d0f9-cdd1-c740-5138-5f7a236f5f88 has not been closed. Publish 1 (task 3) uses this same session.

## Publish 1 (task 3)
Status: published. Revision 7 landed in Development.
- The user confirmed the publish before anything was sent. The user was told that publishing runs the timer LoadSampleDataOnPublish, which sets the Department of the 20 employees.
- Before asking: app_revisions showed revision 6 (2026-11-21T10:56:49Z) as the latest, the same as in task 2. The task 2 run was terminal (succeeded). No other publish of this app was known to be running.
- Turn sent in the same Mentor session 9bd7d0f9-cdd1-c740-5138-5f7a236f5f88, with the app key 07a64c21-0c8c-8afb-28ee-5d8530d55cf8 as the only asset reference.
- Publish turn text: "Publish the app EmployeeCatalogMW now. Publish note: add-department 1: Department static entity, Employee.DepartmentId, one-time department update in LoadSampleData."
- Publish run id: d195b4f5-269f-b3ed-9f70-1fba90df885a. Run status: succeeded, after about 24 seconds (Mentor: "Worked for 24s").
- Run events: publishStarted, publishAccepted (revision 7), publishSucceeded (revision 7). The run reported no conflict and no merge with another revision.
- Revision: 7 (2026-11-22T02:20:28Z), model digest 4ef9300f-41f9-c9e7-a19a-b66a2170f554.
- Publication key: ebf70064-658c-e43c-51fb-44e4fe3e5894
- Outcome: publish_status returned status Finished, outcome success, applicationRevision 7.
- publish_logs: 8 messages, all severity Info, no error code. The last one is OS-DPL-20007 "Publication finished". It includes "Executing database scripts finished".
- env_app (Development, env key 8b036dbd-6d28-2b5c-c50a-77a6bc07d748): revision 7, build key 91aee02e-e01f-b8fe-47e4-939fc203fefa, deployed 2026-11-22T02:20:28Z. URL: https://your-tenant-dev.outsystems.app/EmployeeCatalogMW
- Pending model changes at publish time: none (empty list). The publish run attempted no change (attemptedChange false).
- The publish was sent once and not repeated.
- Mentor session 9bd7d0f9-cdd1-c740-5138-5f7a236f5f88 is closed (closed: true).
- Timer: Kiro cannot see whether LoadSampleDataOnPublish ran or whether it set the Departments. If the Department cells stay empty, the user clicks Run now on LoadSampleDataOnPublish in the ODC Portal (App EmployeeCatalogMW, Configurations, Timers). This is an operational step, not a model change. It is not done by Kiro.
- Next: task 4 (graph check after publish 1) has not been started.
