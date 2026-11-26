# Graph comparison: EmployeeCatalogMCP revision 7 -> revision 8 (add-department, publish 2, screens)
Recorded 2026-11-22 after publish 2 (publication key 21b03612-551f-4695-f1da-ecd2988410e1). Read-only on the tenant: `app_revisions`, `context_graph`. App key debb6b49-7b59-ecf6-b2eb-50a5f78250f3 (Development). Task 7 of `MCP/.kiro/specs/add-department/tasks.md`. Requirements: AC-07, AC-08.

## Files
| File | What it is |
|---|---|
| `8.xre` | Whole-app graph of revision 8, no `root`. One page: `has_more` false, header `revision` 8 = `latest_revision` 8 = the latest revision in `app_revisions` (8, 2026-11-21T23:09:10Z, modelDigest ddd770d0-263a-0738-9537-eae8481d0315) = the revision of the publish 2 run. 11,900 nodes, 22,041 edges. SHA-256 `c1a71163418c2d1129696e8672804b0de62b4eee864f544f32d238e84fd1403a`. Copied from the harness tool-output file. |
| `7.xre` | Previous revision, unchanged. SHA-256 `99250cf08122d67a2e40b9daaecf5ddf907f2dacd76ade3ec57368ccb3c911fd` (same as recorded in `5-to-7-notes.md`). |
| `7-to-8.diff` | Semantic diff, same method as `5-to-7.diff` (nodes by `_key`; edges by source, target and attributes without `index`; sibling index changes on their own lines). Made with a throwaway Python script run from stdin. No script was saved. Long field values are cut at 300 to 400 characters. |

Revision 8 follows revision 7 directly. No other user published in between (run event list of publish 2 has no `publishAutoMerged`), so the whole 7 -> 8 difference is the screens change.

## Result
Nodes 11,778 -> 11,900: 122 added, 0 removed, 4 changed. Edges 21,778 -> 22,041: 303 added, 40 removed, 251 with a changed sibling index.

### Out of scope (changes to the data model, a server action, BootstrapTimer, RunTimer, the menu, roles, existing columns, fields, sort, search or the IsActive filter)
**None.**
- No entity, static entity, entity attribute or static entity record node was added, removed or changed.
- No `IServerAction` (BootstrapData, BootstrapEmployee, template actions), no timer, no role and no menu node was added, removed or changed. `BootstrapData` is not among the 4 changed nodes, so the seed and update literals are unchanged.
- The only 4 changed nodes are `Employee_List`, `GetEmployees`, `Employee_Detail` and `GetEmployeeById`, and for each only `LastModifiedDate` differs (2026-11-21T19:25:37 / 22:32:18 -> 23:05:27 or 23:05:37).
- The screen `RunTimer` and every other screen: no node or edge differs.
- Existing columns and fields: no existing widget, header cell, row cell, expression, text or label node changed. The new cell is `HeaderRow` and `Row` index 4 of `EmployeesTable` (the existing ones are 0 to 3), and the new field is the 6th container of `DetailCard` (index 5, after the five existing ones).
- Sort: the two `ISort` nodes of `GetEmployees` (LastName ascending, then FirstName ascending) are unchanged.
- Search: the search condition on `SearchKeyword` (node `...4fmhOdEOopZQh6PZX0Q.#Condition`) is unchanged. `Input_Search` and the `Search` screen action are unchanged.
- IsActive filter: the condition `Employee.IsActive` (node `...xtWqEhcA806Njo96HbQIIg.#Condition`) is unchanged.

### In scope: Employee_List (83 added nodes, plus 2 of the 3 `IAddSource` nodes)
| Element | Detail |
|---|---|
| Local variable `SelectedDepartmentId` | Data type Department Identifier, at index 1 after `SearchKeyword`. No default value node (empty). |
| Aggregate `GetDepartments` (new, not named in prompt B) | Source Department, one `ISort` on Department.Id ascending, MaxRecords 50, Fetch AtStart, an `OnAfterFetch` event node. It feeds the dropdown. Placed before `GetEmployees` (ScreenDataSets index 0; `GetEmployees` moved from 0 to 1). |
| Aggregate `GetEmployees` | Source Department added (alias `Department`), `IJoin` of type `Left` with LeftSource Employee, RightSource Department, condition `Employee.DepartmentId = Department.Id` (this is "With or Without"). New third filter condition (see below). Source list order is now Department (index 0), Employee (index 1). |
| Dropdown `Dropdown_Department` | In a new container next to `Input_Search` (same parent container as `Input_Search`, index 1), with a new `Label` widget with the text "Department". Variable `SelectedDepartmentId`, List `GetDepartments.List`, Labels `Department.Label`, Values `Department.Id`, EmptyValue "All departments", Mandatory False, Enabled True. `OnChange` is a built-in event whose destination is the existing screen action `Search`. |
| Table column | New `HeaderCell` (text "Department") and `RowCell` with an Expression `GetEmployees.List.Current.Department.Label`, as the last column. |

