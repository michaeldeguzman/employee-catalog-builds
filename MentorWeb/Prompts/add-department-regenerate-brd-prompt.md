# Prompt: regenerate the BRD for EmployeeCatalogMW after add-department

Task: add-department, task 10.
Output file: MentorWeb/BRD/EmployeeCatalogMW-BRD.md (overwritten)
Before-copy of the previous BRD: MentorWeb/Reports/scratch/EmployeeCatalogMW-BRD.before-add-department.md
Docs basis: outsystems-docs MCP, source "odc", last_updated 2026-10-28T09:05:12Z (page eap/agentic-development/mentor-web/requirements-doc.md, read with get_doc, and search_docs for static entities and Mentor Web refinement).
Replaces for this run: Prompts/01-generate-brd.md (first BRD). The format rules are the same.

## Prompt as used

Regenerate the Mentor Web requirement document (BRD) for the app EmployeeCatalogMW from MentorWeb/.kiro/specs/employee-catalog/requirements.md, which now includes Department (Glossary, Requirements 6 and 7, AC-07 and AC-08, the Department assignment table).

Inputs, read only:
- MentorWeb/.kiro/specs/employee-catalog/requirements.md (source of truth)
- SDD Base/.kiro/steering/mentor-standards.md
- SDD Base/vendor/mentor-brd/Mentor-Requirement-Doc-Standards.md
- SDD Base/vendor/mentor-brd/AI-Agent-Enhancement.md (no AI agent is needed, so it contributes nothing)
- outsystems-docs MCP, source "odc": requirements-doc.md
- MentorWeb/Prompts/01-generate-brd.md (the 20 emails, which are not in requirements.md, and the format rules)

Format rules (same as the first BRD):
- Target ODC, Reactive Web only. No custom code, no mobile.
- Write the file as .md, well under 5 MB.
- Use exactly these sections, in this order: App overview, General app settings (omit, nothing to set), Data model, Roles and permissions, Main features and screens, External integrations (omit, none).
- Write everything as nested bullet lists. No tables.
- Use only these data types: Identifier, Text, Boolean, DateTime / Date, Currency, Integer, Email, Phone Number, User Identifier.
- Use the Mentor entity syntax ("Entity: <name>", "This entity is stored locally.", "Attributes include:", "Entity Relationships:"), the static entity syntax ("Entity Name:", "Purpose:", "Records:") and the role syntax ("Role: <name>" with "- <Entity>: View Access").
- Use the recognised UI pattern keyword "Table" for the list screen. Name the attributes on it.
- Use no PII, no code, no images, and no vague words such as "user-friendly" or "intuitive".
- Do not add scope beyond requirements.md. Keep the out-of-scope items as explicit exclusions.

What changes against the first BRD (everything else stays as it was):
- App overview: add the goals "show the department of each employee" and "let a Staff member filter the list by department".
- Data model:
  - Add the static entity Department, with the default static entity attributes only and the 4 records Engineering, Finance, Human Resources, Sales. Its Purpose line says it is a plain lookup list with no lifecycle, no state transitions and no stateflow, so that Mentor does not generate a stateflow for it (mentor-standards, section 4).
  - Add Employee.DepartmentId: An Identifier that is a Foreign Key to the Department static entity, not mandatory.
  - Replace "no relationships, no other entities" with the relationship Department to Employee (One-to-Many, from the Foreign Key).
  - Sample data: each of the 20 records carries its Department from the Department assignment table. Add the totals (Engineering 7 active / 8, Finance 2 / 4, Human Resources 3 / 3, Sales 5 / 5).
- Roles and permissions: no change (Staff, View Access to Employee).
- Main features and screens:
  - Employee_List: the table has the columns FirstName, LastName, JobTitle, Email and Department (AC-01, AC-07). Add the Department filter (AC-08) and the two rules for it (no department chosen means no restriction; an employee with no Department is shown only when no department is chosen).
  - Employee_Detail: shows FirstName, LastName, Email, JobTitle, Department and IsActive (AC-04, AC-07).
  - Remove "Departments. There is no Department entity." from the exclusions. Keep the other exclusions.

Put a one-line "generated, do not edit by hand" comment at the top of the file, naming this prompt. The file is generated and is never edited by hand. To change it, change requirements.md and regenerate.

## Result

Written to MentorWeb/BRD/EmployeeCatalogMW-BRD.md. Not uploaded to Mentor Web. No app was changed.
