# Graph comparison: EmployeeCatalogMCP revision 4 -> revision 5 (add-department task 4)
Recorded 2026-11-22, after publish 1 of add-department (publication key 2419713c-d7ef-3106-f0c7-f2528dfb5698). Read-only on the tenant: `app_revisions`, `context_graph`, `context_entities`. App key debb6b49-7b59-ecf6-b2eb-50a5f78250f3 (Development).

## Files
| File | What it is |
|---|---|
| `5.xre` | Whole-app graph of revision 5, no `root`. One page: `has_more` false, `next_cursor` none, header `revision` 5 = `latest_revision` 5 = the revision of `result-publish-data.json` and `app_revisions` (modelDigest bdf3d2dc-65c9-77fe-45de-481cff29c8a9). 11,778 nodes, 21,778 edges. SHA-256 `399de5339975e6d7b6d07497a1938f689b4738d05e185b1498e02c703c5feb99`. Copied from the harness tool-output file. |
| `4.xre` | Baseline, unchanged. |
| `4-to-5.diff` | Semantic diff. Nodes matched by `_key`. Edges matched by (source, target, attributes without `index`). Sibling `index` changes are listed on their own lines (`EDGE INDEX CHANGED`). Made with a throwaway Python script run from stdin. No script was saved. |

## Result
| Measure | Revision 4 | Revision 5 | Difference |
|---|---|---|---|
| Nodes | 11,630 | 11,778 | +148 added, 0 removed, 10 changed |
| Edges | 21,457 | 21,778 | +322 added, 1 removed, 305 with a changed sibling index |

- **Removed: no node.** One edge: `BootstrapEmployee` (call node in `BootstrapData`) to the End node, replaced by `BootstrapEmployee` to `GetEmployeesWithoutDepartment`. In scope (new logic after the call).
- **No change to:** any screen widget, screen action, local variable or input (Employee_List, Employee_Detail, RunTimer, template screens), the menu, the Staff role (1 IRole), any IPermission (9 and 9), `BootstrapTimer` (1 timer, schedule `WhenPublished`, date unchanged), server actions (5 and 5), client actions, flows (4 and 4), blocks (8 and 8), the module's `DefaultScreen`. No added edge touches an existing screen, role, timer, permission or flow.

## Intended scope check (design.md, publish 1 row)
| Item | Result |
|---|---|
| Static entity Department, 4 records, entity action | Present: `Department` (IsStaticEntity, not public, attributes Id (Integer) and Label (Text 50)), 4 records, entity action `GetDepartment`, `Department Identifier` type. See finding F-1 about the records. |
| Employee.DepartmentId | Present as attribute index 6, type `Department Identifier`, foreign key to Department, IsMandatory false, DeleteRule `Protect`. |
| Other Employee attributes | Unchanged (Id, FirstName, LastName, Email, JobTitle, IsActive: node and edges identical to revision 4). Email: type Email, length 256 (D-3). |
| New logic in `BootstrapData` | Present, see "BootstrapData flow". |
| Seed in `BootstrapEmployee` | Literal text changed (2,466 -> 2,806 characters). |
| Derived changes | `Employee` entity, the three aggregates that use Employee (`GetEmployees` in BootstrapEmployee, `GetEmployees` on Employee_List, `GetEmployeeById` on Employee_Detail): `LastModifiedDate` only. |

## BootstrapData flow (revision 5)
Start -> `BootstrapEmployee` -> aggregate `GetEmployeesWithoutDepartment` (Employee, filter `Employee.DepartmentId = NullIdentifier()`) -> `DeserializeDepartments` (JSON literal, 1,256 characters, list of `DepartmentSeed`) -> For Each over the employees without department -> For Each over the literal rows -> If `Employee.Email = row.Email` -> True: aggregate `GetDepartment` (Department.Label = row.Department, max 1 record) -> Assign `UpdatedEmployee = current employee`, `UpdatedEmployee.DepartmentId = GetDepartment.List.Current.Department.Id` -> `UpdateEmployee` (Employee entity action) -> next row. False: next row. After both loops: End.
- No SQL or advanced query node. No new server action, timer or Bootstrap action. Signature of `BootstrapData` unchanged.
- The lookup is by Label and the written value is the Id, so the update does not depend on the record names (see F-1).

## Entities lookup (`context_entities`, owned only)
- `Department`: isStatic true, attributes Label (Text 50), Id (Integer, primary key, mandatory), not public. Records listed as `["HumanResources","Finance","Sales","Engineering"]` (record names, not Labels).
- `Employee`: FirstName Text 50, LastName Text 50, JobTitle Text 100, Email Email 256, IsActive Boolean, Id Long Integer (primary key), DepartmentId `Department Identifier`, not mandatory, foreign key to Department (attribute key xxxxxxxx-...).

