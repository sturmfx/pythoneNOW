import tkinter as tk
import random

ROWS = 10
COLUMNS = 10
MINES = 10
CELL_SIZE = 50


def create_board():
    board = [[{'value': None, 'hidden': True, 'flagged': False} for j in range(COLUMNS) for i in range(ROWS)]]
    for i in range(MINES):
        while True:
            row = random.randint(0, ROWS - 1)
            col = random.randint(0, COLUMNS - 1)
            if board[row][col]['value'] != '*':
                board[row][col]['value'] = '*'
                break

    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i][j]['value'] != '*':
                count = 0
                for ii in range(max(0, i - 1), min(i + 2, ROWS)):
                    for jj in range(max(0, j - 1), min(j + 2, COLUMNS)):
                        if board[ii][jj]['value'] == '*':
                            count = count + 1
                board[i][j]['value'] = count
    return board

def flag_cell(row, col):
    global board, cells
    cell = board[row][col]
    if cell['hidden']:
        if cell['flagged']:
            cell['flagged'] = False
            #canvas
        else:
            cell['flagged'] = True
            #canvas
            check_win()

def check_win():
    global board
    for i in range(ROWS):
        for j in range(COLUMNS):
    
    
    
board = create_board()
