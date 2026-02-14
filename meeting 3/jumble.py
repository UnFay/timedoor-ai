import random
import string
words = ["python", "computer", "programming", "condition", "else", "break", "input", "print", "while", "for"]
numberOfWords = len(words)
score = 0
pName = input("Enter player name:  ")

while True:
    pick = random.choice(words)
    words.remove(pick)
    random_word = random.sample(pick, len(pick))
    jumbled = "".join(random_word)
    print("Jumbled word is: ", jumbled )
    guess = input("What's your guess?  ")
    if guess.lower() == pick:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer is " + pick)
    if len(words) == 0:
        break
print("Player: " + pName)
print("Final score: "+ str(score) + "/" + str(numberOfWords))
if score == 10:
    print("You won!")
else:
    print("Better luck next time!")