# App Spec: EmployeeCatalogMCP

## 1. Overview

**Purpose:** Employee Catalog is a read-only staff directory. Staff use it to find a colleague's name, job title and email in one place. It is a demo with about 20 employees.

**Target users:** Staff.

**Target app:** EmployeeCatalogMCP (new)

**Style direction:** Apply OutSystems UI defaults

---

## 2. Roles

- **Staff**: the only role. Has View access to Employee: can see employee data, and cannot create, edit or delete it.

---

## 3. Data model

### Entities

| Entity | Attributes (name, type, constraint) | Relationships |
|---|---|---|
| Employee | Id (Long Integer, primary key, automatic), FirstName (Text, 50), LastName (Text, 50), Email (Email, 250), JobTitle (Text, 100), IsActive (Boolean), DepartmentId (Department Identifier, foreign key to Department, not mandatory) | Foreign key to Department via DepartmentId (optional). |

### Static enums

| Enum | Values |
|---|---|
| Department | Engineering, Finance, Human Resources, Sales |

Department is a static entity with the default static entity attributes only and no others. Its records are in the order listed.

---

## 4. Screens + RBAC

| Screen | Purpose | Accessible by (roles) |
|---|---|---|
| Employee_List | Table of active employees with a search input and a department filter | Staff |
| Employee_Detail | All Employee attributes for one employee | Staff |

---

## 5. Server actions

None. Screens read data with aggregates. The only actions are the bootstrap actions for the sample data.

---

## 6. Integrations

None.

---

## 8. Out of scope

- Creating, editing or deleting employees.
- Photos.
- Integrations.
- Dashboards.
- Any screen other than Employee_List and Employee_Detail.
- Any role other than Staff.

---

## 9. Acceptance criteria

- AC-01 (list loads): Given a Staff user is signed in and Active_Employee records exist, When the user opens Employee_List, Then a table shows the columns FirstName, LastName, JobTitle, Email and Department, with one row per Active_Employee.
- AC-02 (search): Given a Staff user is on Employee_List and an Active_Employee has the FirstName "Alice" or the LastName "Alice", When the user enters "Alice" in the search input, Then the table shows only Active_Employee rows whose FirstName or LastName matches "Alice".
- AC-03 (inactive employees hidden): Given at least one Employee has IsActive set to false, When a Staff user opens Employee_List, Then no row is shown for any Employee with IsActive set to false.
- AC-04 (detail screen): Given a Staff user is on Employee_List, When the user opens an employee row, Then Employee_Detail shows FirstName, LastName, Email, JobTitle, IsActive and Department of that employee.
- AC-05 (empty search result): Given a Staff user is on Employee_List, When the user enters a search text that matches no Active_Employee FirstName or LastName, Then the table shows no rows.
- AC-06 (sample data present): Given Employee_Catalog is deployed, When the Employee data is inspected in ODC Studio or the browser, Then it contains 20 fictional Employee records, at least 2 of them with IsActive set to false, and none of them is a real person, and one of them is an active employee with first name Alice.
- AC-07 (department shown): Given a Staff user is signed in and the 20 Employee records have the departments in Department_Assignment, When the user opens Employee_List and then opens Employee_Detail for an employee, Then every Active_Employee row on Employee_List shows a Department column with the department from Department_Assignment, and Employee_Detail shows the same department for that employee.
- AC-08 (department filter): Given a Staff user is on Employee_List, When the user chooses a department in Department_Filter, Then the table shows only Active_Employee rows of that department; and when the user also enters a search text, the table shows only the Active_Employee rows of that department that match the search text by FirstName or LastName.

---

## 10. Notes for Mentor

- Employee_List is a Table with the columns FirstName, LastName, JobTitle, Email and Department.
- The table shows only Employee records where IsActive is true.
- The search input matches FirstName or LastName only.
- Employee_List has a Department_Filter that lets the user choose one Department. With no department chosen, Department_Filter applies no department restriction. When a department is chosen, the table shows only Active_Employee rows of that department, and a search text applies in addition to it.
- An Employee with no Department is shown when no department is chosen and is not shown when a department is chosen.
- Employee_Detail shows FirstName, LastName, Email, JobTitle, IsActive and Department of the employee. Employee Catalog is a read-only staff directory.
- Do not use the patterns "Master detail" or "List with popup".
- Seed exactly the 20 records listed under "Sample data" below, in that order, with the values as given, including the Department of each record, and no others.

### Sample data

| FirstName | LastName | JobTitle | Email | IsActive | Department |
|---|---|---|---|---|---|
| Alice | Anderson | Software Engineer | alice.anderson@example.com | true | Engineering |
| Bruno | Castillo | Product Manager | bruno.castillo@example.com | true | Engineering |
| Carla | Dubois | UX Designer | carla.dubois@example.com | true | Engineering |
| Devon | Marsh | QA Analyst | devon.marsh@example.com | true | Engineering |
| Elena | Novak | Data Analyst | elena.novak@example.com | true | Finance |
| Felix | Okafor | DevOps Engineer | felix.okafor@example.com | true | Engineering |
| Grace | Lindholm | HR Specialist | grace.lindholm@example.com | true | Human Resources |
| Hugo | Brandt | Finance Analyst | hugo.brandt@example.com | false | Finance |
| Irene | Takeda | Marketing Manager | irene.takeda@example.com | true | Sales |
| Jonas | Ferreira | Support Agent | jonas.ferreira@example.com | true | Sales |
| Kara | Whitfield | Project Manager | kara.whitfield@example.com | true | Finance |
| Liam | Oduya | Sales Representative | liam.oduya@example.com | true | Sales |
| Maya | Petrov | Technical Writer | maya.petrov@example.com | false | Engineering |
| Nolan | Reyes | Software Engineer | nolan.reyes@example.com | true | Engineering |
| Olivia | Sandoval | Office Manager | olivia.sandoval@example.com | true | Human Resources |
| Pavel | Hartmann | Security Analyst | pavel.hartmann@example.com | true | Engineering |
| Quinn | Abara | Business Analyst | quinn.abara@example.com | false | Finance |
| Rosa | Lindqvist | Recruiter | rosa.lindqvist@example.com | true | Human Resources |
| Samir | Haddad | Solutions Architect | samir.haddad@example.com | true | Sales |
| Tessa | Moreau | Customer Success Manager | tessa.moreau@example.com | true | Sales |
