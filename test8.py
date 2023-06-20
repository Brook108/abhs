import markdown

# Markdown content
markdown_content = '''
# Heading

This is a paragraph of text. <br>
This is a paragraph of text0. <br>
This is a paragraph of text1. <br>
This is a paragraph of text2. <br>
'''

# Convert Markdown to HTML
html_content = markdown.markdown(markdown_content)

# Add a new line to html_content
html_content += "this is new line"

# Save HTML content to a file
with open('output.md', 'w') as file:
    file.write(html_content)

