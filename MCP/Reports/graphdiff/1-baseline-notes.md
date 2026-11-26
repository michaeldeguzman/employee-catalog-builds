# Graph baseline: EmployeeCatalogMCP revision 1 (task 6)

Recorded 2026-11-22 (AEDT), after the publish of revision 1 (publication key 5f1513df-48de-9153-26e3-cac40540a1aa).

## Files

| File | What it is |
|---|---|
| `1.xre` | Full graph of EmployeeCatalogMCP revision 1 (app_key debb6b49-7b59-ecf6-b2eb-50a5f78250f3). One page, `has_more` false, header `revision` 1 = `latest_revision` 1 = the published revision. SHA-256 `d5a2ba46dfb7eda80c92dc0fc914d975d4f857c7db1599089f4187fe04605325`. 11,220 nodes, 20,628 edges. This is the BASELINE. |
| `reference/EmployeeCatalogMW-r6.xre` | Read-only copy of the graph of EmployeeCatalogMW revision 6, used only to compare the Login screen. Not part of any EmployeeCatalogMCP comparison. |
| `reference/EmployeeCatalog-xxxxxxxx-r6.xre` | Read-only copy of the graph of the app "Employee Catalog" (31b31b9c-c028-bfee-1811-c6b59aba4b5b) revision 6, used only for the same purpose. |

**Rule (user decision, 2026-11-22): everything in `reference/` is a read-only reference for checking only.** Never use anything from the EmployeeCatalogMW graph or the Employee Catalog graph in a Mentor prompt, in spec.md, or to decide what Mentor should build. Check result for the existing prompts in `MCP/Prompts/` (001, 002, 003): none uses content from these files; see `MCP/spec-driven-build/EmployeeCatalogMCP/session.md`.

The harness wrote each graph result outside MCP; each was copied here. No diff file exists: revision 1 is the first revision of EmployeeCatalogMCP.

## Owned elements in revision 1

| Element type | Count | Names |
|---|---|---|
| Entity | 1 | Employee |
| Entity attributes | 6 | Id, FirstName, LastName, Email, JobTitle, IsActive |
| Role | 1 | Staff (plus the generated role exception "Not Staff") |
| Server actions | 5 | BootstrapData, BootstrapEmployee (ours); SendChangeEmail, SendResetPasswordEmail, UpdateUser (template) |
| Timer | 1 | BootstrapTimer (Schedule WhenPublished, timeout 20 min, runs BootstrapData) |
| Screens | 6 | Login, RecoverPasswordRequest, RecoverPasswordReset, InvalidPermissions, UserProfile, ChangePassword (all template, all in flow Common) |
| Flows | 4 | Common, Emails, Layouts, MainFlow (MainFlow is empty) |
| Blocks | 8 | Layout, LayoutTopMenu, LayoutSideMenu, LayoutBlank, Menu, MenuIcon, ApplicationTitle, UserInfo (all template) |
| Static entity records owned | 0 | |

`Employee_List` and `Employee_Detail` do not exist yet, as expected before part 2. The Menu block has no link widget.

## Check b: bootstrap elements, role, Employee attributes

| Check | Result | Evidence |
|---|---|---|
| BootstrapTimer exists exactly once | Pass | 1 ITimer node, name BootstrapTimer, `Schedule: WhenPublished`, Action edge to BootstrapData. The companion action WakeBootstrapTimer appears once (under TimerActions). |
| BootstrapEmployee once, BootstrapData once | Pass | 1 IServerAction node each. BootstrapData has 1 call node, to BootstrapEmployee. |
| Staff is the only role | Pass | 1 IRole (Staff), 1 IRoleException (Not Staff). `context_roles` for the app returns total 1: Staff, key f9f3f634-4449-ffea-b5c8-bae77af37d07. |
| Employee attribute names and types | Pass | Id Long Integer (auto number, mandatory); FirstName, LastName, JobTitle Text; Email Email; IsActive Boolean. No other attributes. |
| FirstName length 50, LastName 50, JobTitle 100 | Pass | `Length` 50, 50, 100 in the graph. |
| Email length 250 | **Does not match** | The graph shows `Length: 256` for Email. The requirement and spec.md say 250. Mentor's summary said "Email 250". See finding F-1. |
| Staff View access to Employee | **Not present** | No permission or access element links Staff to Employee. Employee has no incoming edge from a role or permission. Mentor's summary said the same (D-2). |

## Findings

### F-1: Email length is 256, not 250

- Evidence: `IEntityAttribute` Email, `Length: 256`, DataType Email. In the two other apps read for comparison (EmployeeCatalogMW r6 and "Employee Catalog" r6, both built differently) the Email attribute also shows `Length: 256`, while their Text attributes show 200.
- Inference: the platform fixes the length of the Email data type at 256, so a length of 250 cannot be set through Mentor. This is not proven. The docs search (outsystems-docs, odc, synced 2026-10-28) returned no page on the Email length.
- Effect: the Glossary entry in requirements.md ("Email: Email, length 250") is not met as written. No AC tests the length. Not changed by Kiro; reported only.

