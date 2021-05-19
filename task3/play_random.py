#Ewelina Fiuk
#WSI zadanie 3

import random

def play_random(board, player):
    moves = board.avaliables_moves()
    if len(moves) == 1:
        board.make_move(moves, player.mark)
    else:
        r = random.choice(moves)
        board.make_move(r, player.mark)