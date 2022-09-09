import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Frame
from model.TKModels.TkImages import TkImages
import screens.LoginPage
from model.TKModels.TkUsers import TkUsers
from model.TKModels.TkPlants import TkPlants
from screens.AllPlants import AllPlants
from screens.AllPots import AllPots
from screens.MyProfile import MyProfile
from screens.AddAPlant import AddAPlant
from screens.AddAPot import AddAPot
from screens.SensorSimulator import SensorSimulator

class MainPageContent(Frame):
    def __init__(self, container, session):
        super().__init__(container)
        self.container = container
        self.session = session
        self.grid()
        self.tkImages = TkImages()
        self.tkUsers = TkUsers()
        self.tkPlants = TkPlants()
        self.login = screens.LoginPage
        self.allPlants = AllPlants(self.container, self.session)
        self.allPots = AllPots(self.container, self.session)
        self.addAPot = AddAPot(self.container, self.session)
        self.myProfile = MyProfile(self.container, self.session)
        self.addAPlant = AddAPlant(self.container, self.session)
        self.sensorSimulator = SensorSimulator(self.container, self.session)

    def createHeader(self):

        self.header = ttk.Label(self, image=self.tkImages.headerBkg)
        self.header.grid(row=0, column=0, sticky=tk.N)

        self.logoImg = ttk.Label(self, image=self.tkImages.logo)
        self.logoImg.grid(row=0, column=0, padx=150, sticky=tk.W)

        self.btnLogout = tk.Button(self, text="Logout", font=('Arial', 12, 'bold'), bd=0, relief="flat",
                                      bg="#2E9487", fg="#ffffff", command=self.deleteOnLogout)
        self.btnLogout.grid(row=0, column=0, padx=(0, 150), ipady=5, ipadx=16, sticky=tk.E)

        self.btnSync = tk.Button(self, text="Sync data", font=('Arial', 12, 'bold'), bd=0, relief="flat", bg="#2E9487",
                                 fg="#ffffff", command=self.sync)
        self.btnSync.grid(row=1, column=0, padx=150, pady=(20, 0), ipady=5, ipadx=16, sticky=tk.E)

    def destroyHeader(self):
        self.header.destroy()
        self.btnLogout.destroy()
        self.logoImg.config(image="")

    def createMainContentPage(self):
        self.createHeader()
        self.createTabs()

    def createTabs(self):
        self.tabs = ttk.Notebook(self, width=1200)
        self.tabs.grid(row=2, column=0, sticky=tk.N)

        self.tabAllPots = ttk.Frame(self.tabs)
        self.tabAllPlants = ttk.Frame(self.tabs)
        self.addPots = ttk.Frame(self.tabs)
        self.addPlants = ttk.Frame(self.tabs)
        self.simulator = ttk.Frame(self.tabs)
        self.myProfileTab = ttk.Frame(self.tabs)

        self.tabs.add(self.tabAllPots, text="List all pots")
        self.tabs.add(self.tabAllPlants, text="List all plants")
        self.tabs.add(self.addPots, text="Add a pot")
        self.tabs.add(self.addPlants, text="Add a plant")
        self.tabs.add(self.simulator, text="Sensor simulation")
        self.tabs.add(self.myProfileTab, text="My profile")

        self.allPots.createPotContainer(self.tabAllPots)
        self.allPlants.createAPlant(self.tabAllPlants)
        self.addAPot.createAPot(self.addPots)
        self.addAPlant.createAddAPlantPage(self.addPlants)
        self.myProfile.createMyProfilePage(self.myProfileTab)
        self.sensorSimulator.createSensorSimulator(self.simulator)

    def destroyTabs(self):
        self.tabs.destroy()

    def destroySync(self):
        self.btnSync.destroy()

    def sync(self):
        self.destroyTabs()
        self.createTabs()

    def deleteOnLogout(self):
        self.login.LoginPage.loginPage(self.container)
        self.destroyHeader()
        self.destroyTabs()
        self.destroySync()
        self.allPots.destroyTopWindow()
        self.allPlants.destroyTopWindow()