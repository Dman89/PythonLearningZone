# make a list to hold items
shopping_list = []
# print out instructions
def print_welcome():
    print("What should we pick up at the store?")

def print_done():
    print("Enter 'DONE' to stop adding items or enter 'HELP' to see a list of current commands.")

def print_commands():
    print("""
    (HELP)
    Available Commands:
      'DONE': Typing 'DONE' will end the ability to add new items to the list and print out the list.
      'SHOW': Typing 'SHOW' will print out the current list of items.
      'HELP': Typing 'HELP' will print out a list of available commands.
      """)
    print_welcome()

# print out the list
def print_list():
    print("Here is the list:")
    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    shopping_list.append(new_item)
    print("""
Added Item {}
List now has {} items.
""".format(new_item, len(shopping_list)))

def add_item():
    while True:
    # ask for new items
        new_item = input("> ")
    # be able to quit the app
        if new_item == 'DONE':
            print_list()
            break
        elif new_item == "SHOW":
            print_list()
            continue
        elif new_item == "HELP":
            print_commands()
            continue
    # add new items to the list
        else:
            add_to_list(new_item)

print_welcome()
print_done()
add_item()
