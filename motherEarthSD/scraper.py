import requests
from bs4 import BeautifulSoup
import subprocess

r = requests.get("https://www.motherearthbrewco.com/")

#Save the HTML
html_doc = r.content

#Read the HTML
soup = BeautifulSoup(html_doc, 'html.parser')

soup.fina







# print_this = soup.select(".tap-info-slide")

# # Save File to Compile Text
# with open("tempSave.txt", "w") as text_file:
#     print(print_this, file=text_file)
#
# # Open File to Read Text
# print_this = open("tempSave.txt", "r").read().split(", ")
# save_file = []
# for elem in print_this:
#     elem = elem.replace('<div class="tap-info-slide">', "")
#     elem = elem.replace('\n', "")
#     elem = elem.replace('</div>', "")
#     elem = elem.replace('<ul>', "")
#     elem = elem.replace('</ul>', "")
#     save_file.append(elem)

# Save File
with open("fullPage.txt", "w") as text_file:
    print(save_file, file=text_file)
