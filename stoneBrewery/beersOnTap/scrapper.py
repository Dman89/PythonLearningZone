import requests
from bs4 import BeautifulSoup
import subprocess

#HTTP GET CALL
r = requests.get("http://www.stonebrewing.com/visit/outposts/richmond")

#Save the HTML
html_doc = r.content

#Read the HTML
soup = BeautifulSoup(html_doc, 'html.parser')

# Save File
with open("fullPage.txt", "w") as text_file:
    print(soup, file=text_file)

# Run Name Graber Companies
import name_grabber_beers

# Run Name Graber Location
import name_grabber_location

# Run descrambler
# import text_descramble
