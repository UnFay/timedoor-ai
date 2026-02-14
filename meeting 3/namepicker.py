import random

names = []
print("Add names to shuffle! Input 'x' to exit and start shuffling.")
while True:
    nameInput = input("Add name: ")
    if nameInput == "x" : 
        break
    else:
        names.append(nameInput)

print("Picking names!")
while True:
    randomName = random.choice(names)
    print("Chosen name: ", randomName)
    shuffleInput = input("Choose a name again? Enter y, otherwise end.  ")
    if shuffleInput != "y":
        print("Ending program...")
        break
    