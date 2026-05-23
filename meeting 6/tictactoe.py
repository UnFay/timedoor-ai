import numpy as np
import random
board = np.zeros([3,3], dtype="str")
currentTurn = 1
move = 9
Xline = np.full((3), 'X')
Oline = np.full((3), 'O')

def pickPosition(isComputer):
    currentCoords = [0,0]
    def checkInRange(number):
        if number > 2 | number < 0:
            return False
        return True
    def checkTaken():
        if board[currentCoords[1], currentCoords[0]] == '':
            return False
        return True
    if isComputer:
        while True:
            currentCoords[0] = random.randrange(0,3)
            currentCoords[1] = random.randrange(0,3)
            if not checkTaken():
                break
    else:
        while True:
            currentCoords[0] = -1
            currentCoords[1] = -1
            while currentCoords[0] == -1 & currentCoords[1] == -1:
                try:
                    currentCoords[0] = int(input("Enter X coords for your move: ")) -1
                    currentCoords[1] = int(input("Enter Y coords for your move: ")) -1
                except:
                    print("That's not a number, buddy!")
        
            if checkInRange(currentCoords[0]) == False | checkInRange(currentCoords[1]) == False:
                print("Coordinates out of range, please enter valid values.")
                continue
            if checkTaken():
                print("That position has already been filled. Please pick an empty spot.")
                continue
            if input("Are you sure this is your move? y/n") == 'y':
                break
            else:
                print("Let's input again.")
    return currentCoords

def check_win():
    def isBingo(lineArray):
        # print("Checking ", lineArray)
        firstVal = lineArray[0]
        if firstVal == '':
            return False
        for i in range(3):
            if lineArray[i] != firstVal:
                return False
        print('We have a line!')
        return True
    
    #rows & columns
    for i in range(0,3):
        # print("checking row and column ", i)
        if isBingo(board[:,i]):
            return True
        if isBingo(board[i,:]):
            return True
    #diagonal
    # print("checking diagonals")
    if isBingo(board.diagonal(0)):
        return True
    if isBingo(np.fliplr(board).diagonal(0)):
        return True
    return False

def play_turn():
    if currentTurn == 1:
        print("It's your turn!")
        coordList = pickPosition(False)
        board[coordList[1], coordList[0]] = 'X'
    else:
        print("It's the computer's turn!")
        coordList = pickPosition(True)
        board[coordList[1], coordList[0]] = 'O'
        print("The computer has made its move!")

def printBoard():
    for i in range(3):
        print(board[i, 0], " | ", board[i, 1], " | ", board[i,2])
        if i<2:
            print('-----------')

while move > 0:
    printBoard()
    play_turn()
    if check_win():
        printBoard()
        if currentTurn == 1:
            print("You have won!")
        else:
            print("Computer has won!")
        break
    currentTurn = currentTurn*-1
    move = move-1
if check_win == False & move == 0:
    print("It's a tie!")