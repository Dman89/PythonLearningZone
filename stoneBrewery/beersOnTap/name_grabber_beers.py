from bs4 import BeautifulSoup
import subprocess
import re
def grabBeerNames(link):
    # Open File
    text_file = open("fullPage.txt", "r")

    #Read the HTML
    soup = BeautifulSoup(text_file, 'html.parser')

    data = soup.find_all('h5')

    if len(data) == 0:
        return False

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
    check = len(data)
    if check < 2:
        data = soup.select('#growler-fills > .col-md-12')
    # Save File to Compile Text
    with open("tempSave.txt", "w") as text_file:
        print(data, file=text_file)

    # Open File to Read Text
    text_temp = open("tempSave.txt", "r")

    #Split Array in File
    lines = text_temp.read().split(", <")
    beerStr = lines[0]
    beerSplit = beerStr.split("<h5>Beers from "+company_names[0]+"</h5>")
    try:
        beerArr = beerSplit[1].split("<h5>Beers from "+company_names[1]+"</h5>")
    except IndexError:
        beerArr = beerSplit[0].split("<h5>Beers from "+company_names[1]+"</h5>")
    company_info = []
    company_info_temp = []
    for data in beerArr:
        data = re.sub(r'class=".*"', "", data)
        data = data.replace("\n", "")
        data = data.replace("</span>", ",")
        data = data.replace("</div>", "")
        data = data.replace("<div >", "")
        data = data.replace(" '", "")
        data = data.replace("&amp;", "&")
        data = data.replace("ä", "a")
        data = data.replace("è", "e")
        data = data.replace("é", "e")
        data = data.split(", ")
        for info in data:
            company_info_temp.append(info)

    newSet = 0
    beer_set_one = []
    beer_set_two = []
    for info in company_info_temp:
        ## TODO: Make the array length a variable based on breweries on tap
        info = info.strip()
        if not info:
            newSet += 1
        elif newSet == 1:
            beer_set_two.append(info)
        else:
            beer_set_one.append(info)
        if newSet == 2:
            company_info.append(beer_set_one)
            company_info.append(beer_set_two)

    def company_name_to_beer_list(names, beer_list):
        barList = []
        name_num = 0
        for beers in beer_list:
            object_to_return = {"brewery_name": names[name_num], "beers": beers}
            barList.append(object_to_return)
            name_num += 1
        return(barList)

    bar_data = company_name_to_beer_list(company_names, company_info)

    # Save File (Company Names)
    with open("beerList.txt", "w") as text_file:
        print(bar_data, file=text_file)


    return True
