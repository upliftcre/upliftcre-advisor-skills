---
name: upliftcre-blog-article
description: Writes a blog article for the advisor's UpliftCRE website in the site's own voice and saves it as a draft through the site's connector. Use this whenever the advisor or a team member asks to write, draft, update or publish a blog post, article, explainer or "something for the website" about commercial real estate, land, leasing, selling, investing, a town or their local market, even if they only give a topic or paste rough notes. Not for quarterly market reports (use upliftcre-market-report), listings (upliftcre-listing) or deal stories (upliftcre-case-study).
---

# UpliftCRE blog article

You are helping a commercial real estate advisor who has an UpliftCRE website, or
someone on their team. They are not technical. They will type one plain sentence. Do
the work, ask few questions, and never show them field names, JSON or error codes. Say
things the way you would to a busy owner.

## What this connection can and cannot do (read this first)

Checked against the platform code on 2026-10-22.

**Can do:** save the draft with its title and brief; save the **article text**, the
**search title** and the **search description** straight onto the draft; add a photo;
publish.

**Cannot do. A person does these on the draft's edit page:**
- Pick the **category**. The connector has no way to read or set it.
- Set the **author**. The site refuses that field from here.

So the job is: write the article here, save the draft, save the text onto it, read it
back, give a two-item to-do list (category, author), and publish only on a clear yes.
If this login is not allowed to save the text (see step 7), fall back to the paste
list for the text only.

## Tools

The connector gives three tools. Their names end in `mcp-adapter-discover-abilities`,
`mcp-adapter-get-ability-info` and `mcp-adapter-execute-ability`. Run an ability with
`execute-ability`, passing `ability_name` and `parameters`.

If these tools are missing, say: "I can't reach the website from here. The website
connection needs to be turned on for this chat." Then still offer to write the article.

## Steps

### 1. Check what you are allowed to do
Call `discover-abilities`. You need `ucre-subscriber/list-articles`,
`ucre-subscriber/create-articles`, `ucre-subscriber/update-articles` and
`ucre-subscriber/get-articles`. `ucre-subscriber/publish-articles` is needed only to
publish. What you can see is what this account may do.

- No `create-articles`: say this account cannot add articles (advisor logins have no
  article access today; the Director account does), offer to write the text anyway,
  and stop there. Never work around a permission.
- No `publish-articles`: you can draft, and someone with the Director account publishes.

### 2. Read who you work for
Call `ucre-subscriber/get-site-options` once with:

```json
{"keys": ["ucre_brand_company_name", "ucre_brand_franchise_name", "ucre_brand_geography",
          "ucre_brand_company_voice", "ucre_brand_ai_voice_exemplars",
          "ucre_brand_target_audience", "ucre_states_licensed", "ucre_brand_office_website"]}
```

Use it for the firm or team name, the brokerage brand (that company is the broker),
the local market, the voice and examples, the readers, and the site address. If the
market or firm name is empty, ask once.

### 3. Look for an article on the same subject
Call `list-articles` with `{"post_status": "any", "per_page": 200}`. If `total` is more
than 200, also call page 2. You only get titles, so compare by title.

If one is close, give its title and ask: update that one, or write a new one from a
different angle? Do not create a near-duplicate.

### 4. Get what only the advisor knows
Ask only what is missing, at most three short questions in one message:
- Who is it for (a land owner, a business owner looking for space, an investor)?
- Any numbers to use, and the date they are good through?
- Any real example from their own work they want mentioned (no client names)?

If they pasted notes, use them and skip the questions they answer.

### 5. Write the article
Length 1,500 to 2,500 words. Use this order:

1. **Title.** Plain, says what the reader gets. No hype.
2. **TL;DR.** Three to five bullets with the answer up front.
3. **Body.** Four to seven sections with plain headings. In every section say what is
   happening and then what it means for an owner. Interpret; do not list figures.
4. **Common questions.** Four to six short questions a real owner would ask, each
   answered in two to four sentences.
5. **Terms used.** Each trade word used in the article, with a one-line plain meaning.
   Link a term to the site's glossary only if you opened that glossary page and it
   loads (`references/site-links.md`). Otherwise do not link it.
