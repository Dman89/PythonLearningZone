from bs4 import BeautifulSoup
import subprocess
import re
# Open File
text_file = open("fullPage.txt", "r")

#Read the HTML
soup = BeautifulSoup(text_file, 'html.parser')

address = soup.select('.location-visit .location-address')
number = soup.select('.location-visit > .field-name-field-phone-number .field-item')
name = soup.select("li.active.last")
location_data = [name, number, address]

# Save File to Compile Text
with open("tempSave.txt", "w") as text_file:
    print(location_data, file=text_file)

# Open File to Read Text
text_temp = open("tempSave.txt", "r")

#Split Array in File
lines = text_temp.read().split(", ")

#Array to Save Items
location = []
print(lines)
#Sort Through For Lines and Take Names Out
for elem in lines:
    elem = elem.replace("[", "")
    elem = elem.replace("]", "")
    elem = elem.replace("</span>", "")
    elem = elem.replace("\n", "")
    elem = elem.replace("</br>", "")
    elem = elem.replace("</div>", "")
    elem = elem.replace("</li>", "")
    elem = elem.replace('<div class="field-item even">', "")
    elem = elem.replace('<span class="location-address">', "")
    elem = elem.replace('<li class="active last">', "")
    location.append(elem)
street_city = location[2].split("<br>")
state = location[3][0]+location[3][1]
zipcode = re.findall('\d+', location[3])
location_final = {"name": location[0], "phone": location[1], 'streetName': street_city[0], "city": street_city[1], "state": state, "zipCode": zipode[0]}
# Save File (Company Names)
with open("Stone"+street_city[1]+".txt", "w") as text_file:
    print(location_final, file=text_file)
