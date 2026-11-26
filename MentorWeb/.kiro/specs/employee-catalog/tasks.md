# Implementation Plan: Employee Catalog

## Overview

This is a short demo plan for EmployeeCatalogMW. Kiro generates the BRD from requirements.md, the user generates the app in Mentor Web, and Kiro then inspects the app read-only, checks AC-01 to AC-06, applies fallback Mentor prompts only for failing AC-02, AC-03, AC-05 and AC-06, and writes a verification report.

All files created by these tasks are under MentorWeb/ (BRD in MentorWeb/BRD/, prompts in MentorWeb/Prompts/, report in MentorWeb/Reports/). Nothing is written to SDD Base. The only app touched is EmployeeCatalogMW. There is no custom code and there are no Playwright tests in this plan.

## Tasks

- [x] 1. Generate the BRD and save its generation prompt
  - Read the mentor-standards steering file in SDD Base, plus SDD Base/vendor/mentor-brd/Mentor-Requirement-Doc-Standards.md and AI-Agent-Enhancement.md. Read only; do not change SDD Base.
  - Check the Mentor requirement document format with the outsystems-docs MCP (search_docs, source "odc") and report the last_updated sync date.
  - Generate the BRD from MentorWeb/.kiro/specs/employee-catalog/requirements.md into MentorWeb/BRD/ in Mentor format. Use lists, not tables, and only the allowed data types.
  - The BRD includes the Staff role with View access to Employee, the Employee entity, the screens Employee_List and Employee_Detail, and the sample data: 20 fictional records, at least 2 with IsActive false, one active employee with FirstName Alice.
  - Save the prompt used for generation as one file in MentorWeb/Prompts/.
  - BRD files are generated and are never edited by hand. If the BRD needs a change, change the source and regenerate.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 2. USER STEP (gate): upload the BRD and generate the app in Mentor Web
  - This is a user step and is not run by Kiro. Kiro does not create the app and does not call Mentor for this generation step.
  - The user uploads the BRD from MentorWeb/BRD/ to Mentor Web and generates the app EmployeeCatalogMW on the ODC tenant.
  - Gate: do not start task 3 until the user confirms the app is generated.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 3. Read-only inspection of EmployeeCatalogMW
  - Inspect only the app EmployeeCatalogMW through the OutSystems MCP with read-only calls. Never touch any other app. No writes and no publishes.
  - Record the real aggregate names, the screens, the Staff role and its access, the Employee entity attributes, and the Employee data.
  - Note the findings in the working notes for tasks 4 to 6. Any file written goes under MentorWeb/.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 4. Check AC-01 to AC-06 against the generated app
  - For each of AC-01, AC-02, AC-03, AC-04, AC-05 and AC-06, record pass or fail, with the evidence from task 3.
  - For each AC, record whether Mentor produced it or a fallback was needed.
  - Flag any disagreement between the app and MentorWeb/.kiro/specs/employee-catalog/requirements.md. Do not change either one.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 5. Apply fallback prompts for failing ACs only
  - [x] 5.1 Fallback for AC-02 and AC-05 (search), only if either fails
    - Take the search prompt from design.md ("Open points and risks"). Replace the words "the aggregate that loads the Employee records" with the real aggregate name from task 3.
    - Ask the user to confirm the tenant write, then send it as a single separate Mentor prompt through the OutSystems MCP. Use one Mentor session for this task and poll until it finishes.
    - Ask the user to confirm the publish before publishing. Wait until the previous publish is finished before starting another.
    - Save the exact prompt sent as one file in MentorWeb/Prompts/.
    - Re-check AC-02 and AC-05 and record the result and the intervention.
    - If the Mentor prompt fails, the manual step in ODC Studio is a last resort and is a user step. Record it as an intervention.
    - _Requirements: AC-02, AC-05_

  - [x] 5.2 Fallback for AC-03 (inactive hidden), only if it fails
    - Take the IsActive filter prompt from design.md ("Open points and risks"). Replace the aggregate name with the real name from task 3.
    - Ask the user to confirm the tenant write, then send it as a single separate Mentor prompt through the OutSystems MCP. Use one Mentor session for this task and poll until it finishes.
    - Ask the user to confirm the publish before publishing.
    - Save the exact prompt sent as one file in MentorWeb/Prompts/.
    - Re-check AC-03 and record the result and the intervention.
    - If the Mentor prompt fails, the manual step in ODC Studio is a last resort and is a user step. Record it as an intervention.
    - _Requirements: AC-03_

  - [x] 5.3 Fallback for AC-06 (sample data), only if it fails
    - Take the sample data prompt from design.md ("Open points and risks"). It names no aggregate.
    - Ask the user to confirm the tenant write, then send it as a single separate Mentor prompt through the OutSystems MCP. Use one Mentor session for this task and poll until it finishes.
    - Ask the user to confirm the publish before publishing.
    - Save the exact prompt sent as one file in MentorWeb/Prompts/.
    - Re-check AC-06 and record the result and the intervention.
    - If the Mentor prompt fails, a data upload or entry of the 20 fictional records (at least 2 inactive, one active Alice) is a last resort and is a user step. Record it as an intervention.
    - _Requirements: AC-06_

- [x] 6. Write the verification report
  - Write the report as one file in MentorWeb/Reports/.
  - Per AC (AC-01 to AC-06): pass or fail, and whether Mentor produced it or manual work was needed.
  - Include an "Interventions" section that lists every fallback used, of either kind (Mentor prompt or manual). For each, give the AC, what was done, and the exact prompt or step. This build is compared with a second build.
  - List any disagreement between the app and requirements.md without changing either one.
  - Include the docs sync date from task 1.
  - _Requirements: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06_

- [x] 7. Checkpoint - Scope check
  - Confirm that nothing outside EmployeeCatalogMW was touched, that no file was written outside MentorWeb/, and that SDD Base is unchanged. Ask the user if questions arise.

## Notes

- Tasks 2 and any manual fallback in task 5 are user steps. Kiro does not run them.
- Tasks 5.1 to 5.3 run only for failing ACs among AC-02, AC-03, AC-05 and AC-06, one at a time, each after the user confirms the tenant write and the publish. If an AC passes, mark its task as not needed and note it in the report.
- BRD files are generated and never edited by hand.

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1"] },
    { "id": 1, "tasks": ["2"] },
    { "id": 2, "tasks": ["3"] },
    { "id": 3, "tasks": ["4"] },
    { "id": 4, "tasks": ["5.1"] },
    { "id": 5, "tasks": ["5.2"] },
    { "id": 6, "tasks": ["5.3"] },
    { "id": 7, "tasks": ["6"] },
    { "id": 8, "tasks": ["7"] }
  ]
}
```
