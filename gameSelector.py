import tkinter as tk
from TicTacToe import TicTacToe
from Rock import RockPaperScissors

class GameSelector:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Selector")
        self.master.geometry("500x400")
        self.create_buttons()

    def create_buttons(self):
        tic_tac_toe_button = tk.Button(self.master, text="Tic Tac Toe", height='5', width='40', bg='#a3b3fe', command=self.play_tic_tac_toe)
        tic_tac_toe_button.pack(pady=10)

        rock_paper_scissors_button = tk.Button(self.master, text="Rock Paper Scissors", height='5', width='40', bg='#abb3fe', command=self.play_rock_paper_scissors)
        rock_paper_scissors_button.pack(pady=10)

    def play_tic_tac_toe(self):
        self.master.destroy()
        root = tk.Tk()
        game = TicTacToe(root)
        root.mainloop()

    def play_rock_paper_scissors(self):
        self.master.destroy()
        root = tk.Tk()
        game = RockPaperScissors(root)
        root.mainloop()

# if __name__ == "__main__":
#     root = tk.Tk()
#     game_selector = GameSelector(root)
#     root.mainloop()
