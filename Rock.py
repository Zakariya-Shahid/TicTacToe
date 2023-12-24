import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        # Player choice label and buttons
        player_choice_label = tk.Label(self.master, text="Select your choice:")
        player_choice_label.pack()

        rock_button = tk.Button(self.master, text="Rock", bg='red', height='5', width='30', command=lambda: self.make_choice("rock"))
        rock_button.pack()

        paper_button = tk.Button(self.master, text="Paper", bg='#b3b3fe', height='5', width='30', command=lambda: self.make_choice("paper"))
        paper_button.pack()

        scissors_button = tk.Button(self.master, text="Scissors", bg='blue', height='5', width='30', command=lambda: self.make_choice("scissors"))
        scissors_button.pack()

        # Result label
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

        # Computer choice label
        self.computer_choice_label = tk.Label(self.master, text="")
        self.computer_choice_label.pack()

    def make_choice(self, player_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Update computer choice label
        self.computer_choice_label.config(text=f"Computer chose {computer_choice.capitalize()}")

        # Determine winner
        if player_choice == computer_choice:
            result = "Tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        # Update result label
        self.result_label.config(text=result)

# root = tk.Tk()
# game = RockPaperScissors(root)
# root.mainloop()
