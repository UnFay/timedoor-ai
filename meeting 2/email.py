import random
import string
adjectives = ["sleepy", "slow", "fluffy", "red", "yellow", "blue", "green", "purple", "grey"]

name = input("Enter your first name:  ")
number = random.randrange(0, 100)
adjective = random.choice(adjectives)

print("Your email: " + adjective + name + str(number) + "@gmail.com")