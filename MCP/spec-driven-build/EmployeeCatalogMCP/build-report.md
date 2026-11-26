# Spec-driven build report

- **App:** `debb6b49-7b59-ecf6-b2eb-50a5f78250f3`
- **Generated:** 2026-11-21T19:27:15Z
- **Spec file:** `spec.md`

## Build summary and checks (task 11, skill Steps 7 and 8)

Written 2026-11-22 (AEDT) by Kiro. Only the sections after this one (Mentor turn: data, Mentor turn: screens, Spec used) come from `render-report`. This section was added by hand for task 11. `spec.md` and `requirements.md` were not changed.

### App

| Item | Value |
|---|---|
| App name | EmployeeCatalogMCP (Reactive Web app, `WebApplication`) |
| app_key | debb6b49-7b59-ecf6-b2eb-50a5f78250f3 |
| Portfolio key | 2361d977-28e7-c828-d75b-302e87dcb460 (same as EmployeeCatalogMW) |
| Development environment key | 8b036dbd-6d28-2b5c-c50a-77a6bc07d748 |
| Runtime URL | <https://your-tenant-dev.outsystems.app/EmployeeCatalogMCP> (from `env_app`, Development, revision 4 deployed, build key 8d56a5ae-2d78-2dfc-738d-57562fdced1c) |
| Mentor session | a899ca3b-0707-bf0e-b248-c03509ed6b00, **closed** in task 11 (`mentor_close_session` returned `closed: true`). Everything in it was already published |

### Revisions (from `app_revisions`)

| Revision | Published (UTC) | Made by | What it holds |
|---|---|---|---|
| 1 | 2026-11-21 19:05:40 | Mentor publish turn (run d2ff1b12-ee3b-9672-5d3d-a41270e6f6cf, publication key 5f1513df-48de-9153-26e3-cac40540a1aa) | Part 1: Employee, Staff, `BootstrapEmployee`, `BootstrapData`, `BootstrapTimer` |
| 2 | 2026-11-21 19:34:39 | Mentor publish turn (run a05ef96c-b747-bf05-2cd6-087be9ab10eb, publication key 92338f80-b230-44fb-b754-d8e75c2db824) | Part 2: Employee_List, Employee_Detail, menu link |
| 3 | 2026-11-21 19:46:08 | The user, in ODC Studio (unplanned publish U-1) | No functional change (reference entries and tool markers only) |
| 4 | 2026-11-21 21:01:27 | The user, in ODC Studio (manual intervention M-1) | Adds the `RunTimer` screen, see deviation D-4 |

Revisions 3 and 4 were not made by Kiro or Mentor. Details: `MCP/Reports/interventions.md`. Graph comparisons: `MCP/Reports/graphdiff/`.

### What was built

