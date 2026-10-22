# Linking to pages on the advisor's website

The connector cannot list the site's pages, towns or glossary terms. So:

- **Listings, reports, deals, case studies, articles:** never build the address by hand.
  Call the `list-*` or `get-*` ability and use the `permalink` of a **published** item.
- **Other pages:** UpliftCRE sites usually have the paths below. Before you link one,
  open it once (web fetch) and check it loads and is the right page. If you cannot
  check it, leave the link out.

| Page | Usual path |
|---|---|
| Listings | `/listings/` |
| Market reports | `/market-reports/` |
| Track record (closed deals) | `/track-record/` |
| Case studies | `/case-studies/` |
| Articles | `/blog/` |
| Glossary | `/glossary/` and `/glossary/<term-slug>/` |
| Team | `/team/` |
| Contact | `/contact/` |
| Services | `/services/<slug>/` |
| Town or county pages | `/locations/<slug>/` |

The site's own address is `ucre_brand_office_website` from `get-site-options`. If it is
empty, take it from any `permalink` the connector returned.

## Market area IDs

Listings and market reports link to a town or county page by its **ID**
(`ucre_listing_market`, `ucre_reports_market_area`). There is no ability to look IDs up.
Get one this way, in order:

1. Another listing or report in the same area already has it: read that item with
   `get-listings` or `get-market-reports` and reuse the value.
2. The advisor gives it to you.
3. Otherwise leave the field empty and put "set the market area" on the to-do list.

Never guess an ID.