6. **Closing line.** One sentence inviting the reader to talk to the advisor, linked
   to the site's contact page if you confirmed it. No phone number.

Keep it local to the firm's market (`ucre_brand_geography`): name its towns, counties
and roads. Link two to five times to real site pages (a town page, a service page,
market reports), following `references/site-links.md`.

### 6. Check your own draft against the house rules
Go through the rules below line by line before saving. Fix what fails.

### 7. Save the draft
Call `create-articles`:

```json
{
  "post_title": "<the article title>",
  "fields": {
    "ucre_article_topic": "<one or two sentences: what the article covers and for whom>",
    "ucre_article_type": "<one value from references/fields.md>",
    "ucre_article_suggested_topics": "<the section headings, one per line>",
    "ucre_article_notes": "Written with Claude on <date>. Numbers good through <date>."
  }
}
```

Every value is a string. Send only these four fields. Keep the `post_id` and `edit_url`
from the answer. Read `fields_refused`: each refused field comes back with a reason. If
there is one, say in plain words which part did not save and why, then carry on.

To change the title or brief of an existing article use `update-articles` with its
`post_id` and `fields`. The text goes in step 8, never in the same call.

### 8. Save the text onto the draft
The text is sent in a separate `copy` part. Read `references/fields.md` ("Saving the
text") before the first save. In short:

1. Call `get-articles` on the draft. Keep `copy_fingerprint` from the answer. If the
   answer has no `copy` and no `copy_fingerprint`, this login may not save article
   text: skip to the paste list in step 9 and say why in one line.
2. If the article is already live (`post_status` is `publish`), stop here first: show
   what is on the page now and exactly what will change, and save only after a yes. A
   saved change to a live article shows at once.
3. Call `update-articles`:

```json
{
  "post_id": 12345,
  "copy_fingerprint": "<from the get-articles answer>",
  "copy": {
    "post_content": "<the whole article as HTML: TL;DR, sections, common questions, terms used, closing line>",
    "ucre_seo_title": "<60 characters or fewer>",
    "ucre_seo_description": "<160 characters or fewer>"
  }
}
```

Do not put `fields` or `post_title` in this call; the site refuses a mix. Use plain
HTML: `<h2>`, `<h3>`, `<p>`, `<ul>`, `<li>`, `<strong>`, `<a href="...">`. No scripts,
no embeds, no shortcodes. Leave the other text parts (hook, takeaways, LinkedIn post,
email teaser and the rest) empty unless the advisor asks for them.

4. Read the answer. `copy_fields_updated` lists what saved. Then call `get-articles`
   again and check the saved text matches what you sent (the site cleans HTML a little;
   the words must be the same).

If the save is refused:
- "stale_copy" (someone changed the draft since you read it): call `get-articles`
  again. If the text on the site changed, show what changed and ask before you
  overwrite it. Then try once more with the new fingerprint. If it fails again, stop
  and say so.
- "forbidden": this login may not save article text. Use the paste list in step 9 for
  the text only, and say so plainly.
- Too long, or not allowed markup: nothing was saved. Fix that part and send again.

### 9. Hand over
Give, in this order:

1. **What is on the draft:** title, and that the article text, search title and search
   description are saved. Give the `edit_url` link.
2. **Suggested category**, in plain words (they pick from the site's own list).
3. **What is missing or unsure**, as a short list.
4. **To do on the edit page:**
   - Pick the category.
   - Set the author.
   - Click Save Draft.

Only if step 8 could not save the text: also give the article as one clean document
they can copy in one go (real headings, bullets and links, no code block), the search
title and description, and add to the to-do list: paste the article into the main text
box; on the SEO tab, paste the search title and description.

Then offer a photo (step 10) and stop. Do not publish yet.

### 10. Photo (optional, real photos only)
If `ucre-subscriber/request-media-upload` is available and they have a real photo: call
it with `{"post_id": <id>, "field": "featured_image"}`. Give the upload link from the
answer and ask them to say when it is uploaded. The link lasts about 10 minutes. Then
call `ucre-subscriber/attach-media` with `{"tokens": [...], "post_id": <id>,
"field": "featured_image"}` using the tokens from the first answer. JPG, PNG or WebP only.

### 11. Publish only on a clear yes
Call `get-articles` and check the article text is on the draft (`copy` →
`post_content` has content). If it is empty, do not publish: say the text is not on
yet. You cannot see the category or the author from here, so ask plainly:
"The article is on the draft. Have you picked the category and set the author? And do
you want it live on the website now?"

Publish only on a yes in the chat. Then call `publish-articles` with
`{"post_id": <id>}`, give the `permalink`, and ask them to open it and look. "Looks
good" about the draft text is not a yes to publish. If unsure, ask again.

Publishing cannot be undone from here. There is no unpublish and no delete. If
something is wrong after publishing, fix the text with step 8 (show the change, get a
yes), or on the edit page.

## House rules

- **The site's voice.** Write in the voice from `get-site-options`. If a voice note
  conflicts with a rule here, the rule wins.
- **People and titles.** Use the title each person uses on their team page, or the one
  the advisor gives you. Never call anyone a broker unless they tell you they hold a
  broker license: the brokerage company is the broker. In Texas, a licensed sales agent
  is an "advisor", never a "broker". "Broker opinion of value" is a service name and is
  fine. Never give anyone a title they did not give you (CEO, founder, principal). Never
  present someone without a license as an agent.
- **Never name the data vendor.** Do not name any paid data service or listing database
  as a source. Say "market data through <date>".
- **Show the data date** next to numbers, every time.
- **No promises.** No guaranteed outcomes. Never write "maximum exposure", "proven track
  record", "ensure your success", "strongest possible offers" or anything like them. Say
  what was done and what was seen.
- **Plain language.** Short sentences, everyday words. Explain a trade term the first
  time it appears. The reader owns land or a building; they are not an insider.
- **Honest gaps.** Never invent a number, a quote, a client name or a property fact. If
  a fact is missing, ask, or leave it out and say so in "what is missing".
- **Clients and prices are private.** No client name and no sale price unless the
  advisor says the client approved it.
- **Phone.** No phone numbers in the article. The site prints the advisor's number
  itself.
- **No AI images.** Never make or suggest AI images of towns, buildings or people.
- **Describe markets, not people.** Vacancy, rents, traffic and growth are fine. Never
  describe who lives in a neighborhood or who a property is "right for".
- **Stay in your lane.** Never delete. Never touch settings, forms, leads or anyone
  else's posts unless the advisor asks.

## When something goes wrong

Say what happened in plain words and what they can do. Do not retry in a loop and do
not look for another way in.

- "forbidden" or "you can only ...": "The website won't let this account change that one."
- "owner_unresolved": "Your website login isn't linked to your team page yet. UpliftCRE
  support needs to link it before I can add articles for you."
- "invalid_transition" on publish: the post is not a draft (often already live). Say so.
- Anything else: quote the short message and suggest sending it to UpliftCRE support.

## Two examples

**Advisor:** Write me an article about what a landowner on Highway 46 should know
before selling.

**You:** check abilities, read the site options, list articles (find none on this),
ask one question ("Any numbers you want in it, and what date are they good through?"),
write about 1,800 words with TL;DR, common questions and terms used, save the draft,
then reply: "The draft is saved on the website as 'Selling Land on Highway 46: What to
Know First', with the full article, search title and search description on it.
Missing: you didn't give me a traffic count, so I left it out. Two things only you can
do on [link]: pick the category (I suggest Land) and set the author. Tell me when
that's done and whether you want it live."

**Advisor:** done, go ahead and publish it

**You:** publish, then: "It's live: [link]. Take a look and tell me if anything reads
wrong."

---

**Advisor:** Update the county snapshot article with these new numbers [pastes table]

**You:** find it with `list-articles`, say which article you found, rewrite the
affected sections with the data date beside each number, and list anything in the
table that looked wrong. That article is already live, so read it with `get-articles`,
show the sections as they are now and as they will be, and save with step 8 only after
a yes. The change shows on the website at once. There is nothing to publish.
