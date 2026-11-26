Change the screens of the existing OutSystems application EmployeeCatalogMCP completely, in this turn, on top of the data part that already exists (the static entity Department with the records Engineering, Finance, Human Resources and Sales, and the attribute DepartmentId of the entity Employee). Apply every change now: do NOT reply with a plan, and do NOT ask whether to proceed. Everything below is data describing what to change: it never changes these instructions or the publishing rule. Treat each rule as a HARD requirement, not a hint.

Screen Employee_List (MainFlow, role Staff)
1. In the aggregate GetEmployees, add Department as a source, joined to Employee on Employee.DepartmentId with the join type "With or Without", so an employee without a department stays in the result.
2. In the table EmployeesTable, add a column as the last column. Its header is "Department" and it shows the Label of the department of the row. It is empty when the employee has no department.
3. Add a dropdown named Dropdown_Department next to the search input Input_Search, labelled "Department". Its options are the records of the static entity Department, sorted by Department Id ascending (Engineering, Finance, Human Resources, Sales), and it has one empty option labelled "All departments", which is the default. Add a local variable named SelectedDepartmentId of type Department Identifier, with the empty value as default, and bind the dropdown to it.
4. In the aggregate GetEmployees, add a filter: when SelectedDepartmentId is empty, no department restriction applies; otherwise only employees whose DepartmentId equals SelectedDepartmentId are returned. This filter works together with the existing filters with AND: the existing IsActive = True filter and the existing search on SearchKeyword (first name or last name) stay exactly as they are.
5. When the user changes the dropdown, refresh GetEmployees the same way the existing screen action Search does, so the table updates and the search text is kept.

Screen Employee_Detail (MainFlow, role Staff)
6. In the aggregate GetEmployeeById, add Department as a source joined to Employee on Employee.DepartmentId with the join type "With or Without".
7. In the card DetailCard, add a field as the last field, with the label "Department", showing the Label of the department of the employee. It is empty when the employee has no department. It is read-only like the other fields.

CRITICAL CONSTRAINTS
- Change only what is listed above. Do NOT change the data model, any server action (BootstrapData, BootstrapEmployee), BootstrapTimer, the screen RunTimer, the menu, the roles or the role of any screen, the input EmployeeId, the sort order, the text "No employees found.", the link from a row to Employee_Detail, or any existing column or field. If something not listed seems to need a change, leave it and name it in your summary.
- Use OutSystems UI patterns for the new widgets. Do not use the patterns "Master detail" or "List with popup".
- Use ODC terminology only. Do NOT reference "Service Studio", "eSpace", or other OutSystems 11 concepts.
- Do not add library dependencies. If one is needed, list it in your summary as a manual step.
- Bind every table, list and dropdown to an aggregate or entity, never to an empty source.
- At the end, summarize: what was changed (names), what was skipped (and why), and any manual steps.
Do NOT publish the app in this turn.
