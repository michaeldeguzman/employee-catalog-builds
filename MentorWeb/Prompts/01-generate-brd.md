# Prompt: generate the BRD for EmployeeCatalogMW

Task: employee-catalog, task 1.
Output file: MentorWeb/BRD/EmployeeCatalogMW-BRD.md
Docs basis: outsystems-docs MCP, source "odc", last_updated 2026-10-28T09:05:12Z (page eap/agentic-development/mentor-web/requirements-doc.md).

## Prompt as used

Generate the Mentor Web requirement document (BRD) for the app EmployeeCatalogMW from MentorWeb/.kiro/specs/employee-catalog/requirements.md.

Inputs, read only:
- MentorWeb/.kiro/specs/employee-catalog/requirements.md (source of truth)
- SDD Base/.kiro/steering/mentor-standards.md
- SDD Base/vendor/mentor-brd/Mentor-Requirement-Doc-Standards.md
- SDD Base/vendor/mentor-brd/AI-Agent-Enhancement.md (no AI agent is needed, so it contributes nothing)
- outsystems-docs MCP, source "odc": requirements-doc.md

Format rules:
- Target ODC, Reactive Web only. No custom code, no mobile.
- Write the file as .md, well under 5 MB.
- Use exactly these sections, in this order: App overview, General app settings (omit, nothing to set), Data model, Roles and permissions, Main features and screens, External integrations (omit, none).
- Write everything as nested bullet lists. No tables.
- Use only these data types: Identifier, Text, Boolean, DateTime / Date, Currency, Integer, Email, Phone Number, User Identifier.
- Use the Mentor entity syntax ("Entity: <name>", "This entity is stored locally.", "Attributes include:") and the role syntax ("Role: <name>" with "- <Entity>: View Access").
- Use the recognised UI pattern keyword "Table" for the list screen. Name the attributes on it.
- Use no PII, no code, no images, and no vague words such as "user-friendly" or "intuitive".
- Do not add scope beyond requirements.md. Keep the out-of-scope items as explicit exclusions.

Content to include:
- Entity Employee, stored locally, not a static entity, with Id (Identifier, primary key), FirstName (Text, length 50), LastName (Text, length 50), Email (Email, length 250), JobTitle (Text, length 100), IsActive (Boolean). No relationships, no other entities.
- Role Staff with View Access to Employee. No other roles.
- Screens Employee_List and Employee_Detail, per AC-01 to AC-05 in requirements.md.
- Sample data (AC-06): 20 fictional Employee records, at least 2 with IsActive false, one active employee with FirstName Alice, all emails on example.com. The 20 records used:
  1. Alice Anderson, Software Engineer, alice.anderson@example.com, IsActive true
  2. Bruno Castillo, Product Manager, bruno.castillo@example.com, true
  3. Carla Dubois, UX Designer, carla.dubois@example.com, true
  4. Devon Marsh, QA Analyst, devon.marsh@example.com, true
  5. Elena Novak, Data Analyst, elena.novak@example.com, true
  6. Felix Okafor, DevOps Engineer, felix.okafor@example.com, true
  7. Grace Lindholm, HR Specialist, grace.lindholm@example.com, true
  8. Hugo Brandt, Finance Analyst, hugo.brandt@example.com, false
  9. Irene Takeda, Marketing Manager, irene.takeda@example.com, true
  10. Jonas Ferreira, Support Agent, jonas.ferreira@example.com, true
  11. Kara Whitfield, Project Manager, kara.whitfield@example.com, true
  12. Liam Oduya, Sales Representative, liam.oduya@example.com, true
  13. Maya Petrov, Technical Writer, maya.petrov@example.com, false
  14. Nolan Reyes, Software Engineer, nolan.reyes@example.com, true
  15. Olivia Sandoval, Office Manager, olivia.sandoval@example.com, true
  16. Pavel Hartmann, Security Analyst, pavel.hartmann@example.com, true
  17. Quinn Abara, Business Analyst, quinn.abara@example.com, false
  18. Rosa Lindqvist, Recruiter, rosa.lindqvist@example.com, true
  19. Samir Haddad, Solutions Architect, samir.haddad@example.com, true
  20. Tessa Moreau, Customer Success Manager, tessa.moreau@example.com, true

Put a one-line "generated, do not edit by hand" comment at the top of the file. The file is generated and is never edited by hand. To change it, change requirements.md and regenerate.
