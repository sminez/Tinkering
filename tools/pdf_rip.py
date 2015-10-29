import requests
import sys
import re

# The target url needs to be a website with pdf links in it.
# The url is provided as a command line argument.
target_url = sys.argv[1]
website = requests.get(target_url)
html = website.text
links = re.findall('"((http)s?://.*?)"', html)

# List of (url, name) tuples
pdf_list = list()

# Filter the list of ALL links in the page to select only those that link to a pdf.
for link in links:
    if link[0].endswith('.pdf'):
        name_list = link[0].split('/')
        name = name_list[-1]
        pdf_list.append((link[0], name))

# Retrieve and save all pdfs from the page.
for url in pdf_list:
    print(url)
    req = requests.get(url[0])
    pdf_file = open(str(url[1]), 'wb')
    pdf_file.write(req.content)
