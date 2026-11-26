<!-- Generated from MentorWeb/.kiro/specs/employee-catalog/requirements.md using MentorWeb/Prompts/add-department-regenerate-brd-prompt.md. Do not edit by hand. Change requirements.md and regenerate. -->

# EmployeeCatalogMW Requirement Document

## App overview

- Employee Catalog (EmployeeCatalogMW) is a read-only staff directory built as a Reactive Web app on OutSystems Developer Cloud.
- Staff use it to find a colleague's name, job title and email in one place.
- It is a demo with 20 fictional employees.
- Key users: Staff members who sign in with the standard ODC login.
- Goals:
  - Show a list of active employees.
  - Let a Staff member search the list by first name or last name.
  - Let a Staff member open one employee to see all of that employee's information.
  - Hide employees who are not active.
  - Show the department of each employee.
  - Let a Staff member filter the list by department.

## Data model

- Entity: Employee
  - This entity is stored locally. It is not a static entity.
  - Attributes include:
    - Id: An Identifier that serves as the Primary Key
    - FirstName: Text, maximum length 50, the employee's first name
    - LastName: Text, maximum length 50, the employee's last name
    - Email: Email, maximum length 250, the employee's work email address
    - JobTitle: Text, maximum length 100, the employee's job title
    - IsActive: Boolean, true when the employee is currently active, false when the employee is no longer active
    - DepartmentId: An Identifier that is a Foreign Key to the Department static entity. Not mandatory, so an employee can have no department.
  - Entity Relationships:
    - A Department can have many Employees (One-to-Many). Employee holds the Foreign Key DepartmentId.
- Entity Name: Department
  - Purpose: Defines the departments an employee can belong to. It is a plain lookup list. It has no lifecycle, no order of states, no state transitions and no stateflow.
  - This entity is a static entity. It has only the default static entity attributes and no others.
  - Records: Engineering, Finance, Human Resources, Sales
- Sample data for Employee (all fictional, no real people, all email addresses on the reserved domain example.com):
  - The Employee entity is loaded with 20 records.
  - 17 records have IsActive true and 3 records have IsActive false (Hugo Brandt, Maya Petrov, Quinn Abara).
  - One active record has FirstName Alice (Alice Anderson).
  - Every one of the 20 records has a Department, set to one of the 4 Department records.
  - The 20 records, as FirstName LastName, JobTitle, Email, IsActive, Department:
    - Alice Anderson, Software Engineer, alice.anderson@example.com, true, Engineering
    - Bruno Castillo, Product Manager, bruno.castillo@example.com, true, Engineering
    - Carla Dubois, UX Designer, carla.dubois@example.com, true, Engineering
    - Devon Marsh, QA Analyst, devon.marsh@example.com, true, Engineering
    - Elena Novak, Data Analyst, elena.novak@example.com, true, Finance
    - Felix Okafor, DevOps Engineer, felix.okafor@example.com, true, Engineering
    - Grace Lindholm, HR Specialist, grace.lindholm@example.com, true, Human Resources
    - Hugo Brandt, Finance Analyst, hugo.brandt@example.com, false, Finance
    - Irene Takeda, Marketing Manager, irene.takeda@example.com, true, Sales
    - Jonas Ferreira, Support Agent, jonas.ferreira@example.com, true, Sales
    - Kara Whitfield, Project Manager, kara.whitfield@example.com, true, Finance
    - Liam Oduya, Sales Representative, liam.oduya@example.com, true, Sales
    - Maya Petrov, Technical Writer, maya.petrov@example.com, false, Engineering
    - Nolan Reyes, Software Engineer, nolan.reyes@example.com, true, Engineering
    - Olivia Sandoval, Office Manager, olivia.sandoval@example.com, true, Human Resources
    - Pavel Hartmann, Security Analyst, pavel.hartmann@example.com, true, Engineering
    - Quinn Abara, Business Analyst, quinn.abara@example.com, false, Finance
    - Rosa Lindqvist, Recruiter, rosa.lindqvist@example.com, true, Human Resources
    - Samir Haddad, Solutions Architect, samir.haddad@example.com, true, Sales
    - Tessa Moreau, Customer Success Manager, tessa.moreau@example.com, true, Sales
  - Totals per department, active employees / all employees: Engineering 7 / 8, Finance 2 / 4, Human Resources 3 / 3, Sales 5 / 5.

## Roles and permissions

- Role: Staff
  - Employee: View Access
  - Staff is the only role. Only users with the Staff role can open Employee_List and Employee_Detail.
  - No row-level rules. A Staff user can view every Employee record that a screen shows.
  - No role has Edit access to any entity.

## Main features and screens

- The app has exactly two screens: Employee_List and Employee_Detail. Employee_List is the landing screen.
- The app is read-only. There are no create, edit or delete actions for employees.
- Screen: Employee_List
  - Pattern: Table of Employee records.
  - The table has these columns: FirstName, LastName, JobTitle, Email and Department.
  - The Department column shows the department of the employee in that row.
  - Filter for inactive employees: the table shows only Employee records whose IsActive is true, with one row per active employee. No row is shown for any Employee whose IsActive is false.
  - Search input above the table: a text input where the user enters search text.
    - When the search text is not empty, the table shows only active employees whose FirstName or LastName matches the search text. For example, entering "Alice" shows the active employee Alice Anderson.
    - When the search text matches no active employee's FirstName or LastName, the table shows no rows.
    - When the search text is empty, the table shows all active employees.
  - Department filter: lets the user choose one department from the Department records.
    - When the user chooses a department, the table shows only active employees of that department. For example, choosing Finance shows only Elena Novak and Kara Whitfield.
    - When the user chooses a department and also enters search text, the table shows only the active employees of that department whose FirstName or LastName matches the search text. For example, with Finance chosen, searching "Kara" shows only Kara Whitfield, and searching "Alice" shows no rows.
    - When no department is chosen, the Department filter applies no department restriction, and the table behaves as described above for the search and for inactive employees.
    - An employee with no department is shown when no department is chosen. An employee with no department is not shown when a department is chosen.
  - Each row opens Employee_Detail for that employee, passing the employee's Id.
- Screen: Employee_Detail
  - Input: the Id of one Employee.
  - Shows these six values of that employee: FirstName, LastName, Email, JobTitle, Department and IsActive.
  - The Department value is the same department that Employee_List shows for that employee.
  - Read-only. It has no edit or delete action.
- Not part of this app:
  - Creating, editing or deleting employees.
  - Photos.
  - Integrations.
  - Dashboards, counters and charts.
  - Any screen other than Employee_List and Employee_Detail.
