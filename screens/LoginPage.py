import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Frame
from model.TKModels.TkLogin import TkLogin
from model.TKModels.TkImages import TkImages
import tkinter.font as font
from entity.UserEntity import UserEntity
from screens.MainContent import MainPageContent
from utils.Utils import Utils
from os import path

class LoginPage(Frame):
    def __init__(self, container, session):
        super().__init__(container)
        self.container = container
        self.session = session
        self.grid()
        self.tkLoginModel = TkLogin()
        self.tkImages = TkImages()
        self.loginPage()

    def loginPage(self):
        self.FILE_NAME = "userInfo.txt"

        self.mainPageContent = MainPageContent(self, self.session)
        self.usersFromDB = self.session.query(UserEntity).all()

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.lblHeading = ttk.Label(self, text="Welcome to Flora World", font=('Arial', 30, "bold"), foreground="#50B148")
        self.lblHeading.grid(row=0, column=0, pady=10)
        self.lblHeading.grid_rowconfigure(1, weight=1)
        self.lblHeading.grid_columnconfigure(1, weight=1)

        self.lblLogin = ttk.LabelFrame(self)
        self.lblLogin.grid(row=1, column=0, pady=60, padx=5)

        lblLoginHeading = ttk.Label(self.lblLogin, text="Login", font=('Arial', 21, "bold"))
        lblLoginHeading.grid(row=0, column=0, columnspan=2, pady=30)

        lblUsername = ttk.Label(self.lblLogin, text="Username", font=('Arial', 10, "normal"))
        lblUsername.grid(row=1, column=0, padx=15, pady=5, sticky=tk.W)

        entryUsername = ttk.Entry(self.lblLogin, textvariable=self.tkLoginModel.usernameEntry, width=40)
        entryUsername.grid(row=2, column=0, padx=15, pady=5, ipady=1, sticky=tk.W)

        lblIncorrectUsername = ttk.Label(self.lblLogin, textvariable=self.tkLoginModel.incorrectUsername)
        lblIncorrectUsername.grid(row=3, column=0, pady=(2, 10), padx=15, sticky=tk.W)

        entryUsername.bind("<Return>", self.loginEvent)

        lblPassword = ttk.Label(self.lblLogin, text="Password", font=('Arial', 10, "normal"))
        lblPassword.grid(row=4, column=0, padx=15, pady=5, sticky=tk.W)

        self.entryPassword = ttk.Entry(self.lblLogin, show='*', textvariable=self.tkLoginModel.passwordEntry, width=40)
        self.entryPassword.grid(row=5, column=0, padx=(15, 0), pady=5, ipady=1, sticky=tk.W)

        self.btnTogglePassword = ttk.Button(self.lblLogin, image=self.tkImages.hidePassword, command=self.togglePasswordVisibility)
        self.btnTogglePassword.grid(row=5, column=1, padx=(0, 15), pady=5)

        lblIncorrectPassword = ttk.Label(self.lblLogin, textvariable=self.tkLoginModel.incorrectPassword)
        lblIncorrectPassword.grid(row=6, column=0, pady=(2, 10), padx=15, sticky=tk.W)

        self.entryPassword.bind("<Return>", self.loginEvent)

        saveUserAtLogin = ttk.Checkbutton(self.lblLogin, text="Save at login", variable=self.tkLoginModel.saveUserAtLogin)
        saveUserAtLogin.grid(row=7, column=0, padx=15, pady=(0, 10), sticky=tk.W)

        btnStyle = font.Font(size=11, weight="bold")
        btnLogin = tk.Button(self.lblLogin, text="Login", bg="#50B148", fg="#fff", borderwidth=0, command=self.login)
        btnLogin.grid(row=8, column=0, columnspan=2, padx=15, pady=(15, 25), ipady=3, sticky=tk.EW)
        btnLogin['font'] = btnStyle

        username = self.tkLoginModel.usernameEntry.get()
        password = self.tkLoginModel.passwordEntry.get()
        if username != "" and password != "":
            if self.tkLoginModel.saveUserAtLogin.get():
                with open(self.FILE_NAME, "w") as f:
                    f.write(f"{username};{password}")
                    f.close()
            else:
                with open(self.FILE_NAME, "w") as f:
                    f.write(f";")
                    f.close()

        if path.exists(self.FILE_NAME):
            f = open(self.FILE_NAME)
            line = f.readline()
            f.close()
            username, password = line.split(";")
            if username != "" and password != "":
                self.tkLoginModel.usernameEntry.set(username)
                self.tkLoginModel.passwordEntry.set(password)
                self.tkLoginModel.saveUserAtLogin.set(True)
            else:
                self.tkLoginModel.usernameEntry.set("")
                self.tkLoginModel.passwordEntry.set("")
                self.tkLoginModel.incorrectUsername.set("")
                self.tkLoginModel.incorrectPassword.set("")

    def togglePasswordVisibility(self):
        Utils.showOrHidePassword(self.entryPassword, self.btnTogglePassword, self.tkImages)

    def login(self):
        username = self.tkLoginModel.usernameEntry.get()
        password = self.tkLoginModel.passwordEntry.get()

        for user in self.usersFromDB:
            if username == user.username and password == user.password:
                self.lblHeading.destroy()
                self.lblLogin.destroy()
                self.mainPageContent.createMainContentPage()
            if username != user.username:
                self.tkLoginModel.incorrectUsername.set("Wrong username, try again!")
                self.tkLoginModel.usernameEntry.set("")
            if password != user.password:
                self.tkLoginModel.incorrectPassword.set("Wrong password, try again!")
                self.tkLoginModel.passwordEntry.set("")
                self.btnTogglePassword.config(image=self.tkImages.hidePassword)
                self.entryPassword.config(show="*")

    def loginEvent(self, event):
        self.login()