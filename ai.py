# This module contains functions and variables for computer to play against human
import random
import copy

import Game_var as gv


# This function randomly fills an empty location
def AIfill_rand_loc(ai_symbol):
    r = random.randint(0, 2)
    c = random.randint(0, 2)
    while gv.board[r][c] == "X" or gv.board[r][c] == "O":
        r = random.randint(0, 2)
        c = random.randint(0, 2)

    gv.board[r][c] = ai_symbol


# This function iterates through rows, columns and diagonals
# to check if there is a possibility that triplets of symbols can be formed
# if possibility of a triplet is found, then the empty location(with potential to form triplet) is returned
def tripletPossibility(symbol):

    # checking every row
    for r in range(0, 3):
        empty_el: int = 0
        symbol_el: int = 0
        cord = [-1, -1]
        for c in range(0, 3):
            if gv.board[r][c] != 'X' and gv.board[r][c] != 'O':  # to see if given element is empty or not
                empty_el += 1
                cord = [r, c]
            elif gv.board[r][c] == symbol:
                symbol_el += 1
            if empty_el == 1 and symbol_el == 2:
                return cord

    # checking every column
    for c in range(0, 3):
        empty_el: int = 0
        symbol_el: int = 0
        cord = [-1, -1]
        for r in range(0, 3):
            if gv.board[r][c] != 'X' and gv.board[r][c] != 'O':  # to see if given element is empty or not
                empty_el += 1
                cord = [r, c]
            elif gv.board[r][c] == symbol:
                symbol_el += 1
            if empty_el == 1 and symbol_el == 2:
                return cord

    # checking diagonals

    # diagonal 1
    empty_el: int = 0
    symbol_el: int = 0
    cord = [-1, -1]
    for i in range(0, 3):
        if gv.board[i][i] != 'X' and gv.board[i][i] != 'O':  # to see if given element is empty or not
            empty_el += 1
            cord = [i, i]
        elif gv.board[i][i] == symbol:
            symbol_el += 1
        if empty_el == 1 and symbol_el == 2:
            return cord
    """"
    # diagonal 2
    # create a reversed board and check its diagonals
    # rev_board = gv.board - doing this wrong since effects the original board, since in python
    # setting a variable actually sets a reference to the variable
    rev_board = copy.deepcopy(gv.board)
    for i in range(0, 3):
        # swap first and last element of every row
        temp = rev_board[i][0]
        rev_board[i][0] = rev_board[i][2]
        rev_board[i][2] = temp
    # checking this reversed board
    empty_el: int = 0
    symbol_el: int = 0
    cord = [-1, -1]
    for i in range(0, 3):
        if rev_board[i][i] != 'X' and rev_board[i][i] != 'O':
            empty_el += 1
            cord = [i, i]
        elif rev_board[i][i] == symbol:
            symbol_el += 1
        if empty_el == 1 and symbol_el == 2:
            return cord
    """
    cord = [-1, -1]
    return cord


