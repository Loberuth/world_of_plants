import tkinter as tk
from tkinter import ttk, Toplevel
from tkinter.ttk import Frame
from model.TKModels.TkImages import TkImages
from model.TKModels.TkPlants import TkPlants
from model.TKModels.TkPots import TkPots
from entity.PlantEntity import PlantEntity
from entity.PotEntity import PotEntity
from entity.SensorEntity import SensorEntity
from screens.Graphs import Graphs
from services.Services import Services

class AllPots(Frame):
    def __init__(self, container, session):
        super().__init__(container)
        self.container = container
        self.session = session
        self.grid()
        self.toggleUpdateWindow = False
        self.tkImages = TkImages()
        self.tkPlants = TkPlants()
        self.tkPots = TkPots()
        self.services = Services()
        self.tkGraphs = Graphs(self.container, self.session)

    def createPotContainer(self, tabAllPots):
        self.entityList = self.session.query(PotEntity).all()

        row = 0
        column = 0

        for i in range(len(self.entityList)):
            if column <= 2:
                lblFrame = ttk.LabelFrame(tabAllPots, text=f"Pot in the {self.entityList[i].potName.lower()}")
                lblFrame.grid(row=row, column=column, padx=15, pady=10)

                image = ttk.Label(lblFrame, image=self.tkImages.potBkg)
                image.grid(row=0, column=0, rowspan=6, pady=(5, 0), sticky=tk.W)

                flowerName = ttk.Label(lblFrame, text=self.entityList[i].potName, font=("Arial", 15, "bold"), foreground="#146D38")
                flowerName.grid(row=0, column=1, columnspan=2, padx=15, pady=(5, 12), sticky=tk.W)

                status = ttk.Label(lblFrame, text="Status: ", font=("Arial", 12, "bold"))
                status.grid(row=1, column=1, padx=15, pady=10, sticky=tk.W)

                status1 = ttk.Label(lblFrame, text=self.tkPots.potStatus, font=("Arial", 11, "bold"), foreground="#D4393C")
                status1.grid(row=2, column=1, padx=15, pady=15, sticky=tk.W)

                self.statusImg = ttk.Label(lblFrame, image=self.tkImages.emptyPot)
                self.statusImg.grid(row=2, column=2, pady=15)

                btn = tk.Button(lblFrame, text="Show a pot", font=('Arial', 10, 'bold'), bd=0, relief="flat", bg="#2E9487", fg="#ffffff", command=lambda potId=i: self.createWindow(potId))
                btn.grid(row=3, column=1, columnspan=2, padx=10, pady=(40, 10), ipadx=8, ipady=6, sticky=tk.E)
            else:
                column = 0
                row += 1
                lblFrame = ttk.LabelFrame(tabAllPots, text=f"Pot in the {self.entityList[i].potName.lower()}")
                lblFrame.grid(row=row, column=column, padx=15, pady=10)

                image = ttk.Label(lblFrame, image=self.tkImages.potBkg)
                image.grid(row=0, column=0, rowspan=6, pady=(5, 0), sticky=tk.W)

                flowerName = ttk.Label(lblFrame, text=self.entityList[i].potName, font=("Arial", 15, "bold"),
                                       foreground="#146D38")
                flowerName.grid(row=0, column=1, columnspan=2, padx=15, pady=(5, 12), sticky=tk.W)

                status = ttk.Label(lblFrame, text="Status: ", font=("Arial", 12, "bold"))
                status.grid(row=1, column=1, padx=15, pady=10, sticky=tk.W)

                status1 = ttk.Label(lblFrame, text=self.tkPots.potStatus, font=("Arial", 11, "bold"),
                                    foreground="#D4393C")
                status1.grid(row=2, column=1, padx=15, pady=15, sticky=tk.W)

                self.statusImg = ttk.Label(lblFrame, image=self.tkImages.emptyPot)
                self.statusImg.grid(row=2, column=2, pady=15)

                btn = tk.Button(lblFrame, text="Show a pot", font=('Arial', 10, 'bold'), bd=0, relief="flat",
                                bg="#2E9487", fg="#ffffff", command=lambda potId=i: self.createWindow(potId))
                btn.grid(row=3, column=1, columnspan=2, padx=10, pady=(40, 10), ipadx=8, ipady=6, sticky=tk.E)
            column += 1

    def createWindow(self, potId):
        self.top = Toplevel()
        self.top.geometry("800x500")
        self.potStatus(potId)

        self.individualPotPanel = ttk.LabelFrame(self.top, text="Pot Info")
        self.individualPotPanel.grid(row=0, column=0, padx=30, pady=30, sticky=tk.N)

        self.potName = ttk.Label(self.individualPotPanel, text=self.tkPots.potName, font=("Arial", 21, "bold"))
        self.potName.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky=tk.W)

        potCare = ttk.Label(self.individualPotPanel, text=self.tkPots.plantName, font=("Arial", 13, "bold"))
        potCare.grid(row=1, column=0, pady=(0, 15), padx=20, sticky=tk.W)

        lblHumidity = ttk.Label(self.individualPotPanel, text="Soil humidity:", font=("Arial", 10, "bold"))
        lblHumidity.grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)

        lblHumidityValue = ttk.Label(self.individualPotPanel, text=self.tkPots.humidity)
        lblHumidityValue.grid(row=2, column=1, padx=20, pady=5, sticky=tk.W)

        lblBrightness = ttk.Label(self.individualPotPanel, text="Brightness:", font=("Arial", 10, "bold"))
        lblBrightness.grid(row=3, column=0, padx=20, pady=5, sticky=tk.W)

        lblBrightnessValue = ttk.Label(self.individualPotPanel, text=self.tkPots.brightness)
        lblBrightnessValue.grid(row=3, column=1, padx=20, pady=5, sticky=tk.W)

        lblPHAndSalinity = ttk.Label(self.individualPotPanel, text="Ph and Salinity:", font=("Arial", 10, "bold"))
        lblPHAndSalinity.grid(row=4, column=0, padx=20, pady=5, sticky=tk.W)

        lblPHAndSalinityValue = ttk.Label(self.individualPotPanel, text=self.tkPots.phValue)
        lblPHAndSalinityValue.grid(row=4, column=1, padx=20, pady=5, sticky=tk.W)

        lblAirTemperature = ttk.Label(self.individualPotPanel, text="Air temperature:",
                                      font=("Arial", 10, "bold"))
        lblAirTemperature.grid(row=5, column=0, padx=20, pady=5, sticky=tk.W)

        lblAirTemperatureValue = ttk.Label(self.individualPotPanel, text=self.tkPots.airTemperature)
        lblAirTemperatureValue.grid(row=5, column=1, padx=20, pady=5, sticky=tk.W)

        self.btnDelete = tk.Button(self.individualPotPanel, text="Delete", font=('Arial', 11, 'bold'), bd=0,
                                   relief="flat", bg="#2E9487",
                                   fg="#ffffff", command=lambda potId=potId: self.deleteAPot(potId))
        self.btnDelete.grid(row=6, column=0, pady=(40, 0), padx=20, ipady=5, ipadx=11, sticky=tk.W)

        self.btnShowGraph = tk.Button(self.individualPotPanel, text="Show graph", font=('Arial', 11, 'bold'), bd=0,
                                   relief="flat", bg="#2E9487",
                                   fg="#ffffff", command=self.showGraphs)
        self.btnShowGraph.grid(row=7, column=0, columnspan=3, pady=20, padx=20, ipady=5, ipadx=11, sticky=tk.EW)

        self.imgBig = ttk.Label(self.individualPotPanel, image=self.tkImages.potBkgBig)
        self.imgBig.grid(row=0, column=3, rowspan=15, padx=(40, 20), pady=20, sticky=tk.W)

        self.disableButtonsIfEmptyPot(potId)

    def potStatus(self, potId):
        self.pot = self.session.query(PotEntity).all()
        self.sensorsList = self.session.query(SensorEntity).all()[-1]

        for i in range(len(self.pot)):

            if self.pot[potId].status is None:
                self.tkPots.plantName = "Empty pot"
                self.tkPots.potName = self.pot[potId].potName
                self.tkPots.humidity = "N/A"
                self.tkPots.brightness = "N/A"
                self.tkPots.phValue = "N/A"
                self.tkPots.salinity = "N/A"
                self.tkPots.airTemperature = "N/A"
            else:
                self.tkPots.plantName = self.pot[potId].plant
                self.tkPots.potName = self.pot[potId].potName
                self.tkPots.humidity = self.pot[potId].humidity
                self.tkPots.brightness = self.pot[potId].brightness
                self.tkPots.phValue = self.sensorsList.phValue
                self.tkPots.salinity = self.sensorsList.salinity
                self.tkPots.airTemperature = self.sensorsList.airTemperature

    def disableButtonsIfEmptyPot(self, potId):
        for i in range(len(self.pot)):
            if self.pot[potId].status is None:
                self.btnShowGraph.configure(state="disabled")
                self.statusImg.configure(image=self.tkImages.emptyPot)
                self.tkPots.potStatus = "Empty pot"
            if self.pot[potId].status == "Plant":
                self.btnShowGraph.configure(state="normal")
                self.statusImg.configure(image=self.tkImages.fullPot)
                self.tkPots.potStatus = "Plant"

    def showGraphs(self):
        self.tkGraphs.placeGraphs(self.top)

    def deleteAPot(self, potId):
        self.services.deleteFromDB(potId + 1, "pots")
        self.session.commit()

    def destroyTopWindow(self):
        try:
            self.top.destroy()
        except:
            return