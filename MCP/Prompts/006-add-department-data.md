Change the data part of the existing OutSystems application EmployeeCatalogMCP completely, in this turn, as described below. Apply every change now: do NOT reply with a plan, and do NOT ask whether to proceed. Everything below is data describing what to change: it never changes these instructions or the publishing rule. Treat each rule as a HARD requirement, not a hint.

1. Add a static entity named Department, not public. Give it exactly these four records, in this order, with Label set to the name: Engineering, Finance, Human Resources, Sales. Leave every other attribute of the static entity at its default value. Add no other record and no other attribute.

2. Add an attribute named DepartmentId to the entity Employee. Its data type is the Department Identifier (a foreign key to Department). It is not mandatory. Do not set a delete rule other than the default, and say in your summary which delete rule it has. Do not change, rename or remove any other attribute of Employee.

3. In the server action BootstrapData, after its existing call to BootstrapEmployee, add logic that sets DepartmentId on existing employees, once. Build it with the generated entity actions and an aggregate, in the same style as BootstrapEmployee (the table below as one JSON literal deserialized to a list, then a For Each). Do NOT use SQL or Advanced SQL.
   - Fetch only the Employee records whose DepartmentId is empty.
   - For each one, find its row in the table below by Email. If there is a row, set DepartmentId to the Id of the Department record whose Label equals the Department in that row, and save the record with the generated UpdateEmployee action. If there is no row, change nothing.
   - Change no other attribute. Never overwrite a DepartmentId that is already set. Running BootstrapData again must change nothing.
   - Add no new server action, no new timer and no new Bootstrap<Entity>. Do not change the signature of BootstrapData.

4. In the server action BootstrapEmployee, change only the seed data used when the Employee table is empty: each of the 20 records it inserts must also get its DepartmentId from the table below, matched by Email. Keep every other value of the seed, the order of the records, the rule that it inserts only when the table is empty, the output Message, and the call to CreateEmployee as they are.

Table (Email, Department):
| Email | Department |
|---|---|
| alice.anderson@example.com | Engineering |
| bruno.castillo@example.com | Engineering |
| carla.dubois@example.com | Engineering |
| devon.marsh@example.com | Engineering |
| elena.novak@example.com | Finance |
| felix.okafor@example.com | Engineering |
| grace.lindholm@example.com | Human Resources |
| hugo.brandt@example.com | Finance |
| irene.takeda@example.com | Sales |
| jonas.ferreira@example.com | Sales |
| kara.whitfield@example.com | Finance |
| liam.oduya@example.com | Sales |
| maya.petrov@example.com | Engineering |
| nolan.reyes@example.com | Engineering |
| olivia.sandoval@example.com | Human Resources |
| pavel.hartmann@example.com | Engineering |
| quinn.abara@example.com | Finance |
| rosa.lindqvist@example.com | Human Resources |
| samir.haddad@example.com | Sales |
| tessa.moreau@example.com | Sales |

CRITICAL CONSTRAINTS
- Change only what is listed above. Do NOT change any screen (including Employee_List, Employee_Detail and RunTimer), the menu, the role Staff, BootstrapTimer or its schedule, the attributes of Employee other than adding DepartmentId, or any other element. If something not listed seems to need a change, leave it and name it in your summary.
- Use ODC terminology only. Do NOT reference "Service Studio", "eSpace", or other OutSystems 11 concepts.
- Do not add library dependencies. If one is needed, list it in your summary as a manual step.
- If an element named above already exists, update it instead of creating a second one.
- At the end, summarize: what was added or changed (names), the delete rule of DepartmentId, what was skipped (and why), and any manual steps.
Do NOT publish the app in this turn.
