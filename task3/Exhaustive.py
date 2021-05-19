from board import Boards
from math import inf

def play_exhaustive_search(board, player):
    best_score = -inf
    move = [0,0]
    for i in range(len(board.board)):
        for j in range(len(board.board)):
              if board.board[i][j] == None:
                board.make_move([i,j], player.mark)
                score = exhaustive(board, player, is_maximizing=False)
                board.make_move([i,j], None)
                if score > best_score:
                    best_score = score
                    move = [i,j]
    board.make_move(move, player.mark)

def exhaustive(board, player, is_maximizing):
    if board.is_game_over:
        return player.scores[board.winner]
    if is_maximizing:
        best_score = -inf
        for i in range(len(board.board)):
            for j in range(len(board.board)):
              if board.board[i][j] == None:
                  board.make_move([i,j], player.mark)
                  score = exhaustive(board, player, False)
                  board.make_move([i,j], None)
                  best_score = max(score, best_score)
        return best_score
    else:
        best_score = inf
        for i in range(len(board.board)):
            for j in range(len(board.board)):
              if board.board[i][j] == None:
                  board.make_move([i,j], player.oposite_mark)
                  score = exhaustive(board, player, True)
                  board.make_move([i,j], None)
                  best_score = min(score, best_score)
        return best_score
        