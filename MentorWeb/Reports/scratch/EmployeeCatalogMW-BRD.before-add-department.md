<!-- Generated from MentorWeb/.kiro/specs/employee-catalog/requirements.md using MentorWeb/Prompts/01-generate-brd.md. Do not edit by hand. Change requirements.md and regenerate. -->

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
  - Entity Relationships:
    - None. Employee has no relationships and there are no other entities.
- Sample data for Employee (all fictional, no real people, all email addresses on the reserved domain example.com):
  - The Employee entity is loaded with 20 records.
  - 17 records have IsActive true and 3 records have IsActive false (Hugo Brandt, Maya Petrov, Quinn Abara).
  - One active record has FirstName Alice (Alice Anderson).
  - The 20 records, as FirstName LastName, JobTitle, Email, IsActive:
    - Alice Anderson, Software Engineer, alice.anderson@example.com, true
    - Bruno Castillo, Product Manager, bruno.castillo@example.com, true
    - Carla Dubois, UX Designer, carla.dubois@example.com, true
    - Devon Marsh, QA Analyst, devon.marsh@example.com, true
    - Elena Novak, Data Analyst, elena.novak@example.com, true
    - Felix Okafor, DevOps Engineer, felix.okafor@example.com, true
    - Grace Lindholm, HR Specialist, grace.lindholm@example.com, true
    - Hugo Brandt, Finance Analyst, hugo.brandt@example.com, false
    - Irene Takeda, Marketing Manager, irene.takeda@example.com, true
    - Jonas Ferreira, Support Agent, jonas.ferreira@example.com, true
    - Kara Whitfield, Project Manager, kara.whitfield@example.com, true
    - Liam Oduya, Sales Representative, liam.oduya@example.com, true
    - Maya Petrov, Technical Writer, maya.petrov@example.com, false
    - Nolan Reyes, Software Engineer, nolan.reyes@example.com, true
    - Olivia Sandoval, Office Manager, olivia.sandoval@example.com, true
    - Pavel Hartmann, Security Analyst, pavel.hartmann@example.com, true
    - Quinn Abara, Business Analyst, quinn.abara@example.com, false
    - Rosa Lindqvist, Recruiter, rosa.lindqvist@example.com, true
    - Samir Haddad, Solutions Architect, samir.haddad@example.com, true
    - Tessa Moreau, Customer Success Manager, tessa.moreau@example.com, true

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
  - The table has these columns: FirstName, LastName, JobTitle and Email.
  - Filter for inactive employees: the table shows only Employee records whose IsActive is true, with one row per active employee. No row is shown for any Employee whose IsActive is false.
  - Search input above the table: a text input where the user enters search text.
    - When the search text is not empty, the table shows only active employees whose FirstName or LastName matches the search text. For example, entering "Alice" shows the active employee Alice Anderson.
    - When the search text matches no active employee's FirstName or LastName, the table shows no rows.
    - When the search text is empty, the table shows all active employees.
  - Each row opens Employee_Detail for that employee, passing the employee's Id.
- Screen: Employee_Detail
  - Input: the Id of one Employee.
  - Shows these five attributes of that employee: FirstName, LastName, Email, JobTitle and IsActive.
  - Read-only. It has no edit or delete action.
- Not part of this app:
  - Departments. There is no Department entity.
  - Creating, editing or deleting employees.
  - Photos.
  - Integrations.
  - Dashboards, counters and charts.
  - Any screen other than Employee_List and Employee_Detail.
