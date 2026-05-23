#person class
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    # say hello function
    def sayHello(self):
        print("Hello " + self.name + ", nice to meet you")

    #checkride function
    def ride(self):
        self.sayHello()
        if (self.age > 10 and self.height >= 100):
            print("Congratulations, " + self.name + "! You may ride the roller coaster.")
        else:
            print("Sorry " + self.name +", you may not ride the roller coaster.")

#initialize person objects
james = Person("James", 10, 140)
rose = Person("Rose", 12, 150)
dove = Person("Dove", 12, 150)
diva = Person("Diva", 8, 130)

#loop
while True:
    name = (input("Enter name: ")).lower()
    if (name == "james"):
        james.ride()
    elif (name == "rose"):
        rose.ride()
    elif (name == "dove"):
        dove.ride()
    elif (name == "diva"):
        diva.ride()
    else:
        print("Invalid name input")
    ans = input("Enter 'y' to continue / 'n' to quit")
    if (ans == "n"):
        break