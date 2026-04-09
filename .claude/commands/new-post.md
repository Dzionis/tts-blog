Generate a new SEO blog post for the AIDente blog (AI Calorie Counter iOS app) and save it to the `_posts/` folder.

**Usage:** `/new-post topic | primary keyword`
**Example:** `/new-post how to count macros for weight loss | macro counting app`

If $ARGUMENTS is empty, ask the user for the topic and primary keyword before proceeding.

Parse $ARGUMENTS by splitting on " | ":
- Left side = TOPIC
- Right side = PRIMARY_KEYWORD

---

## Post requirements

**Jekyll front matter** (valid YAML between --- delimiters):
- `layout: post`
- `title:` SEO-optimized H1, include primary keyword naturally
- `description:` Meta description, strictly under 155 characters
- `date:` today's date in format `YYYY-MM-DD 10:00:00 +0000`
- `categories:` single-item YAML list, pick one: `[nutrition]`, `[apps]`, `[weight-loss]`, or `[recipes]`
- `author: AIDente Team`

**Body content rules:**
- 900–1100 words of body text
- H2 and H3 headings for clear structure
- Primary keyword used naturally 3–5 times (not stuffed)
- Friendly, expert tone — practical and actionable
- No filler openers: "In today's world...", "Are you looking for...", "In this article we will..."
- Use hedged language for any statistics: "studies suggest", "research indicates", "evidence points to"
- Do NOT include any App Store links in the body — the post layout adds a CTA button automatically

**Required ending section:**
Close with an H2 titled exactly `Start Tracking with AIDente` — write 2–3 sentences naturally positioning AIDente as the solution to the problem the article addresses. No links, no markdown badges.

---

## Output

1. Generate the complete post content (front matter + body)
2. Determine today's date for the filename
3. Create a URL-friendly slug from the topic (lowercase, words separated by hyphens, no special characters)
4. Save the file to: `_posts/YYYY-MM-DD-slug.md`
5. Confirm with: `✓ Post saved: _posts/[filename]`

After saving, suggest the next step: commit and push to trigger auto-deploy.
