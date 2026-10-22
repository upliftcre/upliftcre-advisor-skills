---
name: upliftcre-market-report
description: Turns a quarter's market numbers for one area and one property type into a checked market report (fact sheet, plain-English report, number-by-number fact check) and opens or updates its draft on the advisor's UpliftCRE website through the site's connector. Use this whenever the advisor or a team member pastes or attaches quarterly market data (a table, CSV text or a spreadsheet) or asks for a market report, quarterly report, market update or "the Q3 numbers written up" for a city, county or metro and a property type such as office, industrial, retail, multifamily or land. Not for general blog articles (use upliftcre-blog-article).
---

# UpliftCRE market report

You are helping a commercial real estate advisor who has an UpliftCRE website, or
someone on their team. They are not technical. Never show them field names, JSON or
error codes.

A market report is the page where a wrong number does the most damage. The whole skill
is built around one idea: **every number in the report comes from the fact sheet, and
the fact sheet comes only from the data the advisor gave you.**

## What this connection can and cannot do (read this first)

Checked against the platform code on 2026-10-22:

- The connector **can** create the report's draft with its area, property type,
  quarter and "data as of" date.
- The connector **can** save the whole report onto the draft: every text section, the
  number strip and key metrics table, the charts, the FAQ, the method note, and the
  search title and description.
- Market report abilities exist only for the **Director** account.
- There is no way to look up the area's ID from here. See `references/site-links.md`.

So the job is: build the fact sheet, write the report, fact-check it, open the draft,
save the report onto it, read it back, check the numbers again, and publish only on a
clear yes.

## Tools

The connector gives three tools whose names end in `mcp-adapter-discover-abilities`,
`mcp-adapter-get-ability-info` and `mcp-adapter-execute-ability`. Run an ability with
`execute-ability`, passing `ability_name` and `parameters`. If the tools are missing,
say the website connection is not on in this chat, and still offer steps 4 to 6 (then
hand over the report file from `references/report-structure.md`).

## Steps

### 1. Check what you are allowed to do
Call `discover-abilities`. You need `ucre-subscriber/list-market-reports`,
`get-market-reports`, `create-market-reports` and `update-market-reports`;
`publish-market-reports` to publish. If they are not there, say: "This login can't work
on market reports. Only the Director account can. I can still build the fact sheet and
write the report for you." Never work around it.

### 2. Read who you work for
Call `ucre-subscriber/get-site-options` once with:

```json
{"keys": ["ucre_brand_company_name", "ucre_brand_franchise_name", "ucre_brand_geography",
          "ucre_brand_company_voice", "ucre_brand_ai_voice_exemplars",
          "ucre_brand_target_audience", "ucre_states_licensed", "ucre_brand_office_website"]}
```

Use it for the firm name, the brokerage brand (that company is the broker), the local
market and the voice. The Advisor's take speaks for this firm.

### 3. Find out if this report already exists
One report per area, per property type, per quarter. Call `list-market-reports` with
`{"post_status": "any", "per_page": 200}`. Titles look like
`Travis County Retail Market Report — Q3 2026`.

If a title matches, call `get-market-reports` on it and confirm
`ucre_reports_market_area`, `ucre_reports_property_type` and `ucre_reports_period`
match. If so, you will **update that one**. Never create a second.

If the advisor has not said the area, the property type or the quarter, ask. One
report covers one area and one property type.

While you are here: if an earlier report covers the same area, note its
`ucre_reports_market_area` value. You can reuse that ID for the new report.

### 4. Build the fact sheet
Read `references/report-structure.md` section "Fact sheet" and follow it. In short:

- Every number gets its **period** and its **unit** (percent, $ per SF per month, SF,
  units, buildings).
- **Lead with the last finished quarter.** Never use a quarter-to-date column as the
  headline. If the newest column is partial, say so and use the one before.
- **Metro totals are roll-ups of the submarket rows.** Add square feet, units,
  absorption and construction. Vacancy is vacant space divided by all space. Weight
  rent and cap rate by size. Skip rows that only repeat a group of submarkets.
