# Fact sheet, report layout and writing standard

Contents: 1. Fact sheet. 2. Writing standard. 3. Report file (the fixed sections).
4. Key metrics rows. 5. Method note wording.

## 1. Fact sheet

Build this first. It is the only allowed source of numbers for the report.

For the report's own area, record each of these for the headline quarter, the same
quarter one year earlier, and any older quarters the data has (three, five and ten
years back are the useful ones):

| Item | Unit |
|---|---|
| Inventory | SF (units for multifamily) |
| Vacancy rate | % |
| Asking rent | $ per SF per month ($ per unit per month for multifamily). State month or year. |
| Rent growth, 12 months | % |
| Cap rate | % |
| Net absorption, 12 months | SF or units |
| Deliveries, 12 months | SF or units |
| Under construction | SF or units, and number of buildings |
| Leasing, 12 months | SF |
| Sales volume, 12 months | $, "reported prices" |

Also record, when the data has them: the high and low for vacancy, cap rate and rent
growth with their quarters; the forecast rows, labelled forecast; the metro figures for
comparison; and one row per submarket.

Rules:

- Write the period beside every number: `Q3 2026`, or `12 months through Q3 2026`.
- Headline quarter = the last **finished** quarter. A quarter-to-date column is never
  the headline, and its 12-month figures are not comparable.
- Metro figure = roll-up of submarket rows. Sum inventory, absorption, deliveries and
  construction. Vacancy = total vacant / total inventory. Rent and cap rate = weighted
  by inventory. Skip rows that are themselves groups of submarkets, or you count twice.
- Rent per year = rent per month x 12. Say which one you are quoting.
- Keep the unrounded figure on the fact sheet. Round only in the text.
- Flag and ask about: blank cells, values far out of line with neighbours, a unit that
  does not fit its column, totals that do not match their parts, a column label you do
  not understand. Do not guess what a column means.

## 2. Writing standard: what changed, in plain English

- Open each section with what changed, then say what it means for an owner or a tenant.
- One idea per sentence. Everyday words. Explain a term the first time:
  "net absorption, the space filled minus the space emptied".
- Give a number its comparison: a year ago, the metro, the ten-year range.
- Honest rounding: 10.05% is "10.1%" or "about 10%", never "10.5%".
- "Highest in ten years of data" only if the data covers ten years and you checked
  every quarter. Otherwise say what the data shows: "the highest since Q3 2022".
- End each body section with a line starting **What it means for you:**.
- Lively is good, hype is not. A plain comparison a local would recognise is welcome.
  A promise is not.
- Use "we" and "our" only in the Advisor's take.
- 900 to 1,600 words in total, depending on how much data there is.

## 3. Report file

Write the finished report in exactly these parts, in this order. Each part is saved
under its own key (the map is in `fields.md`, "Saving the report"). If the report
cannot be saved from this login, hand it over as one document with exactly these
headings, so the advisor or UpliftCRE support can load it. Do not rename or reorder them.

```
## Hero description
Two or three sentences. The one surprising or most useful thing, with its number and quarter.

## Summary
Three to five short paragraphs. First sentence states the headline figure and
"based on market data current through <date>".

## Key takeaways
- **Short bold lead** — one sentence with the number and its quarter.
(three to five bullets)

## Body
### Vacancy: <punchy plain headline>
### How it compares to the metro      (a small table; a caption giving the quarter)
### Rents: <headline>
### Construction: <headline>
### Investment                         (sales volume "with a reported price"; cap rate explained)
### Demand: <headline>
Each section ends with "**What it means for you:** ..." where it fits.
Leave out a section the data cannot support.

## Outlook
The base-case forecast, called a forecast. Then:
**If things go right:** one sentence.
**If things go wrong:** one sentence.

## Advisor's take
Two short paragraphs, clearly opinion. "Our view: ...". No promises.

## Investor implications
**For Buyers** / **For Sellers** / **For Holders**, two sentences each.

## Tenant implications
Two short paragraphs.

## FAQ
**Question a real person would search?**
Answer in one to three sentences, with the number and its quarter.
(four to six questions)

## SEO
One line, 160 characters or fewer, with the headline number and quarter.
```

Above the first heading, add three plain lines (they also go with the file if someone loads it by hand):

```
Area: <area>          Type: <property type>          Period: <e.g. Q3 2026>
Data through: <date>
Search title: <Area> <Type> Market Report Q3 2026     (60 characters or fewer)
```

## 4. Key metrics rows

After the report, list the rows for the number strip, taken straight from the fact
sheet. Use only rows the data supports. They are saved as `ucre_reports_data_table` rows, up to 10. The live reports use these, in this order:

| Metric | Value | Change | Note |
|---|---|---|---|
| Vacancy rate | 10.69% | +0.05 pts YoY | Q3 2026 |
| Asking rent | $0.94/SF/mo | +1.75% YoY | Q3 2026 |
| 12-mo net absorption | 2,888,059 SF | +1,212,752 SF YoY | 12 months through Q3 2026 |
| 12-mo deliveries | 3,327,928 SF | -2,239,892 SF YoY | 12 months through Q3 2026 |
| Under construction | 4,175,221 SF | -396,366 SF YoY | Q3 2026 |
| Market cap rate | 8.18% | +0.08 pts YoY | Q3 2026 |
| 12-mo sales volume (reported prices) | $184.0M | -30.5% YoY | 12 months through Q3 2026 |
| 12-mo leasing | 8,995,519 SF | +16.2% YoY | 12 months through Q3 2026 |
| Inventory | 197,061,489 SF | +9,327,928 SF YoY | Q3 2026 |

(The figures above show the format only. They are not data to reuse.)

Charts are saved as `ucre_reports_charts` rows built only from fact-sheet numbers (rules
in `fields.md`). Never invent a chart point.

## 5. Method note wording

End the file with a method note in this pattern, changing only the facts:

> This report covers the <period> <area> <type> market, with data current through
> <date>. It uses brokerage market data on inventory, vacancy, rents, construction and
> sales. Metro figures are totals of their submarkets. Forecast figures are a base-case
> forecast and are not a promise. Sales totals count only sales with a reported price.

Never name the data service.
