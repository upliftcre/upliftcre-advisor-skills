# Listing and deal fields (checked against the platform code, 2026-10-22)

Contents: 1. Abilities. 2. Value rules. 3. Listing fields. 4. Subtypes. 5. What
intake-listing-facts accepts. 6. Saving the write-up. 6b. What will not save. 7. Deal
(Track Record) fields. 8. Who can do what.

## 1. Abilities

| Ability | Parameters |
|---|---|
| `ucre-subscriber/list-listings` | `post_status` (`draft`, `publish`, `pending`, `any`), `per_page` (max 200), `page` |
| `ucre-subscriber/get-listings` | `post_id` (required, a number). The answer also has `copy` (the saved write-up) and `copy_fingerprint` when this login may save it. |
| `ucre-subscriber/create-listings` | `post_title` (required), and either `fields` (object, every value a **string**) or `copy`, never both |
| `ucre-subscriber/update-listings` | `post_id` (required), then either `post_title` and/or `fields` (strings), or `copy` with `copy_fingerprint` |
| `ucre-subscriber/intake-listing-facts` | `post_id` (required), `facts` (required; values may be strings or numbers), `source_doc` |
| `ucre-subscriber/publish-listings` | `post_id` (required). Draft to live only. |
| `ucre-subscriber/request-media-upload` | `post_id`, `field` (`ucre_featured_image` or `ucre_gallery`), `count` (gallery only) |
| `ucre-subscriber/attach-media` | `tokens` (list of strings), `post_id`, `field` |
| `ucre-subscriber/list-deals`, `get-deals`, `create-deals`, `update-deals`, `publish-deals` | Same shapes as the listing ones |

No other parameters are accepted. An extra key is rejected.

## 2. Value rules

- Numbers as plain digits in a string: `"799000"`, `"4.93"`. No `$`, commas or units.
- Dates as `YYYYMMDD`: `"20261013"`.
- Yes/no as `"1"` or `"0"`.
- A link to another item is its ID as a string: `"12345"`.
- Choice fields: send the value exactly as written below. `create` and `update` do not
  check it.

## 3. Listing fields the connector will save

**Basics**

| Field | Value |
|---|---|
| `ucre_listing_status` | `Active`, `Under Contract`, `Sold`, `Leased`, `Off-Market`, `Coming Soon` (capitals matter). `Off-Market` and `Coming Soon` keep it off the public lists. |
| `ucre_transaction_type` | `Sale`, `Lease`, `Sale or Lease` |
| `ucre_property_type` | `office`, `industrial`, `retail`, `multifamily`, `land`, `hospitality`, `mixed_use`, `special_purpose`, `self_storage` (lower case) |
| subtype | One field, chosen by the type. See section 4. |
| `ucre_building_name` | Optional name |
| `ucre_property_address` | Street address only |
| `ucre_property_city` | City |
| `ucre_property_state` | Two-letter state, e.g. `TX` |
| `ucre_property_zip` | ZIP |
| `ucre_listing_market` | Location ID as a string. There is no lookup: reuse the ID from another listing or report in the same area, or one the advisor gives you. Otherwise leave it empty. |
| `ucre_date_listed` | `YYYYMMDD` |

**Price**

| Field | Value |
|---|---|
| `ucre_price` | Asking price, digits |
| `ucre_price_display` | Text shown instead of the price, e.g. `Call for Pricing` |
| `ucre_lease_rate` | Lease rate, digits |
| `ucre_lease_period` | `/SF/YR`, `/SF/MO`, `/MO`, `/YR` |
| `ucre_lease_structure` | `NNN`, `Gross`, `Modified Gross`, `Full Service`, `Industrial Gross` |
| `ucre_lease_rate_display` | Text shown instead, e.g. `From $650/MO per suite` |
| `ucre_listing_tier` | `"1"` to show NOI, cap rate and occupancy; otherwise leave empty |
| `ucre_noi`, `ucre_cap_rate`, `ucre_occupancy` | Digits. Cap rate and occupancy as percents (`"7.5"`, `"95"`) |

**Property**

| Field | Value |
|---|---|
| `ucre_building_sf` | Building size in square feet |
| `ucre_lot_size` | Lot size in **acres** |
| `ucre_year_built` | Year |
| `ucre_zoning` | Zoning as stated |
| `ucre_parking_spaces` | Count |
| `ucre_parking_type` | `Surface`, `Structure`, `Underground`, `Roof-Top`, `Other` |
| `ucre_clear_height` | Feet (industrial) |
| `ucre_suite_count` | Count |
| `ucre_tenancy` | `single`, `multi` |
| `ucre_construction_status` | `Existing`, `Under Construction`, `Proposed`, `Build to Suit` |
| `ucre_property_condition` | `Excellent`, `Good`, `Average`, `Fair`, `Poor` |
| `ucre_parcel_apn` | Parcel or property ID |
| `ucre_annual_property_tax` | Dollars per year, digits |
| `ucre_tax_jurisdictions` | Text |
| `ucre_demo_traffic_1_road`, `ucre_demo_traffic_1_count` | Main road and vehicles per day (also `_2_`, `_3_`) |
| `ucre_demo_data_year` | Year of the traffic or area figures |