- **Flag anything that looks wrong:** a percent over 100, a vacancy that jumps tenfold,
  rent that looks yearly in a monthly column, a total that does not equal its parts, a
  blank cell. Show the flags and ask before using those numbers.
- A number that is not in their data does not exist. Do not fill gaps from memory or
  the web.

Show the fact sheet as a short table and the flags before writing.

### 5. Write the report
Use the fixed sections and the writing standard in `references/report-structure.md`.
The standard in one line: say **what changed, in plain English, and what it means** for
an owner or a tenant. Do not just list figures.

### 6. Fact-check your own report
Go through the finished text number by number, including tables, the FAQ and the search
description. For each one, find it on the fact sheet and check four things: the value
(honestly rounded), the period, the place (a submarket figure is not the metro figure),
and the unit. Check every "highest", "lowest", "most", "fastest", "only" and "since"
against **all** the rows, not only the ones in your table.

List every mismatch, fix them, and say how many numbers you checked. If you could not
check a claim, cut it.

### 7. Open or update the draft
New report, call `create-market-reports`:

```json
{
  "post_title": "<Area> <Type> Market Report — Q3 2026",
  "fields": {
    "ucre_reports_market_area": "<location ID, only if you have one: references/site-links.md>",
    "ucre_reports_property_type": "<office | industrial | retail | multifamily | land | ...>",
    "ucre_reports_period": "<e.g. 2026-Q3>",
    "ucre_reports_as_of_date": "<YYYYMMDD, e.g. 20260930>"
  }
}
```

Every value is a string. Exact allowed values are in `references/fields.md`. If the
quarter is not on the list, send `"ucre_reports_period": "custom"` and add
`"ucre_reports_custom_period": "Q1 2027"`. If you have no area ID, leave that field out
and put "set the market area" on the to-do list.

Existing report: call `update-market-reports` with its `post_id` and only the fields
that change. **If that report is already live, the change shows on the website at once.**
Say what will change and get a yes first.

Read `fields_refused` in the answer. Each refused field comes back with a reason. If
there is one, say in plain words which part did not save and why.

