import tkinter as tk

# Constants
ROWS = 6
COLS = 7
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

# Initialize board
board = [[EMPTY] * COLS for _ in range(ROWS)]
current_player = PLAYER_1

def draw_board():
    canvas.delete("all")  # Clear previous drawings

    cell_size = 50
    for row in range(ROWS):
        for col in range(COLS):
            x1, y1 = col * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size

            color = "white" if board[row][col] == EMPTY else ("red" if board[row][col] == PLAYER_1 else "yellow")
            canvas.create_oval(x1, y1, x2, y2, fill=color)