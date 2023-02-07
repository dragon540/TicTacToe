import sys

import gameTrack as gt
import Game_var as gv
""""
board = [["0,0", "0,1", "0,2"],
         ["1,0", "1,1", "1,2"],
         ["2,0", "2,1", "2,2"]]

winner = "NaN"
"""
"""def printBoard():
    for i in range(0, 3):
        for j in range(0, 3):
            print(board[i][j], end=" ")
        print("")
"""
"""def printBoard():
    for i in range(0, 3):
        print(board[i])
"""

"""def isGameOver():
    # checking rows
    if ((board[0][0] == board[0][1] == board[0][2]) or (board[1][0] == board[1][1] == board[1][2])
            or (board[2][0] == board[2][1] == board[2][2])):
        return True
    # checking columns
    elif ((board[0][0] == board[1][0] == board[2][0]) or (board[0][1] == board[1][1] == board[2][1])
            or (board[0][2] == board[1][2] == board[2][2])):
        return True
    # checking diagonal elements
    elif (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        return True

    else:
        return False
"""

"""def winnerDef():  # This function modifies the "winner" variable so that winner can be established by reading the variable
    if isGameOver():
        global winner

        #  iterating rows
        if board[0][0] == board[0][1] == board[0][2]:
            winner = board[0][0]
        elif board[1][0] == board[1][1] == board[1][2]:
            winner = board[1][0]
        elif board[2][0] == board[2][1] == board[2][2]:
            winner = board[2][0]

        # iterating columns
        elif board[0][0] == board[1][0] == board[2][0]:
            winner = board[0][0]
        elif board[0][1] == board[1][1] == board[2][1]:
            winner = board[0][1]
        elif board[0][2] == board[1][2] == board[2][2]:
            winner = board[0][2]

        # iterating diagonal elements
        elif board[0][0] == board[1][1] == board[2][2]:
            winner = board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            winner = board[0][2]
"""

"""def allTurnsPlayed():
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == "X" or board[i][j] == "O":
                count = count+1

    if count == 9:
        return True
    else:
        return False
"""

"""def playerA_Turn() :
    row = int(input("PLAYER A \nEnter row of board "))
    column = int(input("Enter column of board "))

    board[row][column] = "X"


def playerB_Turn():
    row = int(input("PLAYER B \nEnter row of board "))
    column = int(input("Enter column of board "))

    board[row][column] = "O"
"""

"""def winnerName():
    winnerDef()
    if isGameOver():
        if winner == "X":
            print("PLAYER A is the winner")
        elif winner == "O":
            print("PLAYER B is the winner")
        elif winner == "NaN":
            print("NaN")
    else:
        pass
"""

"""def gamePlay() :
    printBoard()
    while (not isGameOver()) and (not allTurnsPlayed()) :
        # take input from player 1
        playerA_Turn()
        if isGameOver():
            pass
            # call function to print winner name
            #winnerName()
        elif (not isGameOver()) and (not allTurnsPlayed()):
            # take input from player 2
            playerB_Turn()

        printBoard()
        winnerName()
"""

gt.AI_gamePlay()
print("======================")
gt.winnerName()
print(gv.winner)

