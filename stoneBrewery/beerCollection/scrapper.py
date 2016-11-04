import requests
from bs4 import BeautifulSoup
import subprocess

#HTTP GET CALL
r = requests.get("http://www.stonebrewing.com/beer")

#Save the HTML
html_doc = r.content

#Read the HTML
soup = BeautifulSoup(html_doc, 'html.parser')

# Save File
with open("beerCollection.txt", "w") as text_file:
    print(soup.find_all(class_='field-item even'), file=text_file)

# Run descrambler
import text_descramble
