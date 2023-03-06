# gameTrack.py
# This module contains functions which are required to keep track of the game state
import Game_var as gv
import player_input as pl
import ai as ai


def printBoard():
    for i in range(0, 3):
        print(gv.board[i])


def isGameOver():
    # checking rows
    for i in range(0, 3):
        # checking row
        if gv.board[i][0] == gv.board[i][1] == gv.board[i][2]:
            return True
        # checking column
        elif gv.board[0][i] == gv.board[1][i] == gv.board[2][i]:
            return True
        # checking diagonals
        elif (gv.board[0][0] == gv.board[1][1] == gv.board[2][2]) \
                or (gv.board[0][2] == gv.board[1][1] == gv.board[2][0]):
            return True
        # if no other condition is met and loop is at last iteration
        elif i == 2:
            return False

    """if ((gv.board[0][0] == gv.board[0][1] == gv.board[0][2]) or (gv.board[1][0] == gv.board[1][1] == gv.board[1][2])
            or (gv.board[2][0] == gv.board[2][1] == gv.board[2][2])):
        return True
    # checking columns
    for i in range(0, 3):
        if gv.board[0][i] == gv.board[1][i] == gv.board[2][i]
            return True
    
    elif ((gv.board[0][0] == gv.board[1][0] == gv.board[2][0]) or (gv.board[0][1] == gv.board[1][1] == gv.board[2][1])
            or (gv.board[0][2] == gv.board[1][2] == gv.board[2][2])):
        return True
    # checking diagonal elements
    elif (gv.board[0][0] == gv.board[1][1] == gv.board[2][2]) or (gv.board[0][2] == gv.board[1][1] == gv.board[2][0]):
        return True

    else:
        return False
"""


def allTurnsPlayed():
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if gv.board[i][j] == "X" or gv.board[i][j] == "O":
                count = count+1

    if count == 9:
        return True
    else:
        return False


# This function modifies the "winner" variable(stored in Game_var module)
# so that winner can be established by reading the variable
def winnerDef():
    if isGameOver():

        #  iterating rows
        if gv.board[0][0] == gv.board[0][1] == gv.board[0][2]:
            gv.winner = gv.board[0][0]
        elif gv.board[1][0] == gv.board[1][1] == gv.board[1][2]:
            gv.winner = gv.board[1][0]
        elif gv.board[2][0] == gv.board[2][1] == gv.board[2][2]:
            gv.winner = gv.board[2][0]

        # iterating columns
        elif gv.board[0][0] == gv.board[1][0] == gv.board[2][0]:
            gv.winner = gv.board[0][0]
        elif gv.board[0][1] == gv.board[1][1] == gv.board[2][1]:
            gv.winner = gv.board[0][1]
        elif gv.board[0][2] == gv.board[1][2] == gv.board[2][2]:
            gv.winner = gv.board[0][2]

        # iterating diagonal elements
        elif gv.board[0][0] == gv.board[1][1] == gv.board[2][2]:
            gv.winner = gv.board[0][0]
        elif gv.board[0][2] == gv.board[1][1] == gv.board[2][0]:
            gv.winner = gv.board[0][2]


def winnerName():
    winnerDef()
    if isGameOver():
        if gv.winner == "X":
            print("PLAYER A is the winner")
        elif gv.winner == "O":
            print("PLAYER B is the winner")
        elif gv.winner == "NaN":
            print("Draw")
    else:
        pass


def twoPlayer_gamePlay():
    printBoard()
    while (not isGameOver()) and (not allTurnsPlayed()):
        # take input from player 1
        pl.playerA_Turn()
        if (not isGameOver()) and (not allTurnsPlayed()):
            # take input from player 2
            pl.playerB_Turn()

        printBoard()
        winnerName()


def AI_gamePlay():
    printBoard()
    while (not isGameOver()) and (not allTurnsPlayed()):
        # take input from player
        pl.playerA_Turn()
        if (not isGameOver()) and (not allTurnsPlayed()):
            # take input from AI
            ai.AIfill_rand_loc("O")

        printBoard()
        winnerName()