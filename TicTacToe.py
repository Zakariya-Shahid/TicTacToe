import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("500x640")
        self.create_board()
        self.create_reset_button()

    def create_board(self):
        self.buttons = []
        self.current_player = "X"

        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.master, text=" ", width=9, height=5, font=("Helvetica", 20, "bold"),
                                   command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def create_reset_button(self):
        reset_button = tk.Button(self.master, text="Reset", height='5', width='30',bg='red', command=self.reset_board)
        reset_button.grid(row=3, column=0, columnspan=3)

    def make_move(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == " ":
            button["text"] = self.current_player
            button.config(bg="gray")
            if self.check_win(row, col):
                self.highlight_winner(self.winning_cells)
            elif all(button["text"] != " " for row in self.buttons for button in row):
                messagebox.showinfo("Tie", "It's a tie!")
            else:
                self.switch_players()

    def check_win(self, row, col):
        row_values = [self.buttons[row][c]["text"] for c in range(3)]
        col_values = [self.buttons[r][col]["text"] for r in range(3)]
        diag1_values = [self.buttons[i][i]["text"] for i in range(3)]
        diag2_values = [self.buttons[i][2 - i]["text"] for i in range(3)]

        lines = [row_values, col_values, diag1_values, diag2_values]
        for line in lines:
            if all(x == self.current_player for x in line):
                self.winning_cells = []
                if line == row_values:
                    self.winning_cells = [(row, c) for c in range(3)]
                elif line == col_values:
                    self.winning_cells = [(r, col) for r in range(3)]
                elif line == diag1_values:
                    self.winning_cells = [(i, i) for i in range(3)]
                elif line == diag2_values:
                    self.winning_cells = [(i, 2 - i) for i in range(3)]
                return True
        return False

    def highlight_winner(self, cells):
        for row, col in cells:
            self.buttons[row][col].config(bg="green")
            # checking if the player is x or o
        if self.current_player == "X":
            messagebox.showinfo("Winner", "X wins")
        else:
            messagebox.showinfo("Winner", "O wins")
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def switch_players(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_board(self):
        for row in self.buttons:
            for button in row:
                button.config(text=" ", bg="white", state="normal")
        self.current_player = "X"


# root = tk.Tk()
# game = TicTacToe(root)
# root.mainloop()
