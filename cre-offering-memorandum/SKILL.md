---
name: cre-offering-memorandum
description: Build a branded offering memorandum (OM) PowerPoint for a commercial listing on the KW Commercial, eXp Commercial, SVN, Coldwell Banker Commercial or NAI Global OM template. Starts with an agent interview and a document checklist, then fills the brand's OM template.
---

# Brand OM Builder

This skill turns a listing into a polished 15-page offering memorandum (OM) built on the agent's brand template. It runs in seven stages: brand, interview, documents, fact sheet, build, check, deliver.

**Who you're working with.** The agents are commercial real estate advisors, not tech people. Write in plain English, keep questions short, and end every message with a clear next step. Never say "placeholder", "XML" or "script" to them. Say "I'll fill that in" or "that's marked TBD".

## Stage 0: Pick the brand template

Ask which brand the agent is with, unless they already said. There is one template per brand:

| Brand | Template file name starts with |
|---|---|
| KW Commercial | `KW Commercial OM Template` |
| eXp Commercial | `eXp Commercial OM Template` |
| SVN | `SVN OM Template` |
| Coldwell Banker Commercial | `Coldwell Banker Commercial OM Template` |
| NAI Global | `NAI Global OM Template` |

The templates are free to download from the `om-templates` folder of github.com/upliftcre/upliftcre-advisor-skills; the agent saves the one for their brand to their own folder.

Search the agent's connected folders for a PowerPoint file whose name *starts with* that text, so a renamed suffix ("- DO NOT TOUCH") still matches. If more than one matches, ask which one and say which file you used. If none matches, ask the agent for the template; never build an OM from scratch, and never use another brand's template.

## Stage 1: Interview the agent

Ask these questions a few at a time (no more than 5 per message), in this order. Skip anything the agent already told you. "I don't know" is a fine answer: write it down as an open question and keep going.

**The basics**
1. What's the property address, or how do you describe the location (for example, "S IH 37 at S Presa St")?
2. What type of property is it: land, industrial, retail, office, multifamily, or mixed use? Is an operating business sold with it (for example a restaurant)?
3. What's the asking price? Is it priced per acre, per square foot, or as a total?
4. How big is it (acres and/or building square feet)? Where does that number come from (survey, appraisal district, MLS)?
5. Which folder holds this listing's files?

**The story**
6. Who owns it and why are they selling? Is there anything special about the history (long family ownership, first time on the market, estate sale)?
7. In one sentence, who is the ideal buyer (developer, investor, owner-user, industrial user)?
8. What are the three best things about this property?
9. What will a buyer worry about (floodplain, zoning, no sewer, easements, access, tenants)?

**Facts you may know offhand**
10. Zoning? Utilities (water, sewer, electric, gas)? Any floodplain?
11. Road frontage and access? Traffic counts if you have them?
12. For buildings: year built, occupancy, tenants and leases, NOI or cap rate?
13. Do the mineral rights go with the sale? Any leases, easements or ag exemption?
14. Who signs for the seller? Flag estates, trusts and multiple owners early.

**You and your office** (these go on every page)
15. Which agent or agents go on the OM? For each: name, title, mobile phone, email.
16. Your team or office name, and the website to show (for example "Smith Industrial Group | smithindustrial.com").
17. Your office phone, and the legal name and license number of the brokerage that holds your license.

**Marketing**
18. Is there anything you don't want in the OM (seller's name, reason for sale, price)? For a business sale, must the sale stay confidential (staff and customers may not know)?
19. When do you need it?

## Stage 2: Give the agent a document checklist

After the interview, send one checklist tailored to the property type. Ask them to drop everything into the listing folder. Mark the items you already have.

