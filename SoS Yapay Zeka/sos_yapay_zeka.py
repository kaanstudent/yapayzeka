import numpy as np
import random
import time
import ipywidgets as widgets
from IPython.display import display, clear_output

class XOXGame:
    def __init__(self, size=3):
        self.size = size
        self.board = np.full((size, size), " ")
        self.current_player = "AI"
        self.training = True
        self.ai_score = 0

    def reset(self):
        self.board.fill(" ")
        self.current_player = "AI"

    def is_valid_move(self, row, col):
        return self.board[row, col] == " "

    def make_move(self, row, col, letter):
        if self.is_valid_move(row, col):
            self.board[row, col] = letter
            return True
        return False

    def check_winner(self):
        for i in range(self.size):
            if all(self.board[i, :] == "X") or all(self.board[i, :] == "O"):
                return True
            if all(self.board[:, i] == "X") or all(self.board[:, i] == "O"):
                return True
        if all(np.diag(self.board) == "X") or all(np.diag(self.board) == "O"):
            return True
        if all(np.diag(np.fliplr(self.board)) == "X") or all(np.diag(np.fliplr(self.board)) == "O"):
            return True
        return False

    def print_board(self):
        clear_output(wait=True)
        for row in self.board:
            print(" | ".join(row))
            print("-" * (self.size * 4 - 1))

    def ai_move(self):
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i, j] == " "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            letter = random.choice(["X", "O"])
            self.make_move(row, col, letter)

    def train_ai(self):
        while self.training:
            self.ai_move()
            self.print_board()
            time.sleep(0.5)
            if self.check_winner():
                self.ai_score += 1
                print(f"AI Training - Score: {self.ai_score}")
                self.reset()
        print("AI training stopped. Ready to play!")

    def user_move(self, row, col, letter):
        if self.make_move(row, col, letter):
            self.print_board()
            if self.check_winner():
                print("Congratulations! You won!")
                return True
        return False

game = XOXGame()

train_button = widgets.Button(description="Start AI Training")
stop_training_button = widgets.Button(description="Stop Training")
play_button = widgets.Button(description="Play Game")
stop_playing_button = widgets.Button(description="Stop Playing")
row_input = widgets.BoundedIntText(value=0, min=0, max=2, description='Row:')
col_input = widgets.BoundedIntText(value=0, min=0, max=2, description='Col:')
letter_input = widgets.Dropdown(options=['X', 'O'], description='Letter:')
submit_button = widgets.Button(description="Make Move")

output = widgets.Output()

def start_training(b):
    game.training = True
    game.train_ai()

def stop_training(b):
    game.training = False

def play_game(b):
    with output:
        print("Game started! Choose your move.")
        display(row_input, col_input, letter_input, submit_button)

def stop_playing(b):
    with output:
        print("Game stopped. You can restart training or play again.")
        clear_output()

def on_submit(b):
    with output:
        success = game.user_move(row_input.value, col_input.value, letter_input.value)
        if not success:
            print("Invalid move, try again!")

train_button.on_click(start_training)
stop_training_button.on_click(stop_training)
play_button.on_click(play_game)
stop_playing_button.on_click(stop_playing)
submit_button.on_click(on_submit)

display(train_button, stop_training_button, play_button, stop_playing_button, output)
