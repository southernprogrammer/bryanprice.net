import os
import re
import json
from datetime import datetime, timezone
import pytz

chicago_tz = pytz.timezone('America/Chicago')

# Define source and destination directories
SOURCE_DIR = os.path.join(os.path.dirname(__file__), 'content-md')

def fix_frontmatter(content):
    # Extract title from first Markdown heading
    title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled"

    # Extract key-value pairs from old frontmatter
    frontmatter_pattern = re.compile(r'^(\w+)\n\s*:\s*(.+)', re.MULTILINE)
    frontmatter = dict(frontmatter_pattern.findall(content))

    # Format date
    raw_date = frontmatter.get("date", "").strip()
    try:
        formatted_date = chicago_tz.localize(datetime.strptime(raw_date, "%Y-%m-%d %H:%M")).isoformat()
    except ValueError:
        formatted_date = raw_date  # Leave as-is if parsing fails

    if "tags" in frontmatter:
        tags = frontmatter["tags"].strip()
        tag_list = tags.split(",")
        frontmatter["tags"] = json.dumps(tag_list)

    if "date" in frontmatter:
        frontmatter["date"] = formatted_date

    yaml_lines = ["---", f"title: {title}"] + [f"{k}: {v}" for k, v in frontmatter.items()] + ["---\n"]
    yaml_block = "\n".join(yaml_lines)

    # Remove old frontmatter block
    cleaned_content = re.sub(r'^(\w+\n\s*:\s*.+\n)+', '', content, flags=re.MULTILINE)
    # remove the first line that holds the title
    cleaned_content = re.sub(r'^.*\r?\n', '', cleaned_content)
    # Remove empty lines at the beginning
    cleaned_content = re.sub(r'^(?:\s*\n)+', '', cleaned_content)
    # add the title back
    cleaned_content = f"# {title}\n\n" + cleaned_content

    # Prepend new YAML frontmatter
    return yaml_block + "\n" + cleaned_content.lstrip()

for root, dirs, files in os.walk(SOURCE_DIR):
    # Compute relative path from source root
    rel_path = os.path.relpath(root, SOURCE_DIR)

    for file in [x for x in files if x.endswith('.md')]:
        src_file = os.path.join(root, file)

        with open(src_file, 'r+', encoding='utf-8') as f:
            new_content = fix_frontmatter(f.read())
            f.seek(0)
            f.write(new_content)
            f.truncate()