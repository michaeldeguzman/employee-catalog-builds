---
inclusion: always
---
- SDD Base is read-only for this project. Do not create, change or delete anything in SDD Base unless I explicitly ask. If you think a change there is needed, stop and ask me first.
- Every new file goes in the MCP folder, including scratch and working files such as graph comparisons. Never write to /tmp or any folder outside MCP.
- Project: Employee Catalog, built by Kiro through the OutSystems MCP. The app name on the ODC tenant is EmployeeCatalogMCP. Work only on that app and never touch any other app, including EmployeeCatalogMW.
- Source of truth: MCP/.kiro/specs/employee-catalog/requirements.md, once it exists. If the app and the requirements disagree, report it. Do not silently change either one.
- Flow for the first build:
  1. Requirements are written as a Kiro spec named employee-catalog.
  2. The requirements are converted into the Power's spec format at MCP/spec-driven-build/EmployeeCatalogMCP/spec.md, using the outsystems-spec-driven-build skill in Mode A. Follow the mentor-standards steering file in SDD Base and check with the outsystems-docs MCP. Run validate-spec before any build.
  3. Kiro builds EmployeeCatalogMCP with the outsystems-spec-driven-build skill. Confirm with me before every tenant write and every publish.
  4. Kiro checks the app against the requirements and writes a report in MCP/Reports/.
- Fixes after the build: one Mentor prompt at a time through the OutSystems MCP, each confirmed by me before sending and before publishing, and each logged as an intervention with the exact prompt. Manual work in ODC Studio is a last resort and is also logged.
- After every publish, verify from the published revision with a full graph comparison against the previous revision, and report any change outside the intended scope. Keep the comparison files in MCP/Reports/graphdiff/.
- The spec.md in spec-driven-build/ is a build input generated from requirements.md. Never edit it by hand. Regenerate it after any requirements change.
- Every later change is its own Kiro spec under MCP/.kiro/specs/<change-name>/, describing only what changes and continuing the AC numbering. Its last task updates MCP/.kiro/specs/employee-catalog/requirements.md and regenerates spec.md.
