import subprocess
def combination():
    # Open File to Read Text
    location_info = eval(open("name_temp.txt", "r").read())
    location_beers = eval(open("beerList.txt", "r").read())
    loaded_list = eval(open("compiledList.txt", "r").read())

    brewery_beers = []
    for info in location_beers:
        for beer in info["beers"]:
            tempDict = {"breweryName": info['brewery_name'], "beerName": ""}
            tempDict["beer"] = beer
            brewery_beers.append(tempDict)

    beers_in_brewery = {"beers": brewery_beers}

    return_dict = {**beers_in_brewery, **location_info}

    #Save Dict to Old array
    loaded_list.append(return_dict)

    #Save Final Data
    with open("compiledList.txt", "w") as text_file:
        print(loaded_list, file=text_file)
