import os
import time
goal = {"name": "", "subject": {"name": "", "rank": 0}, "rank": "", "impact": "", "progression": "", "completed": False, "id": time.time(), "value": 0}
subject = {"name": "", "rank": 0}
def top_goals():
    list_top = data
    list_top.reverse()
    clear()
    print("\n\n\n")
    z=0
    for info in list_top:
        if z < 3:
            if info["completed"] == False:
                print(info["name"], "\n", (int(info["value"])/10000), "\n\n")
                z+=1
def compute_goal(subrank, rank, impact, progression):
    return ((int(rank) * int(subrank)) * (int(impact) * int(progression)))
def recompute_data():
    x=0
    for info in data:
        data[x]["value"] = compute_goal(info["subject"]["rank"], info["rank"], info["impact"], info["progression"])
        x+=1
def list_subjects():
    clear()
    z = 1
    for x in subjects:
        print("#"+str(z))
        print("\nName:")
        print(x["name"])
        print("\nValue:")
        print(x["rank"])
        print("\n\n\n")
        z+=1
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def load_file():
    global name
    name = input(str("Username:\n   >>>   "))
    try:
        DATA = open(name+".json", "r")
        data = eval(DATA.read())
        DATA.close()
        print("\nUser Found\n\n")
    except FileNotFoundError:
        data = []
        print("\nUser Created\n\n")
    global subjects
    try:
        DATA = open(name+"_subjects.json", "r")
        subjects = eval(DATA.read())
        DATA.close()
        print("\nSubjects Loaded\n\n")
    except FileNotFoundError:
        subjects = []
        print("\nSubjects Created\n\n")
    return data
def remove_goal():
    clear()
    list_data(0)
    print("\n\nNow removing a goal...")
    edit_num = input(str("Remove #\n  >>> "))
    if edit_num == "EXIT":
        return
    edit_num = int(edit_num) - 1
    check_now = input(str("Are you sure? (Y) >>> "))
    if check_now == "Y":
        del data[edit_num]
        print("Removed Item.")
    else:
        print("Cancelled...")
        return
def remove_subjects():
    clear()
    list_subjects()
    print("\n\nNow removing a subject...")
    edit_num = input(str("Remove #\n  >>> "))
    if edit_num == "EXIT":
        return
    edit_num = int(edit_num) - 1
    check_now = input(str("Are you sure? (Y) >>> "))
    if check_now == "Y":
        for info in data:
            if info["subject"]["name"] == subjects[edit_num]["name"]:
                print("\n\nSubject is still in use, remove goal or change the goal's subject to continue with deleting the 'Subject'.\n\n\n")
                return
        del subjects[edit_num]
        print("Removed Subject.")
    else:
        print("Cancelled...")
        return
def completed_goal():
    clear()
    list_data(0)
    print("\n\nNow marking goal completed...")
    edit_num = input(str("Completed #\n  >>> "))
    if edit_num == "EXIT":
        return
    edit_num = int(edit_num) - 1
    if data[edit_num]["completed"] == True:
        data[edit_num]["completed"] = False
    else:
        data[edit_num]["completed"] = True
    print("Goal Completed.")
def list_editable_goal(goal, number):
    item = input(str("Add a Goal (Old: "+goal["name"]+"): "))
    if item == "EXIT":
        return
    subject = input(str("Goal is for what Subject? (Old: "+goal["subject"]["name"]+"): "))
    new_subject = search_for_subject(subject)
    print("For these next steps, the higher the number, the more important the goal.\n\n")
    if new_subject == True:
        subrank = input(str("Rate the Subject's Value (1-100): "))
    else:
        subrank = new_subject
    rank = input(str("Rate the Goal (1-10) (Old: "+goal["rank"]+"): "))
    impact = input(str("Impact Your Short Term Goals (1-10) (Old: "+goal["impact"]+"): "))
    progression = input(str("What Effect Would this have on Your Development as a Person (1-100) (Old: "+goal["progression"]+"): "))
    value = compute_goal(subrank, rank, impact, progression)
    goal = {"name": item, "subject": {"name": subject, "rank": subrank}, "rank": rank, "impact": impact, "progression": progression, "completed": False, "id": goal["id"], "value": value}
    subject = {"name": subject, "rank": subrank}
    del data[number]
    data.insert(number, goal)
    if new_subject == True:
        subjects.append(subject)
    print("Goal Edited!", "\n", goal["name"], "\n\n")
def list_editable_subject(subj, number):
    check = subjects[number]
    subject = input(str("Name for Subject? (Old: "+subj["name"]+"): "))
    if subject == "EXIT":
        return
    new_subject = search_for_subject(subject)
    if new_subject == True:
        subrank = input(str("Rate the Subject's Value (1-100): "))
    else:
        subrank = input(str("Rate the Subject's Value (1-100) (Old: "+new_subject+"): "))
    print("For these next steps, the higher the number, the more important the goal.\n\n")
    subject_save = {"name": subject, "rank": subrank}
    x = 0
    for info in data:
        if info["subject"]["name"] == check["name"]:
            data[x]["subject"]["name"] = subject
            data[x]["subject"]["rank"] = subrank
        x+=1
    del subjects[number]
    subjects.insert(number, subject_save)
    print("Subject Edited!", "\n", subject_save["name"], "\n\n")
    recompute_data()
    print("Data Recomputed\n\n")
