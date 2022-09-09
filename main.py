import tkinter as tk
from tkinter import ttk
from screens.LoginPage import LoginPage
from config.DBConfig import engine, base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
base.metadata.create_all(engine)

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))
        self.title("PyFlora")

        self.container = ttk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True)
        self.container['relief'] = tk.GROOVE
        self.container['borderwidth'] = 10
        self.createPyFlora()

    def createPyFlora(self):
        LoginPage(self.container, session)


if __name__ == '__main__':
    app = App()
    app.mainloop()