### In scope: Employee_Detail (26 added nodes, plus 1 `IAddSource` node)
| Element | Detail |
|---|---|
| Aggregate `GetEmployeeById` | Source Department added, `IJoin` of type `Left` (Employee left, Department right) on `Employee.DepartmentId = Department.Id`. Source list order is now Department (index 0), Employee (index 1). Its existing filter nodes did not change. |
| Field | New container as the last child of `DetailCard`, with a label text "Department" and an Expression `GetEmployeeById.List.Current.Department.Label`. Same style classes as the other fields. |

### Derived changes (module level and references)
- New anonymous structure `Department, Employee Record` (attributes `Department` and `Employee`) and its list type `Department, Employee Record List`, with 6 runtime properties. They are the result type of the two aggregates now that each has two sources. The old `Employee Record List` list type stays in the graph.
- 19 edges that pointed to `Employee Record List` (the `Type` of `GetEmployees` and `GetEmployeeById`, their `List`, and the data type of the expressions that read `GetXxx.List`), 10 `Current` edges and 10 `Employee` attribute edges, and 1 `Empty` edge were re-pointed to the new list type, its `Current` and `Empty` properties and its `Employee` attribute. Each of the 40 removed edges has an added edge from the same source. They sit in the expressions of `Employee_List` (28) and `Employee_Detail` (12), and they are the existing column and field expressions reading through the new structure. No expression text or order changed.
- 251 sibling index changes: 249 in the module-level `AnonymousStructures` (169) and `ListTypes` (80) lists, because the new structure and list type are inserted ahead of later ones; 1 for `GetEmployees` in `ScreenDataSets` (0 -> 1, because `GetDepartments` is now first); 1 for the Employee source in `GetEmployees` (`Sources` 0 -> 1, because Department is now first).

Counts by owner. Added nodes: Employee_List 85, Employee_Detail 27, module level 10 (total 122). Added edges: Employee_List 210, Employee_Detail 71, module level 22 (total 303). Removed edges: Employee_List 28, Employee_Detail 12 (total 40).

## GetEmployees filter check (as far as the graph shows)
`GetEmployees` on `Employee_List` has three `FiltersConditions` entries on the same source, in this order. ODC combines separate filter entries of one aggregate with AND.
| Index | Condition | Status vs revision 7 |
|---|---|---|
| 0 | `Employee.IsActive` | Unchanged |
| 1 | `SearchKeyword = "" Or Employee.FirstName Like ("%" + SearchKeyword + "%") Or Employee.LastName Like ("%" + SearchKeyword + "%")` (the two `Like` patterns each add a 1-character text before and after `SearchKeyword`; the nodes are not in the changed set) | Unchanged |
| 2 (new) | `SelectedDepartmentId = NullIdentifier() Or Employee.DepartmentId = SelectedDepartmentId` | New |

Result: the IsActive filter and the search on `SearchKeyword` are intact, and the department filter is a separate third condition, so it is combined with them by AND. With no department chosen the new condition is true, so no restriction applies. An employee with an empty `DepartmentId` fails the third condition once a department is chosen (the join is Left, so such an employee stays in the result when no department is chosen).

## Observations for the browser checks (not out of scope)
1. **Source order.** In both aggregates the Department source is now listed first and Employee second, with the join defined as Employee left, Department right. The graph shows the join type `Left` with Employee as the left source, which is "With or Without". How ODC orders the SQL for that combination is not visible in the graph. The browser check of 17 rows, and EmployeeId 8, 13 and 17 in Employee_Detail, will show if any employee drops out. All 20 employees have a department by the assignment table, so the browser cannot show a no-department employee unless one is created.
2. **`GetDepartments` is an element that prompt B did not name.** It is inside Employee_List and is the aggregate the dropdown needs. Reported so that it is not a surprise. It is not a model-wide change.
3. **Mentor's summary of task 5** (`result-screens.json`) is the source for which screens it said it changed. This comparison matches it: only Employee_List and Employee_Detail.
4. Whether `BootstrapData` ran on publish 2 is not visible in the graph (`app_logs` returned 0 entries). The browser check decides.
