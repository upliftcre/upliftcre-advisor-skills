# Article fields (checked against the platform code, 2026-10-22)

Post type: `articles`. Public address: `/blog/<slug>/`.

## Abilities

| Ability | Parameters |
|---|---|
| `ucre-subscriber/list-articles` | `post_status` (`draft`, `publish`, `pending`, `any`), `per_page` (max 200), `page` |
| `ucre-subscriber/get-articles` | `post_id` (required, a number). The answer also has `copy` (the saved text) and `copy_fingerprint` when this login may save text. |
| `ucre-subscriber/create-articles` | `post_title` (required), and either `fields` (object, every value a string) or `copy` (see "Saving the text"), never both |
| `ucre-subscriber/update-articles` | `post_id` (required), then either `post_title` and/or `fields`, or `copy` with `copy_fingerprint` |
| `ucre-subscriber/publish-articles` | `post_id` (required). Draft to live only. |
| `ucre-subscriber/request-media-upload` | `post_id`, `field`: `"featured_image"` |
| `ucre-subscriber/attach-media` | `tokens` (list), `post_id`, `field`: `"featured_image"` |
| `ucre-subscriber/get-site-options` | `keys`: `[]` (always send `keys`, an empty list is fine) |

No other parameters are accepted. A create or update with any extra key is rejected.

## Fields the connector will save

| Field | What to put |
|---|---|
| `ucre_article_topic` | One or two sentences on what the article covers |
| `ucre_article_type` | One value from the list below |
| `ucre_article_suggested_topics` | Section headings, one per line |
| `ucre_article_notes` | Short working note (date written, data date) |

`ucre_article_type` values (send the left side exactly):

| Value | Meaning |
|---|---|
| `market_insight` | Market insight / analysis |
| `thought_leader` | Thought leadership |
| `how_to` | How-to / guide |
| `trend_report` | Trend report |
| `case_highlight` | Deal recap |
| `opinion` | Opinion / commentary |
| `educational` | Explainer |
| `listicle` | List article |

Do not send `ucre_article_kind`. The site sets it.

## Saving the text

The article text and the search title and description go in a separate `copy` object,
not in `fields`.

| Copy key | What it is | Where it shows |
|---|---|---|
| `post_content` | The whole article, as HTML | The article body. The site picks where to store it; the answer says which in `copy_body_storage`. Either way the page prints it. |
| `ucre_seo_title` | Search title, 60 characters or fewer | Search results |
| `ucre_seo_description` | Search description, 160 characters or fewer | Search results |

Other copy keys exist (`ucre_articles_hook`, `ucre_article_key_takeaways`,
`ucre_articles_summary`, `ucre_articles_linkedin_post`, `ucre_articles_email_teaser`,
`ucre_articles_author_byline`, `ucre_articles_implications`,
`ucre_articles_advisor_take`, `ucre_articles_action_items`,
`ucre_articles_email_alert`). Leave them empty unless the advisor asks.

Rules the site enforces:
- **Update needs a fingerprint.** `update-articles` with `copy` must also send
  `copy_fingerprint` from the latest `get-articles`. If the text changed since then the
  site refuses ("stale_copy") and saves nothing. Read again and retry once.
- **One kind of write per call.** `copy` cannot go with `fields` or `post_title`.
- **All or nothing.** One bad part (an unknown key, too long, a script or embed, a
  shortcode) refuses the whole call and saves nothing.
- **Limits.** Article HTML up to 256 KB; plain text up to 10,000 characters; whole call
  up to 1 MB.
- **HTML is cleaned** to the normal post set (headings, paragraphs, lists, links, bold,
  tables). Square brackets are turned into safe characters.
- **The answer** has `copy_fields_updated` (the list of keys saved) and `review_flags`.

## What the connector still will NOT save (done by hand on the edit page)

| Thing | Where on the edit page |
|---|---|
| Category | Categories box. The connector cannot set categories. |
| Author | "Author" (choose the advisor). The site refuses `ucre_articles_author`. |

There is no excerpt field: the site makes the short preview from the start of the
article, so make the first lines count.

## Categories

The connector cannot read or set categories, and every site has its own list. Suggest
one to three in plain words (for example "Land" or "Leasing"). The person picks from
the site's own list on the edit page.

## Who can do what

- Director account: everything above, including saving the text and publishing.
- Staff account: draft and edit own drafts only, including saving the text while it is
  a draft. No publish, no photo upload.
- Advisor account: no article abilities at all today.
