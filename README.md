# Employee Catalog builds

The same small app, built twice on OutSystems Developer Cloud (ODC) with two AI-assisted approaches. The repo holds the specs, prompts and verification reports from both builds, so you can compare how each one went.

## The app

Employee Catalog is a read-only staff directory built as a Reactive Web app.

- Staff sign in with the standard ODC login.
- They see a list of active employees and can search by first or last name.
- They can open one employee to see all of that employee's details.
- Inactive employees are hidden.
- A later change adds a `Department` static entity (Engineering, Finance, Human Resources, Sales), a department column and a department filter.
- Data is 20 fictional employees on the reserved `example.com` domain.

## The two builds

| | [`MCP/`](MCP) | [`MentorWeb/`](MentorWeb) |
|---|---|---|
| App name on ODC | `EmployeeCatalogMCP` | `EmployeeCatalogMW` |
| Approach | Kiro drives ODC Mentor through the OutSystems MCP, using the spec-driven-build skill | Requirements written as a BRD and uploaded to Mentor Web |
| Input | Kiro spec converted to `spec.md` | Generated BRD in `BRD/` |
| Human gates | Confirm before every tenant write and every publish | Prompts run in Mentor Web and Kiro |
| Verification | Full graph comparison of each published revision against the previous one | Checks of the app against the requirements |

Both builds follow the same flow: requirements, build, verify against the requirements, then each later change as its own spec. The `add-department` change was applied to both.

## Repository layout

```
MCP/
  .kiro/steering/       project rules for the Kiro agent
  .kiro/specs/          employee-catalog and add-department specs
  spec-driven-build/    working files for the spec-driven-build skill (spec.md, results, session log)
  Prompts/              the numbered prompts sent to Kiro and Mentor
  Reports/              requirement checks, interventions log, graphdiff comparisons, architecture view
  templates/            requirements and change-requirements templates

MentorWeb/
  .kiro/                steering and specs
  BRD/                  BRD generated from the requirements, for Mentor Web upload
  Prompts/              prompts used in Mentor Web and Kiro
  Reports/              verification reports, working notes, graph comparisons
  templates/            requirements and change-requirements templates
```

Good places to start:

- Requirements: `MCP/.kiro/specs/employee-catalog/requirements.md`
- Rules the agent worked under: `MCP/.kiro/steering/mcp.md`
- What went wrong and how it was handled: `MCP/Reports/interventions.md`
- Build outcome: `MCP/spec-driven-build/EmployeeCatalogMCP/build-report.md`
- Verification of the MentorWeb build: `MentorWeb/Reports/EmployeeCatalogMW-verification-report.md`

## Notes on this copy

- This is a sanitized export. Tenant names, user identities, local paths and OutSystems asset, environment and build keys were replaced with placeholders, so URLs such as `your-tenant-dev.outsystems.app` and the keys do not resolve to a real tenant.
- Screen recordings, raw agent session logs and exported model files (`.xre`) are not included.
- The files refer to a shared, read-only base workspace called SDD Base, which holds generic steering and guides. It is not part of this repo.
- The build was done with the tools and skills available in November 2026. Treat the reports as a record of that run and not as a guaranteed recipe.

## Reproducing

This repo is documentation and not a runnable project. To redo a build you need an ODC tenant, the OutSystems MCP server and Kiro or a similar agent. Start from `MCP/templates/requirements.md` or `MentorWeb/templates/requirements.md` and follow the flow in the steering file.
