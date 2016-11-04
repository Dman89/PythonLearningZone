from bs4 import BeautifulSoup
import subprocess
import re
# Open File
text_file = open("fullPage.txt", "r")

#Read the HTML
soup = BeautifulSoup(text_file, 'html.parser')

data = soup.find_all('h5')

# Save File to Compile Text
with open("tempSave.txt", "w") as text_file:
    print(data, file=text_file)

# Open File to Read Text
text_temp = open("tempSave.txt", "r")

#Split Array in File
lines = text_temp.read().split(", ")
beerArr = lines[0]
#Array to Save Items
company_names = []

#Sort Through For Lines and Take Names Out
for elem in lines:
    if elem.find("Beers") >= 0:
        elem = elem.replace("<h5>", "")
        elem = elem.replace("</h5>", "")
        elem = elem.replace("]\n", "")
        elem = elem.replace("Beers from ", "")
        company_names.append(elem)


data = soup.select('#growler-fills > .col-md-6')

# Save File to Compile Text
with open("tempSave.txt", "w") as text_file:
    print(data, file=text_file)

# Open File to Read Text
text_temp = open("tempSave.txt", "r")

#Split Array in File
lines = text_temp.read().split(", <")
beerStr = lines[0]


beerSplit = beerStr.split("<h5>Beers from "+company_names[0]+"</h5>")
beerArr = beerSplit[1].split("<h5>Beers from "+company_names[1]+"</h5>")
company_info = []
for data in beerArr:
    data = re.sub(r'class=".*"', "", data)
    company_info.append(data)

# # Save File (Company Names)
# with open("beerList.txt", "w") as text_file:
#     print(company_names, file=text_file)
