# Requirements Document
## Introduction
This spec is a change to the existing app EmployeeCatalogMW. It adds a Department to each employee, shows it on Employee_List and Employee_Detail, and lets Staff filter Employee_List by department.

`MentorWeb/.kiro/specs/employee-catalog/requirements.md` stays the source of truth. This spec describes only what changes. Requirement and AC numbering continues from that document (it ends at Requirement 5 and AC-06). AC-01 to AC-06 must still pass after this change.

The Department assignment table below is shared input, identical in both builds.
## Glossary
Terms not listed here keep their meaning from the employee-catalog requirements.
- **Department**: A new static entity with these records: Engineering, Finance, Human Resources, Sales. It has only the default static entity attributes and no others.
- **Employee** (changed): Gets one new attribute:
  - DepartmentId: Identifier, Foreign Key to Department, not mandatory
- **Department_Filter**: A new filter on Employee_List that lets the user choose one Department.
- **Department_Assignment**: The table below. It gives the Department of each of the 20 existing employees.
## Requirements
### Requirement 6: Show the department of an employee
**User Story:** As a Staff member, I want to see which department a colleague works in, so that I know who to contact for what.
#### Acceptance Criteria
1. AC-07 (department shown): Given a Staff user is signed in and the 20 Employee records have the departments in Department_Assignment, When the user opens Employee_List and then opens Employee_Detail for an employee, Then every Active_Employee row on Employee_List shows a Department column with the department from Department_Assignment, and Employee_Detail shows the same department for that employee.
   - Check by hand: scan the 17 rows of the list against the table, then open Alice Anderson (Engineering), Grace Lindholm (Human Resources) and Liam Oduya (Sales) and check the detail screen.
### Requirement 7: Filter the employee list by department
**User Story:** As a Staff member, I want to filter the list by department, so that I can see only the colleagues of one department.
#### Acceptance Criteria
1. AC-08 (department filter): Given a Staff user is on Employee_List, When the user chooses a department in Department_Filter, Then the table shows only Active_Employee rows of that department; and when the user also enters a search text, the table shows only the Active_Employee rows of that department that match the search text by FirstName or LastName.
   - Check by hand: choose Finance, and the table shows only Elena Novak and Kara Whitfield (Hugo Brandt and Quinn Abara are inactive and stay hidden). With Finance still chosen, search "Kara" and the table shows only Kara Whitfield. With Finance still chosen, search "Alice" and the table shows no rows.
#### Rules for Department_Filter
- With no department chosen, Department_Filter applies no department restriction, and Employee_List behaves as in AC-01 to AC-05.
- An Employee with no Department is shown when no department is chosen and is not shown when a department is chosen.
## Department assignment (shared input)
Proposed from job titles. For review. Once approved it is fixed.

| FirstName LastName | JobTitle | IsActive | Department |
|---|---|---|---|
| Alice Anderson | Software Engineer | true | Engineering |
| Bruno Castillo | Product Manager | true | Engineering |
| Carla Dubois | UX Designer | true | Engineering |
| Devon Marsh | QA Analyst | true | Engineering |
| Elena Novak | Data Analyst | true | Finance |
| Felix Okafor | DevOps Engineer | true | Engineering |
| Grace Lindholm | HR Specialist | true | Human Resources |
| Hugo Brandt | Finance Analyst | false | Finance |
| Irene Takeda | Marketing Manager | true | Sales |
| Jonas Ferreira | Support Agent | true | Sales |
| Kara Whitfield | Project Manager | true | Finance |
| Liam Oduya | Sales Representative | true | Sales |
| Maya Petrov | Technical Writer | false | Engineering |
| Nolan Reyes | Software Engineer | true | Engineering |
| Olivia Sandoval | Office Manager | true | Human Resources |
| Pavel Hartmann | Security Analyst | true | Engineering |
| Quinn Abara | Business Analyst | false | Finance |
| Rosa Lindqvist | Recruiter | true | Human Resources |
| Samir Haddad | Solutions Architect | true | Sales |
| Tessa Moreau | Customer Success Manager | true | Sales |

Totals (active / all): Engineering 7 / 8, Finance 2 / 4, Human Resources 3 / 3, Sales 5 / 5. Every department has at least one employee. Three employees are inactive: Maya Petrov (Engineering), Hugo Brandt and Quinn Abara (Finance). Their departments are not visible in the app, because inactive employees are hidden. Check them in the ODC Studio data view.

