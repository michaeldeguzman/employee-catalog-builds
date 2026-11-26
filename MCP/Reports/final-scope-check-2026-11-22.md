# Final scope check (task 13), 2026-11-22

Run at about 08:28 to 08:35 AEDT. Read-only: three tenant lookups on EmployeeCatalogMW and EmployeeCatalogMCP, plus file searches. No tenant write, no publish, no file written outside `MCP/`, and nothing changed in `requirements.md`, `spec.md`, the app or SDD Base.

## Result

| # | Check | Result |
|---|---|---|
| 1 | Only EmployeeCatalogMCP was touched, and EmployeeCatalogMW is unchanged | **Pass** (with one note on the lost first draft) |
| 2 | No files outside `MCP/` (`/tmp`, `Employee Catalog/MentorWeb`, skill folder) | **Pass** |
| 3 | SDD Base unchanged | **Pass** |
| 4 | Scratch copies in `MCP/Reports/scratch/` removed only with the user's agreement | **Not removed.** The user answered "No, keep all" |

## Reference times used

- `tasks.md` modification time is 2026-11-22 08:28:25. That is when task 13 was marked in progress, not when the plan was approved. Using it alone would search a window of about a minute, so it is not a useful reference.
- The approval time is not recorded. The earliest task execution in `tasks.meta.json` is task 2 at 05:35:17 (timestamp 1795286117183). The `MCP` folder itself was created at 05:07:10, and `requirements.md` was written at 05:11:08.
- The searches below use the broadest of these, **2026-11-22 05:07:00**, and for SDD Base also the literal `tasks.md` time and 05:35:17. Every search gave the same answer for every reference.

## 1. Only EmployeeCatalogMCP was touched

**Tenant writes found in `MCP/Prompts/` and the run facts**

| Write | Evidence | App key |
|---|---|---|
| Creation turn | `Prompts/001-create-app.md` names EmployeeCatalogMCP and the portfolio key xxxxxxxx-... only. `result-create.json` assetFacts: one asset | debb6b49-7b59-ecf6-b2eb-50a5f78250f3 |
| Part 1 data turn | `Prompts/002-part1-data.md`. `result-data.json` assetFacts: one asset. `session.md` records the asset reference | xxxxxxxx-... |
| Publish 1 (revision 1) | `Prompts/003-publish-part1.md` names xxxxxxxx-... . `result-publish-part1.json`: publicationKey xxxxxxxx-..., outcome success | xxxxxxxx-... |
| Part 2 screens turn | `Prompts/004-part2-screens.md`. `result-screens.json` assetFacts: one asset | xxxxxxxx-... |
| Publish 2 (revision 2) | `Prompts/005-publish-part2.md` names xxxxxxxx-... . `result-publish-part2.json`: publicationKey xxxxxxxx-... | xxxxxxxx-... |

`002` and `004` are the `build-prompt` output and carry no key in their text. The key went in the asset references, which `session.md` records and the saved runs' assetFacts confirm. Each saved run lists exactly one asset, xxxxxxxx-... .

**Note: a second key exists, for the lost first draft of the same app.** Incident P-1 (`Reports/interventions.md`): the first creation turn and part 1 turn ran in session 29f880cb-69a8-3d38-93d2-bd0c1a879024 on app_key ee94947f-4977-cf9d-8863-0aedede9b3d7. That draft was named EmployeeCatalogMCP, was never published, and was lost with the session. `app_info` for that key today returns 404 Not Found. So the writes carry two keys, but both are the EmployeeCatalogMCP draft, and neither is any other app.

**Other writes on xxxxxxxx-... that Kiro did not send.** Revision 3 (unplanned Studio publish U-1) and revision 4 (manual intervention M-1, screen `RunTimer`) were published by the user in ODC Studio. Both are on the same app and are logged in `interventions.md`.

**Tenant state now (read-only, 2026-11-22 about 08:30 AEDT)**

