# Design Document

## Overview

This design describes how Kiro builds EmployeeCatalogMCP through the OutSystems MCP with the Power's outsystems-spec-driven-build skill (a Beta Feature; Kiro tells the user so and links the Beta agreement the first time it uses the skill). The input is `requirements.md` in this folder. The output is a published Reactive Web app on the ODC tenant, a build report, and a check report against AC-01 to AC-06.

Nothing in this design touches the tenant. All tenant writes happen later, one at a time, each after the user confirms.

### Sources used

- `requirements.md` (this folder): the source of truth.
- SKILL.md of outsystems-spec-driven-build v1.5.0 and its `scripts/build.py` guardrail text, and SKILL.md of the main outsystems skill.
- SDD Base `mentor-standards.md` (cached 2026-09-04) and `Mentor-Requirement-Doc-Standards.md`. These are written for Mentor Web BRD upload. Only the UI pattern vocabulary applies here. `AI-Agent-Enhancement.md` does not apply because no AI agent is in scope.
- outsystems-docs MCP, source "odc". `last_updated` returned 2026-10-28T09:05:12Z, the same sync as the Research notes in `requirements.md`. The docs were searched again for this design. They confirm that Mentor Studio and the MCP path document prompts for filtering an aggregate, creating an entity with attribute lengths, adding and deleting roles, and creating a Timer that runs when the app is published (sources: `eap/building-apps/data/fetch-data/filter-results.md`, `eap/building-apps/data/modeling/entity-create.md`, `eap/agentic-development/mentor-web/prompts.md` (Authorization prompts), `eap/building-apps/timers/timer-create-run.md`). The Research notes in `requirements.md` were written for Mentor Web. The build here uses the Mentor session of the OutSystems MCP, so the Research flags are treated as risk indicators, not as facts about this path.

## Build flow

The numbers are the skill's own steps. Kiro confirms with the user before every item marked **[confirm]**.

0. **Save every prompt.** Each Mentor prompt Kiro sends is first written to `MCP/Prompts/` as one file, named `NNN-<short-name>.md` (for example `001-create-app.md`, `002-part1-data.md`). The file holds the exact text sent.

1. **Convert requirements.md to spec.md (skill Step 1, Mode A).** Kiro writes `MCP/spec-driven-build/EmployeeCatalogMCP/spec.md` in the skill's template (`templates/spec-template.md`, sections 1 to 10) from `requirements.md`. Section 9 holds AC-01 to AC-06 word for word, and every Text length is kept. The section-by-section mapping is in "spec.md content". spec.md is generated, never hand-edited.

2. **validate-spec (Step 2).** `python3 "<skill>/scripts/build.py" validate-spec --spec ".../spec.md"`. Errors must be zero. Warnings are shown to the user.

3. **Show the spec and ask for the go/no-go (Step 3) [confirm].** Kiro runs `show-spec`, displays it, and asks whether to fire Mentor. The question names the target app, says a new Web app is created from the standard template, and says the build runs in two parts with a publish after each.

4. **Create the app from the standard Web template (Step 4) [confirm].**
   - Kiro first searches the tenant's apps for the exact name EmployeeCatalogMCP. If it exists, Kiro stops and asks. It never touches EmployeeCatalogMW or any other app, and picks a search result only when the name matches exactly.
   - Kiro states the portfolio and asks the user to confirm it. It never guesses one.
   - After confirmation, one Mentor session is opened and the creation is sent as a turn of its own: create a new Web application named EmployeeCatalogMCP in the named portfolio from the standard Web application template, and do nothing else. Kiro polls it to terminal and keeps `app_key` from the run's per-app facts. A new app is listed only after its first publish, so a lost key is never answered by creating the app again; Kiro asks the user to check ODC Studio.

5. **Mentor part 1: data model and sample data bootstrap (Step 5).** Kiro sends the output of `build-prompt --part data` unchanged, in the same session, with `app_key` in the asset references. The prompt carries spec sections 1, 2, 3, 6, 8, 9 and 10 and the skill's data guardrails: data only, exact attribute types, roles by exact name, Timer-based bootstrap, no duplicates, do not publish. Kiro polls to terminal, saves `result-data.json`, renders the report, and checks that Mentor did not publish on its own. If the turn did not land, one fix turn is allowed.

6. **Publish part 1 [confirm].** Kiro restates "publish the data model of EmployeeCatalogMCP to its development environment", then sends a publish turn with a short note and reads the outcome from the run. It never publishes again while the outcome is unknown.

