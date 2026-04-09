Generate fresh SEO blog post ideas for the Text to Speech blog (Text to Speech iOS app), avoiding repetition with already published posts.

## Step 1 — Read existing posts

List all files in `_posts/` and read the `title:` line from the front matter of each post. Build a list of already-covered topics.

## Step 2 — Generate new ideas

Suggest **10 new blog post topics** that:
- Are NOT already covered by existing posts (check titles from Step 1)
- Target search queries people actually type about text to speech, audio reading, productivity, or accessibility
- Each targets a distinct keyword with real search intent
- Cover a variety of angles: how-to guides, comparisons, explainers, use-case posts, app features

For each idea, output:
1. **Title** — ready-to-use SEO title
2. **Keyword** — the exact search phrase to target
3. **Angle** — one sentence on the hook / what makes it useful

## Output format

Number each idea 1–10. After the list, add one line:

> To write any of these, run: `/new-post [title]`
