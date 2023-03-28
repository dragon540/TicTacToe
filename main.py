import sys

import gameTrack as gt
import Game_var as gv

# COMMAND LINE GAME INTERFACE
mode = input("Enter Mode:\nSingle Player - S\nMultiplayer Player - M\n")

if mode == 'M' or mode == 'm':
    gt.twoPlayer_gamePlay()
elif mode == 'S' or mode == 's':
    gt.AI_gamePlay()

