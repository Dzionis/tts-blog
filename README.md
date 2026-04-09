# Text to Speech Blog

SEO blog for the [Text to Speech - AI Book Reader](https://apps.apple.com/us/app/id739280962) iOS app.

Site: **text2speech.co** · Stack: Jekyll + GitHub Pages · Deploy: automatic on push to `main`

---

## Quick start: add a new post

### Option 1 — Slash command in Claude Code (recommended)

Open VSCode with Claude Code and type in chat:

```
/new-post topic | primary keyword
```

**Examples:**

```
/new-post how to listen to PDFs on iPhone | text to speech PDF
/new-post best text to speech apps for studying | text to speech for students
/new-post how to convert photos to audio | image to speech app
/new-post speed reading with text to speech | listen faster with TTS
```

Claude will generate the post and **save the file automatically** to `_posts/`. Then:

```bash
git add _posts/
git commit -m "Add: [post title]"
git push
```

The post will appear on the site in ~2 minutes.

---

### Option 2 — Python script from terminal

Requires Claude Code CLI (`claude`) installed and authenticated.

```bash
# From the project root:
python scripts/generate_article.py \
  --topic "how to use text to speech for studying" \
  --keyword "text to speech for students"

# With explicit output folder:
python scripts/generate_article.py \
  --topic "best voices for long listening sessions" \
  --keyword "best TTS voice" \
  --output _posts/
```

The script calls `claude --print` under the hood — no API keys needed.

After generating:

```bash
git add _posts/
git commit -m "Add: new article"
git push
```

---

## Deploy

Deploy happens **automatically** on every `git push` to `main` via GitHub Actions.

Deploy status: **Actions** tab in the GitHub repository.

**Initial GitHub Pages setup** (one time only):
1. Open the repository on GitHub
2. Settings → Pages → Source → select **"GitHub Actions"**
3. Push any commit — the site deploys automatically

---

## Post ideas

SEO topics worth targeting:

| Topic | Primary keyword |
|-------|-----------------|
| How to listen to any book without an audiobook | listen to books without audiobook |
| Best text to speech apps for iPhone | best TTS apps iPhone |
| How to import PDFs into a TTS app | text to speech PDF iPhone |
| How to use TTS for studying | text to speech for studying |
| How to listen while commuting | listen to articles while commuting |
| Convert photos and documents to audio | image to speech app |
| Speed up reading with text to speech | listen faster with TTS |
| How to choose the best TTS voice | best text to speech voice |
| Text to speech vs audiobooks | TTS vs audiobooks |
| How to listen to web articles on iPhone | listen to web pages iPhone |

---

## Project structure

```
tts-blog/
├── _config.yml          # Jekyll settings, app_store_url
├── _layouts/            # Page templates
│   ├── default.html     # Base HTML
│   ├── post.html        # Post template (with CTA block)
│   └── page.html        # Static page template
├── _includes/           # Reusable partials
│   ├── header.html
│   ├── footer.html
│   └── seo-head.html    # SEO tags + Smart App Banner
├── _posts/              # Blog posts (YYYY-MM-DD-slug.md)
├── assets/css/main.css  # All CSS
├── index.html           # Landing page
├── blog/index.html      # Post listing
├── scripts/
│   └── generate_article.py  # Article generator via Claude CLI
├── .claude/commands/
│   └── new-post.md      # /new-post slash command
├── .github/workflows/
│   └── deploy.yml       # Auto-deploy to GitHub Pages
└── CNAME                # text2speech.co
```

---

## Post format

Every file in `_posts/` is Markdown with Jekyll front matter:

```markdown
---
layout: post
title: "How to Listen to Any Book Without an Audiobook"
description: "Meta description under 155 characters."
date: 2026-04-10 10:00:00 +0000
categories: [how-to]
author: Text to Speech Team
---

Post body...

## Start Listening with Text to Speech

Final paragraph positioning the app as the solution. No App Store link needed — the layout adds a CTA button automatically.
```

Valid categories: `productivity`, `apps`, `learning`, `how-to`
