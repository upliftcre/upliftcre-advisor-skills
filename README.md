# UpliftCRE advisor skills

Claude skills and offering memorandum templates for commercial real estate advisors.

Four skills work with an UpliftCRE website. Each one teaches Claude how to do one
website job through the site's connector, in the site's own voice, with drafts first
and nothing published without the advisor's yes. A fifth skill builds a branded OM
from five brand templates (see below).

Checked against the UpliftCRE platform on 2026-10-22.

| Skill | Claude saves on the site | A person still does |
|---|---|---|
| `upliftcre-blog-article` | Draft with title and brief; article text; search title and description; photo | Pick the category; set the author |
| `upliftcre-market-report` | Draft with area, type, quarter, data date; every report section, the number strip, charts, FAQ, method note, search text | Set the market area, when no ID is known |
| `upliftcre-listing` | Draft with all facts; facts from the OM; description, highlights, search text; photos; sold/leased; Track Record deal | Set Primary Agent and Co-Agent; upload the OM; check the map pin; set the market area, when no ID is known |
| `upliftcre-case-study` | Draft with facts, listing link and private notes; the story; permission switches, lead agent, team and asking price; photos; deal link | Nothing |

## Offering memorandum (OM) templates

Five branded 15-page OM templates for PowerPoint, plus the `cre-offering-memorandum`
skill that fills them. The skill interviews the agent, collects the documents, checks
the facts for conflicts, fills the template and lists the open questions. It works from
the agent's own files and does not need the website connector.

| Brand | Template | Preview |
|---|---|---|
| KW Commercial | [KW Commercial OM Template](om-templates/KW%20Commercial%20OM%20Template%20-%20DO%20NOT%20TOUCH.pptx) | [all pages](om-templates/previews/kw-commercial.png) |
| eXp Commercial | [eXp Commercial OM Template](om-templates/eXp%20Commercial%20OM%20Template%20-%20DO%20NOT%20TOUCH.pptx) | [all pages](om-templates/previews/exp-commercial.png) |
| SVN | [SVN OM Template](om-templates/SVN%20OM%20Template%20-%20DO%20NOT%20TOUCH.pptx) | [all pages](om-templates/previews/svn.png) |
| Coldwell Banker Commercial | [Coldwell Banker Commercial OM Template](om-templates/Coldwell%20Banker%20Commercial%20OM%20Template%20-%20DO%20NOT%20TOUCH.pptx) | [all pages](om-templates/previews/coldwell-banker-commercial.png) |
| NAI Global | [NAI Global OM Template](om-templates/NAI%20Global%20OM%20Template%20-%20DO%20NOT%20TOUCH.pptx) | [all pages](om-templates/previews/nai-global.png) |

Pages: cover, at a glance, property highlights, highest and best use, two photo pages,
aerial map, labeled area map, survey, sale comparables, demographics, market overview,
about the agent, brokerage disclosure (for example the Texas IABS form; delete it if
your state has none), and confidentiality and disclaimer. Agent, team, website,
state and brokerage details are `{{TOKENS}}` the skill fills in.

To use one: download the template for your brand, keep a clean copy (never edit it
directly), and install `cre-offering-memorandum.zip` from `dist/`.

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

1. Download each zip you need from [`dist/`](dist/). Do not unzip it.
2. In Claude (claude.ai or the desktop app): **Settings > Capabilities**. Turn on
   **Code execution and file creation** (called **Create and edit files** in newer versions).
3. **Customize > Skills**, click **+**, then **Create skill**, then **Upload a skill**.
   Upload one zip at a time.
4. Make sure each skill is switched on.

Skills work on every Claude plan. On Team and Enterprise, an organization owner may need
to allow skills first. Menu names checked against Claude's help centre on 2026-10-27.

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