### F-2: Login screen and the other five template screens carry a Staff permission, and Login now checks the Staff role

Evidence from the graph of revision 1:

- All 6 screens each have one `Permissions` child (IPermission) pointing to role Staff: Login, RecoverPasswordRequest, RecoverPasswordReset, InvalidPermissions, UserProfile, ChangePassword.
- Login, RecoverPasswordRequest, RecoverPasswordReset and InvalidPermissions have `AccessibleBy: True`. UserProfile and ChangePassword have `AccessibleBy: False`.
- The Login screen's client action `LoginOnClick` contains: DoLogin, then a call to `CheckStaffRole`, then an If "Has Role?". When the answer is no, it calls DoLogout and shows an error message. The graph's own comments on these nodes read "performs a secondary check for specific user roles before granting access to the application" and "Logs out users who lack the required roles to prevent unauthorized session persistence".
- `CheckStaffRole` is the generated check action of the role Staff (IRole Staff has CheckStaffRole, GrantStaffRole, RevokeStaffRole).
- The Mentor run result (`result-data.json`) lists only one screen as changed: Login (Modified). The other five screens are not listed.
- The task 5 summary says Mentor "renamed the template's default role to Staff".

Comparison with other apps (read-only): EmployeeCatalogMW r6 and "Employee Catalog" r6 have no `Check*Role` call and no IPermission on Login, RecoverPasswordRequest, RecoverPasswordReset or InvalidPermissions. They are not a clean reference: both were built from an older template version (different Login layout, "AnimatedLabel", IsExecuting variable, no UserProfile or ChangePassword screens) and edited by AppGenerator. The comparison therefore shows only that this Login differs from theirs, not what Mentor changed.

Inference (not proven; no copy of the unmodified template exists on the tenant):

- The `CheckStaffRole` call and the Staff permissions were most likely in the standard Web template under the template's default role name, and Mentor renamed the role. That explains why Login (the one screen that references the role's check action by name in its logic) shows as Modified, and why the five other screens carry the same permission without showing as modified.
- If that is right, Mentor changed the Login screen only through the role rename, and nothing else on Login.
- Consequence if the check is live at runtime: a user who signs in without the Staff role is logged out again by Login. The test user must have Staff (task 7) before any browser test.

Open: whether the permission and the check were in the template before Mentor touched it, or were added by Mentor, cannot be settled from the tenant. Settling it would need the template's unmodified Login, for example a new, unpublished template app. Not done.

### F-3: BootstrapEmployee seeds from one JSON text, not from 20 generated Create calls

- Evidence: BootstrapEmployee has an aggregate (GetEmployees), an If "GetEmployees.Count = 0?", a JSON Deserialize node (DeserializeEmployees), a For Each, and one CreateEmployee call inside it. The text literal that feeds the deserializer is 2,466 characters long with hash prefix `2e83c0b72a`.
- Evidence (check I ran on the repository file): compact JSON of the 20 records of spec.md section 10, keys in the order FirstName, LastName, JobTitle, Email, IsActive, in the order of the list, is 2,466 characters and its SHA-1 starts with `2e83c0b72aee805e...`. The graph's hash prefix matches. So the literal is, with very high probability, exactly the 20 records of the spec in spec.md order, values as given (3 with IsActive false: Hugo Brandt, Maya Petrov, Quinn Abara; Alice Anderson active).
- Deviation: constraint 7 of the prompt asks for "one generated Create<Entity> call per row". Mentor used a loop over a JSON literal. Neither this nor the data content is a failure. The graph shows what the action contains, not that it ran: task 8's manual check settles the stored rows.
- BootstrapEmployee assigns `Message = "BootstrapEmployee: inserted " + IntegerToText(DeserializeEmployees.Data.Length) + " rows"` (or "skipped, N present") to its output parameter. This confirms D-1 in the model: no log node in the action.

## Scope check against the intended content of publish 1

Intended: Employee, Staff, the bootstrap actions and BootstrapTimer, plus whatever the standard Web template carries.

- Outside the intended list, apart from the template: nothing found beyond the findings above. F-1 (Email length) and F-3 (JSON literal instead of 20 Create calls) are differences in how the intended elements were built. F-2 is a template-owned screen carrying a Staff permission and a role check.
- No screens other than the six template screens, no other entities, roles, timers or server actions, no static entities, no integrations.
- The template's other elements (themes, resources, site properties TenantId and TenantName, Layout and menu blocks, email templates ChangeEmail and ResetPassword, validation messages) are the standard template and are part of this baseline.

## For the task 10 comparison

Compare the revision 2 graph with `1.xre`. Ignore the order of nodes. Intended differences: two new screens, their menu links, their role permissions and, if part 2 adds it, Staff View access to Employee. Anything changed in Employee attributes, the Staff role, `Bootstrap*` elements or the six template screens is out of scope, including the Login screen.
