#!/usr/bin/env python3
"""
generate_article.py — Generate SEO blog posts for Text to Speech using Claude Code CLI.

Uses your Claude Code subscription (no separate API key needed).
Requires `claude` CLI to be installed and authenticated.

Usage:
    python scripts/generate_article.py --topic "AI calorie tracking tips" --keyword "AI calorie tracker"
    python scripts/generate_article.py --topic "..." --keyword "..." --output _posts/
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import date

APP_STORE_URL = "https://apps.apple.com/us/app/id739280962"

PROMPT_TEMPLATE = """Generate a complete Jekyll blog post for the Text to Speech blog (Text to Speech iOS app).

Topic: {topic}
Primary keyword: {keyword}
Today's date: {today}

Requirements:
- Start with Jekyll front matter (--- block) containing: layout: post, title, description (under 155 chars), date ({today} 10:00:00 +0000), categories (list), author: Text to Speech Team
- 900–1100 words of body content
- H2 and H3 headings for structure
- Primary keyword used naturally 3–5 times
- Friendly, expert tone — practical and actionable
- No filler openers like "In today's world..." or "Are you looking for..."
- Use hedged language for statistics: "studies suggest", "research indicates"
- Do NOT include any App Store links — the layout adds a CTA button automatically
- End with H2 "Start Listening with Text to Speech" — 2–3 sentences, no links

Output ONLY the raw markdown content, nothing else. No commentary before or after."""


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text


def generate_with_claude_cli(topic: str, keyword: str) -> str:
    prompt = PROMPT_TEMPLATE.format(
        topic=topic,
        keyword=keyword,
        today=date.today().isoformat(),
    )

    result = subprocess.run(
        ["claude", "--print", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    if result.returncode != 0:
        print(f"Error from claude CLI:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)

    return result.stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a Jekyll blog post using Claude Code CLI"
    )
    parser.add_argument("--topic", required=True, help="Article topic")
    parser.add_argument("--keyword", required=True, help="Primary SEO keyword")
    parser.add_argument(
        "--output", default="_posts", help="Output directory (default: _posts)"
    )
    args = parser.parse_args()

    print(f"Generating: {args.topic}")
    print(f"Keyword: {args.keyword}")
    print("Calling Claude Code CLI...")

    content = generate_with_claude_cli(args.topic, args.keyword)

    today = date.today().isoformat()
    slug = slugify(args.topic)
    filename = f"{today}-{slug}.md"
    filepath = os.path.join(args.output, filename)

    os.makedirs(args.output, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        f.write("\n")

    print(f"✓ Saved: {filepath}")


if __name__ == "__main__":
    main()