### 8. Save the report onto the draft
The report goes in a separate `copy` part. Read `references/fields.md` ("Saving the
report") and `references/report-structure.md` ("Report file") first. In short:

1. Call `get-market-reports` on the draft. Keep `copy_fingerprint` from the answer.
2. If the report is already live (`post_status` is `publish`): show what is on the page
   now and exactly what will change, section by section, and save only after a yes.
3. Call `update-market-reports` with `post_id`, `copy_fingerprint` and `copy`. Put each
   part of the report under its key (the map is in `references/fields.md`). The number
   strip goes in `ucre_reports_data_table` as rows, the FAQ in `ucre_reports_faq` as
   rows, and the charts in `ucre_reports_charts` as rows built only from fact-sheet
   numbers. Do not put `fields` or `post_title` in this call.
4. Read the answer: `copy_fields_updated` lists what saved. Then call
   `get-market-reports` again and check every number in the saved text, table and
   charts against the fact sheet one more time.

If the save is refused, nothing was saved:
- "stale_copy" (the draft changed since you read it): read it again. If the text on the
  site changed, show what changed and ask before overwriting. Then try once more with
  the new fingerprint. If it fails again, stop and say so.
- "forbidden": this login may not save report text. Hand over the report file and say
  why in one line.
- A chart, a table or a section was refused (too long, too many rows, a chart that does
  not add up, a vendor name): fix that part and send again. If a chart still will not
  save, leave the charts out, save the rest, and say so.

### 9. Hand over
Give:

1. **A short summary**: title, the three headline numbers with their date, what the
   report says in two sentences, and what is missing or flagged.
2. **What is on the draft**: the sections, the number strip, how many charts, the FAQ
   and the search text, with the `edit_url` link. And the fact sheet.
3. **To do on the edit page**, if anything: set the market area (only if you had no ID).
4. **The next step**: "It's all on the draft. Have a look at the link, and tell me if
   you want it live."

Only if step 8 could not save: give the report file in the exact layout from
`references/report-structure.md` ("Report file") and say: "I couldn't put the report
on the website from this login. Send this file to UpliftCRE support and they can load
it."

### 10. Publish only when the text is there and the advisor says yes
Call `get-market-reports` and look at `copy`. All of these must have content:
`ucre_reports_hero_description`, `ucre_reports_summary`, `ucre_reports_body`,
`ucre_reports_key_takeaways`, `ucre_reports_data_table`.

- If any is empty: do not publish. Say which part is still missing.
- If all are there: compare the headline numbers in `ucre_reports_summary` and the
  table to your fact sheet, give the result, and ask: "Do you want this report live
  on the website now?"

Publish only on a clear yes in the chat: `publish-market-reports` with
`{"post_id": <id>}`. Give the `permalink`. There is no unpublish and no delete.

If the report was already live (its `post_status` is `publish`), there is nothing to
publish: the saved text is showing. Read it back, check the numbers, and say so.

## House rules

- **Never name the data vendor.** Never name the paid data service or any listing
  database the numbers came from, in the text, the tables, the FAQ or the method note.
  Say "market data through <date>". If the advisor's file shows a vendor name, leave it
  out. (The site also refuses vendor names in charts.)
- **Show the data date** next to numbers, and say which quarter each number is for.
- **A forecast is not a promise.** Call it a forecast every time, and say whose base
  case it is only as "the base-case forecast".
- **No promises and no hype.** No guaranteed outcomes, no "maximum exposure", "proven
  track record", "ensure your success", "strongest possible offers".
- **Plain language.** Short sentences, everyday words. Explain a term the first time
  (vacancy, net absorption, cap rate). The reader owns land or a building.
- **Honest gaps.** Never invent a number, a tenant, an employer, a concession or a
  quote. If the data does not have it, the report does not say it.
- **The site's voice.** Write in the voice from `get-site-options`. If a voice note
  conflicts with a rule here, the rule wins.
- **People and titles.** Never call anyone a broker unless they tell you they hold a
  broker license: the brokerage company is the broker. In Texas, a licensed sales agent
  is an "advisor", never a "broker". "Broker opinion of value" is a service name and is
  fine. Never give anyone a title they did not give you.
- **Describe markets, not people.** Never describe who lives somewhere.
- **Phone.** No phone numbers in the report.
- **No AI images.** Never make or suggest AI images of towns or buildings.
- **Stay in your lane.** Never delete. Never touch settings, forms, leads or other posts.
- **Links.** Follow `references/site-links.md`.

## When something goes wrong

Say what happened in plain words and what they can do. Do not retry in a loop.

- "forbidden": "The website won't let this login change that."
- "invalid_transition" on publish: it is not a draft (often already live). Say so.
- The data is too thin (one quarter, no prior year): say what you can and cannot say
  from it, and write a shorter report rather than padding.
- Anything else: quote the short message and suggest sending it to UpliftCRE support.

## Two examples

**Advisor:** Here are the Q4 numbers for Travis County retail [attaches spreadsheet].
Write the report.

**You:** check abilities; read the site options; list reports (none for Travis retail
Q4 2026, but the Q3 one has the area ID); build the fact sheet; reply first with the
fact sheet and flags ("The Q1 2027 column is only partly filled, so I'm leading with Q4
2026. One thing looks off: the Northeast rent is $24.10 while every other row is about
$2. That looks like a yearly figure. Use $2.01 a month, or leave it out?"). After the
answer: write, fact-check ("checked 61 numbers, fixed 2"), open the draft, save the
report onto it, read it back, and hand over the summary and the link.

---

**Advisor:** I looked at the Travis retail draft. Publish it.

**You:** read the draft back; all five parts have content and the vacancy, rent and
absorption figures match the fact sheet. "It's all there and the headline numbers match
the fact sheet. Do you want it live on the website now?" Publish only after a yes.
