#!/usr/bin/env python3
"""Validate frontmatter in database post files."""

import re
import sys
from pathlib import Path

import yaml

POSTS_DIR = Path("_posts")
TEMPLATE_FILE = POSTS_DIR / "_template.md"

# Required fields that must be present
REQUIRED_FIELDS = [
    "title",
    "database",
    "categories",
    "author",
    "external_link",
    "access",
    "publicly_available",
]

# Valid categories
VALID_CATEGORIES = {"image", "video", "audiovisual", "audio"}

# Fields that should be boolean
BOOLEAN_FIELDS = ["partner", "publicly_available", "subjective_scores", "broken_link"]

# Fields that should be strings (not lists/dicts unless specified)
STRING_FIELDS = ["title", "database", "author", "external_link", "access", "citation", "license", "contact_name", "contact_email", "resolution", "method", "doi", "excerpt"]

# Fields that should be integers (ratings can be string for ranges like "20-30")
INTEGER_FIELDS = ["total", "src", "hrc"]


def extract_frontmatter(content: str) -> tuple[dict | None, str | None]:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return None, "No valid frontmatter found (must start with ---)"

    try:
        data = yaml.safe_load(match.group(1))
        return data, None
    except yaml.YAMLError as e:
        return None, f"YAML parsing error: {e}"


def validate_url(value: str, field_name: str) -> list[str]:
    """Validate that a URL field contains a valid URL, not markdown."""
    errors = []

    if not isinstance(value, str):
        errors.append(f"  - {field_name}: expected string URL, got {type(value).__name__}")
        return errors

    # Check for markdown link syntax [text](url)
    if re.match(r"^\[.*\]\(.*\)$", value.strip()):
        errors.append(f"  - {field_name}: contains markdown link syntax. Use plain URL instead.")

    # Check for obviously invalid URLs
    if value and not value.startswith(("http://", "https://", "ftp://")):
        # Allow empty strings
        if value.strip():
            errors.append(f"  - {field_name}: URL should start with http://, https://, or ftp://")

    return errors


def validate_frontmatter(data: dict, filepath: Path) -> list[str]:
    """Validate frontmatter fields."""
    errors = []

    # Check required fields
    has_broken_link = data.get("broken_link", False)
    is_public = data.get("publicly_available", True)
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"  - Missing required field: {field}")
        elif data[field] is None or (isinstance(data[field], str) and not data[field].strip()):
            # Allow empty strings for some fields
            # - excerpt is always optional
            # - external_link can be empty for databases with broken links or non-public databases
            if field == "excerpt":
                continue
            if field == "external_link" and (has_broken_link or not is_public):
                continue
            errors.append(f"  - Required field '{field}' is empty")

    # Validate categories
    if "categories" in data:
        cats = data["categories"]
        if isinstance(cats, str):
            cats = [cats]
        if not isinstance(cats, list):
            errors.append(f"  - categories: expected list, got {type(cats).__name__}")
        else:
            for cat in cats:
                if cat not in VALID_CATEGORIES:
                    errors.append(f"  - categories: invalid category '{cat}'. Must be one of: {', '.join(sorted(VALID_CATEGORIES))}")

    # Validate boolean fields
    for field in BOOLEAN_FIELDS:
        if field in data and data[field] is not None:
            if not isinstance(data[field], bool):
                errors.append(f"  - {field}: expected boolean (true/false), got {type(data[field]).__name__}: {data[field]}")

    # Validate string fields aren't lists (common YAML mistake)
    for field in STRING_FIELDS:
        if field in data and data[field] is not None:
            if isinstance(data[field], list):
                errors.append(f"  - {field}: expected string, got list. Check YAML syntax.")
            elif isinstance(data[field], dict):
                errors.append(f"  - {field}: expected string, got dict. Check YAML syntax.")

    # Validate integer fields
    for field in INTEGER_FIELDS:
        if field in data and data[field] is not None:
            if not isinstance(data[field], int):
                errors.append(f"  - {field}: expected integer, got {type(data[field]).__name__}")

    # Validate URL fields
    if "external_link" in data and data["external_link"]:
        errors.extend(validate_url(data["external_link"], "external_link"))

    if "doi" in data and data["doi"]:
        # DOI can be a URL or just the DOI identifier
        doi = data["doi"]
        if isinstance(doi, str) and re.match(r"^\[.*\]\(.*\)$", doi.strip()):
            errors.append(f"  - doi: contains markdown link syntax. Use plain DOI or URL.")

    # Validate references format
    if "references" in data and data["references"] is not None:
        refs = data["references"]
        if not isinstance(refs, dict):
            errors.append(f"  - references: expected dictionary/mapping, got {type(refs).__name__}")
        else:
            for key, value in refs.items():
                if not isinstance(value, str):
                    errors.append(f"  - references.{key}: expected string, got {type(value).__name__}")

    # Validate tags format
    if "tags" in data and data["tags"] is not None:
        tags = data["tags"]
        if not isinstance(tags, list):
            errors.append(f"  - tags: expected list, got {type(tags).__name__}")

    return errors


def main():
    """Main entry point."""
    all_errors = {}
    files_checked = 0

    for filepath in sorted(POSTS_DIR.glob("*.md")):
        # Skip template
        if filepath.name == "_template.md":
            continue

        files_checked += 1
        content = filepath.read_text(encoding="utf-8")

        data, parse_error = extract_frontmatter(content)

        if parse_error:
            all_errors[filepath] = [f"  - {parse_error}"]
            continue

        if data is None:
            all_errors[filepath] = ["  - Empty frontmatter"]
            continue

        errors = validate_frontmatter(data, filepath)
        if errors:
            all_errors[filepath] = errors

    # Report results
    print(f"Checked {files_checked} files")

    if all_errors:
        print(f"\nFound errors in {len(all_errors)} files:\n")
        for filepath, errors in all_errors.items():
            print(f"{filepath}:")
            for error in errors:
                print(error)
            print()
        sys.exit(1)
    else:
        print("All frontmatter is valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()
