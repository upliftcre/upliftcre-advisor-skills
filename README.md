# UpliftCRE advisor skills

Four Claude skills for commercial real estate advisors who have an UpliftCRE website.
Each skill teaches Claude how to do one website job through the site's connector, in the
site's own voice, with drafts first and nothing published without the advisor's yes.

Checked against the UpliftCRE platform on 2026-10-22.

| Skill | Claude saves on the site | A person still does |
|---|---|---|
| `upliftcre-blog-article` | Draft with title and brief; article text; search title and description; photo | Pick the category; set the author |
| `upliftcre-market-report` | Draft with area, type, quarter, data date; every report section, the number strip, charts, FAQ, method note, search text | Set the market area, when no ID is known |
| `upliftcre-listing` | Draft with all facts; facts from the OM; description, highlights, search text; photos; sold/leased; Track Record deal | Set Primary Agent and Co-Agent; upload the OM; check the map pin; set the market area, when no ID is known |
| `upliftcre-case-study` | Draft with facts, listing link and private notes; the story; permission switches, lead agent, team and asking price; photos; deal link | Nothing |

## How the skills behave

- **Drafts first.** Everything is saved as a draft. Publishing needs a clear yes in the
  chat.
- **Live pages are protected.** Before any change to a live page, Claude shows what will
  change and waits for a yes. Text changes need a fresh read, so nobody's edit is
  overwritten by accident.
- **Nothing invented.** No made-up numbers, quotes, clients or property facts. A market
  report uses only the numbers the advisor supplies, checked one by one.
- **Clients and prices stay private** unless the advisor says the client approved.
- **Your site's voice.** Each skill reads the firm name, brokerage brand, market and voice
  notes from the site at the start.

## Install

1. In Claude (claude.ai or the desktop app): **Settings > Capabilities**. Make sure code
   execution / file creation is on.
2. **Skills > Upload skill**. Upload each zip from [`dist/`](dist/), one at a time, and
   turn it on.

## Connect your website

1. **Settings > Connectors > Add custom connector.**
2. Address: your site's connector address, from the AI Connector settings page on your
   UpliftCRE site.
3. Click Connect, sign in with your own website login, and approve. Administrator logins
   are refused.

Safe first test: "What can you do on my website?" Claude lists what your login can do
and changes nothing.

## Who can use which skill

| Skill | Director | Advisor login | Staff login |
|---|---|---|---|
| Blog article | Yes, incl. text and publish | No article access today | Own drafts, incl. text |
| Market report | Yes, incl. text | No | No |
| Listing | Yes, any listing | Own listings, incl. text, publish and photos | Own drafts, incl. text, no photos |
| Track Record deal (inside Listing) | Yes | Own | No |
| Case study | Yes | Own, incl. text, publish and photos | Own drafts, incl. text, no photos |

## Rebuild the zips

```
python build_zips.py
```

It checks each `SKILL.md` (name, description length, linked files exist) and writes
`dist/<skill>.zip` with one top-level folder holding `SKILL.md`.
