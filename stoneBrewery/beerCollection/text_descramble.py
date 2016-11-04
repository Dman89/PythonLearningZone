# Open File
text = open("beerCollection.txt", "r")
#Split Array in File
lines = text.read().split(", ")
#Global Variables to Manipulate
arrToSave = []
save = 0
num = 0
tempArr = []
newArr = []

# Find the Data that is Relevant
for line in lines:

    # Start of Data(May have to change in the future)
    search = line.find("rtecenter")

    # End of Data (May have to change in the future)
    searchEnd = line.find("tee")

    if save == 1:

        # Saving File
        if searchEnd == -1:
            arrToSave.append(line)

        # Turn Save Off because 2nd Variable was found
        else:
            save = 0

# Turn Save On because 1st Variable was found
    if search >= 0:
        save = 1

#Manipulate Saved Array
for saved in arrToSave:
    # global num
    # global tempArr

    #Count to Three to Save Items
    num += 1

    # Remove HTML Tags
    saved2 = saved.replace("""<div class="field-item even">""", "")
    saved3 = saved2.replace("</div>", "")

    #Take Three Items and Append Them to an Array
    tempArr.append(saved3)

    #Reset Temp Array and Number Count after Appending to Final Array
    if num == 3:
        newArr.append(tempArr)
        tempArr = []
        num = 0

#Save Final Array
with open("beerCollectionSorted.txt", "w") as text_file:
    print(newArr, file=text_file)
