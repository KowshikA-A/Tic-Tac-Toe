import tkinter as tk
import random  
from tkinter import messagebox
def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    if all(board[i][i] == player for i in range(len(board))) or all(board[i][len(board) - 1 - i] == player for i in range(len(board))):
        return True

    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def on_button_click(row, col):
    global current_player, board
    if board[row][col] == ' ':
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state=tk.DISABLED)
        if current_player == 'X':
            buttons[row][col].config(fg='red')  
        else:
            buttons[row][col].config(fg='#FFA500')  
        
        if check_winner(board, current_player):
            result_label.config(text=f"Player {current_player} wins! in the last game", fg='red', font=('Times New Roman', 40)) 
            disable_buttons()
            ask_play_again()
        elif is_full(board):
            result_label.config(text="It's a tie!", fg='green', font=('Helvetica', 40))  
            disable_buttons()
            ask_play_again()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def disable_buttons():
    for row in range(size):
        for col in range(size):
            buttons[row][col].config(state=tk.DISABLED)

def ask_play_again():
    play_again = tk.messagebox.askyesno("Play Again", "Do you want to play again?")
    if play_again:
        restart_game()
    else:
        window.destroy()

def restart_game():
    global current_player, board
    # Clear the board and reset the current player
    board = create_board(size)
    current_player = random.choice(['X', 'O'])
    for row in range(size):
        for col in range(size):
            buttons[row][col].config(text=' ', state=tk.NORMAL, fg='white')

# Gets user input for the number of rows and columns (must be equal and at least 3, and not more than 24)
while True:
    try:
        size = int(input("Enter the number of rows and columns (must be equal and at least 3, and not more than 24): "))
        if size < 3 or size > 24:
            raise ValueError("Size must be at least 3 and not more than 24.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")
    def ask_play_again():
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")  
        # Using messagebox from tkinter
    if play_again:
        restart_game()
    else:
        windows_events.destroy()

board = create_board(size)
current_player = random.choice(['X', 'O'])  
# Randomly assigning the first player
    
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Setting the background color of the window to steel blue
window.configure(bg='steel blue')

# Creating a frame to center the board
frame = tk.Frame(window)
frame.pack(expand=True)

buttons = [[None for _ in range(size)] for _ in range(size)]

for row in range(size):
    for col in range(size):
        buttons[row][col] = tk.Button(frame, text=' ', width=5, height=1, command=lambda row=row, col=col: on_button_click(row, col), bg='steel blue')
        buttons[row][col].grid(row=row, column=col)

result_label = tk.Label(window, text='', font=('Helvetica', 16), bg='steel blue', fg='white')
result_label.pack(pady=60)

window.mainloop()



















