import random
import tkinter as tk

# Initialization
ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'
RESULT_DRAW = 'DRAW'
RESULT_PLAYER_WINS = 'PLAYER WINS'
RESULT_COMPUTER_WINS = 'COMPUTER WINS'

# Player choice
def get_player_choice():
    return player_choice_var.get()

# Computer choice
def get_computer_choice():
    choices = [ROCK, PAPER, SCISSORS]
    return random.choice(choices)

# Checking the winner result
def get_winner(computer_choice, player_choice):
    if computer_choice == player_choice:
        return RESULT_DRAW
    elif (computer_choice == ROCK and player_choice == PAPER) or \
         (computer_choice == PAPER and player_choice == SCISSORS) or \
         (computer_choice == SCISSORS and player_choice == ROCK):
        return RESULT_PLAYER_WINS
    else:
        return RESULT_COMPUTER_WINS

# Working on button click
def start_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    winner = get_winner(computer_choice, player_choice)

    # Message on game over
    result_message.set(f"You picked {player_choice} and computer picked {computer_choice}, therefore you ")

    if winner == RESULT_DRAW:
        result_message.set(result_message.get() + 'had a draw.')
    elif winner == RESULT_PLAYER_WINS:
        result_message.set(result_message.get() + 'won.')
    else:
        result_message.set(result_message.get() + 'lost.')

# Create GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("500x150")

player_choice_var = tk.StringVar(value="")

rock_radio = tk.Radiobutton(root, text="Rock", variable=player_choice_var, value=ROCK)
rock_radio.pack()

paper_radio = tk.Radiobutton(root, text="Paper", variable=player_choice_var, value=PAPER)
paper_radio.pack()

scissors_radio = tk.Radiobutton(root, text="Scissors", variable=player_choice_var, value=SCISSORS)
scissors_radio.pack()

start_game_btn = tk.Button(root, text="Start Game", command=start_game)
start_game_btn.pack()

result_message = tk.StringVar()
result_label = tk.Label(root, textvariable=result_message)
result_label.pack()

root.mainloop()