7. **Sample data check (skill Step 5, item 5).** `BootstrapTimer` runs after the publish. Kiro reads `app_logs` for "Bootstrap", only lines written after the publish finished, and expects `BootstrapEmployee: inserted 20 rows`. If the line is missing or shows an error, Kiro does not start part 2. It sends the skill's one fix turn (ending with "Never create a second Bootstrap<Entity>, BootstrapData or BootstrapTimer. Do NOT publish the app in this turn."), then asks for confirmation to publish it. This check only counts rows. The IsActive values and Alice are checked in the final check (see AC-06 below).

8. **Mentor part 2: screens and access (Step 6).** After the part 1 publish, Kiro sends `build-prompt --part screens` unchanged in the same session. Guardrails: role per screen exactly as in section 4, OutSystems UI, out-of-scope respected, build on the data part without changing bootstrap, mandatory inputs, tables bound to aggregates, do not publish. Same handling as part 1.

9. **Publish part 2 [confirm].** Same rules as item 6.

10. **The skill's checks and build report (Steps 7 and 8).** Kiro takes the runtime URL from the environment's app info, compares each screen's roles with section 4 using the screens and roles lookups, releases the session, and writes `build-report.md` in the working folder. The skill's report to the user states revision numbers, what was built, what Mentor added or skipped, and that `BootstrapTimer` refills empty sample-data tables on every publish, deployment and automatic patch.

11. **Check against the requirements.** Kiro compares the published app with `requirements.md` for each AC and writes `MCP/Reports/check-<revision>-<yyyy-mm-dd>.md`. The report lists each deviation. It does not change the app or `requirements.md`.

Working files stay in `MCP/spec-driven-build/EmployeeCatalogMCP/`: `spec.md`, `result-data.json`, `result-screens.json`, one `result-*-fix.json` per fix turn, and `build-report.md`.

### Verification after every publish

`context_graph` returns only the latest revision's graph, and it has no revision argument. The previous revision therefore cannot be read after the next publish. Kiro saves the full graph of each published revision, so the next publish has something to compare with.

- After each publish Kiro reads the whole-app graph (no `root`, because `@DataModel` and `@ScreenModel` as `root` are refused), follows `next_cursor` until `has_more` is false, checks that the header `revision` equals the revision just published, and saves the pages to `MCP/Reports/graphdiff/<revision>.xre`. Codes such as `graph_pending` are retried as the tool description says, one call at a time.
- The comparison is a full diff of the new file against the previous revision's file, saved as `MCP/Reports/graphdiff/<previous>-to-<new>.diff`. The first publish has no previous revision, so it is recorded as the baseline.
- Kiro reports every difference outside the intended scope for that publish:
  - Publish 1 (baseline): Employee, Staff, the bootstrap actions and `BootstrapTimer`, plus whatever the standard Web template carries.
  - Publish 2: only the Employee_List and Employee_Detail screens, their menu entries, their role assignments and the Staff access to Employee. Any change to Employee attributes, roles, or `Bootstrap*` elements is out of scope.
  - A fix publish: only the element the fix names.
- Any file written by the harness outside MCP when a result is too large is copied into MCP; Kiro writes nothing itself to `/tmp` or any folder outside MCP.

## spec.md content

| spec.md section | Content, derived only from requirements.md |
|---|---|
| 1 Overview | Purpose and target users from the Introduction and the Staff glossary entry. Target app: `EmployeeCatalogMCP (new)`. Style direction: Apply OutSystems UI defaults. |
| 2 Roles | One role, **Staff**: view-only access to Employee, no create, edit or delete. No other role is listed. |
| 3 Data model | Entity **Employee**: Id (implicit primary key), FirstName (Text, 50), LastName (Text, 50), Email (Email, 250), JobTitle (Text, 100), IsActive (Boolean). Relationships: none, single entity. Static enums: none. Mandatory flags are not set, because the requirements do not state them. |
| 4 Screens + RBAC | Employee_List (Staff), Employee_Detail (Staff). No Login row: the sign-in screen is the platform's, not a requirement. |
| 5 Server actions | "None. Screens read data with aggregates. The only actions are the bootstrap actions the skill adds for AC-06." This stops Mentor from deriving actions from the screens. |
| 6 Integrations | "None." |
| 7 UI/UX direction | Omitted (optional). The requirements state no theme, layout or responsive rule. |
| 8 Out of scope | The six items of the requirements' Out of scope list, word for word, plus two restatements of the Glossary: no role other than Staff ("The only role") and no Employee attribute other than the five listed. |
| 9 Acceptance criteria | AC-01 to AC-06 verbatim, unchanged. |
| 10 Notes for Mentor | Directives that restate the criteria so the guardrails and the spec agree: (a) Employee_List is a Table with the columns FirstName, LastName, JobTitle, Email. (b) The table shows only Employee records where IsActive is True. (c) The search input matches FirstName or LastName only, never JobTitle or Email. (d) Employee_Detail displays the five attributes read-only, with no edit, create or delete widget anywhere. (e) Do not use the keywords "Master detail" or "List with popup", because these patterns add editing (SDD Base `mentor-standards.md`). (f) Sample data is 20 made-up employees, at least 2 with IsActive False, one active employee with FirstName Alice, no real person. |

