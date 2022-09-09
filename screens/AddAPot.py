import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Frame
from utils.Utils import Utils
from model.TKModels.TkPots import TkPots
from model.TKModels.TkPlants import TkPlants
from entity.PlantEntity import PlantEntity
from entity.PotEntity import PotEntity
from model.TKModels.TkImages import TkImages

class AddAPot(Frame):

    def __init__(self, container, session):
        super().__init__(container)
        self.container = container
        self.session = session
        self.grid()
        self.utils = Utils()
        self.tkPots = TkPots()
        self.tkPlants = TkPlants()
        self.tkImages = TkImages()

    def createAPot(self, addPots):
        self.addPots = addPots
        lblName = ttk.Label(self.addPots, text="Pot Name:")
        lblName.grid(row=0, column=0, padx=10, pady=15, sticky=tk.W)

        entryName = ttk.Entry(self.addPots, width=40, textvariable=self.tkPots.potName)
        entryName.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(self.addPots, image=self.tkImages.bin, command=lambda btnId=1: self.utils.deleteFromEntry(btnId, self.tkPots.potName))
        btnDeleteFromEntry.grid(row=1, column=1, pady=5, sticky=tk.W)

        lblHumidity = ttk.Label(self.addPots, text="Pot status:")
        lblHumidity.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.optionList = ["Empty pot", "Put a plant"]
        emptyPot = ttk.Radiobutton(self.addPots, text=self.optionList[0], value=1, variable=self.tkPots.potStatus)
        emptyPot.grid(row=3, column=0, padx=(10, 15), pady=5, sticky=tk.W)

        plantInAPot = ttk.Radiobutton(self.addPots, text=self.optionList[1], value=2, variable=self.tkPots.potStatus)
        plantInAPot.grid(row=3, column=0, padx=(110, 10), pady=5, sticky=tk.W)

        btnSave = tk.Button(self.addPots, text="Save", font=('Arial', 10, 'bold'), bd=0, relief="flat",
                            bg="#2E9487", fg="#ffffff", command=self.chooseAnOption)
        btnSave.grid(row=4, column=0, ipadx=5, ipady=5, padx=10, pady=10, sticky=tk.W)

        message = tk.Label(self.addPots, textvariable=self.tkPots.message)
        message.grid(row=5, column=0, columnspan=5, pady=10, padx=10, sticky=tk.W)

    def createOtherOptions(self):
        self.allPlants = []
        self.plants = self.session.query(PlantEntity).all()
        for plant in self.plants:
            self.allPlants.append(plant.plant)
        tkPlantList = tk.StringVar(value=self.allPlants)
        self.listbox = tk.Listbox(self.addPots, width=20, listvariable=tkPlantList)
        self.listbox.grid(row=5, rowspan=5, column=0, columnspan=10, padx=10, pady=10, sticky=tk.W)
        self.listbox.bind("<Double-1>", self.chooseAPlant)

        self.plantNameLbl = ttk.Label(self.addPots, text="Plant name:")
        self.plantNameLbl.grid(row=5, column=0, columnspan=24, pady=10, padx=150, sticky=tk.W)

        self.plantNameEntry = ttk.Entry(self.addPots, textvariable=self.tkPots.plantName)
        self.plantNameEntry.grid(row=5, column=0, columnspan=24, padx=250, pady=10, sticky=tk.W)

        self.humidityLbl = ttk.Label(self.addPots, text="Humidity:")
        self.humidityLbl.grid(row=6, column=0, columnspan=24, pady=10, padx=150, sticky=tk.W)

        self.humidityEntry = ttk.Entry(self.addPots, textvariable=self.tkPots.humidity)
        self.humidityEntry.grid(row=6, column=0, columnspan=24, padx=250, pady=10, sticky=tk.W)

        self.brightnessLbl = ttk.Label(self.addPots, text="Brightness:")
        self.brightnessLbl.grid(row=7, column=0, columnspan=24, pady=10, padx=150, sticky=tk.W)

        self.brightnessEntry = ttk.Entry(self.addPots, textvariable=self.tkPots.brightness)
        self.brightnessEntry.grid(row=7, column=0, columnspan=24, padx=250, pady=10, sticky=tk.W)

        self.warmthLbl = ttk.Label(self.addPots, text="Warmth:")
        self.warmthLbl.grid(row=8, column=0, columnspan=24, pady=10, padx=150, sticky=tk.W)

        self.warmthEntry = ttk.Entry(self.addPots, textvariable=self.tkPots.warmth)
        self.warmthEntry.grid(row=8, column=0, columnspan=24, padx=250, pady=10, sticky=tk.W)

        self.substratesLbl = ttk.Label(self.addPots, text="Substrates:")
        self.substratesLbl.grid(row=9, column=0, columnspan=24, pady=10, padx=150, sticky=tk.W)

        self.substratesEntry = ttk.Entry(self.addPots, textvariable=self.tkPots.substrates)
        self.substratesEntry.grid(row=9, column=0, columnspan=24, padx=250, pady=10, sticky=tk.W)

        btnSaveToDB = tk.Button(self.addPots, text="Add to Pot", font=('Arial', 10, 'bold'), bd=0, relief="flat", bg="#2E9487",
                            fg="#ffffff", command=self.saveToDB)
        btnSaveToDB.grid(row=10, column=0, ipadx=5, ipady=5, padx=10, pady=10, sticky=tk.W)

    def destroyOtherOptions(self):
        self.plantNameLbl.destroy()
        self.plantNameEntry.destroy()
        self.humidityLbl.destroy()
        self.humidityEntry.destroy()
        self.brightnessLbl.destroy()
        self.brightnessEntry.destroy()
        self.warmthLbl.destroy()
        self.warmthEntry.destroy()
        self.substratesLbl.destroy()
        self.substratesEntry.destroy()
        self.listbox.destroy()

    def chooseAnOption(self):
        if self.tkPots.potStatus.get() == 2:
            self.createOtherOptions()
        if self.tkPots.potStatus.get() == 1:
            self.saveToDBEmpty()
            self.tkPots.potName.set("")
            self.tkPots.potStatus.set("0")
            self.tkPots.message.set("Succesfully added to database")
            try:
                self.destroyOtherOptions()
            except:
                return

    def chooseAPlant(self, event):
        self.choice = event.widget.curselection()
        self.index = self.choice[0]
        self.tkPots.plantName.set(self.plants[self.index].plant)
        self.tkPots.humidity.set(self.plants[self.index].humidity)
        self.tkPots.brightness.set(self.plants[self.index].brightness)
        self.tkPots.warmth.set(self.plants[self.index].warmth)
        self.tkPots.substrates.set(self.plants[self.index].substrates)

    def saveToDB(self):
        addAPot = PotEntity(potName=self.tkPots.potName.get(), plant=self.tkPots.plantName.get(), status="Plant", humidity=self.tkPots.humidity.get(), brightness=self.tkPots.brightness.get())
        self.session.add(addAPot)
        self.session.commit()

    def saveToDBEmpty(self):
        addAPot = PotEntity(potName=self.tkPots.potName.get(), plant=None, status=None, humidity=None, brightness=None)
        self.session.add(addAPot)
        self.session.commit()