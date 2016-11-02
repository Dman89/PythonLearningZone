import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.stonebrewing.com/beer")
html_doc = r.content
soup = BeautifulSoup(html_doc, 'html.parser')
with open("text.txt", "w") as text_file:
    print(soup.find_all(class_='field-item even'), file=text_file)