| App | Key | Latest revision | modelDigest | Baseline (task 4, `Reports/scope-baseline.md`) |
|---|---|---|---|---|
| EmployeeCatalogMW | 07a64c21-0c8c-8afb-28ee-5d8530d55cf8 | 6 (2026-11-21T10:56:49.208634Z) | 35873f58-1351-11c1-6d2d-9ad864ae3a67 | Revision 6, same time, same digest. **Unchanged** |
| EmployeeCatalogMCP | debb6b49-7b59-ecf6-b2eb-50a5f78250f3 | 4 (2026-11-21T21:01:27.066171Z) | 5def1eaa-a690-f49e-7637-346fb75e1366 | Revisions 1 and 2 by Kiro's publish turns, 3 and 4 by the user in Studio |
| Employee Catalog | 31b31b9c-c028-bfee-1811-c6b59aba4b5b | 6 (2026-11-11T01:38:32.753425Z) | e1900ddb-b47e-8abe-c19e-3fc3f31adcf5 | Revision 6 as recorded. The baseline did not record its digest |

`app_revisions` for EmployeeCatalogMW still lists six revisions (1 to 6), newest at 2026-11-21T10:56:49Z. No revision was added.

## 2. No files outside `MCP/`

| Location | Search | Finding |
|---|---|---|
| `/tmp` (symlink to `/private/tmp`) | files created or modified after 2026-11-22 05:07:00 | One file: `/private/tmp/android-user/.../opengl_log.txt`, modified 08:30:13 and still growing. It belongs to an Android emulator process, not to this project. Nothing else |
| `Employee Catalog/MentorWeb` (build A) | anything modified after 05:07:00 | None. The newest file is `.DS_Store` at 05:02:08, then `SDD-EmployeeCatalogMW.code-workspace` at 04:49:39, both before the `MCP` folder existed |
| Skill folder (`~/.kiro/powers/installed/outsystems` and `~/.kiro/powers/repos/outsystems`) | anything modified after 05:07:00, and `__pycache__` or `.pyc` | None. The newest file is dated 2026-11-21 17:53:01 (install time). No `__pycache__` or `.pyc` files |

Outside access: only read access to build A's `requirements.md` and BRD is allowed. A modification-time search cannot show reads, so reads are not checked here.

**Pre-existing files in `/tmp`, not from this plan.** `/private/tmp` holds `employee-catalog-requirements.before.md`, `employee-catalog-requirements.before2.md`, `employee-catalog-design.before.md`, `employee-catalog-design.before2.md`, `mentorweb.before.md` (all 2026-11-21 18:06 to 18:18) and a folder `graphdiff/` (`rev2.txt` to `rev6.txt`, `diff.py`, `flow.py`, `scope.py`, 2026-11-21 21:41 to 21:57). They are dated about 11 hours before the `MCP` folder was created, so they belong to build A and earlier work. They are not changes since the plan, and they were not touched. Kiro did not delete them, because they are outside `MCP/` and not part of this project.

## 3. SDD Base unchanged

- Files newer than `tasks.md` (08:28:25): none.
- Files newer than 05:35:17 and newer than 05:07:00: none.
- Newest file in SDD Base: `.kiro/steering/outsystems-ui.md` and `.kiro/steering/mentor-standards.md`, both 2026-11-21 17:56:45.
- Limit: SDD Base is not a git repository, so there is no hash comparison. The result rests on modification times.

## 4. Scratch copies

`MCP/Reports/scratch/` holds six files: `design.before.md`, `design.before2.md`, `requirements.original.md`, `spec.before2.md`, `tasks.before2.md`, `part1-data.rerun.md`. The user was asked whether to remove them and answered **No, keep all**. Nothing was deleted. `session.md` cites `part1-data.rerun.md` as evidence, which stays valid.

## Disagreements

- None between the app and `requirements.md` that are new here. The existing ones stay as logged: extra screen `RunTimer` (D-4), Email length 256 against 250 (D-3), and the Staff-role entity permission note (D-2, resolved).
