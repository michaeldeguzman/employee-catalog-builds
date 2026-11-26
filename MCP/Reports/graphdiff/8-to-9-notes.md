# Graph comparison: EmployeeCatalogMCP revision 8 -> revision 9 (not part of add-department)
Recorded 2026-11-22 during task 9 of `MCP/.kiro/specs/add-department/tasks.md`. Read-only on the tenant: `app_revisions`, `env_app`, `app_logs`, `context_graph`. App key debb6b49-7b59-ecf6-b2eb-50a5f78250f3 (Development).

Revision 9 was not published by Kiro and is not in any earlier record (`interventions.md`, `session.md`, the add-department result files). It was found because `app_revisions` showed a revision newer than 8. This comparison was made to say what it changed.

## Files
| File | What it is |
|---|---|
| `9.xre` | Whole-app graph of revision 9, no `root`. One page: `has_more` false, header `revision` 9 = `latest_revision` 9 = latest in `app_revisions` (9, 2026-11-22T01:00:56.020536Z, modelDigest 89f31b38-ca52-171c-3a27-ebd1d86c934b) = deployed revision in `env_app` (build key 2218804b-eaea-362d-5ece-8f0407f005c9). 11,914 nodes, 22,065 edges. SHA-256 `a50ceb4684487ee01a92684449e462e8d3d8f78beb4d6bce12679be48fac9fc3`. Copied from the harness tool-output file. |
| `8.xre` | Previous revision, unchanged. SHA-256 `c1a71163418c2d1129696e8672804b0de62b4eee864f544f32d238e84fd1403a` (same as in `7-to-8-notes.md`). |
| `8-to-9.diff` | Semantic diff, same method as `7-to-8.diff` (nodes by `_key`; edges by source, target and attributes without `index`; sibling index changes on their own lines). Made with a throwaway Python script run from stdin. No script was saved. Edges are compared as a set, so one duplicate edge in each file is collapsed (22,040 and 22,064 unique edges against 22,041 and 22,065 in the headers). |

## Result
Nodes 11,900 -> 11,914: 14 added, 0 removed, 3 changed. Edges: 24 added, 0 removed, 0 sibling index changes.

- **Added (all inside the screen `RunTimer`):** a client screen action `RunEmployeeDeptOnClick` with only a Start node and an End node, one Start to End connector, and no call to any action. A Button widget (text "Run Employee Dept") inside the screen, whose On Click destination is `RunEmployeeDeptOnClick`.
- **Changed (metadata only):** the module `EmployeeCatalogMCP` (`LastModifiedByTool` AgentExperience -> ODCStudio), the flow `MainFlow` (same tool marker, `LastModifiedDate` 2026-11-21T21:00:28 -> 2026-11-22T00:58:45) and the screen `RunTimer` (`LastModifiedDate` 21:00:52 -> 2026-11-22T00:59:05).
- **Not changed:** the data model (Employee, Department, DepartmentId, the 4 records), `BootstrapData`, `BootstrapEmployee`, `BootstrapTimer`, the Staff role, the menu, `Employee_List`, `Employee_Detail`, every other screen. The two literal hashes are the same as in revision 5 (update `ce1312410b`, 1,256 characters; seed `808c85070a`, 2,806 characters).
- **Who:** the nodes carry the same user name as the user's own Studio work (`developer@example.com`) and the tool marker ODCStudio. The log shows the publish at 2026-11-22T01:00:56Z (12:00:56 AEDT). No Mentor prompt was sent by Kiro for it. By these markers it is a Studio publish by the user. Earlier Studio publishes by the user: U-1 (revision 3), M-1 (revision 4) and U-2 (revision 6). The user has not confirmed this one.
- **Effect:** the new button runs an action that does nothing. It does not call `BootstrapData`. The existing button (`RunTimerOnClick`, calls `BootstrapData`) is unchanged. The purpose of the new button is not stated in any record.

## Out of scope for add-department
The whole change is out of the scope of add-department (a new button and action on RunTimer). It was not made by this change, so it is reported, not judged against design.md. `RunTimer` is already deviation D-4 (extra screen). The new button adds to D-4.