**Copy and links**

| Field | Value |
|---|---|
| `ucre_elevator_pitch` | One sentence |
| `ucre_exec_summary` | Three to five factual sentences |
| `ucre_video_url`, `ucre_matterport_url`, `ucre_landid_map_url` | Full web addresses |
| `ucre_external_url` | Link to the listing on an outside listing site |
| `ucre_map_pin` | Leave empty unless the advisor gives coordinates |

**After closing**

| Field | Value |
|---|---|
| `ucre_date_closed` | `YYYYMMDD` |
| `ucre_closed_price` | Do not write. Private. |

Do not write `ucre_internal_notes` or `ucre_seller_motivation` unless the advisor asks.

## 4. Subtype fields

Send the one that matches `ucre_property_type`. `mixed_use` has none.

| Type | Field | Values |
|---|---|---|
| office | `ucre_property_subtype_office` | `office_building`, `medical_office`, `creative_loft`, `executive_suites`, `government_institutional`, `office_warehouse`, `coworking_space`, `lab_life_science` |
| industrial | `ucre_property_subtype_industrial` | `warehouse_distribution`, `manufacturing`, `flex_space`, `cold_storage`, `truck_terminal_cross_dock`, `industrial_outdoor_storage`, `data_center`, `office_showroom` |
| retail | `ucre_property_subtype_retail` | `strip_center`, `neighborhood_center`, `community_center`, `power_center`, `freestanding_retail`, `auto_service_repair`, `restaurant_bar`, `qsr_fast_food`, `retail_pad`, `street_retail`, `lifestyle_center` |
| multifamily | `ucre_property_subtype_multifamily` | `garden_low_rise`, `mid_rise`, `high_rise`, `student_housing`, `senior_living`, `affordable_housing_section_8`, `mobile_home_park`, `sfr_portfolio` |
| land | `ucre_property_subtype_land` | `commercial_land`, `residential_land`, `industrial_land`, `ranch_recreational`, `agricultural_farm`, `land_other` |
| hospitality | `ucre_property_subtype_hospitality` | `full_service_hotel`, `limited_service`, `boutique_independent`, `resort`, `extended_stay`, `motel_economy` |
| special_purpose | `ucre_property_subtype_special_purpose` | `car_wash`, `school_education`, `religious_facility`, `marina`, `golf_course`, `event_venue` |
| self_storage | `ucre_property_subtype_self_storage` | `self_storage_facility`, `climate_controlled`, `boat_rv`, `portable_container` |

## 5. What `intake-listing-facts` accepts

Only these. Anything else comes back in `skipped_invalid`.

`ucre_zoning`, `ucre_year_built`, `ucre_building_sf`, `ucre_lot_size`,
`ucre_clear_height`, `ucre_parking_spaces`, `ucre_parking_type`, `ucre_suite_count`,
`ucre_tenancy`, `ucre_construction_status`, `ucre_property_condition`,
`ucre_property_type`, the eight subtype fields, `ucre_building_name`,
`ucre_property_address`, `ucre_property_city`, `ucre_property_state`,
`ucre_property_zip`, `ucre_price`, `ucre_lease_rate`, `ucre_lease_period`,
`ucre_lease_structure`, `ucre_noi`, `ucre_cap_rate`, `ucre_occupancy`,
`ucre_demo_traffic_1_road` / `_count` (also `_2_`, `_3_`), `ucre_demo_employers`,
`ucre_demo_developments`, `ucre_parcel_apn`, `ucre_annual_property_tax`,
`ucre_tax_jurisdictions`, `ucre_assessed_value`, `ucre_legal_description`.

It refuses numbers outside these ranges (it never rescales them):

| Field | Allowed |
|---|---|
| `ucre_price` | 1,000 to 500,000,000 |
| `ucre_cap_rate` | 1 to 25 (percent, so `7.5`, not `0.075`) |
| `ucre_occupancy` | 1 to 100 |
| `ucre_year_built` | 1800 to 2100 |
| `ucre_lot_size` | 0.01 to 5,000 acres |
| `ucre_clear_height` | 6 to 120 feet |
| `ucre_annual_property_tax` | 10 to 5,000,000 |
| `ucre_assessed_value` | 100 to 500,000,000 |

The address must be the property's own address, never the owner's mailing address.
Status, sale-or-lease, date listed, market area, pitch and summary are **not** accepted
by intake: send those with `create-listings` or `update-listings`.