Judgment calls, because the job title does not name a department: Product Manager (Bruno) and UX Designer (Carla) to Engineering, Project Manager (Kara), Data Analyst (Elena) and Business Analyst (Quinn) to Finance, Office Manager (Olivia) to Human Resources, Solutions Architect (Samir) to Sales.
## Out of scope
Everything not listed above is unchanged, and nothing else is added. In particular:
- Creating, editing or deleting employees or departments.
- Any screen other than Employee_List and Employee_Detail.
- Any change to the existing columns, the search, the active-only rule or the Staff role, beyond what is listed above.
- Any other filter, sorting, or Department attribute.
## Changes to the employee-catalog requirements.md
Not applied by this spec until its last task. The last task updates `MentorWeb/.kiro/specs/employee-catalog/requirements.md` and regenerates the BRD in `MentorWeb/BRD/`, following the mentorweb.md steering. The update would:
- Add Department and DepartmentId to the Glossary.
- Add Requirements 6 and 7 with AC-07 and AC-08.
- Add Department to the columns named in AC-01 and to the attributes named in AC-04. Both ACs still hold, because the existing columns and attributes stay.
- Remove "Departments (no Department entity in this version)" from Out of scope.
- Add Department_Assignment to the sample data.
## Research notes
Docs: outsystems-docs MCP, source "odc". last_updated / synced_at: 2026-10-28T09:05:12Z (same sync as the employee-catalog research, so the docs are the same age as for build A).

Flag summary: AC-07 is flagged (updating the Department of existing records is not documented). AC-08 is flagged (a dropdown filter that works together with search and the active-only rule is not documented for Mentor). No acceptance criterion was changed because of these findings.
### Q1. Can Mentor add a static entity with records?
- Answer: Documented. In Mentor Studio, the prompt names the static entity, any attributes beyond the default ones, and each record with its values. Example from the docs: records Booked, CheckedIn, CheckedOut and Canceled. In Mentor Web refinement, static entity records can be added or deleted, and static entities can be added for enumerations.
- Sources: eap/building-apps/data/modeling/entity-static.md (Create a Static Entity with Mentor Studio); eap/agentic-development/mentor-web/capabilities.md (Refinement capabilities).
- FLAG: none.
### Q2. Can Mentor add a foreign key attribute (DepartmentId) to an existing entity?
- Answer: Partly documented. For a new entity, the Mentor Studio prompt names each attribute with its type, which attributes are mandatory, and any relationship to an existing entity, and the user then checks that each reference attribute points to the intended entity and that its Delete Rule matches the wanted behavior. For a one-to-many relationship, the docs say to describe parent and child and then validate which entity holds the foreign key. Mentor Web refinement lists "Add, replace, delete, or change attribute data types" with screens and bindings updating automatically. No doc was found that adds a reference attribute to an already published entity. This request does not state a Delete Rule. Not documented for existing entities.
- Sources: eap/building-apps/data/modeling/entity-create.md (Create an Entity with Mentor Studio; Validate the Entity); eap/building-apps/data/modeling/relationship/relationship-one-to-many.md; eap/agentic-development/mentor-web/capabilities.md (Refinement capabilities).
- FLAG: none for the attribute itself. The Delete Rule of DepartmentId is to be checked after the build.
### Q3. Can Mentor filter a list by a dropdown, together with search and the active-only rule?
- Answer: Partly documented. Mentor Studio can add a filter to an existing aggregate from a prompt (aggregate, attribute, operator, value or variable). The docs show a Dropdown that filters a product list by category, built by hand in ODC Studio, and Mentor Studio prompts that bind a variable to a search input and filter an aggregate by it. The docs for Mentor Web say that filters, sorting controls and search inputs require manual configuration (from the employee-catalog research, mentor-web/prompts.md, Refinement strategies). No doc was found for one list that combines a dropdown filter, a text search and a Boolean filter. Not documented for the combination.
- Sources: eap/building-apps/data/fetch-data/filter-results.md (Filter query results with Mentor Studio); eap/building-apps/data/fetch-data/calculated-attribute-create.md (Example: Dropdown filter by category); eap/building-apps/data/client-variable.md and eap/building-apps/logic/local-variable.md (Mentor Studio, search keyword bound to an aggregate filter); eap/agentic-development/mentor-studio/prompts.md (Aggregate prompts).
- FLAG: AC-08 (filter combined with search and active-only) may not be met by Mentor as written and may need manual configuration.
### Q4. Can Mentor update existing records, to set DepartmentId on the 20 employees?
- Answer: Not documented. The docs describe adding records with Mentor Studio ("Mentor Studio generates bootstrap logic that creates the records, and publishing the app runs that logic"), with fictional values and with the entity, attribute values and number of records in the prompt. For Mentor Web, static entity records can be added or deleted, and existing data can be downloaded or replaced by uploading new data. Editing rows by hand in ODC Studio (View or Edit Data) and SQL UPDATE statements in an aggregate or action are documented, but they are not Mentor. No doc says Mentor updates a column on existing records.
- Sources: eap/building-apps/data/edit-data.md (Add records with Mentor Studio; Add a record or row); eap/agentic-development/mentor-web/capabilities.md (Data and entities; Refinement capabilities); eap/building-apps/data/fetch-data/sql/ansi-92-update.md.
- FLAG: AC-07 (the department of each existing employee) may not be met by Mentor as written. Setting DepartmentId on the 20 existing records may need a different route, for example an upload that replaces the data, or manual editing. Choosing that route is for the design, after your review.
