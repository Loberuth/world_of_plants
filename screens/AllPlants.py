from io import BytesIO
import tkinter as tk
from tkinter import ttk, Toplevel
from tkinter.ttk import Frame
from model.TKModels.TkImages import TkImages
from model.TKModels.TkPlants import TkPlants
from entity.PlantEntity import PlantEntity
from services.Services import Services
from entity.SensorEntity import SensorEntity
from PIL import Image, ImageTk
from model.TKModels.TkSensors import TkSensors

class AllPlants(Frame):
    def __init__(self, container, session):
        super().__init__(container)
        self.container = container
        self.session = session
        self.grid()
        self.toggleUpdateWindow = False
        self.tkSensors = TkSensors()
        self.tkImages = TkImages()
        self.tkPlants = TkPlants()
        self.services = Services()

    def createAPlant(self, allPlants):

        row = 0
        column = 0

        self.entityList = self.session.query(PlantEntity).all()

        self.canvas = tk.Canvas(allPlants)
        self.canvas.grid(row=0, column=9, padx=5, pady=5, sticky=tk.NE)

        self.scrollbar = ttk.Scrollbar(allPlants, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.window = tk.Frame(allPlants)

        self.canvas.create_window((0, 0), window=self.window, anchor="nw")

        for i in range(len(self.entityList)):
            img = Image.open(BytesIO(self.entityList[i].image)).resize((150, 250))
            self.tkImage = ImageTk.PhotoImage(img)

            if column <= 2:
                labelframe = ttk.LabelFrame(self.window, text=f"Plant {i + 1} - {self.entityList[i].plant}")
                labelframe.grid(row=row, column=column, padx=15, pady=10)

                lblPlantImage = ttk.Label(labelframe, image=self.tkImage)
                lblPlantImage.image = self.tkImage
                lblPlantImage.grid(row=0, column=0, rowspan=6, pady=(5, 0), sticky=tk.W)

                lblPlantName = ttk.Label(labelframe, text=self.entityList[i].plant, font=("Arial", 17, "bold"), foreground="#146D38")
                lblPlantName.grid(row=0, column=1, columnspan=2, padx=15, pady=(5, 12), sticky=tk.W)

                lblHumidity = ttk.Label(labelframe, text="Humidity: ", font=("Arial", 11, "bold"))
                lblHumidity.grid(row=1, column=1, padx=15, pady=5, sticky=tk.W)

                lblPlantHumidity = ttk.Label(labelframe, text=f"{self.entityList[i].humidity}%", font=("Arial", 10))
                lblPlantHumidity.grid(row=1, column=2, padx=20, pady=5, sticky=tk.W)

                lblBrightness = ttk.Label(labelframe, text="Brightness: ", font=("Arial", 11, "bold"))
                lblBrightness.grid(row=2, column=1, padx=15, pady=5, sticky=tk.W)

                lblPlantBrightness = ttk.Label(labelframe, text=f"{self.entityList[i].brightness} fc", font=("Arial", 10))
                lblPlantBrightness.grid(row=2, column=2, padx=20, pady=5, sticky=tk.W)

                lblWarmth = ttk.Label(labelframe, text="Soil warmth: ", font=("Arial", 11, "bold"))
                lblWarmth.grid(row=3, column=1, padx=15, pady=5, sticky=tk.W)

                lblPlantWarmth = ttk.Label(labelframe, text=f"{self.entityList[i].warmth}°C", font=("Arial", 10))
                lblPlantWarmth.grid(row=3, column=2, padx=20, pady=5, sticky=tk.W)

                lblSubstrate = ttk.Label(labelframe, text="Substrates: ", font=("Arial", 11, "bold"))
                lblSubstrate.grid(row=4, column=1, padx=15, pady=5, sticky=tk.W)

                lblPlantSubstrate = ttk.Label(labelframe, text=self.entityList[i].substrates, font=("Arial", 10))
                lblPlantSubstrate.grid(row=4, column=2, padx=20, pady=5, sticky=tk.W)

                btn = tk.Button(labelframe, text="Show a plant", font=('Arial', 10, 'bold'), bd=0, relief="flat",
                                bg="#2E9487", fg="#ffffff", command=lambda plantId=i: self.createWindow(plantId))
                btn.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=8, ipady=6, sticky=tk.E)
            else:
                column = 0
                row += 1
                labelframe = ttk.LabelFrame(self.window, text=f"Plant {i + 1} - {self.entityList[i].plant}")
                labelframe.grid(row=row, column=column, padx=15, pady=10)
                lblPlantImage = ttk.Label(labelframe, image=self.tkImage)
                lblPlantImage.image = self.tkImage
                lblPlantImage.grid(row=0, column=0, rowspan=6, pady=(5, 0), sticky=tk.W)

                lblPlantName = ttk.Label(labelframe, text=self.entityList[i].plant, font=("Arial", 17, "bold"), foreground="#146D38")
                lblPlantName.grid(row=0, column=1, columnspan=2, padx=15, pady=(5, 12), sticky=tk.W)

                lblHumidity = ttk.Label(labelframe, text="Humidity: ", font=("Arial", 11, "bold"))
                lblHumidity.grid(row=1, column=1, padx=15, pady=5, sticky=tk.W)

                lblPlantHumidity = ttk.Label(labelframe, text=f"{self.entityList[i].humidity}%", font=("Arial", 10))
                lblPlantHumidity.grid(row=1, column=2, padx=20, pady=5, sticky=tk.W)

                lblBrightness = ttk.Label(labelframe, text="Brightness: ", font=("Arial", 11, "bold"))
                lblBrightness.grid(row=2, column=1, padx=15, pady=5, sticky=tk.W)

                lblPlantBrightness = ttk.Label(labelframe, text=f"{self.entityList[i].brightness} fc", font=("Arial", 10))
                lblPlantBrightness.grid(row=2, column=2, padx=20, pady=5, sticky=tk.W)

                lblWarmth = ttk.Label(labelframe, text="Soil warmth: ", font=("Arial", 11, "bold"))
                lblWarmth.grid(row=3, column=1, padx=15, pady=5, sticky=tk.W)

                lblPlantWarmth = ttk.Label(labelframe, text=f"{self.entityList[i].warmth}°C", font=("Arial", 10))
                lblPlantWarmth.grid(row=3, column=2, padx=20, pady=5, sticky=tk.W)

                lblSubstrate = ttk.Label(labelframe, text="Substrates: ", font=("Arial", 11, "bold"))
                lblSubstrate.grid(row=4, column=1, padx=15, pady=5, sticky=tk.W)

                lblPlantSubstrate = ttk.Label(labelframe, text=self.entityList[i].substrates, font=("Arial", 10))
                lblPlantSubstrate.grid(row=4, column=2, padx=20, pady=5, sticky=tk.W)

                btn = tk.Button(labelframe, text="Show a plant", font=('Arial', 10, 'bold'), bd=0, relief="flat",
                                bg="#2E9487", fg="#ffffff", command=lambda plantId=i: self.createWindow(plantId))
                btn.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=8, ipady=6, sticky=tk.E)
            column += 1

    def createWindow(self, plantId):
        self.top = Toplevel()
        self.top.geometry("760x450")

        sensorsList = self.session.query(SensorEntity).all()[-1]

        for i in range(len(self.entityList)):
            img = Image.open(BytesIO(self.entityList[plantId].image)).resize((300, 300))
            self.tkImage = ImageTk.PhotoImage(img)

        for item in self.entityList:

            if int(sensorsList.humidity) < int(self.entityList[plantId].humidity):
                self.tkSensors.humidity = "Low (I need water!)"
            if int(sensorsList.humidity) > int(self.entityList[plantId].humidity):
                self.tkSensors.humidity = "High (I am not that thirsty!)"
            if int(sensorsList.humidity) == int(self.entityList[plantId].humidity):
                self.tkSensors.humidity = "Ideal (Good life!)"

            if int(sensorsList.brightness) < int(self.entityList[plantId].brightness):
                self.tkSensors.brightness = "Low (Give me light!)"
            if int(sensorsList.brightness) > int(self.entityList[plantId].brightness):
                self.tkSensors.brightness = "High (Hide me!)"
            if int(sensorsList.brightness) == int(self.entityList[plantId].brightness):
                self.tkSensors.brightness = "Ideal (I love sun!)"

            if int(sensorsList.warmth) < int(self.entityList[plantId].warmth):
                self.tkSensors.warmth = "Low (It's coooold!)"
            if int(sensorsList.warmth) > int(self.entityList[plantId].warmth):
                self.tkSensors.warmth = "High (Do you want me to dry?)"
            if int(sensorsList.warmth) == int(self.entityList[plantId].warmth):
                self.tkSensors.warmth = "Ideal (I love heat!)"


            self.individualPlantPanel = ttk.LabelFrame(self.top, text="Sensor Info")
            self.individualPlantPanel.grid(row=0, column=0, padx=30, pady=30, sticky=tk.W)

            imgBig = ttk.Label(self.individualPlantPanel, image=self.tkImage)
            imgBig.image = self.tkImage
            imgBig.grid(row=0, column=2, rowspan=15, padx=(40, 20), pady=(20, 30), sticky=tk.W)

            self.plantName = ttk.Label(self.individualPlantPanel, text=self.entityList[plantId].plant, font=("Arial", 21, "bold"))
            self.plantName.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky=tk.W)

            plantCare = ttk.Label(self.individualPlantPanel, text="Sensor Info", font=("Arial", 13, "bold"))
            plantCare.grid(row=1, column=0, pady=(0, 15), padx=20, sticky=tk.W)

            plantCare = ttk.Label(self.individualPlantPanel, text="Status", font=("Arial", 13, "bold"))
            plantCare.grid(row=1, column=1, pady=(0, 15), padx=20, sticky=tk.W)

            lblHumidity = ttk.Label(self.individualPlantPanel, text="Humidity:", font=("Arial", 10, "bold"))
            lblHumidity.grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)

            lblHumidityValue = ttk.Label(self.individualPlantPanel, text=self.tkSensors.humidity)
            lblHumidityValue.grid(row=2, column=1, padx=20, pady=5, sticky=tk.W)

            lblBrightness = ttk.Label(self.individualPlantPanel, text="Brightness:", font=("Arial", 10, "bold"))
            lblBrightness.grid(row=3, column=0, padx=20, pady=5, sticky=tk.W)

            lblBrightnessValue = ttk.Label(self.individualPlantPanel, text=self.tkSensors.brightness)
            lblBrightnessValue.grid(row=3, column=1, padx=20, pady=5, sticky=tk.W)

            lblWarmth = ttk.Label(self.individualPlantPanel, text="Soil warmth:", font=("Arial", 10, "bold"))
            lblWarmth.grid(row=4, column=0, padx=20, pady=5, sticky=tk.W)

            lblWarmthValue = ttk.Label(self.individualPlantPanel, text=self.tkSensors.warmth)
            lblWarmthValue.grid(row=4, column=1, padx=20, pady=5, sticky=tk.W)

            self.btnUpdate = tk.Button(self.individualPlantPanel, text="Update", font=('Arial', 11, 'bold'), bd=0,
                                       relief="flat", bg="#2E9487", fg="#ffffff", command=lambda plantID=plantId: self.updateWindow(plantID))
            self.btnUpdate.grid(row=5, column=0, pady=(40, 20), padx=20, ipady=5, ipadx=11, sticky=tk.W)

            self.btnDelete = tk.Button(self.individualPlantPanel, text="Delete", font=('Arial', 11, 'bold'), bd=0,
                                       relief="flat", bg="#2E9487", fg="#ffffff", command=lambda plantID=plantId: self.deleteFromDB(plantID))
            self.btnDelete.grid(row=5, column=1, pady=(40, 20), padx=20, ipady=5, ipadx=11, sticky=tk.W)

    def destroyTopWindow(self):
        try:
            self.top.destroy()
        except:
            return

    def updateWindow(self, plantId):

        if not self.toggleUpdateWindow:

            self.top.geometry("760x700")

            self.updateFrame = ttk.LabelFrame(self.top, text="Update plant")
            self.updateFrame.grid(row=1, column=0, padx=30, pady=15, sticky=tk.W)

            nameLbl = ttk.Label(self.updateFrame, text="Plant name:")
            nameLbl.grid(row=0, column=0, padx=8, pady=(10, 5), sticky=tk.W)

            plantEntry = ttk.Entry(self.updateFrame, textvariable=self.tkPlants.plantName, width=30)
            plantEntry.grid(row=1, column=0, padx=8, pady=5)

            humidityLbl = ttk.Label(self.updateFrame, text="Humidity:")
            humidityLbl.grid(row=0, column=1, padx=8, pady=(10, 5), sticky=tk.W)

            humidityEntry = ttk.Entry(self.updateFrame, textvariable=self.tkPlants.humidity, width=30)
            humidityEntry.grid(row=1, column=1, padx=8, pady=5)

            brightnessLbl = ttk.Label(self.updateFrame, text="Brightness:")
            brightnessLbl.grid(row=0, column=2, padx=8, pady=(10, 5), sticky=tk.W)

            brightnessEntry = ttk.Entry(self.updateFrame, textvariable=self.tkPlants.brightness, width=30)
            brightnessEntry.grid(row=1, column=2, padx=8, pady=5)

            warmthLbl = ttk.Label(self.updateFrame, text="Soil warmth:")
            warmthLbl.grid(row=2, column=0, padx=8, pady=(10, 5), sticky=tk.W)

            warmthEntry = ttk.Entry(self.updateFrame, textvariable=self.tkPlants.warmth, width=30)
            warmthEntry.grid(row=3, column=0, padx=8, pady=5)

            substratesLbl = ttk.Label(self.updateFrame, text="Substrates:")
            substratesLbl.grid(row=2, column=1, padx=8, pady=(10, 5), sticky=tk.W)

            substratesEntry = ttk.Entry(self.updateFrame, textvariable=self.tkPlants.substrates, width=30)
            substratesEntry.grid(row=3, column=1, padx=8, pady=5)

            updateBtn = tk.Button(self.updateFrame, text="Update", font=('Arial', 11, 'bold'), bd=0, relief="flat", bg="#2E9487", fg="#ffffff", command=lambda id=plantId: self.updateInDB(plantId))
            updateBtn.grid(row=3, column=2, padx=8, pady=(15, 5), sticky=tk.EW)

            self.toggleUpdateWindow = True

        else:
            self.updateFrame.destroy()
            self.top.geometry("760x450")
            self.toggleUpdateWindow = False
        self.getUserInfoFromDB(plantId)

    def getUserInfoFromDB(self, plantId):
        self.entityList = self.session.query(PlantEntity).all()
        for i in self.entityList:
            self.tkPlants.plantName.set(self.entityList[plantId].plant)
            self.tkPlants.humidity.set(self.entityList[plantId].humidity)
            self.tkPlants.brightness.set(self.entityList[plantId].brightness)
            self.tkPlants.warmth.set(self.entityList[plantId].warmth)
            self.tkPlants.substrates.set(self.entityList[plantId].substrates)

    def updateInDB(self, plantId):
        entryPlantName = self.tkPlants.plantName.get()
        plantNameFromDB = self.session.query(PlantEntity).filter_by(id=plantId + 1).first()
        plantNameFromDB = plantNameFromDB.plant

        entryHumidity = self.tkPlants.humidity.get()
        humidityFromDB = self.session.query(PlantEntity).filter_by(id=plantId + 1).first()
        humidityFromDB = humidityFromDB.humidity

        entryBrightness = self.tkPlants.brightness.get()
        brightnessFromDB = self.session.query(PlantEntity).filter_by(id=plantId + 1).first()
        brightnessFromDB = brightnessFromDB.brightness

        entryWarmth = self.tkPlants.warmth.get()
        warmthFromDB = self.session.query(PlantEntity).filter_by(id=plantId + 1).first()
        warmthFromDB = warmthFromDB.warmth

        entrySubstrates = self.tkPlants.substrates.get()
        substratesFromDB = self.session.query(PlantEntity).filter_by(id=plantId + 1).first()
        substratesFromDB = substratesFromDB.substrates

        if entryPlantName != plantNameFromDB:
            plantName = self.session.query(PlantEntity).get(plantId + 1)
            newPlantName = self.tkPlants.plantName.get()
            entryPlantName = newPlantName
            plantName.plant = entryPlantName
            self.session.commit()

        if entryHumidity != humidityFromDB:
            humidity = self.session.query(PlantEntity).get(plantId + 1)
            newHumidity = self.tkPlants.humidity.get()
            entryHumidity = newHumidity
            humidity.humidity = entryHumidity
            self.session.commit()

        if entryBrightness != brightnessFromDB:
            brightness = self.session.query(PlantEntity).get(plantId + 1)
            newbrightness = self.tkPlants.brightness.get()
            entryBrightness = newbrightness
            brightness.brightness = entryBrightness
            self.session.commit()

        if entryWarmth != warmthFromDB:
            warmth = self.session.query(PlantEntity).get(plantId + 1)
            newWarmth = self.tkPlants.warmth.get()
            entryWarmth = newWarmth
            warmth.warmth = entryWarmth
            self.session.commit()

        if entrySubstrates != substratesFromDB:
            substrates = self.session.query(PlantEntity).get(plantId + 1)
            newSubstrates= self.tkPlants.substrates.get()
            entrySubstrates = newSubstrates
            substrates.substrates = entrySubstrates
            self.session.commit()

    def deleteFromDB(self, plantId):
        self.services.deleteFromDB(plantId + 1, "plants")
        self.session.commit()

    def reset_scrollregion(self):
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.bbox())

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * int(event.delta / 50), "units")