## 6. Saving the write-up

The public write-up goes in a separate `copy` object, not in `fields`.

| Copy key | What it is | Shape |
|---|---|---|
| `ucre_listings_property_description` | Property Description, 150 to 250 words | HTML (`<p>`, `<ul>`, `<li>`, `<strong>`) |
| `ucre_highlights` | Highlight bullets | Rows `[{"highlight": "..."}]`, up to 50 (use three to six) |
| `ucre_seo_title` | Search title | Plain, 60 characters or fewer |
| `ucre_seo_description` | Search description | Plain, 160 characters or fewer |

Other copy keys exist. Leave them empty unless the advisor asks: `ucre_listings_buyer_personas`,
`ucre_listings_hbu_analysis`, `ucre_listings_financial_summary`,
`ucre_listings_location_intelligence`, `ucre_listings_talking_points`,
`ucre_listings_objections`, `ucre_listings_linkedin_post`,
`ucre_listings_facebook_post`, `ucre_listings_reel_script`, `ucre_listings_hashtags`
(plain), `ucre_listings_email_buyer`, `ucre_listings_email_broker`,
`ucre_listings_email_seller`. The house rules apply to every one.

Rules the site enforces:
- **Update needs a fingerprint** from the latest `get-listings`. A stale one is refused
  ("stale_copy") and nothing is saved.
- **One kind of write per call.** `copy` cannot go with `fields` or `post_title`.
- **All or nothing.** One bad part (unknown key, too long, a missing cell, a script or
  embed, a shortcode) refuses the whole call.
- **Limits.** HTML up to 256 KB; plain text up to 10,000 characters; whole call 1 MB.
- **The answer** has `copy_fields_updated` (the keys saved) and `review_flags`. A
  `confidential_rent_roll_match` flag means the text repeats a private rent-roll figure.

## 6b. What will not save (a person does it on the edit page)

Refused fields come back in `fields_refused` with a reason.

| Thing | Field | Where on the edit page |
|---|---|---|
| Primary Agent, Co-Agent | `ucre_listing_agent`, `ucre_co_agent` | "Agent Assignment" tab |
| Public OM, documents, floor plans | `ucre_public_om`, `ucre_public_docs`, `ucre_floor_plans` | "Documents" and "Photos & Videos" tabs |
| Location and memo highlight lists | `ucre_location_highlights`, `ucre_memo_highlights` | "Marketing Inputs" tab |
| Unit mix and tenant rows | `ucre_units_rows`, `ucre_tenancy_rows` | "Units" and "Pricing & Financials" tabs |
| Buyer, seller and contract details | `ucre_listing_buyer_*`, `ucre_listing_seller_*`, `ucre_listing_contract_*` | "Deal Tracking" |

`get-listings` returns `ucre_listing_agent` (read only), so you can see who the primary
agent is. A listing created by the Director account
starts with no primary agent. A listing created by an advisor's own login starts with
that advisor as primary agent.

## 7. Deal (Track Record) fields the connector will save

Post type `deals`. Public address `/track-record/<slug>/`.

| Field | Value |
|---|---|
| `ucre_deals_type` | `sale`, `lease`, `sale_leaseback`, `ground_lease`, `investment`, `sublease` |
| `ucre_deals_representation` | `seller`, `buyer`, `landlord`, `tenant`, `dual` |
| `ucre_deals_property_type` | Same nine values as `ucre_property_type` |
| `ucre_deals_address` | Street address |
| `ucre_deals_city`, `ucre_deals_state` | City; two-letter state |
| `ucre_deals_sf` | Building square feet, digits |
| `ucre_deals_close_date` | `YYYYMMDD`. Required: do not create a deal without it. |
| `ucre_deals_confidential` | `"1"` = price hidden. Always `"1"` unless the advisor says the client approved showing it. |
| `ucre_deals_value` | Dollars, digits. Only if the advisor gives it. |
| `ucre_deals_value_type` | `sale_price`, `total_lease`, `annual_rent` |
| `ucre_deals_listing` | The listing's ID as a string |
| `ucre_deals_case_study` | A case study's ID as a string |
| `ucre_deals_client_name` | Leave empty unless the advisor says the client approved being named |

Will not save: the team members on the deal (`ucre_deals_agents`), the deal's write-up
(`ucre_deals_summary`, `ucre_deals_narrative` and the rest), lease term and rate. A
photo goes on with `request-media-upload` using `"field": "featured_image"`.

## 8. Who can do what

- Director account: everything, on every listing and deal, including the
  write-up.
- Advisor account: own listings and deals only, including the write-up, publish and
  photos.
- Staff account: draft listings only, including the write-up while it is an own draft.
  No publish, no photos, no deals.
