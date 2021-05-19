#Ewelina Fiuk
#WSI zadanie 3

import numpy as np
import random
from math import inf
import time

from board import Boards
from Player import Player
from play_random import play_random
from Mini_max import play_mini_max
from Exhaustive import play_exhaustive_search

    
def end(board):
        if board.is_game_over:
            return True
        if board.is_full():
            return True
        else:
            return False

def random_vs_mini_max(board, player1, player2):
    while not end(board):
        play_mini_max(board, player1)
        if end(board):
            break
        play_random(board, player2)
    return board.winner

def random_vs_exhaustive(board, player1, player2):
    while not end(board):
        play_exhaustive_search(board, player1)
        if end(board): 
            break
        play_random(board, player2)
    return board.winner

def mini_max_vs_exhaustive(board, player1, player2):
    while not end(board):
        play_mini_max(board, player1)
        if end(board): 
            break
        play_exhaustive_search(board, player2)
    return board.winner


def tournament_r_m(n):
    win_mm=0
    win_r=0
    tie=0
    times=[]
    for _ in range(n):
        b = Boards()
        p_mini_max = Player("X")
        p_random = Player("O")
        start = time.time()
        winner= random_vs_mini_max(b, p_mini_max, p_random)
        end = time.time()
        times.append(end-start)
        if winner == "X":
            win_mm+=1
        elif winner == "O":
            win_r+=1
        else:
            tie+=1
    print("MINI-MAX with ALPHA-BETA vs RANDOM algorithm")
    print("Win mini-max:", win_mm)
    print("Win random:", win_r)
    print("Ties:", tie)
    average_time = sum(times)/n
    print()
    print("Average time:", average_time)
    
def tournament_r_e(n):
    win_r = 0
    win_e =0
    tie=0
    times=[]
    for _ in range(n):
        b = Boards()
        p_exhaustive = Player("X")
        p_random = Player("O")
        start = time.time()
        winner = random_vs_exhaustive(b, p_exhaustive, p_random)
        end = time.time()
        times.append(end-start)
        if winner == "X":
            win_e+=1
        elif winner == "O":
            win_r+=1
        else:
            tie+=1
    print("EXHAUSTIVE SEARCH vs RANDOM algorithm")
    print("Win exhaustive:", win_e)
    print("Win random:", win_r)
    print("Ties:", tie)
    average_time = sum(times)/n
    print("Average time:", average_time)
    print()
    
    
def tournament_m_e(n):
    win_mm = 0
    win_e =0
    tie=0
    times=[]
    for _ in range(n):
        b = Boards()
        p_mini_max = Player("X")
        p_exhaustive = Player("O")
        start = time.time()
        winner = mini_max_vs_exhaustive(b, p_mini_max, p_exhaustive)
        end = time.time()
        times.append(end-start)
        if winner == "X":
            win_mm+=1
        elif winner == "O":
            win_e+=1
        else:
            tie+=1
    print("MINI-MAX with ALPHA-BETA vs EXHAUSTIVE SEARCH algorithm")
    print("Win mini max:", win_mm)
    print("Win exhaustive:", win_e)
    print("Ties:", tie)
    print()
    average_time = sum(times)/n
    print("Average time:", average_time)
    print()

if __name__=="__main__":
    number_of_iter =10
    tournament_r_m(number_of_iter)
    tournament_r_e(number_of_iter)
    tournament_m_e(number_of_iter)