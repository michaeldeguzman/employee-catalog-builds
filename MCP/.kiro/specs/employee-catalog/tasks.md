# Implementation Plan

## Standing rules for every task

- Tasks run in order. None starts until the user approves this plan.
- **[CONFIRM]** marks a point where Kiro states the exact action and waits for the user's explicit yes. Every tenant write and every publish is one. The skill's go/no-go in task 3 covers the Mentor build turns only, not creation or publishes.
- Before Kiro sends any Mentor prompt, it saves the exact text as `MCP/Prompts/NNN-<short-name>.md`.
- After every publish, Kiro runs the graph verification from design.md ("Verification after every publish") and reports any change outside the intended scope.
- Kiro works only on EmployeeCatalogMCP. It never touches EmployeeCatalogMW or any other app.
- Every new file goes in `MCP/`. SDD Base is read-only.
- A fix turn (one Mentor prompt) is sent only after the user confirms the exact prompt. Any fix after the first build is logged in `MCP/Reports/interventions.md`.
- There are no test-writing tasks in this plan.

## Tasks

- [x] 1. Convert requirements.md to spec.md (flow step 1, Mode A)
  - Read the skill's `templates/spec-template.md`. Write `MCP/spec-driven-build/EmployeeCatalogMCP/spec.md` section by section as mapped in design.md "spec.md content".
  - Section 9 holds AC-01 to AC-06 verbatim. Every Text length is kept: FirstName 50, LastName 50, JobTitle 100, Email 250.
  - Read build A's BRD (`Employee Catalog/MentorWeb/BRD/EmployeeCatalogMW-BRD.md`) for this one purpose. Copy its 20 records (names, job titles, emails, IsActive) into section 10 exactly. Run the checks in design.md "Sample data". If a check fails, stop and tell the user.
  - Section 10 notes restate `requirements.md` only, apart from one pattern note (no "Master detail" or "List with popup") that comes from the SDD Base mentor-standards file. Section 8 adds only "Any role other than Staff" to the requirements' own Out of scope list.
  - Do not change `requirements.md`. Do not hand-edit spec.md afterwards.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 2. Run validate-spec (flow step 2)
  - Run `python3 "<skill>/scripts/build.py" validate-spec --spec "MCP/spec-driven-build/EmployeeCatalogMCP/spec.md"`.
  - Errors must be zero. Show any warnings to the user. If spec.md needs a change, regenerate it from task 1. Do not edit it by hand.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 3. Show the spec and get the go/no-go (flow step 3)
  - Run `show-spec` and display the full spec.md to the user.
  - **[CONFIRM]** Ask "Ready to fire Mentor with this spec?" The question names a new Web app EmployeeCatalogMCP, created from the standard template in the EmployeeCatalogMW portfolio, built in two parts with a publish after each. Wait for an explicit yes.
  - Tell the user the skill is a Beta Feature and link <https://www.outsystems.com/legal/beta-features-agreement>.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 4. Create the app from the standard Web template (flow step 4)
  - Search the tenant's apps for the exact name EmployeeCatalogMCP. If it exists, stop and ask. Pick a result only on an exact name match.
  - Read the portfolio of EmployeeCatalogMW from the app listing or app info (read-only). Also record EmployeeCatalogMW's latest revision, for the scope check in task 13. State the portfolio name and key.
  - **[CONFIRM]** Restate: "create a new Web app named EmployeeCatalogMCP in portfolio <name> from the standard Web application template". Wait for an explicit yes.
  - Open one Mentor session and send the creation turn: create the app and do nothing else. Poll to terminal. Keep `app_key` and the `sessionId`.
  - If the turn fails, read the run's per-app facts before doing anything else. Never create the app a second time. If the key is lost, ask the user to check ODC Studio.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 5. Mentor part 1: data model and sample data bootstrap (flow step 5)
  - Run `build-prompt --part data`. Save it to `MCP/Prompts/`. Send it unchanged in the same session, with `app_key` in the asset references.
  - Poll to terminal. Save `result-data.json` and render the report. Check that Mentor did not publish on its own. If it did, tell the user and follow that publish to its outcome.
  - Check the result: Employee has the five attributes with the lengths above, Staff is the only role, `BootstrapEmployee`, `BootstrapData` and `BootstrapTimer` exist once each, and nothing else was added.
  - If the turn did not land: **[CONFIRM]** the exact fix prompt, then send one fix turn. If that does not land either, stop and report the Landed lines and the `sessionId`.
  - _Requirements: AC-06_

- [x] 6. Publish part 1 (flow step 6)
  - **[CONFIRM]** Restate "publish the data model of EmployeeCatalogMCP to its development environment". Wait for an explicit yes.
  - Send the publish turn with a short note. Read the outcome from the run. If the outcome is unknown, check by publication key or revision history. Never publish again while it is unknown.
  - Run the graph verification. Save the graph of this revision as the baseline in `MCP/Reports/graphdiff/`.
  - _Requirements: AC-06_

- [x] 7. User task: give the test user the Staff role
  - **For the user.** Kiro does not do this.
  - In the ODC Portal, give the same test user as build A the Staff role for EmployeeCatalogMCP. The Staff role exists after task 6.
  - **Kiro tells the user as soon as the Staff role exists on the tenant.** Right after the task 6 publish succeeds, Kiro checks with the roles lookup for EmployeeCatalogMCP (read-only) and sends the user a message that Staff is there and can be assigned. Kiro does this before starting task 8.
  - This is setup, not an intervention. It is not logged in `interventions.md`.
  - Must be done before task 12. It can be done while tasks 8 to 11 run.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05_

