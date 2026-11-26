# Graph comparison: EmployeeCatalogMCP revision 1 -> revision 2 (task 10)

Recorded 2026-11-22 (AEDT), after the publish of revision 2 (publication key 92338f80-b230-44fb-b754-d8e75c2db824).

## Files

| File | What it is |
|---|---|
| `2.xre` | Full graph of EmployeeCatalogMCP revision 2 (app_key debb6b49-7b59-ecf6-b2eb-50a5f78250f3). One page, `has_more` false, header `revision` 2 = `latest_revision` 2 = the published revision. SHA-256 `7947efef6268265e951a115dd92fe2ee3dba34a30bf5bb27605c44428c9a63ab`. 11,587 nodes, 21,382 edges. Copied from the harness's tool-output file into MCP. |
| `1.xre` | Baseline (revision 1), unchanged. |
| `1-to-2.diff` | Semantic diff of `1.xre` and `2.xre`: nodes matched by `_key`, edges by (source `_key`, target `_key`, attributes). Node order ignored. A plain line diff is meaningless here because each file is two long lines. The diff was produced with a throwaway Python script run from stdin; no script was saved. |

## Result

| Measure | Revision 1 | Revision 2 | Difference |
|---|---|---|---|
| Nodes | 11,220 | 11,587 | +367 added, 0 removed, 2 changed |
| Edges | 20,628 | 21,382 | +754 added, 0 removed |

- **Removed: nothing** (no node, no edge).
- **Changed nodes: 2.** `MainFlow` (IMobileFlow) and `Menu` (IMobileBlock). Only `LastModifiedBy` (None -> developer@example.com) and `LastModifiedDate` (0001-01-01 -> 2026-11-21T19:25:37) differ. No functional field changed.
- **Added: 367 nodes.** All belong to the two new screens, the menu link, and their expressions.
  - Employee_List: screen, `SearchKeyword` local variable, `GetEmployees` aggregate (sources Employee), `Search` client screen action (refresh data node), the table `EmployeesTable` with four header and four row cells, `Input_Search`, an If widget for the empty state, lifecycle events, one Staff IPermission.
  - Employee_Detail: screen, `EmployeeId` input parameter, `GetEmployeeById` aggregate, detail card with five Expression widgets, back link, lifecycle events, one Staff IPermission.
  - Menu: one Link widget added under the existing `PageLinks` container.
  - Expression helper nodes (ExpressionAST 59, RuntimeProperty 58, CompoundIdentifier 54, Identifier 28, Text 25, Boolean 16, BinaryOperation 11, Integer 3, Argument 3).
- **Added edges from a pre-existing node** (these are the only attachments to old elements): MainFlow -> Employee_List and Employee_Detail (screens in flow MainFlow); PageLinks -> the new Link; **module EmployeeCatalogMCP -> Employee_List, `DefaultScreen`** (see O-1).
- **Added edges from a new node to a pre-existing node**: layout and menu block instances (LayoutTopMenu, Menu) and their parameters, the aggregates' sources (Employee), references to Employee attributes, the two Staff IPermissions -> role Staff, built-in function references. No edge was added to or removed from any Employee attribute, the Staff role, or any `Bootstrap*` element.

## Intended scope check

| Item | Result |
|---|---|
| Screens Employee_List, Employee_Detail exist, in MainFlow | Present. 8 screens now (6 template + 2). |
| Their menu entries | One Link in the Menu block's PageLinks container. The Link text and destination nodes are present; Mentor reported one `Employees` link to Employee_List. |
| Role assignments | Employee_List and Employee_Detail each have one IPermission -> IRole Staff, `AccessibleBy` False (Staff only). |
| Staff access to Employee | No model element exists for this (see D-2 below). |
| Employee attributes | Unchanged (no changed or added node or edge on Employee's attributes). |
| Staff role | Unchanged. Still 1 IRole and 1 role exception. |
| BootstrapEmployee, BootstrapData, BootstrapTimer, WakeBootstrapTimer | Unchanged (no changed node, no added or removed edge). |
| The six template screens (including Login), flows Common/Emails/Layouts, other blocks | Unchanged. |
| Other entities, roles, timers, server actions, client actions, structures | None added. Server actions 5, client actions 5, timers 1, roles 1, entities 1 (same as revision 1). |

## Changes outside the intended scope

- **O-1: the module's default screen is now Employee_List.** Revision 1 had no `DefaultScreen` edge from the module; revision 2 has one to Employee_List. Mentor's summary for the screens turn said "I didn't set a default landing screen". This is a small difference between Mentor's report and the model. It is not a requirement (none states a landing screen), and the effect is that the app root opens Employee_List for a signed-in Staff user. Reported, nothing changed.
- **O-2: LastModifiedBy / LastModifiedDate on `MainFlow` and `Menu`.** Metadata only. Both elements are expected to be touched by the intended scope (screens added to MainFlow, link added to Menu).
- No other change outside scope.

## D-2 check (user decision 2026-11-22): "Staff has View access to Employee only"

Rule: met if both screens require Staff and the app has no way to create, edit or delete Employee records, apart from BootstrapData's insert of the 20 sample rows.

| Point | Evidence in `2.xre` | Result |
|---|---|---|
| Employee_List requires Staff | IPermission (key ...LHytsf4qwkOoO9noGzhZRg) -> IRole Staff; screen `AccessibleBy` False | Met |
| Employee_Detail requires Staff | IPermission (key ...aks_+M+1AUuhNlBJt6iehQ) -> IRole Staff; screen `AccessibleBy` False | Met |
| No create, update or delete of Employee outside the bootstrap | The entity's generated actions are `CreateEmployee`, `CreateOrUpdateEmployee`, `CreateOrUpdateSomeEmployees`, `DeleteEmployee`, `DeleteAllEmployees`, `GetEmployee`, `GetEmployeeForUpdate`, `UpdateEmployee`. The only call to any of them is `CreateEmployee` from `BootstrapEmployee` (one call node inside its loop). The other entity actions have no caller. Employee's only incoming edges are 3 aggregate sources (GetEmployees, GetEmployeeById, BootstrapEmployee's aggregate), the module's Entities edge, and type references. | Met |
| No SQL or advanced query that could write | No SQL or advanced-query node type in the graph (checked by type name). | Met |
| No server action, timer or screen action other than `BootstrapData` changes Employee | Server actions are the same 5 as revision 1 (BootstrapData, BootstrapEmployee, 3 template email/user actions). The one new client screen action is `Search` (refresh data only). | Met |

**D-2: resolved.**

## Extra evidence for the browser check (not a verification of behaviour)

- `GetEmployees` conditions reference `IsActive` and, for the search, `FirstName` and `LastName` only. No condition references JobTitle or Email (AC-02, AC-03). The conditions' operators and joins were not decoded; the browser check in task 12 settles behaviour.
- Employee_List shows four columns (four header cells and four row cells). Employee_Detail shows five Expression widgets (matching the five attributes).
- Mentor's extras (sort by last name then first name, the "No employees found" message, the back link on Employee_Detail) are present in the graph as the ISort nodes, the If widget and the Link widget. Recorded as extras; no fix turn was sent.
