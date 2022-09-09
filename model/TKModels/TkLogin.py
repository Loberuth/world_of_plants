import tkinter as tk

class TkLogin:
    def __init__(self):
        self.usernameEntry = tk.StringVar()
        self.passwordEntry = tk.StringVar()
        self.incorrectUsername = tk.StringVar()
        self.incorrectPassword = tk.StringVar()
        self.saveUserAtLogin = tk.BooleanVar()