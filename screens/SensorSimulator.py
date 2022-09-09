import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Frame
from model.TKModels.TkSensors import TkSensors
from utils.Utils import Utils
from entity.SensorEntity import SensorEntity
from model.TKModels.TkImages import TkImages

class SensorSimulator(Frame):

    def __init__(self, container, session):
        super().__init__(container)
        self.container = container
        self.session = session
        self.grid()
        self.tkSensors = TkSensors()
        self.utils = Utils()
        self.tkImages = TkImages()

    def createSensorSimulator(self, sensorSimulator):

        humidityLbl = ttk.Label(sensorSimulator, text="Humidity:")
        humidityLbl.grid(row=0, column=0, padx=10, pady=15, sticky=tk.W)


        humidityEntry = ttk.Entry(sensorSimulator, width=30, textvariable=self.tkSensors.humidity)
        humidityEntry.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(sensorSimulator, image=self.tkImages.bin, command=lambda btnId=1: self.utils.deleteFromEntry(btnId, self.tkSensors.humidity))
        btnDeleteFromEntry.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)

        brightnessLbl = ttk.Label(sensorSimulator, text="Brightness:")
        brightnessLbl.grid(row=2, column=0, padx=10, pady=15, sticky=tk.W)


        brightnessEntry = ttk.Entry(sensorSimulator, width=30, textvariable=self.tkSensors.brightness)
        brightnessEntry.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(sensorSimulator, image=self.tkImages.bin, command=lambda btnId=2: self.utils.deleteFromEntry(btnId, self.tkSensors.brightness))
        btnDeleteFromEntry.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

        warmthLbl = ttk.Label(sensorSimulator, text="Warmth:")
        warmthLbl.grid(row=4, column=0, padx=10, pady=15, sticky=tk.W)


        warmthEntry = ttk.Entry(sensorSimulator, width=30, textvariable=self.tkSensors.warmth)
        warmthEntry.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(sensorSimulator, image=self.tkImages.bin, command=lambda btnId=3: self.utils.deleteFromEntry(btnId, self.tkSensors.warmth))
        btnDeleteFromEntry.grid(row=5, column=1, pady=5, padx=5, sticky=tk.W)

        phLbl = ttk.Label(sensorSimulator, text="Ph value:")
        phLbl.grid(row=6, column=0, padx=10, pady=15, sticky=tk.W)


        phEntry = ttk.Entry(sensorSimulator, width=30, textvariable=self.tkSensors.phValue)
        phEntry.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(sensorSimulator, image=self.tkImages.bin, command=lambda btnId=4: self.utils.deleteFromEntry(btnId, self.tkSensors.phValue))
        btnDeleteFromEntry.grid(row=7, column=1, pady=5, padx=5, sticky=tk.W)

        salinityLbl = ttk.Label(sensorSimulator, text="Salinity:")
        salinityLbl.grid(row=8, column=0, padx=10, pady=15, sticky=tk.W)


        salinityEntry = ttk.Entry(sensorSimulator, width=30, textvariable=self.tkSensors.salinity)
        salinityEntry.grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(sensorSimulator, image=self.tkImages.bin, command=lambda btnId=5: self.utils.deleteFromEntry(btnId, self.tkSensors.salinity))
        btnDeleteFromEntry.grid(row=9, column=1, pady=5, padx=5, sticky=tk.W)

        airTemperatureLbl = ttk.Label(sensorSimulator, text="Air temperature::")
        airTemperatureLbl.grid(row=10, column=0, padx=10, pady=15, sticky=tk.W)


        airTemperatureEntry = ttk.Entry(sensorSimulator, width=30, textvariable=self.tkSensors.airTemperature)
        airTemperatureEntry.grid(row=11, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(sensorSimulator, image=self.tkImages.bin, command=lambda btnId=6: self.utils.deleteFromEntry(btnId, self.tkSensors.airTemperature))
        btnDeleteFromEntry.grid(row=11, column=1, pady=5, padx=5, sticky=tk.W)

        btnSendData = tk.Button(sensorSimulator, text="Send data", font=('Arial', 11, 'bold'), bd=0, relief="flat", bg="#2E9487", fg="#ffffff", command=self.addToDB)
        btnSendData.grid(row=12, column=0, columnspan=2, pady=(15, 0), padx=10, sticky=tk.EW)

        errorMessage = ttk.Label(sensorSimulator, textvariable=self.tkSensors.errorMsg)
        errorMessage.grid(row=13, column=0, columnspan=10, padx=10, pady=5, sticky=tk.W)

    def addToDB(self):
        humidity = self.tkSensors.humidity.get()
        brightness = self.tkSensors.brightness.get()
        warmth = self.tkSensors.warmth.get()
        phValue = self.tkSensors.phValue.get()
        salinity = self.tkSensors.salinity.get()
        airTemperature = self.tkSensors.airTemperature.get()

        if humidity == "" and brightness == "" and warmth == "" and phValue == "" and salinity == "" and airTemperature == "":
            self.tkSensors.errorMsg.set("All fields are empty, nothing was added!")
        elif humidity == "" or brightness == "" or warmth == "" or phValue == "" or salinity == "" or airTemperature == "":
            self.tkSensors.errorMsg.set("Please check your inputs, all fields should be filled out!")
        else:
            sensors = SensorEntity(humidity=humidity, brightness=int(brightness), warmth=int(warmth), phValue=float(phValue), salinity=float(salinity), airTemperature=int(airTemperature))
            self.session.add(sensors)
            self.session.commit()
            self.tkSensors.errorMsg.set("Successfully added to database!")
            self.tkSensors.humidity.set("")
            self.tkSensors.brightness.set("")
            self.tkSensors.warmth.set("")
            self.tkSensors.phValue.set("")
            self.tkSensors.salinity.set("")
            self.tkSensors.airTemperature.set("")