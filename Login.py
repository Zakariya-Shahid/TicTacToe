import tkinter as tk
import sqlite3
from tkinter import messagebox
from gameSelector import GameSelector

class UserDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT
            )
        """)
        self.conn.commit()

    def add_user(self, username, password):
        self.cursor.execute("""
            INSERT INTO users (username, password)
            VALUES (?, ?)
        """, (username, password))
        self.conn.commit()

    def authenticate_user(self, username, password):
        self.cursor.execute("""
            SELECT id FROM users
            WHERE username = ? AND password = ?
        """, (username, password))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

class RegisterPage:
    def __init__(self, master, user_db, login_button):
        self.master = master
        self.user_db = user_db
        self.master.title("Register")

        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(self.master, text="Register",height='2', width='15',bg='#ddd3fe', command=lambda : self.register(register_button))
        self.register_button.pack(pady=10)
        #self.register_button.destroy()

    def register(self, registration_button):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            self.user_db.add_user(username, password)
            messagebox.showinfo("Success", "Registration successful.")
            #self.master.destroy()
            registration_button.destroy()
            self.username_entry.destroy()
            self.password_entry.destroy()
            self.username_label.destroy()
            self.password_label.destroy()
            login_button = tk.Button(self.master, text="Login",height='2', width='15',bg='#ddd3fe', command=lambda: LoginPage(self.master, self.user_db))
        else:
            messagebox.showerror("Error", "Username and password are required.")

class LoginPage:
    def __init__(self, master, user_db):
        self.master = master
        self.user_db = user_db
        self.master.title("Login")

        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()


        self.login_button = tk.Button(self.master, text="Login",height='2', width='15',bg='#ddd3fe', command=lambda : self.login(master))
        self.login_button.pack(pady=10)

    def login(self, master):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_id = self.user_db.authenticate_user(username, password)
        if user_id:
            messagebox.showinfo("Success", "Login successful.")
            #self.master.destroy()
            game_selector = GameSelector(master)
        else:
            messagebox.showerror("Error", "Invalid username or password.")



if __name__ == "__main__":
    user_db = UserDatabase("users.db")

    root = tk.Tk()
    root.title("Welcome")
    root.geometry("600x600")

    photo = tk.PhotoImage(file="xoxo.png")

    # Create a Label to display the photo
    image_label = tk.Label(root, image=photo)
    image_label.pack()
    login_button = tk.Button(root, text="Login",height='2', width='15',bg='#ddd3fe', command=lambda: LoginPage(root, user_db))
    login_button.pack(pady=10)
    #login_button.destroy()
    register_button = tk.Button(root, text="Register",height='2', width='15',bg='#ddd3fe', command=lambda: RegisterPage(root, user_db,login_button))
    register_button.pack()

    root.mainloop()