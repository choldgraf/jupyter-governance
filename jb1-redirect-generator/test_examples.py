#!/usr/bin/env python3
"""Simple test examples demonstrating URL transformations.

This script shows how the redirect generator transforms Jupyter Book v1
URLs to MyST/Jupyter Book v2 URLs, including edge cases.

Run with: python test_examples.py
"""

from generate_redirects import sanitize_for_myst_url


def test_url_transformations():
    """Test URL sanitization against various edge cases."""

    test_cases = [
        # (input_file, expected_slug, description)
        ("overview.md", "overview", "Basic file"),
        ("Test_File.md", "test-file", "Underscores to hyphens"),
        ("TestMixedCase.md", "testmixedcase", "Mixed case to lowercase"),
        ("Test With Spaces.md", "test-with-spaces", "Spaces to hyphens"),
        ("_LeadingUnderscore.md", "leadingunderscore", "Strip leading underscore"),
        ("Multiple___Special.md", "multiple-special", "Collapse multiple hyphens"),
        ("charters/MediaStrategy.md", "charters/mediastrategy", "Nested directory"),
        ("nested/Test_File.md", "nested/test-file", "Nested with underscores"),
    ]

    print("Testing URL transformations:")
    print("=" * 80)

    all_passed = True
    for input_file, expected_slug, description in test_cases:
        # Remove extension to simulate file path processing
        input_path = input_file.replace('.md', '')
        result = sanitize_for_myst_url(input_path)

        passed = result == expected_slug
        status = "✓" if passed else "✗"

        if passed:
            print(f"{status} {description:30} | {input_file:30} → /{result}/")
        else:
            print(f"{status} {description:30} | {input_file:30} → /{result}/ (expected: /{expected_slug}/)")
            all_passed = False

    print("=" * 80)

    if all_passed:
        print("✨ All tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1


def test_redirect_html_example():
    """Show example of generated redirect HTML."""

    print("\nExample redirect HTML for 'overview.html':")
    print("=" * 80)

    html = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=https://example.com/overview/">
    <meta charset="utf-8">
    <title>Redirecting...</title>
</head>
<body>
    <p>This page has moved. Redirecting to <a href="https://example.com/overview/">https://example.com/overview/</a></p>
</body>
</html>"""

    print(html)
    print("=" * 80)


if __name__ == "__main__":
    import sys

    exit_code = test_url_transformations()
    test_redirect_html_example()

    sys.exit(exit_code)
