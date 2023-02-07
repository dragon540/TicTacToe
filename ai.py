# This module contains functions and variables for computer to play against human
import random

import Game_var as gv


def AIfill_rand_loc(ai_symbol):
    r = random.randint(0, 2)
    c = random.randint(0, 2)
    while gv.board[r][c] == "X" or gv.board[r][c] == "O":
        r = random.randint(0, 2)
        c = random.randint(0, 2)

    gv.board[r][c] = ai_symbol
