import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return f"You win! Computer chose {computer_choice}."
    else:
        return f"You lose! Computer chose {computer_choice}."

# Function to handle button clicks
def on_button_click(choice):
    result = determine_winner(choice)
    messagebox.showinfo("Result", result)

# Create the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create buttons for Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click('Rock'))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click('Paper'))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click('Scissors'))
scissors_button.pack(pady=10)

# Run the main event loop
root.mainloop(
