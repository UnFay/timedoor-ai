import random
import string
print("Welcome to Password Maker!")

adjectives = ["sleepy", "slow", "fluffy", "red", "yellow", "blue", "green", "purple", "grey"]
nouns = ["Dinosaur", "Ball", "Dragon", "Dog", "Cat", "Sheep", "Hammer", "Screwdriver", "Apple", "Orange", "Banana", "Strawberry", "Melon", "Lemon", "Pineapple", "Duck", "Chicken", "Panda"]
adjective = random.choice(adjectives)
noun = random.choice(nouns)
number= random.randrange(0, 100)
char = random.choice(string.punctuation)
password = adjective + noun + str(number) + char
print("Password: " + password)