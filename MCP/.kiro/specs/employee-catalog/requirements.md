# Requirements Document

## Introduction

Employee Catalog is a read-only staff directory. Staff use it to find a colleague's name, job title and email in one place. It is a demo with about 20 employees. The app name on the ODC tenant is EmployeeCatalogMCP. It is built by Kiro through the OutSystems MCP with the Power's outsystems-spec-driven-build skill.

## Glossary

- **Employee_Catalog**: The EmployeeCatalogMCP Reactive Web app.
- **Employee**: A local entity with these attributes:
  - FirstName: Text, length 50
  - LastName: Text, length 50
  - Email: Email, length 250
  - JobTitle: Text, length 100
  - IsActive: Boolean
  - DepartmentId: Identifier, Foreign Key to Department, not mandatory
- **Department**: A static entity with these records: Engineering, Finance, Human Resources, Sales. It has only the default static entity attributes and no others.
- **Staff**: The only role. It has View access to Employee.
- **Employee_List**: The screen showing a table of employees.
- **Employee_Detail**: The screen showing all Employee attributes for one employee.
- **Active_Employee**: An Employee whose IsActive is true.
- **Department_Filter**: A filter on Employee_List that lets the user choose one Department.
- **Department_Assignment**: The table "Department assignment" below. It gives the Department of each of the 20 employees.

## Requirements

### Requirement 1: Browse the employee list

**User Story:** As a Staff member, I want to see a list of employees, so that I can find a colleague's name, job title and email.

#### Acceptance Criteria

1. AC-01 (list loads): Given a Staff user is signed in and Active_Employee records exist, When the user opens Employee_List, Then a table shows the columns FirstName, LastName, JobTitle, Email and Department, with one row per Active_Employee.

### Requirement 2: Search the employee list

**User Story:** As a Staff member, I want to search by first or last name, so that I can find a colleague quickly.

#### Acceptance Criteria

1. AC-02 (search): Given a Staff user is on Employee_List and an Active_Employee has the FirstName "Alice" or the LastName "Alice", When the user enters "Alice" in the search input, Then the table shows only Active_Employee rows whose FirstName or LastName matches "Alice".
2. AC-05 (empty search result): Given a Staff user is on Employee_List, When the user enters a search text that matches no Active_Employee FirstName or LastName, Then the table shows no rows.

### Requirement 3: Hide inactive employees

**User Story:** As a Staff member, I want to see only active employees, so that I do not contact people who have left.

#### Acceptance Criteria

1. AC-03 (inactive employees hidden): Given at least one Employee has IsActive set to false, When a Staff user opens Employee_List, Then no row is shown for any Employee with IsActive set to false.

### Requirement 4: View employee details

**User Story:** As a Staff member, I want to open an employee's details, so that I can see all of the employee's information.

#### Acceptance Criteria

1. AC-04 (detail screen): Given a Staff user is on Employee_List, When the user opens an employee row, Then Employee_Detail shows FirstName, LastName, Email, JobTitle, IsActive and Department of that employee.

### Requirement 5: Provide sample data

**User Story:** As a demo presenter, I want fictional employees preloaded, so that the app can be shown without entering data.

#### Acceptance Criteria

1. AC-06 (sample data present): Given Employee_Catalog is deployed, When the Employee data is inspected in ODC Studio or the browser, Then it contains 20 fictional Employee records, at least 2 of them with IsActive set to false, and none of them is a real person, and one of them is an active employee with first name Alice.

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

## Department assignment

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

- Creating, editing or deleting employees.
- Photos.
- Integrations.
- Dashboards.
- Any screen other than Employee_List and Employee_Detail.

## Research notes

Research done for build A on the 2026-10-28 docs sync; kept unchanged so both builds share the same requirements.

Docs: outsystems-docs MCP, source "odc". last_updated / synced_at: 2026-10-28T09:05:12Z (sync date 2026-10-28).

Flag summary: AC-02, AC-03 and AC-05 are flagged (search and filter need manual configuration). AC-06 is flagged (sample data content is not controlled by the document). AC-01 and AC-04 have no flag. No acceptance criterion was changed because of these findings.

### Q1. Does Mentor Web generate sample data from a requirement document?

- Answer: Partly documented. Mentor Web uses sample data in generated apps, and a data preview with sample data is ready the first time the app preview is opened after generation. Mentor Web uses sample data only when accessed via the built-in OutSystems domain, not via a custom domain. The user can download existing data or upload new data to replace sample data. The docs do not say that Mentor takes specific sample records (such as 20 named employees, or at least 2 inactive) from a requirement document, nor that it controls the IsActive values or the record count. Static entities are the only place where the docs say records listed in the document are created (they list "Records"). Employee is not a static entity.
- Sources: eap/agentic-development/mentor-web/capabilities.md (Data and entities; info box on sample data); eap/agentic-development/mentor-web/how-it-works.md (Generate the app); eap/agentic-development/mentor-web/requirements-doc.md (requirement document structure).
- FLAG: AC-06 (20 fictional employees, at least 2 inactive) may not be met by Mentor as written. Mentor-generated sample data is not documented to follow the requirement document's counts or IsActive values. Manual loading (upload data to replace sample data) may be needed.

### Q2. How does Mentor generate list screens with search, and can it filter out records by a Boolean such as IsActive?

- Answer: Mentor Web generates a Table pattern from the keyword "table" with the entity and attributes named nearby (for example: List "Product" records in a table with columns ...). The docs say plainly, in the Refinement strategies section: "Filters, sorting controls, and search inputs require manual configuration." No doc found for Mentor Web filtering list records by a Boolean attribute such as IsActive in the generated screen. In Mentor Studio, filtering an aggregate by an attribute value can be done with a prompt (Filter query results), but that is Mentor Studio and applies to an existing app. In Mentor Web, dashboard lists have no filters; counters and charts can use status filters. Documented as: "Not documented" for Boolean list filtering in Mentor Web.
- Sources: eap/agentic-development/mentor-web/prompts.md (Table; Refinement strategies); eap/agentic-development/mentor-web/capabilities.md (Screen generation; Dashboards); eap/building-apps/data/fetch-data/filter-results.md (Mentor Studio).
- FLAG: AC-02 (search by first or last name) and AC-03 (inactive employees hidden) may not be met by Mentor Web as written, because search inputs and filters require manual configuration (for example in ODC Studio or a Mentor Studio prompt after generation). AC-05 (empty search result) depends on the search from AC-02 and carries the same risk.

### Q3. How does Mentor set up role-based View access?

- Answer: Documented. In the requirement document, roles are written as "Role: <name>" followed by entity-level access lines such as "- Customer: View Access". Entity-level access levels are View, Edit and No Access. Mentor suggests roles from context and applies authorization rules at the entity level, and the user adjusts roles and permissions in the blueprint before generation. Roles can also be changed with prompts after generation (add role, delete role, edit permissions). The generated app uses the ODC login screen. A prompt example in the docs uses a role named "Staff". No contradiction with the criteria found.
- Sources: eap/agentic-development/mentor-web/requirements-doc.md (Role with permissions); eap/agentic-development/mentor-web/capabilities.md (Security; Refinement capabilities); eap/agentic-development/mentor-web/prompts.md (Authorization prompts).
- FLAG: none for the Staff View-access rule. Note for the reader only: AC criteria do not currently cover role access, so there is no AC to flag.
