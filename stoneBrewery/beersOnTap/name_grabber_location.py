from bs4 import BeautifulSoup
import subprocess
import re

def request_html():
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
    #Sort Through For Lines and Take Names Out
    address2 = ""
    suit_present = 0
    airport = 0
    city = ""
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
        if "Suite" in elem:
            number_remove = re.findall('\d+', elem)
            address2 = "Suite " + number_remove[0]
            elem = elem.replace(address2 + "<br>", '')
            suit_present = 1
        if "Airport" in elem:
            airport = 1
        location.append(elem)
    street_city = location[2].split("<br>")
    state = location[3][0]+location[3][1]
    if airport == 1:
        zipcode = re.findall('\d+', location[4])
        city = street_city[0]
    elif suit_present == 0:
        zipcode = re.findall('\d+', location[3])
        city = street_city[1]
    else:
        zipcode = re.findall('\d+', location[4])
        city = location[3]
        state = location[4][0]+location[4][1]
    location_final = {
                        "name": location[0],
                        "phone": location[1],
                        "streetName": street_city[0],
                        "address2": address2,
                        "city": city,
                        "state": state,
                        "zipCode": zipcode[0]
                      }
    # Save File (Company Names)
    with open("name_temp.txt", "w") as text_file:
        print(location_final, file=text_file)