## Assignment match (seed, update, table)
The graph does not hold the text of a literal, only its length and the first 10 hex characters of its SHA-1 (`TextLength`, `TextHash`). I rebuilt the literals from the table and compared length and hash, the same method as F-3 in `1-baseline-notes.md`.
| Literal | Where | Graph (length, hash) | Rebuilt from the table | Match |
|---|---|---|---|---|
| Seed, revision 4 | `BootstrapEmployee`, `DeserializeEmployees` | 2,466, `2e83c0b72a` | 20 records of spec.md section 10, compact JSON | yes |
| Seed, revision 5 | same | 2,806, `808c85070a` | same 20 records, in the same order, plus `"DepartmentId":N` after `IsActive`, N = 1 Engineering, 2 Finance, 3 Human Resources, 4 Sales | yes |
| Update | `BootstrapData`, `DeserializeDepartments` | 1,256, `ce1312410b` | 20 objects `{"Email":...,"Department":"<name>"}` in table order | yes |
- The Email and Department of every row came from the table in `requirements.md` (name, job title, active flag, department) and the emails of spec.md. I checked these against the table in prompt 006 (by Email): 20 of 20 rows agree. The rebuilt literals then match the graph exactly, so the seed and the update both hold the 20 rows of the table, with the same department for every email, and they agree with each other.
- Id to Label in the graph (Label from its SHA-1 prefix and length): Id 1 Engineering, Id 2 Finance, Id 3 Human Resources, Id 4 Sales. The seed's numeric DepartmentId therefore points to the right Label.
- Limit: this is a match by length plus a 40-bit hash prefix, not a read of the text. The chance of a different text with the same length and hash is negligible, but it is not a reading. The stored data is checked in the browser (task 8).

## D-2 re-check
Calls to Employee entity actions in revision 5 (incoming edges of each entity action):
| Entity action | Called from |
|---|---|
| `CreateEmployee` | `BootstrapEmployee` (one call node) |
| `UpdateEmployee` | `BootstrapData` (one call node, new) |
| `CreateOrUpdateEmployee`, `CreateOrUpdateSomeEmployees`, `DeleteEmployee`, `DeleteAllEmployees`, `GetEmployee`, `GetEmployeeForUpdate` | no caller |
Result: only `CreateEmployee` in `BootstrapEmployee` and `UpdateEmployee` in `BootstrapData`. `UpdateEmployee` in `BootstrapData` is the second allowed write path, run by `BootstrapTimer` or by RunTimer (`RunTimerOnClick` calls `BootstrapData`). No SQL or advanced query node exists. `Department` has no write action (static entity, only `GetDepartment`, no caller).

## Delete rule of DepartmentId (as found, not changed)
`Protect`. The graph shows `DeleteRule` = `Protect` on `Employee.DepartmentId`. Mentor's summary of task 2 says the same ("`Protect`, the default").

## Findings outside the scope in design.md, or that need a decision
- **F-1: the Department record names do not match their Labels, and the graph order of the records differs from requirements.md.** From `5.xre` (record node, its Id value, its Label value identified by SHA-1 prefix and length):

  | Graph record index | Record name (Identifier) | Id | Label |
  |---|---|---|---|
  | 0 | Finance | 1 | Engineering |
  | 1 | HumanResources | 2 | Finance |
  | 2 | Engineering | 4 | Sales |
  | 3 | Sales | 3 | Human Resources |

  By Id the Labels are in the required order (Engineering, Finance, Human Resources, Sales) and the 4 Labels are right. But (a) every record name belongs to a different Label than the one it carries, so `Entities.Department.Engineering` would be Id 4, whose Label is Sales; (b) in record (index) order the Labels read Engineering, Finance, Sales, Human Resources, which differs from the order in `requirements.md` in the last two places. Nothing in the model refers to a record by name (no edge points to a record except from Department itself), so the update and the seed are not affected: the update matches by Label and sets the Id, the seed uses the Ids. Prompt B asks for a dropdown with the records "in record order", so (b) would show in the dropdown if the order is taken from the record position. I cannot tell from the graph whether ODC uses the record position or the Id for that order. Not changed.
- **F-2: elements not named in the scope row.** `DepartmentSeed` structure with attributes `Email` and `Department` (plus the generated list, anonymous-structure and attribute-type nodes the module holds for Department and DepartmentSeed: 4 list types, 2 anonymous structures, 2 attribute types), needed by the JSON literal of the update; Mentor named it in its summary and offered to delete it. Also two built-in nodes that the new logic references: the function `NullIdentifier` and the type `Integer Identifier`. Supporting elements of the intended logic, not behaviour changes.
- **F-3: metadata changes on nodes outside the intended elements.** `LastModifiedByTool` ODCStudio -> AgentExperience on the module `EmployeeCatalogMCP` and on the flow `MainFlow`. No functional field changed. (Same kind of change as O-2 in `2-notes.md`.)
- **F-4: screens.** The screen aggregates `GetEmployees` (Employee_List) and `GetEmployeeById` (Employee_Detail) show only `LastModifiedDate` 2026-11-21T19:25:37 -> 2026-11-21T22:32:18. Derived from the Employee change. Their sources, filters, columns and widgets are identical.
- **F-5: layout and order noise.** End node of `BootstrapData`: Y 4346 -> 9665 and its sibling index 2 -> 9. 304 sibling-index renumberings under the module (160 `ListTypes`, 144 `AnonymousStructures`), caused by the 4 new list types and 2 new anonymous structures in the module's lists. No node removed.
- No removed node, no change to Employee attributes other than the added one, Staff role, `BootstrapTimer`, screens, RunTimer, menu or default screen.

## Verdict for task 4
No change to a screen, role, timer, menu or server-action signature. The seed and the update match the table and each other. D-2 holds. F-1 (record names and record order) needs a decision before prompt B. F-2 to F-5 are reported for the record.
