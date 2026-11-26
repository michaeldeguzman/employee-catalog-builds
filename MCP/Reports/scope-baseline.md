# Scope baseline (task 4)

Recorded read-only from the tenant before any write to EmployeeCatalogMCP. Used by the final scope check (task 13).

## EmployeeCatalogMW (must stay unchanged)

| Field | Value |
|---|---|
| Name | EmployeeCatalogMW |
| assetKey | 07a64c21-0c8c-8afb-28ee-5d8530d55cf8 |
| Latest revision | 6 |
| revisionDateTime | 2026-11-21T10:56:49.208634Z |
| modelDigest | 35873f58-1351-11c1-6d2d-9ad864ae3a67 |
| Deployed in Development (env 8b036dbd-6d28-2b5c-c50a-77a6bc07d748) | revision 6, buildKey 298fc5bd-cadd-5ca4-d36c-a03d7d603cf1, deploymentKey 54d13cb0-0fb9-3a77-32df-59ccb42cb1fd |
| portfolioKey | 2361d977-28e7-c828-d75b-302e87dcb460 |

Revision history (newest first, top 3 of 6): 6 (2026-11-21T10:56:49Z), 5 (2026-11-21T10:47:43Z), 4 (2026-11-21T10:42:58Z).

## Portfolio

- Key: `2361d977-28e7-c828-d75b-302e87dcb460`
- Name: not exposed. `app_list`, `app_info`, `app_revisions`, `env_list` and `env_app` return only the key. The Development environment (`env_list`) carries the same portfolioKey.

## Other apps seen in the search for "EmployeeCatalog" (not to be touched)

- `Employee Catalog`, assetKey 31b31b9c-c028-bfee-1811-c6b59aba4b5b, revision 6, same portfolio.

## Name check

- `app_list` search "EmployeeCatalogMCP" returned 0 results (2026-11 tenant listing at the time of this task). No exact match, so the app does not exist yet as a published app.

## Tenant

- Development environment key: `8b036dbd-6d28-2b5c-c50a-77a6bc07d748` (domain your-tenant-dev.outsystems.app, region ap-southeast-1). Only environment on the tenant.
