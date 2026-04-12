# Site Context — Text to Speech Blog

Use this document when making decisions about content, design, SEO, analytics, or development for this project.

---

## The App

- **Name:** Text to Speech: AI Book Reader
- **Platform:** iOS (iPhone + iPad)
- **App Store ID:** 739280962
- **App Store URL:** https://apps.apple.com/us/app/id739280962
- **Core features:**
  - Text-to-speech with natural, lifelike voices
  - Import PDFs, documents, web pages
  - OCR (scan photos → listen)
  - Voice input / dictation
  - Export as audio file
  - Speed controls and word highlighting
- **Target users:** students, commuters, professionals, accessibility users, multitaskers

---

## The Website

- **URL:** https://text2speech.co
- **Purpose:** Marketing + SEO blog for the iOS app. Goal is organic search traffic → App Store installs.
- **Tech stack:** Jekyll (static site generator), deployed as static HTML
- **Hosting:** Static (no server-side logic)
- **CSS:** Custom (main.css), no utility framework
- **Fonts:** Inter (Google Fonts)
- **Plugins:** jekyll-sitemap, jekyll-seo-tag, jekyll-feed

---

## Site Structure

```
/               — Homepage (hero, features, reviews, CTA, blog preview)
/blog/          — Blog listing (all posts)
/blog/:year/:month/:title/  — Individual blog posts
/privacy/       — Privacy policy
/terms/         — Terms of service
```

### Templates / Layouts

| File | Purpose |
|---|---|
| `_layouts/default.html` | Base layout (header + footer + scripts) |
| `_layouts/post.html` | Blog post layout with end-of-post CTA |
| `_layouts/page.html` | Static pages (privacy, terms) |
| `_includes/header.html` | Site header (logo + nav: Blog, Get App) |
| `_includes/footer.html` | Footer (brand, nav links, copyright) |
| `_includes/seo-head.html` | SEO meta tags via jekyll-seo-tag |
| `_includes/analytics.html` | GA4 gtag.js init snippet |

### Key JS files

| File | Purpose |
|---|---|
| `assets/js/animations.js` | Scroll-triggered appear animations |
| `assets/js/analytics.js` | GA4 event tracking (data-attribute driven) |

---

## Analytics Setup

- **GA4 Measurement ID:** G-02VV0R6Y60
- **Firebase:** Connected to the iOS app (Firebase SDK in app)
- **GA4 ↔ Firebase:** Linked (web + app data in same property)

### Custom Events Tracked

| Event | Where fired | Key parameters |
|---|---|---|
| `hero_cta_click` | Hero "Download on App Store" button | `button_location`, `destination`, `page_name` |
| `cta_click` | Homepage bottom CTA "Start Listening" | `button_location`, `destination`, `page_name` |
| `footer_cta_click` | End-of-post CTA "Download on App Store — Free" | `button_location`, `destination`, `page_name` |
| `app_store_click` | Footer nav "App Store" link | `button_location`, `destination`, `page_name` |
| `blog_post_click` | Blog cards (homepage preview + blog listing) | `button_location`, `post_title`, `page_name` |
| `scroll_90` | 90% page scroll depth reached | `page_name` |
| `faq_click` | Ready — add `data-ga-event="faq_click"` to FAQ elements | `button_location`, `page_name` |

### Event tracking approach

Events are wired via `data-ga-*` HTML attributes. The JS in `analytics.js` uses event delegation — no inline `onclick` handlers. To add tracking to any new element:

```html
<a href="..."
   data-ga-event="event_name"
   data-ga-location="location_string"
   data-ga-destination="url">
  Label
</a>
```

### App Install Attribution

- Firebase SDK is in the iOS app
- GA4 + Firebase are linked → `first_open` events appear in GA4
- App Store URLs include `?ct=campaign_name&mt=8` for campaign attribution
- Can build web→app funnel in GA4 Explore: `app_store_click` → `first_open`
- Attribution is aggregated (SKAdNetwork, 24–48h delay) — Apple privacy constraint

---

## Blog Content

**14 published posts** across these categories:

| Category | Posts |
|---|---|
| `apps` | Best TTS apps for iPhone 2026 |
| `productivity` | Import PDFs, studying, commuting, speed reading, export audio, read documents aloud, text to audio on iPhone, TTS for PDF |
| `how-to` | Listen to any book without audiobook, convert photos/docs to audio, photo to speech |
| `comparison` | TTS vs audiobooks |
| `voices` | Natural voices TTS, how to choose the best TTS voice |

**Content strategy:** SEO-driven how-to articles targeting long-tail keywords around text-to-speech on iPhone. Each post ends with a CTA to download the app.

**Post date range:** October 2025 – April 2026

---

## Homepage Sections (in order)

1. **Hero** — headline, sub, "Download on App Store" CTA, app screenshot
2. **Features** — "Made for Every Day" (Study Smarter, Work on the Go, Focus More Easily)
3. **Ways** — "Built to Turn Text Into Audio" (Natural TTS, Import from Anywhere, OCR + Voice Input, Export as Audio)
4. **Reviews** — 3 user testimonials (★★★★★)
5. **Bottom CTA** — "Listen Anywhere, Anytime" + "Start Listening" button
6. **Blog Preview** — Latest 3 posts

---

## Brand

- **Tagline:** "Read Less, Listen More" / "Listen Instead of Reading"
- **Primary color:** `#FF6B35` (orange)
- **Font:** Inter
- **Tone:** Direct, practical, benefit-focused. No hype.
- **App ID (Apple):** 739280962

---

## Config Values (_config.yml)

```yaml
url: "https://text2speech.co"
app_store_url: "https://apps.apple.com/us/app/id739280962"
ga_measurement_id: "G-02VV0R6Y60"
permalink: /blog/:year/:month/:title/
```

---

## What This Site Does NOT Have (yet)

- FAQ section (event ready: `faq_click`)
- Email capture / newsletter
- Search
- Dark mode
- Per-button App Store campaign tokens (`ct=hero_cta` etc.)
- Any server-side logic or database
