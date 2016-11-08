import requests
from bs4 import BeautifulSoup
import subprocess

# Run Name Graber Location
from name_grabber_location import request_html

# Run Name Graber Companies
from name_grabber_beers import grabBeerNames

#combined Data
from combined_names_and_beers import combination

## array to go through
outposts = [
                "http://www.stonebrewing.com/visit/outposts/pasadena",
                "http://www.stonebrewing.com/visit/outposts/richmond",
                "http://www.stonebrewing.com/visit/outposts/oceanside",
                "http://www.stonebrewing.com/visit/outposts/on-kettner",
                "http://www.stonebrewing.com/visit/outposts/tap-room"
            ]

#clear compiledList
with open("compiledList.txt", "w") as text_file:
    print("[]", file=text_file)

#HTTP GET CALL
abc = 0
for outpost in outposts:
    print("\n\n", abc ,"\n\n", "\n", outpost, "\n")
    abc += 1
    r = requests.get(outpost)

    #Save the HTML
    html_doc = r.content

    #Read the HTML
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Save File
    with open("fullPage.txt", "w") as text_file:
        print(soup, file=text_file)

    # Run Name Graber Location
    request_html()

    # Run Name Graber Companies
    continue_var = grabBeerNames(outpost)

    if continue_var == False:
        print("skipped","\n")
    else:
        #combined Data
        combination()

    # Run descrambler
    # import text_descramble
import read_data
