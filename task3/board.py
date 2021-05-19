import numpy as np

class Boards:
    def __init__(self):
        self.board = np.array([ [None] * 3 for _ in range(3) ])
        self.is_game_over = False
        self.winner = None

    def make_move(self, move, player):
        self.board[move[0]][move[1]] = player
        self.check_board()

    def avaliables_moves(self):
        moves = []
        for i,row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == None:
                    moves.append([i,j])
        return moves

    def is_full(self):
        i = 0
        for row in self.board:
            for col in row:
                if col != None: i+=1
        if i == 9: return True
        else: return False

    def row_win(self):
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0]!= None: 
                self.is_game_over = True
                self.winner = self.board[i][0]
                return True
        return False
    
    def col_win(self):
        for i in range(len(self.board)):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]  and self.board[0][i] != None: 
                self.is_game_over = True
                self.winner = self.board[0][i]
                return True
        return False

    def diagonal_win(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2]  and self.board[0][0] != None:
            self.is_game_over = True
            self.winner = self.board[0][0]
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]  and self.board[0][2]!= None: 
            self.is_game_over = True
            self.winner = self.board[0][2]
            return True
        else:
            return False
            
    def check_board(self):
        if not self.row_win() and not self.col_win() and not self.diagonal_win():
            self.is_game_over=False
            self.winner = None