# player_input.py
# this module is for calling input from both players
import Game_var
import gameTrack as gt


def playerA_Turn():
    row = int(input("PLAYER A \nEnter row of board "))
    column = int(input("Enter column of board "))

    # add checks for wrong input
    # do something to stop player from changing the value of a location which is not empty
    if gt.IsEmpty(row, column):
        Game_var.board[row][column] = "X"
    else:
        print("This box is already filled")
        playerA_Turn()



def playerB_Turn():
    row = int(input("PLAYER B \nEnter row of board "))
    column = int(input("Enter column of board "))

    # add checks for wrong input
    # do something to stop player from changing the value of a location which is not empty

    if gt.IsEmpty(row, column):
        Game_var.board[row][column] = "O"
    else:
        print("This box is already filled")
        playerA_Turn()
