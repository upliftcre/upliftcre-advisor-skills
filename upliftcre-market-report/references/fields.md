# Market report fields (checked against the platform code, 2026-10-22)

Post type: `market-reports`. Public address: `/market-reports/<slug>/`.
All market report abilities are Director-only.

## Abilities

| Ability | Parameters |
|---|---|
| `ucre-subscriber/list-market-reports` | `post_status` (`draft`, `publish`, `pending`, `any`), `per_page` (max 200), `page` |
| `ucre-subscriber/get-market-reports` | `post_id` (required, a number). The answer also has `copy` (the saved report) and `copy_fingerprint`. |
| `ucre-subscriber/create-market-reports` | `post_title` (required), and either `fields` (object, every value a string) or `copy`, never both |
| `ucre-subscriber/update-market-reports` | `post_id` (required), then either `post_title` and/or `fields`, or `copy` with `copy_fingerprint` |
| `ucre-subscriber/publish-market-reports` | `post_id` (required). Draft to live only. |

No other parameters are accepted.

## Fields the connector will save

| Field | Value |
|---|---|
| `ucre_reports_market_area` | Location ID as a string. There is no lookup: reuse the ID from an earlier report or listing in the same area, or one the advisor gives you. Otherwise leave it empty. |
| `ucre_reports_property_type` | `office`, `industrial`, `retail`, `multifamily`, `land`, `hospitality`, `mixed_use`, `special_purpose`, `self_storage`, `all` |
| `ucre_reports_period` | `2026-Q4`, `2026-Q3`, `2026-Q2`, `2026-Q1`, `2025-Q4`, `2025-Q3`, `2025-Q2`, `2025-Q1`, `2024-Q4`, `2025-annual`, `2024-annual`, `custom` |
| `ucre_reports_custom_period` | Free text, only with `custom` (e.g. `Q1 2027`) |
| `ucre_reports_as_of_date` | Last day the data covers, `YYYYMMDD` (e.g. `20260930`) |
| `ucre_reports_published_date` | `YYYYMMDD`. Leave it alone unless the advisor asks. |

Values are stored as sent, with no checking. A misspelled value (`Retail`, `2026 Q3`,
`2026-09-30`) saves and then breaks the page. Send them exactly as written here.

Title pattern used by every live report: `<Area> <Type> Market Report — Q3 2026`
(for example `San Antonio Industrial Market Report — Q3 2026`).

## Saving the report

The report goes in a separate `copy` object, not in `fields`. Text parts are HTML
strings (`<h2>`, `<h3>`, `<p>`, `<ul>`, `<li>`, `<strong>`, `<table>`, `<a>`). Lists of
rows are arrays of objects, and every row must have every cell (use `""` for an empty
one).

| Report file part | Copy key | Shape |
|---|---|---|
| Hero description | `ucre_reports_hero_description` | HTML |
| Summary | `ucre_reports_summary` | HTML |
| Key takeaways | `ucre_reports_key_takeaways` | HTML (`<ul><li>`) |
| Body | `ucre_reports_body` | HTML |
| Outlook | `ucre_reports_outlook` | HTML |
| Advisor's take | `ucre_reports_advisor_take` | HTML |
| Investor implications | `ucre_reports_investor_implications` | HTML |
| Tenant implications | `ucre_reports_tenant_implications` | HTML |
| Method note | `ucre_reports_sources_methodology` | HTML |
| Key metrics rows (number strip and table) | `ucre_reports_data_table` | Rows `{"metric","value","change","note"}`, up to 10 |
| FAQ | `ucre_reports_faq` | Rows `{"question","answer"}` (answer may be HTML), up to 50 |
| Charts | `ucre_reports_charts` | Rows, see below, up to 80 |
| Search title | `ucre_seo_title` | Plain, 60 characters or fewer |
| SEO line | `ucre_seo_description` | Plain, 160 characters or fewer |

`ucre_reports_linkedin_post` also exists. Leave it empty unless the advisor asks.

**Chart rows.** One row per point:
`{"chart_id","chart_title","archetype","series_label","point_label","point_value","unit","vintage"}`.
- `chart_id`: a short name shared by every row of one chart (e.g. `vacancy-trend`). At
  most 4 charts.
- `archetype`: `trend` (a line over quarters), `comparison` (bars side by side),
  `supply_demand` (deliveries against absorption; unit `SF` or `%` only) or
  `composition` (parts of a whole; the parts must add up to 100%, so use it only when
  the data has every part).
- `series_label`: the line or bar group name. One unit per series.
- `point_label`: the quarter or submarket. `point_value`: a plain number, no `$` or `%`.
- `unit`: `%`, `SF`, `$` or `count`.
- `vintage`: the data date, e.g. `Q3 2026`. Never empty.
- A trend line needs at least two points.
- Never put a data vendor or listing site name in any chart text: the site refuses it.
- Every point comes from the fact sheet. If you cannot check a point, leave the chart out.

Rules the site enforces:
- **Update needs a fingerprint** from the latest `get-market-reports`. A stale one is
  refused ("stale_copy") and nothing is saved.
- **One kind of write per call.** `copy` cannot go with `fields` or `post_title`.
- **All or nothing.** One bad part (unknown key, too long, too many rows, a missing
  cell, a chart that fails the checks, a script or embed) refuses the whole call.
- **Limits.** Each HTML part up to 256 KB; plain text up to 10,000 characters; the
  whole call up to 1 MB.
- **The answer** has `copy_fields_updated` (the keys saved) and `review_flags`.
