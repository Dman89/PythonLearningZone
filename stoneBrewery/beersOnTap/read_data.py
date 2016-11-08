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
        print("\n\nName:\n",item["name"])
        print("Phone Number:\n",item["phone"])
        print("Street:\n",item["streetName"])
        print("Address Suffix:\n",item["address2"])
        print("City:\n",item["city"])
        print("Zipcode:\n",item["zipCode"])
        print("State:\n",item["state"])
        for beer in item["beers"]:
            print("Beer:\n",beer)

print_full()
