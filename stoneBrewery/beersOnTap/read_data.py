import subprocess

# Open File to Read Text
loaded_list = eval(open("compiledList.txt", "r").read())

def print_name():
    for item in loaded_list:
        print(item["name"])

def print_beers():
    for item in loaded_list:
        print(item["beers"])

def print_full():
    for item in loaded_list:
        print(item["name"])
        print(item["phone"])
        print(item["streetName"])
        print(item["address2"])
        print(item["city"])
        print(item["zipCode"])
        print(item["state"])
        for beer in item["beers"]:
            print(beer)

print_full()
