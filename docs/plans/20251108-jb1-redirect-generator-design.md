# JB1 Redirect Generator Design

**Date:** 2025-11-08
**Status:** Approved

## Purpose

Create a standalone, generalized tool from the existing `scripts/generate_redirects.py` that any Jupyter Book 2 / MyST project can use to generate redirects from old Jupyter Book 1 URLs to new MyST-style URLs.

## Design Principles

- **Simplicity first:** Minimal changes, easy to understand and maintain
- **MVP approach:** Only essential features, no over-engineering
- **Standalone:** Self-contained tool others can use via `uv run`

## File Structure

```
jb1-redirect-generator/
├── generate_redirects.py    # Main script (copy + minimal tweaks)
├── test_examples.py          # Simple test showing URL transformations
└── README.md                 # Usage guide with examples
```

## Changes to generate_redirects.py

### 1. Config Discovery Enhancement
**Current behavior:** Defaults to `docs/myst.yml`

**New behavior:** Try multiple common locations in order:
1. `./myst.yml` (current directory)
2. `./docs/myst.yml` (docs subdirectory)
3. If neither found, show helpful error message

**Implementation:** ~2-5 lines of code change in the default parameter handling

### 2. Update Default Output Directory
**Current:** `_build/redirects`
**New:** `_build/html` (where users typically want to insert redirect files)

### 3. Generic Documentation
Remove project-specific references from docstrings, make examples generic.

## test_examples.py

Simple demonstration script that shows URL transformations:

**Purpose:**
- Verify the tool works correctly
- Document expected behavior with examples
- No complex test framework needed

**Output format:**
```
Testing URL transformations:
✓ overview.md → overview.html → https://example.com/overview/
✓ Test_File.md → Test_File.html → https://example.com/test-file/
✓ nested/page.md → nested/page.html → https://example.com/nested/page/
```

**Test cases:**
- Basic transformation
- Mixed case filenames (sanitization)
- Spaces and underscores (sanitization)
- Nested directories
- Index file detection (first TOC entry)

## README.md

Concise usage guide (~100 lines max) including:

1. **Purpose:** What this tool does (JB1 → JB2 redirect generation)

2. **Prerequisites:**
   - Python 3.10+
   - uv installed

3. **Usage Examples:**
   ```bash
   # Basic usage (auto-discovers myst.yml)
   uv run generate_redirects.py --base-url https://example.com/

   # Custom config location
   uv run generate_redirects.py --base-url https://example.com/ --myst-config path/to/myst.yml

   # Custom output directory
   uv run generate_redirects.py --base-url https://example.com/ --output-dir public/redirects

   # Run directly from GitHub
   uv run https://raw.githubusercontent.com/jupyter/governance/main/jb1-redirect-generator/generate_redirects.py --base-url https://example.com/
   ```

4. **How it works:** Brief explanation of URL transformation

5. **Testing:** How to run test_examples.py

## Implementation Scope

**What's included:**
- Standalone folder with script, test, and README
- Smart myst.yml discovery
- Updated defaults for broader use
- Simple test demonstrating transformations

**What's NOT included (keeping it simple):**
- No new CLI flags or features
- No validation mode
- No URL pattern selection (html vs dirhtml)
- No remote config fetching

## Success Criteria

1. Tool can be run via `uv run [URL]` from any JB2 project
2. Auto-discovers myst.yml without user intervention (common cases)
3. Test demonstrates correctness with clear examples
4. README enables users to get started in < 2 minutes
5. Code remains simple and maintainable (< 400 lines)

## Non-Goals

- Complex validation features
- Support for non-standard MyST configurations
- Integration with build systems
- Automated deployment
