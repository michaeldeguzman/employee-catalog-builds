---
inclusion: always
---

- Project: Employee Catalog, built with Mentor Web. The app name on the ODC tenant is EmployeeCatalogMW. Work only on that app and never touch any other app.
- Source of truth: MentorWeb/.kiro/specs/employee-catalog/requirements.md, once it exists. If the app and the requirements disagree, report it. Do not silently change either one.
- Flow for the first build:
  1. Requirements are written as a Kiro spec named employee-catalog.
  2. The BRD is generated from requirements.md into MentorWeb/BRD/, in Mentor format. Follow the mentor-standards steering file in SDD Base and check with the outsystems-docs MCP.
  3. I upload the BRD to Mentor Web and generate the app myself. Kiro does not create the app or call Mentor for this generation step. After generation, Kiro may send the fallback Mentor prompts from design.md through the OutSystems MCP, one at a time, only after I confirm each tenant write and each publish.
  4. Kiro checks the app against the requirements and writes a report in MentorWeb/Reports/.
- Every later change is its own Kiro spec under MentorWeb/.kiro/specs/<change-name>/, describing only what changes and continuing the AC numbering. Its last task updates MentorWeb/.kiro/specs/employee-catalog/requirements.md and regenerates the BRD.
- BRD files are generated. Never edit them by hand.
