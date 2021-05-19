from board import Boards
from math import inf


def play_mini_max(board, player):
    best_score = -inf
    move = [None, None]
    for i in range(len(board.board)):
        for j in range(len(board.board)):
              if board.board[i][j] == None:
                board.make_move([i,j], player.mark)
                score = minimax(board, player, 0, is_maximizing=False)
                board.make_move([i,j], None)
                if score > best_score:
                    best_score = score
                    move = [i,j]
    board.make_move(move, player.mark)

def minimax(board, player, depth, is_maximizing, alpha=-inf, beta=inf):
    if board.is_game_over:
        return player.scores[board.winner]
    if is_maximizing:
        best_score = -inf
        for i in range(len(board.board)):
            for j in range(len(board.board)):
              if board.board[i][j] == None:
                  board.make_move([i,j], player.mark)
                  score = minimax(board, player, depth+1, False, alpha, beta)
                  board.make_move([i,j], None)
                  best_score = max(score, best_score)
                  alpha = max(alpha, score)
                  if beta <= alpha:
                    break
        return best_score
    else:
        best_score = inf
        for i in range(len(board.board)):
            for j in range(len(board.board)):
              if board.board[i][j] == None:
                  board.make_move([i,j], player.oposite_mark)
                  score = minimax(board, player, depth+1, True, alpha, beta)
                  board.make_move([i,j], None)
                  best_score = min(score, best_score)
                  beta = min(beta, score)
                  if beta <= alpha:
                    break
        return best_score