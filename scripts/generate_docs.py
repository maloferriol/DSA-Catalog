#!/usr/bin/env python3
"""Generate Docusaurus markdown pages for all DSA topics from dsa_enriched.json."""

import json
import os
import re
from pathlib import Path

PROJ = Path(__file__).parent.parent
DATA = PROJ / "data" / "dsa_enriched.json"
DOCS = PROJ / "docs-site" / "docs"

SLUG_MAP = {}

def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s

def category_dir(kind, category):
    kind_map = {
        "Data Structure": "data-structures",
        "Algorithm": "algorithms",
        "Paradigm": "paradigms",
        "Technique": "techniques",
    }
    cat_slug = slugify(category)
    return kind_map.get(kind, "other") + "/" + cat_slug

def difficulty_emoji(d):
    return {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}.get(d, "")

def generate_page(topic):
    name = topic["name"]
    slug = slugify(name)
    SLUG_MAP[name] = slug
    kind = topic["kind"]
    category = topic["category"]
    definition = topic.get("definition", "")
    time_c = topic.get("time", "")
    space_c = topic.get("space", "")
    techniques = topic.get("techniques", "")
    notes = topic.get("notes", "")
    wikipedia = topic.get("wikipedia", "")
    resources = topic.get("resources", "")
    leetcode = topic.get("leetcode", [])

    # Build page
    lines = []
    lines.append("---")
    lines.append(f"title: \"{name}\"")
    lines.append(f"sidebar_label: \"{name}\"")
    tags = [slugify(kind), slugify(category)]
    lines.append(f"tags: [{', '.join(tags)}]")
    lines.append("---")
    lines.append("")
    lines.append(f"# {name}")
    lines.append("")
    lines.append(f"> {definition}")
    lines.append("")

    # Quick facts
    lines.append("## Quick Facts")
    lines.append("")
    lines.append(f"| | |")
    lines.append(f"|---|---|")
    lines.append(f"| **Kind** | {kind} |")
    lines.append(f"| **Category** | {category} |")
    if time_c:
        lines.append(f"| **Time** | {time_c} |")
    if space_c:
        lines.append(f"| **Space** | {space_c} |")
    lines.append("")

    # Key techniques
    if techniques:
        lines.append("## Key Techniques")
        lines.append("")
        for t in techniques.split(";"):
            t = t.strip()
            if t:
                lines.append(f"- {t}")
        lines.append("")

    # Notes / tips
    if notes:
        lines.append("## Notes & Interview Tips")
        lines.append("")
        lines.append(f"{notes}")
        lines.append("")

    # LeetCode problems
    if leetcode:
        lines.append("## LeetCode Problems")
        lines.append("")
        lines.append("| # | Problem | Difficulty | Curated Lists |")
        lines.append("|---|---------|-----------|---------------|")
        for p in sorted(leetcode, key=lambda x: x.get("difficulty_rank", 0)):
            num = p.get("number", "")
            title = p.get("title", "")
            diff = p.get("difficulty", "")
            url = p.get("url", "")
            tags = []
            if p.get("grind75"):
                tags.append("G75")
            if p.get("blind75"):
                tags.append("B75")
            if p.get("neetcode150"):
                tags.append("NC150")
            tag_str = ", ".join(tags) if tags else "-"
            link = f"[{title}]({url})" if url else title
            lines.append(f"| {num} | {link} | {difficulty_emoji(diff)} {diff} | {tag_str} |")
        lines.append("")

    # Resources
    lines.append("## Resources")
    lines.append("")
    if wikipedia:
        lines.append(f"- [Wikipedia]({wikipedia})")
    if resources:
        for r in resources.split("|"):
            r = r.strip()
            if r:
                # Extract domain for display name
                domain = re.search(r"https?://(?:www\.)?([^/]+)", r)
                label = domain.group(1) if domain else r
                lines.append(f"- [{label}]({r})")
    lines.append("")

    return "\n".join(lines)


def generate_category_index(kind, category, topics):
    """Generate a _category_.json for Docusaurus sidebar."""
    return json.dumps({
        "label": category,
        "position": 1,
        "link": {
            "type": "generated-index",
            "description": f"{category} — {kind}"
        }
    }, indent=2)


def generate_kind_index(kind):
    kind_descriptions = {
        "Data Structure": "Fundamental data structures for organizing and storing data efficiently.",
        "Algorithm": "Step-by-step procedures for solving computational problems.",
        "Paradigm": "High-level approaches and strategies for algorithm design.",
        "Technique": "Specific patterns and tricks commonly used in coding interviews.",
    }
    kind_map = {
        "Data Structure": "data-structures",
        "Algorithm": "algorithms",
        "Paradigm": "paradigms",
        "Technique": "techniques",
    }
    return json.dumps({
        "label": kind + "s" if kind != "Technique" else "Techniques",
        "position": list(kind_map.keys()).index(kind) + 1,
        "link": {
            "type": "generated-index",
            "description": kind_descriptions.get(kind, "")
        }
    }, indent=2)


def main():
    with open(DATA) as f:
        data = json.load(f)

    # Clean out existing docs (except intro)
    for d in ["data-structures", "algorithms", "paradigms", "techniques"]:
        p = DOCS / d
        if p.exists():
            import shutil
            shutil.rmtree(p)

    # Group by kind -> category
    structure = {}
    for topic in data:
        k = topic["kind"]
        c = topic["category"]
        if k not in structure:
            structure[k] = {}
        if c not in structure[k]:
            structure[k][c] = []
        structure[k][c].append(topic)

    total = 0
    for kind, categories in structure.items():
        kind_dir_name = {
            "Data Structure": "data-structures",
            "Algorithm": "algorithms",
            "Paradigm": "paradigms",
            "Technique": "techniques",
        }[kind]

        kind_path = DOCS / kind_dir_name
        kind_path.mkdir(parents=True, exist_ok=True)

        # Kind-level _category_.json
        with open(kind_path / "_category_.json", "w") as f:
            f.write(generate_kind_index(kind))

        for category, topics in categories.items():
            cat_slug = slugify(category)
            cat_path = kind_path / cat_slug
            cat_path.mkdir(parents=True, exist_ok=True)

            # Category-level _category_.json
            with open(cat_path / "_category_.json", "w") as f:
                f.write(generate_category_index(kind, category, topics))

            for topic in topics:
                slug = slugify(topic["name"])
                page = generate_page(topic)
                with open(cat_path / f"{slug}.md", "w") as f:
                    f.write(page)
                total += 1

    print(f"Generated {total} topic pages")


if __name__ == "__main__":
    main()
