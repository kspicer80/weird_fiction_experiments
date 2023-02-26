import re
import pandas as pd
pd.set_option('display.max_rows', None)
from pathlib import Path

file_path = Path('texts/wf_anthology.txt')

# Read in the text file as a string
with open(file_path, 'r') as f:
    text = f.read()

# define the regular expression pattern to match the section title, author's name, and introductory paragraph
pattern = r'^##(.+?)\n\n(.+?)\n\n((?:.|\n)*?)\n\n'

# process each section
new_text = ''
for match in re.finditer(pattern, text, re.MULTILINE | re.DOTALL):
    # extract the relevant information
    title = match.group(1)
    author = match.group(2)
    intro = match.group(3)

    # remove the unwanted text
    new_intro = re.sub(r'^' + author + r'(?:.|\n)*?\n\n', '', intro)

    # concatenate the modified section to the new text
    new_text += '##' + title + '\n\n' + author + '\n\n' + new_intro

with open('wf_anthology_manually_tidied_v1.txt', 'w') as outfile:
    outfile.write(''.join(new_text))






'''
# Split the text by the '##' delimiter and extract the text content
blocks = []
for block in re.split(r'(?m)^##', text)[1:]:
    # Extract the story name and author name
    match = re.match(r'(.*?)\n\n(.*?)\n\n', block, re.DOTALL)
    if match:
        story_name = match.group(1)
        author_name = match.group(2).replace('\n', '')
    else:
        story_name = ''
        author_name = ''

    # Extract only the text content
    text_content = re.sub(r'(.*?)\n\n(.*?)\n', '', block, re.DOTALL).strip().replace('\n', '')

    # Add the block to the list of dictionaries
    blocks.append({'story_name': story_name, 'author_name': author_name, 'text': text_content})

# Create a pandas DataFrame from the list of dictionaries
df = pd.DataFrame(blocks)
print(df)
'''
