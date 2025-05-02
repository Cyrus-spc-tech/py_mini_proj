import markdown as mk

# Sample Markdown text
markdown_text = """
# This is a heading

This is a paragraph with **bold** text and *italic* text.

- Item 1
- Item 2
- Item 3
"""

# Convert Markdown to HTML
html_output = mk.markdown(markdown_text)

# Print the output
print(html_output)