**Every listing**
- Photos: drone/aerial shots plus 10-12 ground photos. A good cover shot is the most important.
- Survey or site plan (PDF).
- A property report from their data tools (zoning, flood zone, taxes, owner and legal description).
- A trade area report for the ZIP code (traffic counts, ZIP growth, daytime population), for example from RPR.
- MLS or listing-platform printout.
- A sale comps report with 6-10 comparable sales.
- Map exports: location map, aerial with boundary, nearby employers.
- Appraisal district (CAD) or county assessor page for the parcel.
- Listing agreement (to confirm the seller's legal name).

**Land, add:** FEMA flood map or the surveyor's floodplain acreage, a utility letter from the local utility, any easement or title documents, and any zoning verification letter.

**Buildings, add:** rent roll, leases or lease abstracts, an operating statement (income and expenses or T-12), floor plans, building specs (clear height, docks, power, HVAC, roof age), and the Phase I environmental report if there is one.

**Business sale (a restaurant or other operating business), add:** profit and loss statements for the last 3 years plus year to date, sales tax reports, business tax returns, an equipment and furniture (FF&E) list showing what stays, a staff summary (headcount and roles, no names), permits and licenses (health permit, liquor license if it sells alcohol), equipment leases and vendor contracts, and what transfers with the sale (trade name, website, phone number, online ordering and social pages). Ask about the asking price split between real estate and business, a training period, and whether the sale must stay confidential.

**Every listed agent:** a headshot, and the state's required brokerage disclosure form if there is one (in Texas, a current IABS form).

When the agent says the files are in, read every one before building. Skim PDFs page by page, and pull text from the PDFs and images out of them.

## Stage 3: Build a fact sheet and conflict list

Before touching the deck, write down every fact with its source. List every conflict you find, because these are the things that embarrass an agent. Common ones:

- **Size:** survey vs. appraisal district vs. MLS. Use the survey and say so.
- **Flood zone:** the MLS often says "Zone X" when the property report or FEMA shows AE or A.
- **Taxes and assessed value:** these differ between reports. Tell the agent to confirm on the appraisal district site before quoting.
- **Price per acre or SF:** recompute it from the price and the surveyed size. The MLS may have used a rounded size.
- **Zoning:** the reports may disagree with what the agent says. Show what the agent says and note the source.
- **Owner of record:** an estate means signing authority is a question.
- **Agent contact info** that's out of date on reports (old emails, old brokerage names). Check each agent's phone and email against their profile page on the brand or team website, and their disclosure form. Flag any difference.
- **Listing history:** RPR and listing sites show past listings and price cuts. Buyers will see them, so tell the agent.

Never put a number in the OM that a source told you not to quote, such as an eyeball floodplain estimate.

## Stage 4: Build the deck from the template

Copy the brand template into the listing folder as `<Short property name> OM.pptx`. Never edit the template itself.

**How to fill it.** Use python-pptx.
- Replace each `{{TOKEN}}` with the run's text so the formatting stays. Some runs have a hint sentence after the token, for example `{{COVER_SUMMARY}} Three or four sentences...`. Replace the whole run text.
- For picture placeholders, center-crop the real image to the frame's aspect ratio with PIL. Then add it as an image part and point the existing picture's `a:blip r:embed` at it, so the frame keeps its size and position. Remove any `a:srcRect`.
- After swapping pictures, drop image relationships the slide no longer uses, so old pictures don't bloat the file.
- For table rows, fill each cell directly by row and column.
- When a page doesn't fit the property, delete the page or rename its title. For example, rename Highest & Best Use to "Investment Highlights" for a leased building, or to "Best Use & Buyer Fit" for a business sale.
- Only change the picture you mean to change. Every page has a header-bar picture, a header logo and a footer logo, so pick a picture frame by its position and size, not by size alone. **Never replace or recolor the brand logos or the header bar.**
- If a photo, map or survey is missing, keep the template's labeled frame (for example "COVER PHOTO") so the agent sees what is still needed. Never leave a photo from another listing in the deck.

**Agent and office tokens (every page).**
- Footer: AGENT_NAME, AGENT_TITLE, AGENT_PHONE, AGENT_EMAIL, plus TEAM_NAME and WEBSITE under the logo. The phone and email runs are links: set the link to `tel:<digits>` and `mailto:<email>` at the same time you set the text.
- Page 13: AGENT_BIO, AGENT_NAME and AGENT_PHONE. Page 14: AGENT_NAME, AGENT_TITLE, AGENT_PHONE, OFFICE_PHONE and AGENT_EMAIL.
- Page 15: TEAM_NAME, STATE, BROKERAGE_LEGAL_NAME and BROKERAGE_LICENSE. Keep the brand's "independently owned and operated" sentence where the template has one.
- STATE is the two-letter state on the cover and demographics pages, and the full state name is fine on page 15.

**Titles.** Use the title the agent gives you. In Texas, call an individual agent "Commercial Advisor" (not "Broker") unless they hold a broker license.

**Price not set yet.** Put "PRICE TBD" in the price badge and the price tile. Use the PPU slot for another fact (for example LOT ACRES / 0.74). On the Sale Comparables page, show the subject's price and price per unit as TBD.

**More than one agent.** Add an agent only when asked. For each extra agent:
- Footer, every page: put a contact box for each agent side by side to the right of the logo, at 11pt with four lines (name, title, phone, email). Make the email a mailto link. Keep every box inside the footer band and above the bottom edge.
- Add an About Us page for the agent: copy page 13, swap in their headshot and a short first-person bio. Base the bio on their profile page, and ask the agent to approve it. If there is no headshot yet, keep the labeled "AGENT PHOTO" frame.
- Add their disclosure form as its own page, if their state has one.

**Pages and tokens**
1. **Cover.** HEADLINE (for example "111.65 Acres on Interstate 37 in San Antonio, TX"), the cover photo, PRICE (badge), SIZE_LABEL/SIZE (for example ACRES / 111.65), ZONING, PPU_LABEL/PPU (for example PRICE / ACRE / $18,809), ADDRESS, CITY, STATE, ZIP, COUNTY and COVER_SUMMARY (3-4 sentences).
2. **At a Glance.** Eight tiles: PRICE, SIZE, PPU and ZONING, plus STAT_5 to STAT_8, each with a _LABEL. Good picks are traffic count, frontage, utilities, ownership history, year built, occupancy and cap rate. Below the tiles goes OPPORTUNITY, a full paragraph.
3. **Property Highlights.** HIGHLIGHT_1 to HIGHLIGHT_10, LOCATION_1 to LOCATION_6 and the location map photo. Keep each bullet to one line and delete unused ones.
4. **Highest & Best Use.** USE_1/2/3_TITLE and _TEXT (primary, secondary and value add), CONSIDERATION_1 to CONSIDERATION_4 (what a buyer must plan for), and the broker-opinion footnote.
5-6. **Property Photos.** Twelve photo frames. Delete the second page if there are fewer than 7 photos.
7. **Aerial Map.** An aerial with the property boundary outlined.
8. **Labeled area map.** An aerial with nearby employers, highways and landmarks labeled. Draw the labels with PIL as white rounded boxes with dark text in the brand's heading color, and make the subject label the brand's accent color.
9. **Survey.** The survey or site plan, cropped to the drawing.
10. **Sale Comparables.** Three tiles: BEST_COMP_PPU/NAME/NOTE (the most supportive nearby comp), AVG_COMP_PPU with COMP_COUNT and COMP_YEARS, and the subject's PPU. The table has a subject row plus COMP_1 to COMP_8 (Property, County, Sold, Price, Size, $/Unit, Miles), then COMP_SOURCE. Sort by relevance and put the best comp first. Measure miles straight-line and say so.
11. **Demographics.** POP, HH, HHSIZE, AGE, INCOME and HOMEVAL for 1, 3 and 5 mile rings.
12. **Market Overview.** TRAFFIC_1 to TRAFFIC_3 (count, ROAD, WHERE), plus ZIP_POP, ZIP_GROWTH and DAYTIME_POP with their notes, YEAR, and MARKET_SOURCES. A trade area report has most of this.
13. **About Us.** The agent photo and bio.
14. **Brokerage Disclosure.** Replace the labeled frame with each listed agent's state disclosure form (render the PDF at 200 dpi). In Texas this is the IABS form. If the state has no required form, delete the page. If a form is missing, put it on the open questions list.
15. **Confidentiality & Disclaimer.** ADDRESS, CITY, STATE, ZIP, TEAM_NAME and the brokerage tokens.

**Demographics method.** If the agent has no paid demographics report:
- Geocode the address with the Census geocoder (geocoding.geo.census.gov, onelineaddress, benchmark Public_AR_Current).
- Get **census block** centroids within 5 miles and their 2020 population (POP100, CENTLAT, CENTLON) from Census TIGERweb (tigerWMS_Census2020: layer 10 is blocks, layer 8 is block groups, layer 6 is tracts). Use blocks, not block groups: in rural areas no block group centroid may fall inside the 1-mile ring, and the ring then shows zero.
- Get each tract's total 2020 population by adding up its block groups (layer 8, `GEOID LIKE '<tract>%'`).
- Get ACS 5-year tract values from the Esri Living Atlas layer **ACS Population and Housing Basics** (P3ePLMYs2RVChkJx.svcs.arcgis.com, `ACS_Population_and_Housing_Basics_View_Boundaries/FeatureServer/2`): B01001_001E population, B25003_001E households, B01002_001E median age, B19049_001E median household income, B25077_001E median home value. Average household size is population divided by households. The api.census.gov service now needs a key, so don't use it.
- Give each ring a share of each tract, based on the population of that tract's blocks whose centroids fall inside the ring.
- Medians are population-weighted averages of tract medians.
- Say on the page that the numbers are estimates.
- Keep URLs short, because long query URLs get rejected.

## Stage 5: Design rules and checking

- **Font:** Calibri everywhere, including any picture you draw (use Carlito, which has the same letter widths). It opens the same on every computer.
- **Colors:** use only the brand's colors below. The template already has them; keep new shapes and drawn labels in the same set.

| Brand | Header bar | Accent (badge, stripe) | Headings | Light tile |
|---|---|---|---|---|
| KW Commercial | `#000000` | `#CE011F` red | `#CE011F` | `#F5F5F5` |
| eXp Commercial | `#0C0F24` navy | `#A3B075` sage (stripe only) | `#0C0F24` | `#F3F4F4` |
| SVN | `#171715` charcoal | `#ED6B26` orange | `#171715` | `#F4F4F3` |
| Coldwell Banker Commercial | `#012269` navy | `#1D5EFF` blue | `#012269` | `#EEF2FB` |
| NAI Global | `#1A1A1B` | `#D03238` red | `#D03238` | `#F4F4F4` |

- **Text sizes:** page titles are 26pt bold, white and all caps. Body text is at least 11pt and bullets 12pt. Footnotes can be 9pt.
- **Keep the template's layout.** Header bar, logos and footer stay as they are. Don't move or resize them.
- **Render and look.** Convert to PDF with any renderer you have (GenOffice, LibreOffice or PowerPoint), render each page to an image, and look at every page. A page title that sits on the header bar is by design and is not an overlap. Check:
  - no text overflows or overlaps, especially the cover stats box and the price badge
  - no `{{` tokens are left, including inside the phone and email links
  - the same numbers appear on every page (size, price, price per unit, zoning)
  - photos aren't stretched
  - nothing sits over the footer line, and long bios do not run into the footer (make the bio text smaller or the box shorter)
  - the footer contact boxes stay inside the page
- Fix anything you find, then render and look again.

## Stage 6: Deliver

1. Save the OM in the listing folder as `<Short property name> OM.pptx`. If it still has TBD items, add " - DRAFT" to the name. When it is final, also save a PDF copy for the website.
2. Make a Word document called `<Property> Open Questions.docx`.
   - Group the questions by who answers them: seller, surveyor, title company, city zoning, utility, appraisal district, MLS fixes, and the agent's own info.
   - Give each question a short "why it matters" note, a checkbox and space for the answer.
   - Use Calibri and the brand's heading color for headers, on US Letter paper.
3. Send the agent a short plain-English message:
   - where the files are
   - what's in the OM
   - what's still TBD and why
   - the conflicts to fix (MLS and reports)
   - one or two next steps
4. **Putting it on the website.** If the listing lives on an UpliftCRE website, the agent uploads the final OM PDF by hand: open the listing, go to the Documents tab and upload it in the Public OM field. Tell the agent this step.
5. Never hand third-party reports (RPR and similar) to buyers as they are. Their covers can show old contact details.
