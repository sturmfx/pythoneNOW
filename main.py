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
            canvas.itemconfigure(cells[row][col], fill='gray', text='')
        else:
            cell['flagged'] = True
            canvas.itemconfigure(cells[row][col], fill='orange', text='F')
            check_win()

def check_win():
    global board
    for i in range(ROWS):
        for j in range(COLUMNS):
            cell = board[i][j]
            if cell['hidden'] and not cell['flagged']:
                return
    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i][j]['value'] == '*':
                canvas.itemconfigure(cells[i][j], fill='black', text='*')
    canvas.unbind("<Button-1>")
    #canvas binding here
def create_cell(row, col):
    global cells
    x0 = col * CELL_SIZE
    y0 = row * CELL_SIZE
    x1 = x0 + CELL_SIZE
    y1 = y0 + CELL_SIZE
    cell = canvas.create_rectangle(x0, y0, x1, y1, fill='gray', tags='cell')
    canvas.tag_bind(cell, 'Button-1', lambda event, row=row, col=col:show_cell(row, col))
    canvas.tag_bind(cell, 'Button-3', lambda event, row=row, col=col: flag_cell(row, col))
    cells[row][col] = cell

def show_cell(row, col):
    global board, cells
    cell = board[row][col]
    if cell['hidden'] and not cell['flagged']:
        cell['hidden'] = False
        if cell['value'] == '*':
            for i in range(ROWS):
                for j in range(COLUMNS):
                    if board[i][j]['value'] == '*':
                        canvas.itemconfigure(cells[i][j], fill='red')
            canvas.unbind("<Button-1>")
        elif cell['value'] == 0:
            canvas.itemconfigure(cells[row][col], fill='green', text='')
            for i in range(max(0, row-1), min(row + 2, ROWS)):
                for j in range(max(0, col-1), min(col+2, COLUMNS)):
                    show_cell(i, j)
        else:
            canvas.itemconfigure(cells[row][col], fill='green', text=str(cell['value']))
            check_win()
root = tk.Tk()
root.Title("САПЁР")
canvas = tk.Canvas(root, width=COLUMNS * CELL_SIZE, height = ROWS * CELL_SIZE)
canvas.pack()

cells = [[None for j in range(COLUMNS)] for i in range(ROWS)]
for i in range(ROWS):
    for j in range(COLUMNS):
        create_cell(i, j)

board = create_board()
root.mainloop()
