# Case study fields (checked against the platform code, 2026-10-22)

Post type: `case-studies`. Public address: `/case-studies/<slug>/`.

## Abilities

| Ability | Parameters |
|---|---|
| `ucre-subscriber/list-case-studies` | `post_status` (`draft`, `publish`, `pending`, `any`), `per_page` (max 200), `page` |
| `ucre-subscriber/get-case-studies` | `post_id` (required, a number). The answer also has `copy` (the saved story) and `copy_fingerprint` when this login may save it. |
| `ucre-subscriber/create-case-studies` | `post_title` (required), and either `fields` (object, every value a string) or `copy`, never both |
| `ucre-subscriber/update-case-studies` | `post_id` (required), then either `post_title` and/or `fields`, or `copy` with `copy_fingerprint` |
| `ucre-subscriber/publish-case-studies` | `post_id` (required). Draft to live only. |
| `ucre-subscriber/list-deals`, `get-deals`, `update-deals` | Same shapes |
| `ucre-subscriber/get-listings` | `post_id` |
| `ucre-subscriber/set-case-study-permissions` | `post_id` (required); `client_named` (true/false); `figures_shown` (true/false); `list_price` (digits, `""` clears); `lead_agent` (agent profile ID, or `"me"`); `team` (list of agent profile IDs, `[]` clears) |
| `ucre-subscriber/request-media-upload` | `post_id`, `field` (`ucre_cs_featured_image` or `ucre_cs_gallery`), `count` (gallery only, up to 20 per request, 30 in all) |
| `ucre-subscriber/attach-media` | `tokens` (list of strings), `post_id`, `field` |

No other parameters are accepted.

## Value rules

Every value is a string. Dates are `YYYYMMDD`. A link to another item is its ID as a
string. Choice values must match exactly; nothing checks them on save.

## Fields the connector will save

| Field | Value | Shown on the public page |
|---|---|---|
| `ucre_cs_location` | `City, ST` (two-letter state) | Yes |
| `ucre_cs_deal_type` | See list below | No |
| `ucre_cs_property_type` | `office`, `industrial`, `retail`, `multifamily`, `land`, `hospitality`, `mixed_use`, `special_purpose`, `self_storage` | Yes |
| `ucre_cs_close_date` | `YYYYMMDD` | Yes ("Closed") |
| `ucre_cs_agent_role` | `seller`, `buyer`, `both` | No |
| `ucre_cs_related_listing` | Listing ID. An advisor or staff login may link only its own listings. Send `"0"` to clear. | Link to the listing |
| `ucre_case_study_context` | Private notes ("Rough Context / Notes"): the facts and the advisor's answers | **No. Private since 2026-10-13; never printed** |

`ucre_cs_deal_type` values: `office_lease`, `office_sale`, `industrial_lease`,
`industrial_sale`, `retail_lease`, `retail_sale`, `multifamily_sale`, `land_sale`,
`investment_sale`, `tenant_rep`, `landlord_rep`, `1031_exchange`, `build_to_suit`,
`sale_leaseback`.

On the deal: `ucre_deals_case_study` = the case study's ID as a string (set it with
`update-deals` after the case study is published).

## Saving the story

The story goes in a separate `copy` object, not in `fields`.

| Part | Copy key | Shape | Tab on the edit page |
|---|---|---|---|
| Headline | `ucre_case_study_headline` | Plain text | 1. Overview, "Marketing Headline" |
| Summary | `ucre_case_study_summary` | HTML | 1. Overview, "Executive Summary" (some site designs do not print it) |
| Challenge | `ucre_case_study_challenge` | HTML | 2. Challenge |
| Strategy | `ucre_case_study_strategy` | HTML | 3. Strategy |
| Outcome | `ucre_case_study_outcome` | HTML | 4. Outcome |
| Lessons | `ucre_case_study_lessons` | HTML | 4. Outcome, "Key Lessons" |
| Testimonial | `ucre_case_study_testimonial` | HTML | 5. Testimonial. Only real, approved words. |
| Search title, description | `ucre_seo_title` (60 max), `ucre_seo_description` (160 max) | Plain | SEO |

`ucre_case_study_linkedin_post` and `ucre_case_study_email_prospect` also exist. Leave
them empty unless the advisor asks.

Rules the site enforces:
- **Update needs a fingerprint** from the latest `get-case-studies`. A stale one is
  refused ("stale_copy") and nothing is saved.
- **One kind of write per call.** `copy` cannot go with `fields` or `post_title`.
- **All or nothing.** One bad part (unknown key, too long, a script or embed, a
  shortcode) refuses the whole call.
- **Limits.** HTML up to 256 KB; plain text up to 10,000 characters; whole call 1 MB.
- **The answer** has `copy_fields_updated` (the keys saved) and `review_flags`:
  `confidential_figure_match` (the price, or a figure worked out from it, while figures
  are not approved) and `unresolved_placeholder` (a blank left in the text).

## Set with `set-case-study-permissions`, never in `fields`

| Part | Parameter | Notes |
|---|---|---|
| Client may be named | `client_named` | `true` only if the advisor said the client approved |
| Price and figures may be shown | `figures_shown` | `true` only if the advisor said so |
| Asking price | `list_price` | Printed on the public page if filled. Only when approved. |
| Lead agent | `lead_agent` | `"me"` for your own profile, or an agent profile ID |
| Team | `team` | Agent profile IDs credited on the case study |

Sending these in `fields` is refused (`ucre_cs_list_price`, `ucre_cs_agent`,
`ucre_cs_team`). Audio and documents (`ucre_case_study_audio`,
`ucre_case_study_documents`) are edit-page only.

The site also has its own Case Study Builder (The Deal, Materials, Your Story,
Generate, Review). If the advisor would rather record the story and let the site write it, that
is his choice; the same rules on names and prices apply to what it writes.

## Deal fields you will read with `get-deals`

`ucre_deals_type`, `ucre_deals_representation`, `ucre_deals_property_type`,
`ucre_deals_address`, `ucre_deals_city`, `ucre_deals_state`, `ucre_deals_sf`,
`ucre_deals_close_date`, `ucre_deals_listing`, `ucre_deals_case_study`,
`ucre_deals_confidential`, `ucre_deals_value`, `ucre_deals_client_name`.

`ucre_deals_confidential` = 1 means the price is private. Treat `ucre_deals_value` and
`ucre_deals_client_name` as private whatever the flag says, until the advisor approves.

## Who can do what

- Director account: everything, including the story.
- Advisor account: own case studies and deals, including the story, publish and photos.
- Staff account: own draft case studies only, including the story while it is a draft.
  No deals, no photos, no publish.