The notes add no requirement. Each one restates AC-01 to AC-06 or the Glossary.

## Expected result

**Data model** (local entity, Reactive Web app):

| Attribute | Type | Length |
|---|---|---|
| Id | Long Integer, primary key, automatic | not applicable |
| FirstName | Text | 50 |
| LastName | Text | 50 |
| Email | Email | 250 |
| JobTitle | Text | 100 |
| IsActive | Boolean | not applicable |

**Role and access:** one role, Staff, with View access to Employee and nothing else. No Admin or other role. Both screens require Staff.

**Screens:**

- **Employee_List**: a Table of Active_Employee records with columns FirstName, LastName, JobTitle, Email, one row per active employee, and a search input that matches FirstName or LastName. Opening a row navigates to Employee_Detail.
- **Employee_Detail**: shows FirstName, LastName, Email, JobTitle and IsActive of the selected employee, read-only.

**Sample data:** 20 made-up Employee records created by `BootstrapEmployee`, called by `BootstrapData`, run by `BootstrapTimer` when the app is published. At least 2 records have IsActive False. One active record has FirstName Alice. No record is a real person.

**Elements allowed beyond the requirements** (nothing else): `BootstrapEmployee`, `BootstrapData`, `BootstrapTimer` (required by the skill to meet AC-06), the template's own login and layout, and the menu entries of the two screens. There are no other server actions, timers or screens.

## Traceability

| AC | Design element | How Kiro verifies it |
|---|---|---|
| AC-01 list loads | Employee_List table, columns FirstName, LastName, JobTitle, Email | `context_screens` for the screen and its role. In the browser, a Staff user sees the four columns and one row per active employee. |
| AC-02 search | Search input on Employee_List, matching FirstName or LastName | In the browser, search "Alice": only matching rows. Then search a term that occurs only in a JobTitle or Email: no rows. |
| AC-03 inactive hidden | Aggregate filter IsActive = True | Visible rows equal 20 minus the number of inactive records. No inactive person appears. |
| AC-04 detail | Employee_Detail, five attributes, read-only | In the browser, open a row: five values shown, no edit control. |
| AC-05 empty search | Same search as AC-02 | In the browser, search a text that matches nothing: no rows. |
| AC-06 sample data | `BootstrapEmployee`, `BootstrapData`, `BootstrapTimer` | `app_logs` shows `BootstrapEmployee: inserted 20 rows`. The table shows Alice. With 20 records seeded, at most 18 visible rows proves at least 2 inactive. If the table paginates, Kiro adds up the pages. A data view in ODC Studio or the ODC Portal settles the exact count. Kiro reads the names for fictional status. |

A Staff user is needed for the browser checks. Assigning the Staff role to a test user is done by the user in the ODC Portal. It is not part of the build.

## Expected gaps after generation

The guardrails are the ones in `build.py`. "Prevented?" is Kiro's expectation from reading them, not a result. Each fallback is a single Mentor prompt, sent in its own Mentor session on EmployeeCatalogMCP (`app_key` in the asset references), one at a time, and ends with "Do NOT publish the app in this turn."

