import random

fName = input("Please enter your first name!  ")
lName = input("Please enter your last name!  ")
classCode = input("Please enter your class code!  ")

def problem() :
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operatorID = random.randint(1,3)
    if operatorID == 1 :
        userans = input("What is " + str(num1) + " + " + str(num2) + " ?  ")
        ans = num1 + num2
    elif operatorID == 2 :
        userans = input("What is " + str(num1) + " - " + str(num2) + " ?  ")
        ans = num1 - num2
    else : 
        userans = input("What is " + str(num1) + " x " + str(num2) + " ?  ")
        ans = num1 * num2
    if ans == int(userans) :
        return True
    else: 
        return False
    
points = 0
for i in range(1,10):
    if problem() == True:
        points = points + 1

print("Name: " + fName + " " + lName)
print("Class: " + classCode)
print("Score: " + str(points) + "/10")