import requests
from bs4 import BeautifulSoup
import subprocess
import json

r = requests.get("http://alehub.gear.host/api/brewersapi/1")

# Save File to Compile Text
with open("get_check.txt", "w") as text_file:
    print(r.text, file=text_file)



# # Open File to Read Text
# loaded_list = open("get_check.txt", "r").read()

text = r.json()
data_send = {

  "brewerId": 1,

  "name": "Stone Brewing Co.",

  "description": "The best brewer in San Diego.",

  "googlePlaceId": "ChIJtZVYp-b024AR494LJGzTCxg",
  "logoPath": None,

  "address": "Changed",

  "address1": None,

  "city": "Escondido",

  "state": "California",

  "zipCode": 96576,

  "beers": [],

  "dateAdded": None

}


check_me = text["brewerId"]
print(check_me)
if check_me == 1:
    print("Oh Yeah, it works Dawg!")



send = requests.put("http://alehub.gear.host/api/brewersapi/1", data = data_send)

print(send)