def edit_goal():
    clear()
    list_data(0)
    print("\n\nNow editing a goal...")
    edit_num = input(str("Edit #\n  >>> "))
    if edit_num == "EXIT":
        return
    edit_num = int(edit_num) - 1
    goal = data[edit_num]
    list_editable_goal(goal, edit_num)
def edit_subjects():
    clear()
    list_subjects()
    print("\n\nNow editing a subject...")
    edit_num = input(str("Edit #\n  >>> "))
    if edit_num == "EXIT":
        return
    edit_num = int(edit_num) - 1
    subject = subjects[edit_num]
    list_editable_subject(subject, edit_num)
def save_file(name, data):
    try:
        with open(str(name)+".json", "w", encoding="UTF-8") as text_file:
            print(data, file=text_file)
    except TypeError:
        print("\n\n\n","Didnt Save File", "\n\n\n\n")
    try:
        with open(str(name)+"_subjects.json", "w", encoding="UTF-8") as text_file:
            print(subjects, file=text_file)
    except TypeError:
        print("\n\n\n","Didnt Save File", "\n\n\n\n")
def p_welcome():
    return print("Welcome!\n")
def search_for_subject(subj):
    for x in subjects:
        if subj == x["name"]:
            return x["rank"]
        else:
            continue
    return True
def list_data(num):
    z=0
    while (z < len(data)):
        x=0
        y=1
        while (y < len(data)):
            if data[x]["value"] > data[y]["value"]:
                save_info = data[x]
                del data[x]
                data.insert(y, save_info)
            x+=1
            y+=1
        z+=1
    print("\n\nListing Items...")
    if num == 1:
        number = int(len(data))
    else:
        number = 1
    for info in data:
        print("\n\n___---***^^#"+str(number)+"^^***---___\n\n")
        print("#"+str(number))
        print("Goal:")
        print(info["name"])
        print("Subject:")
        print(info["subject"]["name"])
        print("Progression:")
        print(info["progression"])
        print("Impact:")
        print(info["impact"])
        print("Rank:")
        print(info["rank"])
        print("Completed:")
        print(info["completed"])
        print("\nTotal Value:")
        print(int(info["value"]) / 10000)
        print("\n\n___---***^^#"+str(number)+"^^***---___\n\n")
        if num == 1:
            number -= 1
        else:
            number += 1
    print("\n")
def i_add_item():
    item = input(str("Add a Goal: "))
    if item == "EXIT":
        return
    subject = input(str("Goal is for what Subject?: "))
    if subject == "EXIT":
        return
    new_subject = search_for_subject(subject)
    print("For these next steps, the higher the number, the more important the goal.\n\n")
    if new_subject == True:
        subrank = input(str("Rate the Subject's Value (1-100): "))
        if subrank == "EXIT":
            return
    else:
        subrank = new_subject
    rank = input(str("Rate the Goal (1-10): "))
    if rank == "EXIT":
        return
    impact = input(str("Impact Your Short Term Goals (1-10): "))
    if impact == "EXIT":
        return
    progression = input(str("What Effect Would this have on Your Development as a Person (1-100): "))
    if progression == "EXIT":
        return
    value = compute_goal(subrank, rank, impact, progression)
    goal = {"name": item, "subject": {"name": subject, "rank": subrank}, "rank": rank, "impact": impact, "progression": progression, "completed": False, "id": time.time(), "value": value}
    subject = {"name": subject, "rank": subrank}
    data.append(goal)
    if new_subject == True:
        subjects.append(subject)
    print("Goal Added!", "\n", goal["name"], "\n\n")
def i_order(name, data):
    order = input(str("Would you like to ADD, EDIT, EDIT SUBJECTS, REMOVE, REMOVE SUBJECTS, mark a goal COMPLETE, LIST, list SUBJECTS, view TOP goals, EXIT, or SAVE?\n>>> "))
    print("{}:".format(order))
    if order == "ADD":
        print("\n\nNow adding a goal...")
        i_add_item()
    elif order == "EDIT":
        edit_goal()
    elif order == "TOP":
        top_goals()
    elif order == "EDIT SUBJECTS":
        edit_subjects()
    elif order == "REMOVE":
        print("\n\nNow removing a goal...")
        remove_goal()
    elif order == "REMOVE SUBJECTS":
        print("\n\nNow removing a subject...")
        remove_subjects()
    elif order == "COMPLETE":
        print("\n\nNow marking a goal complete...")
        completed_goal()
    elif order == "SAVE":
        print("\n\nNow Saving...")
        save_file(name, data)
        print("\n\nSaved!\n")
    elif order == "SUBJECTS":
        print("\n\nNow Lisitng Subjects...")
        list_subjects()
    elif order == "LIST":
        clear()
        list_data(1)
    elif order == "EXIT":
        print("\n\nNow Exiting...")
        return False
# Main
clear()
p_welcome()
data = load_file()
while (True):
    check = i_order(name, data)
    if check == False:
        break