- [x] 8. Sample data check (flow step 7)
  - Do not open ODC Studio. Check `app_logs` for EmployeeCatalogMCP (development stage), only lines written after the revision 1 publish finished, for any error or warning from `BootstrapTimer`, `BootstrapData` or `BootstrapEmployee`. Report what is found, including if nothing is found. `BootstrapEmployee` writes no "inserted N rows" log line (deviation D-1, see `MCP/Reports/interventions.md`), so an empty result is not proof that the data was inserted.
  - The manual data check moves to after task 10, in the browser, together with AC-06 in task 12: 20 rows, Hugo Brandt, Maya Petrov and Quinn Abara inactive, Alice active, values matching spec.md section 10. The user does not report back before task 9.
  - If `app_logs` shows an error or warning from the bootstrap elements, do not start task 9. Check whether `BootstrapData` exists, then **[CONFIRM]** the exact fix prompt (it must end with "Never create a second Bootstrap<Entity>, BootstrapData or BootstrapTimer. Do NOT publish the app in this turn."). Send one fix turn, save `result-seed-fix.json`, then **[CONFIRM]** the publish of the fix, publish it, run the graph verification, and check `app_logs` again.
  - _Requirements: AC-06_

- [x] 9. Mentor part 2: screens and access (flow step 8)
  - Run `build-prompt --part screens`. Save it to `MCP/Prompts/`. Send it unchanged in the same session.
  - Poll to terminal. Save `result-screens.json` and render the report with every build and fix turn so far. Check that Mentor did not publish on its own.
  - Check the result: only Employee_List and Employee_Detail were created, both require Staff, Staff has View access to Employee only, and the bootstrap elements were not changed.
  - If the turn did not land: **[CONFIRM]** the exact fix prompt, then send one fix turn. If that does not land either, stop and report.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05_

- [x] 10. Publish part 2 (flow step 9)
  - **[CONFIRM]** Restate "publish the screens of EmployeeCatalogMCP to its development environment". Wait for an explicit yes.
  - Send the publish turn. Read the outcome from the run. Same rules as task 6.
  - Run the graph verification and compare with the task 6 baseline. Intended scope: the two screens, their menu entries, their role assignments and Staff access to Employee. Report every other change.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05_

- [x] 11. The skill's checks and build report (flow step 10)
  - Get the runtime URL from the environment's app info and give it to the user as a link.
  - Compare each screen's roles with spec.md section 4 using the screens and roles lookups.
  - Write `build-report.md` in `MCP/spec-driven-build/EmployeeCatalogMCP/`. Release the Mentor session now that its work is published.
  - Report to the user: app name, `app_key`, each publish revision, what was built, anything Mentor skipped or added, the checks, and that `BootstrapTimer` refills empty sample-data tables on every publish, deployment and automatic patch.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 12. Check the app against the requirements (flow step 11)
  - Needs task 7 done. Kiro cannot sign in as the test user, so Kiro gives the user a checklist and the user runs the browser steps and reports what they see.
  - AC-01: the table shows FirstName, LastName, JobTitle and Email, one row per active employee.
  - AC-02: search "Alice" shows only matching rows. Search a term that occurs only in a JobTitle or Email shows no rows.
  - AC-03: no inactive employee is shown. The row count equals 20 minus the inactive records in the spec.md list.
  - AC-04: opening a row shows FirstName, LastName, Email, JobTitle and IsActive, with no edit control.
  - AC-05: a search text that matches nothing shows no rows.
  - AC-06: 20 records, at least 2 inactive, an active Alice, none a real person. This includes the sample data check moved from task 8, done in the browser after task 10: 20 rows, the 3 inactive records Hugo Brandt, Maya Petrov and Quinn Abara, and active Alice. Compare the data with the list in spec.md section 10, using a data view in ODC Studio or the ODC Portal for exact values.
  - Write `MCP/Reports/check-<revision>-<yyyy-mm-dd>.md` with a result per AC, every deviation, and, where one applies, the matching gap number from the "Expected gaps" table of design.md. Do not change the app or `requirements.md`. If they disagree, report it.
  - No fix prompt is written in advance. If the check finds a real failure, Kiro writes one Mentor prompt for it then, using the real names from the built app, and shows it to the user. Then: **[CONFIRM]** the exact prompt, send it, **[CONFIRM]** the publish, run the graph verification, and log it in `MCP/Reports/interventions.md`. Each fix is its own step, one at a time.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 13. Final scope check
  - Only EmployeeCatalogMCP was touched. Compare every tenant write in `MCP/Prompts/` and the run facts with the one `app_key`. Compare EmployeeCatalogMW's latest revision with the one recorded in task 4: it must be unchanged.
  - No files outside `MCP/`. Search for files created or modified since this plan was approved in `/tmp`, the build A folder (`Employee Catalog/MentorWeb`), and the skill folder. The only allowed outside access was reading build A's `requirements.md` and BRD.
  - SDD Base unchanged. Search it for files newer than `MCP/.kiro/specs/employee-catalog/tasks.md` and report any.
  - Remove the scratch copies in `MCP/Reports/scratch/` only if the user agrees.
  - Report each of the four checks as pass or fail with the evidence.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_
