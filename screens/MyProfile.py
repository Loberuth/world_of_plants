import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Frame
from model.TKModels.TkUsers import TkUsers
from entity.UserEntity import UserEntity
from model.TKModels.TkLogin import TkLogin
from utils.Utils import Utils
from model.TKModels.TkImages import TkImages

class MyProfile(Frame):
    def __init__(self, container, session):
        super().__init__(container)
        self.container = container
        self.session = session
        self.grid()
        self.utils = Utils()
        self.tkUsers = TkUsers()
        self.tkLoginModel = TkLogin()
        self.tkImages = TkImages()

    def createMyProfilePage(self, myProfileTab):
        lblName = ttk.Label(myProfileTab, text="First Name:")
        lblName.grid(row=0, column=0, padx=10, pady=15, sticky=tk.W)

        entryName = ttk.Entry(myProfileTab, width=40, textvariable=self.tkUsers.firstName)
        entryName.grid(row=1, column=0, padx=10, pady=5)
        btnDeleteFromEntry = ttk.Button(myProfileTab, image=self.tkImages.bin, command=lambda btnId=1: self.utils.deleteFromEntry(btnId, self.tkUsers.firstName))
        btnDeleteFromEntry.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)

        lblLastName = ttk.Label(myProfileTab, text="Last Name:")
        lblLastName.grid(row=2, column=0, padx=10, pady=15, sticky=tk.W)

        entryLastName = ttk.Entry(myProfileTab, width=40, textvariable=self.tkUsers.lastName)
        entryLastName.grid(row=3, column=0, padx=10, pady=5)
        btnDeleteFromEntry = ttk.Button(myProfileTab, image=self.tkImages.bin, command=lambda btnId=2: self.utils.deleteFromEntry(btnId, self.tkUsers.lastName))
        btnDeleteFromEntry.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

        lblUsername = ttk.Label(myProfileTab, text="Username:")
        lblUsername.grid(row=4, column=0, padx=10, pady=15, sticky=tk.W)

        entryUsername = ttk.Entry(myProfileTab, width=40, textvariable=self.tkUsers.username)
        entryUsername.grid(row=5, column=0, padx=10, pady=5)
        btnDeleteFromEntry = ttk.Button(myProfileTab, image=self.tkImages.bin, command=lambda btnId=3: self.utils.deleteFromEntry(btnId, self.tkUsers.username))
        btnDeleteFromEntry.grid(row=5, column=1, pady=5, padx=5, sticky=tk.W)

        lblPassword = ttk.Label(myProfileTab, text="Password:")
        lblPassword.grid(row=6, column=0, padx=10, pady=15, sticky=tk.W)

        self.entryPassword = ttk.Entry(myProfileTab, show='*', width=40, textvariable=self.tkUsers.password)
        self.entryPassword.grid(row=7, column=0, padx=10, pady=5)

        self.btnTogglePassword = ttk.Button(myProfileTab, image=self.tkImages.hidePassword, command=self.togglePasswordVisibility)
        self.btnTogglePassword.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

        btnDeleteFromEntry = ttk.Button(myProfileTab, image=self.tkImages.bin, command=lambda btnId=4: self.utils.deleteFromEntry(btnId, self.tkUsers.password))
        btnDeleteFromEntry.grid(row=7, column=2, pady=5, padx=5, sticky=tk.W)

        lblPosition = ttk.Label(myProfileTab, text="Position:")
        lblPosition.grid(row=8, column=0, padx=10, pady=15, sticky=tk.W)

        entryPosition = ttk.Entry(myProfileTab, width=40, state="disabled", textvariable=self.tkUsers.position)
        entryPosition.grid(row=9, column=0, padx=10, pady=5)

        asterisk = ttk.Label(myProfileTab, text="*", foreground="red", font=2)
        asterisk.grid(row=9, column=1, pady=5, sticky=tk.W)

        btnUpdateUser = tk.Button(myProfileTab, text="Update", font=('Arial', 11, 'bold'), bd=0, relief="flat", bg="#2E9487", fg="#ffffff", command=self.updateUser)
        btnUpdateUser.grid(row=9, column=2, padx=5, pady=5, ipadx=10, sticky=tk.W)

        note = ttk.Label(myProfileTab, text="* This is the only profile that has admin rights, hence you cannot change your position!\n"
                                            "Only admin has the rights to add/update/delete any data.", foreground="red")
        note.grid(row=10, column=0, columnspan=20, padx=10, pady=5)

        self.getUserInfoFromDB()

    def getUserInfoFromDB(self):
        username = self.session.query(UserEntity).filter_by(id=1).first() # s obzirom da je samo 1 korisnik, odmah dohvacamo tog jednog korisnika
        self.tkUsers.firstName.set(username.firstName)
        self.tkUsers.lastName.set(username.lastName)
        self.tkUsers.username.set(username.username)
        self.tkUsers.password.set(username.password)
        self.tkUsers.position.set(username.position)

    def togglePasswordVisibility(self):
        Utils.showOrHidePassword(self.entryPassword, self.btnTogglePassword, self.tkImages)

    def updateUser(self):
        entryName = self.tkUsers.firstName.get()
        nameFromDB = self.session.query(UserEntity).filter_by(id=1).first()
        nameFromDB = nameFromDB.firstName

        entrysurname = self.tkUsers.lastName.get()
        surnameFromDB = self.session.query(UserEntity).filter_by(id=1).first()
        surnameFromDB = surnameFromDB.lastName

        entryusername = self.tkUsers.username.get()
        usernameFromDB = self.session.query(UserEntity).filter_by(id=1).first()
        usernameFromDB = usernameFromDB.username

        entrypassword = self.tkUsers.password.get()
        passwordFromDB = self.session.query(UserEntity).filter_by(id=1).first()
        passwordFromDB = passwordFromDB.firstName

        if entryName != nameFromDB:
            user = self.session.query(UserEntity).get(1)
            newName = self.tkUsers.firstName.get()
            entryName = newName
            user.firstName = entryName
            self.session.commit()

        if entrysurname != surnameFromDB:
            user = self.session.query(UserEntity).get(1)
            newSurname = self.tkUsers.lastName.get()
            entrysurname = newSurname
            user.lastName = entrysurname
            self.session.commit()

        if entryusername != usernameFromDB:
            user = self.session.query(UserEntity).get(1)
            newUsername = self.tkUsers.username.get()
            entryusername = newUsername
            user.username = entryusername
            self.session.commit()

        if entrypassword != passwordFromDB:
            user = self.session.query(UserEntity).get(1)
            newPassword = self.tkUsers.password.get()
            entrypassword = newPassword
            user.password = entrypassword
            self.session.commit()