- **Entities: 1.** Employee with Id (Long Integer, automatic), FirstName (Text 50), LastName (Text 50), Email (Email), JobTitle (Text 100), IsActive (Boolean). Email length is 256 in the published model, not 250 (deviation D-3).
- **Roles: 1.** Staff (key f9f3f634-4449-ffea-b5c8-bae77af37d07). The `context_roles` lookup returns only this role.
- **Screens built by Mentor: 2.** Employee_List and Employee_Detail, both in `MainFlow`, both with role Staff.
- **Bootstrap elements (from the skill's bootstrap guardrail):** server actions `BootstrapEmployee` and `BootstrapData`, and timer `BootstrapTimer` (schedule "when published").
- **Menu:** one `Employees` link to Employee_List.
- **Template screens (6):** Login, UserProfile, ChangePassword, RecoverPasswordRequest, RecoverPasswordReset, InvalidPermissions, all in the `Common` flow. They come from the standard Web template, not from the spec.
- **Screen total on the tenant now: 9** (6 template, 2 Mentor, 1 added by the user).

### Check: access per screen against spec.md section 4

Lookups used: `context_screens` and `context_roles` for app debb6b49-7b59-ecf6-b2eb-50a5f78250f3, run on 2026-11-22 after the Mentor session was closed. Index timestamps on the rows: 2026-11-21T19:35:33Z (Employee_List, Employee_Detail) and 21:02:39Z (RunTimer).

| Screen | spec.md section 4 | `context_screens` roles | Result |
|---|---|---|---|
| Employee_List | Staff | Staff | Match |
| Employee_Detail | Staff | Staff | Match |
| RunTimer (not in spec.md) | not listed | Staff | Extra screen, deviation D-4 |
| Login, UserProfile, ChangePassword, RecoverPasswordRequest, RecoverPasswordReset, InvalidPermissions (template) | not listed | Staff on each | Template screens, not part of spec.md section 4. Findings F-2 accepted by the user |

Limits of this check:

- The screens lookup rows carry no `additionalData.anonymousAccess` field in this response. The tool description says a missing field means access is unknown and must not be read as "login required". The roles list alone therefore does not prove that a screen requires login.
- The published graph settles it for the two spec screens. In `2.xre` (task 10, `MCP/Reports/graphdiff/2-notes.md`) Employee_List and Employee_Detail each have one permission to the Staff role and `AccessibleBy` False. `4.xre` still shows `AccessibleBy` False on Employee_List. For the template screens the lookup says Staff, but this report does not claim they require login: Login and the password-recovery screens are normally open to everyone, and the lookup cannot show that.
- Staff has no model-level View permission on Employee. ODC has no such setting, so this was resolved as D-2 (decision 2026-11-22): both screens require Staff, and the only call to an Employee create, update or delete action is `CreateEmployee` inside `BootstrapEmployee`. Re-checked on revision 4 in `MCP/Reports/check-2-2026-11-22.md`: still true, but a Staff user can now trigger that insert through `RunTimer`.

### What Mentor added, skipped or left manual

Added beyond the spec (kept, not interventions):
- Sort order: last name, then first name.
- "No employees found" message on an empty result.
- Link back to the list on Employee_Detail.
- The module's default screen is Employee_List (Mentor said it set none; graph note O-1).
- Mentor renamed the template's default role to Staff, so Staff is on all six template screens (F-2, accepted).

Skipped or different from the prompt:
- D-1: `BootstrapEmployee` returns "inserted N rows" as an output Message and writes no log line.
- D-3: Email length 256 instead of 250.
- No model-level View permission for Staff on Employee (D-2, resolved as above).
- `BootstrapEmployee` seeds from one JSON literal and has no exception handler (F-3, accepted).

Manual steps left to the user:
- Give users the Staff role in the ODC Portal (task 7, done by the user).
- No library dependencies were added.

### Sample data (skill Step 5, item 5) and the timer

- Run the sample data check in the browser, not through logs. The `app_logs` check (task 8, `MCP/Reports/task8-applogs-check.md`) was inconclusive: the Development log source was silent, and D-1 means no "inserted N rows" line exists in any case.
- The manual data check happens in task 12: 20 records, Hugo Brandt, Maya Petrov and Quinn Abara inactive, an active Alice, values as in `spec.md` section 10. User browser observations so far (not a verdict): 17 rows on Employee_List after the `RunTimer` run, and Alice's detail screen shows five values, read-only. The 20 records and the 3 inactive ones are not yet checked.
- `BootstrapTimer` itself has not run. The Development stage's daily timer limit blocked it (incident P-2, error OS-TMR-42900). The data was loaded by `BootstrapData` through the `RunTimer` button (M-1), not by the timer.
- **The app now contains `BootstrapData` and `BootstrapTimer`.** The timer runs on every publish, deployment and automatic patch, in whichever stage the app is in, and refills any empty sample-data table. `BootstrapEmployee` inserts only when Employee is empty, so a table with rows is skipped. To keep the table empty, the timer has to be removed first. That can be done in one Mentor turn on this app, confirmed and published like any other change. No such turn has been sent.

### Not covered by this section

- The result per AC is task 12 (`MCP/Reports/check-<revision>-<yyyy-mm-dd>.md`).
- Nothing is unpublished. No session is open.

## Mentor turn: data

- **Run ID:** `6d9624d6-584a-4809-8474-56b53ea9ae28`
- **Status:** `succeeded`
- **Landed:** yes (succeeded, no validation errors)
- **Result file:** `result-data.json`

I built the data part of `EmployeeCatalogMCP`. It isn't published, and I made no screens.

### Created
- **Roles:** 1. I renamed the template's default role to `Staff`.
- **Entities:** 1. `Employee` has an automatic `Id` (Long Integer), `FirstName` (Text 50), `LastName` (Text 50), `Email` (Email 250), `JobTitle` (Text 100) and `IsActive` (Boolean). It has no relationships.
- **Static entities:** 0. The spec has none.
- **Bootstrap actions:** 2.
  - `BootstrapEmployee` adds the 20 sample employees from the spec, in order and with the values as given. It runs only if `Employee` is empty. The spec has no date values.
  - `BootstrapData` calls `BootstrapEmployee`.
- **Timer:** `BootstrapTimer` runs `BootstrapData` when the app is published.

### Not done
- **Log line:** `BootstrapEmployee` returns its "inserted N rows" or "skipped, N present" line as an output called `Message`, not as a log entry. I found no log action to call. If you want it in the logs, tell me and I'll add one.
- **View-only access:** I set up no permission on `Employee` for `Staff`. It is read-only because the next turn's screens won't create, edit or delete employees, not because of a model setting.
- **Out of scope:** I skipped departments, photos, integrations, dashboards and any other roles, as the spec says.

### Manual steps
None. I added no library dependencies.

The screens `Employee_List` and `Employee_Detail` come in the next turn, after you publish.

## Mentor turn: screens

- **Run ID:** `52f44c49-aeb3-fc4b-176b-ed3352ff7571`
- **Status:** `succeeded`
- **Landed:** yes (succeeded, no validation errors)
- **Result file:** `result-screens.json`

I built the two screens, `Employee_List` and `Employee_Detail`, with no validation errors. The only warnings are about the template's font URLs in the stylesheet. I haven't published, and I haven't opened the screens in a browser, so please check the layout and the search there.

### Created
- **Screens:** 2, both in `MainFlow` and restricted to the `Staff` role, using the top-menu layout.
  - `Employee_List` shows a table with First name, Last name, Job title and Email. It lists only employees with `IsActive` set to true, sorted by last name, then first name. A search input filters on first or last name as the user types, and a "No employees found" message appears when nothing matches. The first name in each row opens the detail screen.
  - `Employee_Detail` takes an `EmployeeId` and shows first name, last name, email, job title and active status in a card, with a link back to the list. It is read-only.
- **Actions:** 1 screen action, `Search`, which refreshes the list from the search input.
- **Menu:** one `Employees` link to `Employee_List`.

### Data part
I added nothing to the data part. The bootstrap actions and timer are unchanged.

### Skipped
- **Extra styling:** I used the OutSystems UI defaults only, as the spec asks.
- **Master-detail and popup patterns:** I didn't use them, per the spec.
- **Other screens and roles:** I built nothing beyond the spec.

### Manual steps
- **Role assignment:** Give users the `Staff` role in the ODC Portal. The template's login and profile screens already use `Staff` as well.
- **Landing page:** I didn't set a default landing screen, so open `Employee_List` from the menu or by its URL.
- **Libraries:** I added no library dependencies.

## Spec used (for reference)

<details>
<summary>Click to expand the full spec</summary>

# App Spec: EmployeeCatalogMCP

## 1. Overview

**Purpose:** Employee Catalog is a read-only staff directory. Staff use it to find a colleague's name, job title and email in one place. It is a demo with about 20 employees.

**Target users:** Staff.

**Target app:** EmployeeCatalogMCP (new)

**Style direction:** Apply OutSystems UI defaults

---

## 2. Roles

- **Staff**: the only role. Has View access to Employee: can see employee data, and cannot create, edit or delete it.

---

## 3. Data model

### Entities

| Entity | Attributes (name, type, constraint) | Relationships |
|---|---|---|
| Employee | Id (Long Integer, primary key, automatic), FirstName (Text, 50), LastName (Text, 50), Email (Email, 250), JobTitle (Text, 100), IsActive (Boolean) | None. Single entity. |

### Static enums

None.

---

## 4. Screens + RBAC

| Screen | Purpose | Accessible by (roles) |
|---|---|---|
| Employee_List | Table of active employees with a search input | Staff |
| Employee_Detail | All Employee attributes for one employee | Staff |

---

## 5. Server actions

None. Screens read data with aggregates. The only actions are the bootstrap actions for the sample data.

---

## 6. Integrations

None.

---

## 8. Out of scope

- Departments (no Department entity in this version).
- Creating, editing or deleting employees.
- Photos.
- Integrations.
- Dashboards.
- Any screen other than Employee_List and Employee_Detail.
- Any role other than Staff.

---

## 9. Acceptance criteria

- AC-01 (list loads): Given a Staff user is signed in and Active_Employee records exist, When the user opens Employee_List, Then a table shows the columns FirstName, LastName, JobTitle and Email, with one row per Active_Employee.
- AC-02 (search): Given a Staff user is on Employee_List and an Active_Employee has the FirstName "Alice" or the LastName "Alice", When the user enters "Alice" in the search input, Then the table shows only Active_Employee rows whose FirstName or LastName matches "Alice".
- AC-03 (inactive employees hidden): Given at least one Employee has IsActive set to false, When a Staff user opens Employee_List, Then no row is shown for any Employee with IsActive set to false.
- AC-04 (detail screen): Given a Staff user is on Employee_List, When the user opens an employee row, Then Employee_Detail shows FirstName, LastName, Email, JobTitle and IsActive of that employee.
- AC-05 (empty search result): Given a Staff user is on Employee_List, When the user enters a search text that matches no Active_Employee FirstName or LastName, Then the table shows no rows.
- AC-06 (sample data present): Given Employee_Catalog is deployed, When the Employee data is inspected in ODC Studio or the browser, Then it contains 20 fictional Employee records, at least 2 of them with IsActive set to false, and none of them is a real person, and one of them is an active employee with first name Alice.

---

## 10. Notes for Mentor

- Employee_List is a Table with the columns FirstName, LastName, JobTitle and Email.
- The table shows only Employee records where IsActive is true.
- The search input matches FirstName or LastName only.
- Employee_Detail shows FirstName, LastName, Email, JobTitle and IsActive of the employee. Employee Catalog is a read-only staff directory.
- Do not use the patterns "Master detail" or "List with popup".
- Seed exactly the 20 records listed under "Sample data" below, in that order, with the values as given and no others.

### Sample data

| FirstName | LastName | JobTitle | Email | IsActive |
|---|---|---|---|---|
| Alice | Anderson | Software Engineer | alice.anderson@example.com | true |
| Bruno | Castillo | Product Manager | bruno.castillo@example.com | true |
| Carla | Dubois | UX Designer | carla.dubois@example.com | true |
| Devon | Marsh | QA Analyst | devon.marsh@example.com | true |
| Elena | Novak | Data Analyst | elena.novak@example.com | true |
| Felix | Okafor | DevOps Engineer | felix.okafor@example.com | true |
| Grace | Lindholm | HR Specialist | grace.lindholm@example.com | true |
| Hugo | Brandt | Finance Analyst | hugo.brandt@example.com | false |
| Irene | Takeda | Marketing Manager | irene.takeda@example.com | true |
| Jonas | Ferreira | Support Agent | jonas.ferreira@example.com | true |
| Kara | Whitfield | Project Manager | kara.whitfield@example.com | true |
| Liam | Oduya | Sales Representative | liam.oduya@example.com | true |
| Maya | Petrov | Technical Writer | maya.petrov@example.com | false |
| Nolan | Reyes | Software Engineer | nolan.reyes@example.com | true |
| Olivia | Sandoval | Office Manager | olivia.sandoval@example.com | true |
| Pavel | Hartmann | Security Analyst | pavel.hartmann@example.com | true |
| Quinn | Abara | Business Analyst | quinn.abara@example.com | false |
| Rosa | Lindqvist | Recruiter | rosa.lindqvist@example.com | true |
| Samir | Haddad | Solutions Architect | samir.haddad@example.com | true |
| Tessa | Moreau | Customer Success Manager | tessa.moreau@example.com | true |


</details>
