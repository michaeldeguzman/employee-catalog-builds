# Graph comparison: EmployeeCatalogMCP revision 5 -> revision 7 (add-department, intervention I-1)
Recorded 2026-11-22 after the I-1 publish (publication key 027d5b64-ff46-b1b9-b0c5-af6eaa7c5070). Read-only on the tenant: `app_revisions`, `context_graph`. App key debb6b49-7b59-ecf6-b2eb-50a5f78250f3 (Development).

## Why 7 and not 6
The task text and the user's message expected the publish to be revision 6. It is revision 7. Revision 6 was published by someone else (Developer, 2026-11-21T22:49:05.120546Z, modelDigest 9ef82f58-8fa3-5e6a-05c0-b98ebc173514) between publish 1 (revision 5, 22:40:02Z) and the I-1 publish. Mentor's publish turn merged it automatically (event `publishAutoMerged`, mergedRevision 6) and then published revision 7 (modelDigest 9bfe03ed-2029-7222-1490-579d50506088, 22:56:22Z). The graph service serves only the newest revision, so revision 6 was never read on its own and there is no `6.xre`. The file is named by its revision: `7.xre`. The comparison is 5 -> 7, which covers both the I-1 change and whatever revision 6 added.

## Files
| File | What it is |
|---|---|
| `7.xre` | Whole-app graph of revision 7, no `root`. One page: `has_more` false, header `revision` 7 = `latest_revision` 7 = the revision of the publish run and of `app_revisions`. 11,778 nodes, 21,778 edges. SHA-256 `99250cf08122d67a2e40b9daaecf5ddf907f2dacd76ade3ec57368ccb3c911fd`. Copied from the harness tool-output file. |
| `5.xre` | Baseline, unchanged. SHA-256 `399de5339975e6d7b6d07497a1938f689b4738d05e185b1498e02c703c5feb99`. |
| `5-to-7.diff` | Semantic diff, same method as `4-to-5.diff` (nodes by `_key`; edges by source, target and attributes without `index`; sibling index changes on their own lines). Made with a throwaway Python script run from stdin. No script was saved. |

## Result
Nodes 11,778 -> 11,778: 0 added, 0 removed, 7 changed. Edges 21,778 -> 21,778: 0 added, 0 removed, 0 with a changed sibling index.

| Changed node | Fields that differ | Origin |
|---|---|---|
| Static entity records, 4 nodes (keys ending 4YLXTL..., MdChtT..., wraUxf..., yt6x0g...) | `DisplayName` and `Identifier` (the record name), `LastModifiedDate` | I-1, intended |
| `BootstrapData` (IServerAction) | `LastModifiedByTool` AgentExperience -> ODCStudio, `ModifiedByTools` AgentExperience -> "ODCStudio, AgentExperience", `LastModifiedDate` 2026-11-21T22:33:53 -> 22:44:54 | Revision 6 (Studio), outside I-1 |
| `UpdateEmployee` call node in `BootstrapData` | X 6742 -> 5029, Y 13211 -> 11429 | Revision 6 (Studio), layout only |
| For Each node in `BootstrapData` (the first For Each, key ...mSJq_K3yIDoFeP71qjZcob) | X 4969 -> 5029, Y 7892 -> 8000 | Revision 6 (Studio), layout only |

No flow connection, no element and no value of `BootstrapData` changed. The attribution to revision 6 is by the Studio marker and the 22:44:54 date (before revision 6 at 22:49:05Z and before the I-1 turn). Revision 6 itself was not readable.

## Department records
| Position (index in the graph) | Record name, revision 5 | Record name, revision 7 | Id | Label (SHA-1 prefix, length) |
|---|---|---|---|---|
| 0 | Finance | Engineering | 1 | Engineering (4143d04801, 11) |
| 1 | HumanResources | Finance | 2 | Finance (1b48d3f014, 7) |
| 2 | Engineering | Sales | 4 | Sales (d0edfb6e8c, 5) |
| 3 | Sales | HumanResources | 3 | Human Resources (9b864cbc52, 15) |

- **Names now match Labels.** Every record name is its Label (Human Resources without the space, as asked).
- **Ids and Labels unchanged.** The Id values and the Label hashes and lengths are identical in 5.xre and 7.xre.
- **Order not changed.** The prompt asked to order the records by Id, which means position 2 is Id 3 and position 3 is Id 4. The graph shows no sibling index change: the `Records` edges are the same, so the position of each record node is the same. The positions still read Id 1, 2, 4, 3 (Engineering, Finance, Sales, Human Resources). Mentor's summary said the records "appear in this order", and its own pending-changes list shows only four Modified elements, with no move. What changed is the name carried by each of the four nodes, not their position. Whether ODC orders a static entity's records by position or by Id for the dropdown is not known from the graph.

## Checks asked for
| Check | Result |
|---|---|
| Only the Department record names and order change | The record names changed (4 nodes). The order did not. Three more nodes changed in `BootstrapData` (tool marker, date, two layout positions), from revision 6 |
| Ids and Labels unchanged | Yes, see above |
| Seed hash unchanged | Yes: `BootstrapEmployee` literal 2,806 characters, `808c85070a`, in 5.xre and 7.xre |
| Update hash unchanged | Yes: `BootstrapData` literal 1,256 characters, `ce1312410b`, in 5.xre and 7.xre |
| Employee, `DepartmentId`, `DepartmentSeed`, screens, roles, timers | No node or edge differs (0 nodes added or removed, 0 edges differ) |
| Static entity Department attributes | Not in the changed set: Id (Integer) and Label (Text 50) as in revision 5 |