| # | Possible gap | Basis | Prevented by the skill's guardrails? | Smallest fallback prompt |
|---|---|---|---|---|
| 1 | Search matches more than FirstName and LastName (for example JobTitle or Email) | Research Q2 (search inputs need manual configuration); build A | **No.** No guardrail covers search logic. Only spec note (c) helps. | "In the Employee_List screen, change the aggregate filter that uses the search input so that it matches the search text only against Employee.FirstName and Employee.LastName, with the match the search already uses. Remove any condition on other attributes. Change nothing else." |
| 2 | The list shows inactive employees (no IsActive filter) | Research Q2 (no documented Boolean filter on list for Mentor Web); build A | **No.** `BIND_TO_AGGREGATES` only requires an aggregate. Spec note (b) and AC-03 help. | "In the aggregate that feeds the table on Employee_List, add a filter so that it returns only employees whose IsActive is True. Change nothing else." |
| 3 | Sample data does not match AC-06 (not 20, fewer than 2 inactive, no active Alice) | Research Q1 (counts and IsActive values not documented as followed); build A | **Partly.** `BOOTSTRAP` forces a seeding Timer and the part 1 check proves the row count. Nothing checks IsActive values or Alice. Because the action skips a table that already has rows, wrong rows stay after a fix publish unless the fix replaces them. | "Change BootstrapEmployee so that when the Employee table does not hold exactly 20 records with at least 2 whose IsActive is False and one active employee with FirstName Alice, it deletes all Employee records and inserts 20 made-up employees that meet this. Otherwise it still skips. Keep the log lines. Do not create another Bootstrap action or Timer." |
| 4 | Wrong Text lengths | build A | **Partly.** `EXACT_TYPES` covers data types, not lengths. The spec states every length. | "In the Employee entity, set the length of [only the attributes found wrong, each with its value from this list: FirstName 50, LastName 50, JobTitle 100, Email 250]. Change nothing else." |
| 5 | An extra role such as Admin | build A | **Mostly.** `ROLES` creates the listed roles by exact name. Section 8 lists "no role other than Staff", which `OUT_OF_SCOPE` enforces. Neither says "only". | "Delete the role [name] from the app and remove every use of it in screen access and entity permissions. Change nothing else." (Deleting a role is a documented Mentor prompt.) |
| 6 | Staff has edit or create rights on Employee, or the screens offer create, edit or delete | build A | **No.** `ROLE_PER_SCREEN` covers who opens a screen, not the entity access level. Only the spec text (section 2 and note (d)) helps. | "Set the access of the Staff role to the Employee entity to View only: no create, update or delete. Remove any create, edit or delete button, action or screen for Employee. Change nothing else." |
| 7a | An extra screen (including one from the template) | build A | **Mostly.** `OUT_OF_SCOPE` applies section 8, which lists every screen other than the two. It does not control the screens the standard template carries. | "Delete the screen [name] and its menu entry. It is not Employee_List or Employee_Detail. Change nothing else." |
| 7b | An extra Employee attribute | build A | **Partly.** Section 8 restates the five attributes, but no guardrail forbids extra ones. Id is expected and not a deviation. | "Delete the attribute [name] from the Employee entity and remove every use of it. Change nothing else." |

If a fallback prompt does not land, the skill's rule applies: one fix turn per part, then stop and report. A Mentor reply that only gives a plan counts as not landed.

## Interventions

- Every fallback prompt sent after the first build is an intervention, whether it fixes a gap in the table above or something else.
- Each intervention is logged in `MCP/Reports/interventions.md` with: number, date, the gap or finding, the exact prompt (also saved as its own file in `MCP/Prompts/`), `sessionId`, `runId`, whether it landed, the publish revision, and the graph comparison result.
- Before each intervention Kiro shows the user the exact prompt and waits for confirmation. It confirms again before the publish that follows.
- After the publish, Kiro runs the verification above and reports any change outside the intervention's scope.
- Manual work in ODC Studio is a last resort, used only when a Mentor prompt has been tried and did not land. It is logged in the same file as a manual intervention: what was changed, why Mentor could not do it, and the graph comparison result of the next publish.
- Neither `requirements.md` nor the app is changed to hide a deviation. If the app and the requirements disagree after the interventions, the check report says so.

## Decisions for the user

1. **Portfolio** for the new app. Kiro asks at the app creation step and does not guess.
2. **Sample records:** the spec states AC-06 as written and leaves the 20 records to Mentor, which keeps the requirements identical to build A. Listing 20 records would make AC-06 deterministic but changes the shared requirements.
3. **Interventions log location:** `MCP/Reports/interventions.md` and the `MCP/Prompts/NNN-<short-name>.md` naming are Kiro's proposal. They are not in `mcp.md`.
4. **Template screens:** the screens of the standard Web template are known only after the app exists. Gap 7a covers anything beyond Employee_List and Employee_Detail that Kiro finds.
