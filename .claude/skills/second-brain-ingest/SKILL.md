---
name: second-brain-ingest
description: >
  Process raw source documents into wiki pages. Use when the user adds
  files to raw/ and wants them ingested, says "process this source",
  "ingest this article", "I added something to raw/", or wants to
  incorporate new material into their knowledge base.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Second Brain — Ingest

Process raw source documents into structured, interlinked wiki pages.

## Identify Sources to Process

Determine which files need ingestion:

1. If the user specifies a file or files, use those
2. If the user says "process new sources" or similar, detect unprocessed files:
   ```
   python tools/ingest.py status
   ```
   If `unprocessed: 0`, tell the user — nothing to process.
   Otherwise get the file paths:
   ```
   python tools/ingest.py next N
   ```
   where N is the number of files you want to process in this session (default: 10).

## Process Each Source

For each source file, follow this workflow:

### 1. Read the source

How to read depends on the file type:

**`.url` file** (Windows Internet Shortcut — found in `raw/urls/`):
```bash
url=$(grep -i "^URL=" "<path-to-file>" | cut -d= -f2-)
summarize "$url"
```
This fetches the full web page text. For images on the page that contain important information (diagrams, charts, screenshots), read them directly — Claude can view images.

**Markdown/text file:**
- If the file is short (<150 lines): read it directly.
- If the file is long (≥150 lines): run `summarize <path>` first for a structural overview, then read the full file for detail.
- If the file contains image references (`![](path/to/image)`): read those images separately. If an image contains important information (diagrams, charts, data), describe its contents in the wiki page so the knowledge is captured in text form.

**Image file** (`.png`, `.jpg`, etc.):
Read the image directly — Claude can view it. Describe all important visual content in text form in the wiki page.

### 2. Discuss key takeaways with the user

Before writing anything, share the 3-5 most important takeaways from the source. Ask the user if they want to emphasize any particular aspects or skip any topics. Wait for confirmation before proceeding.

### 3. Create source summary page

Create a new file in `wiki/sources/` named after the source (slugified). Include:

    ---
    tags: [relevant, tags]
    sources: [original-filename.md]
    created: YYYY-MM-DD
    updated: YYYY-MM-DD
    ---

    # Source Title

    **Source:** original-filename.md
    **Date ingested:** YYYY-MM-DD
    **Type:** article | paper | transcript | notes | etc.

    ## Summary

    Structured summary of the source content.

    ## Key Claims

    - Claim 1
    - Claim 2
    - ...

    ## Entities Mentioned

    - [[Entity Name]] — brief context
    - ...

    ## Concepts Covered

    - [[Concept Name]] — brief context
    - ...

### 4. Update entity and concept pages

For each entity (person, organization, product, tool) and concept (idea, framework, theory, pattern) mentioned in the source:

**If a wiki page already exists:**
- Read the existing page
- Add new information from this source
- Add the source to the `sources:` frontmatter list
- Update the `updated:` date
- Note any contradictions with existing content, citing both sources

**If no wiki page exists:**
- Create a new page in the appropriate subdirectory:
  - `wiki/entities/` for people, organizations, products, tools
  - `wiki/concepts/` for ideas, frameworks, theories, patterns
- Include YAML frontmatter with tags, sources, created, and updated fields
- Write a focused summary based on what this source says about the topic

### 5. Add wikilinks

Ensure all related pages link to each other using `[[wikilink]]` syntax. Every mention of an entity or concept that has its own page should be linked.

### 6. Update wiki/index.md

For each new page created, add an entry under the appropriate category header:

    - [[Page Name]] — one-line summary (under 120 characters)

### 7. Update wiki/log.md

Append:

    ## [YYYY-MM-DD] ingest | Source Title
    Processed source-filename.md. Created N new pages, updated M existing pages.
    New entities: [[Entity1]], [[Entity2]]. New concepts: [[Concept1]].

### 8. Update the qmd index

After all wiki pages are written and the log is updated, refresh the search index so new pages are immediately queryable:

```bash
qmd update
qmd embed
```

`qmd update` re-indexes file contents (BM25/text search). `qmd embed` refreshes vector embeddings for semantic search. Both are needed after creating or modifying wiki pages.

### 9. Mark the source as processed

Only after the index is updated:

```
python tools/ingest.py add <path-to-source-file>
```

This records the file's content hash so it won't appear in `next` again unless the file changes.

### 10. Report results

Tell the user what was done:
- Pages created (with links)
- Pages updated (with what changed)
- New entities and concepts identified
- Any contradictions found with existing content

## Conventions

- Source summary pages are **factual only**. Save interpretation and synthesis for concept and synthesis pages.
- A single source typically touches **10-15 wiki pages**. This is normal and expected.
- When new information contradicts existing wiki content, **update the wiki page and note the contradiction** with both sources cited.
- **Prefer updating existing pages** over creating new ones. Only create a new page when the topic is distinct enough to warrant its own page.
- Use `[[wikilinks]]` for all internal references. Never use raw file paths.

## What's Next

After ingesting sources, the user can:
- **Ask questions** with `/second-brain-query` to explore what was ingested
- **Ingest more sources** — clip another article and run `/second-brain-ingest` again
- **Health-check** with `/second-brain-lint` after every 10 ingests to catch gaps
