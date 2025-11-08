# JB1 Redirect Generator

Generate HTML redirect files when migrating from Jupyter Book v1 to MyST/Jupyter Book v2.

## What This Does

When you migrate from Jupyter Book v1 to JB2/MyST, your URL structure changes:
- **Old (JB1):** `https://example.com/overview.html`
- **New (JB2):** `https://example.com/overview/`

This tool generates HTML redirect files so old links continue to work.

## Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) installed

## Usage

### Typical Workflow with Jupyter Book 2

First, build your Jupyter Book site, then generate the redirects:

```bash
# Build your JB2 site
jupyter-book build docs/

# Generate redirect files in the same output directory
uv run https://raw.githubusercontent.com/jupyter/governance/main/jb1-redirect-generator/generate_redirects.py \
  --base-url https://example.com/
```

Or with MyST CLI:

```bash
# Build your MyST site
myst build --html

# Generate redirect files in _build/html
uv run https://raw.githubusercontent.com/jupyter/governance/main/jb1-redirect-generator/generate_redirects.py \
  --base-url https://example.com/
```

This will:
1. Auto-discover your `myst.yml` (tries `./myst.yml`, then `./docs/myst.yml`)
2. Generate redirect files in `_build/html/` alongside your built site
3. Map each old `.html` URL to the new directory-based URL

### Basic Usage

From your JB2 project directory (must contain `myst.yml`):

```bash
uv run https://raw.githubusercontent.com/jupyter/governance/main/jb1-redirect-generator/generate_redirects.py \
  --base-url https://example.com/
```

### Custom Config Location

If your `myst.yml` is elsewhere:

```bash
uv run generate_redirects.py \
  --base-url https://example.com/ \
  --myst-config path/to/myst.yml
```

### Custom Output Directory

To generate redirects in a different location:

```bash
uv run generate_redirects.py \
  --base-url https://example.com/ \
  --output-dir public/redirects
```

### Quiet Mode

Suppress progress output:

```bash
uv run generate_redirects.py \
  --base-url https://example.com/ \
  --quiet
```

## How It Works

1. **Reads your `myst.yml`** to find all content files
2. **Generates old-style URLs** (e.g., `path/to/page.html`)
3. **Applies MyST's URL sanitization** (lowercase, hyphens, etc.)
4. **Creates redirect HTML files** with meta-refresh tags

### URL Transformation Examples

| Input File | Old URL (JB1) | New URL (JB2) |
|------------|---------------|---------------|
| `overview.md` | `overview.html` | `/overview/` |
| `Test_File.md` | `Test_File.html` | `/test-file/` |
| `charters/Media.md` | `charters/Media.html` | `/charters/media/` |

## Testing

Run the test examples to see URL transformations:

```bash
python test_examples.py
```

## Deployment

After generating redirects:

1. Copy redirect files to your web server (they're already in `_build/html/`)
2. Deploy alongside your JB2 site
3. Old `.html` URLs will automatically redirect to new directory-based URLs

## Example Output

```bash
$ uv run generate_redirects.py --base-url https://jupyter.org/governance/

ℹ️  Auto-discovered config: ./docs/myst.yml
ℹ️  Detected index file: intro.md (slug: intro)
✓ intro.html → https://jupyter.org/governance/
✓ overview.html → https://jupyter.org/governance/overview/
✓ people.html → https://jupyter.org/governance/people/
...

✨ Generated 25 redirect files in _build/html

Next steps:
1. Copy the redirect files to your web server
2. Ensure .html files are served with the redirect HTML
3. Test the redirects work correctly
```

## Common Issues

### "Could not find myst.yml"

Make sure you're running from your JB2 project directory, or use `--myst-config` to specify the path.

### Redirects not working

Ensure your web server is configured to serve `.html` files. Some servers require explicit configuration.

## Credits

Inspired by [Silas Santini's](https://github.com/pancakereport) work in the [data-8/textbook](https://github.com/data-8/textbook) repository.

## License

Same as the Jupyter governance repository (BSD 3-Clause).
