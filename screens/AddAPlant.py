import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.ttk import Frame
from model.TKModels.TkPlants import TkPlants
from entity.PlantEntity import PlantEntity
from PIL import Image, ImageTk
from utils.Utils import Utils
from model.TKModels.TkImages import TkImages

class AddAPlant(Frame):
    def __init__(self, container, session):
        super().__init__(container)
        self.container = container
        self.session = session
        self.grid()
        self.lblImage = None
        self.utils = Utils()
        self.tkPlants = TkPlants()
        self.tkImages = TkImages()

    def createAddAPlantPage(self, addPlants):
        lblName = ttk.Label(addPlants, text="Plant Name:")
        lblName.grid(row=0, column=0, padx=10, pady=15, sticky=tk.W)

        entryName = ttk.Entry(addPlants, width=40, textvariable=self.tkPlants.plantName)
        entryName.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(addPlants, image=self.tkImages.bin, command=lambda btnId=1: self.utils.deleteFromEntry(btnId, self.tkPlants.plantName))
        btnDeleteFromEntry.grid(row=1, column=1, pady=5, sticky=tk.W)

        lblHumidity = ttk.Label(addPlants, text="Humidity:")
        lblHumidity.grid(row=2, column=0, padx=10, pady=15, sticky=tk.W)

        entryHumidity = ttk.Entry(addPlants, width=40, textvariable=self.tkPlants.humidity)
        entryHumidity.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(addPlants, image=self.tkImages.bin, command=lambda btnId=2: self.utils.deleteFromEntry(btnId, self.tkPlants.humidity))
        btnDeleteFromEntry.grid(row=3, column=1, pady=5, sticky=tk.W)

        lblBrightness = ttk.Label(addPlants, text="Brightness:")
        lblBrightness.grid(row=4, column=0, padx=10, pady=15, sticky=tk.W)

        entryBrightness = ttk.Entry(addPlants, width=40, textvariable=self.tkPlants.brightness)
        entryBrightness.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(addPlants, image=self.tkImages.bin, command=lambda btnId=3: self.utils.deleteFromEntry(btnId, self.tkPlants.brightness))
        btnDeleteFromEntry.grid(row=5, column=1, pady=5, sticky=tk.W)

        lblWarmth = ttk.Label(addPlants, text="Warmth:")
        lblWarmth.grid(row=6, column=0, padx=10, pady=15, sticky=tk.W)

        entryWarmth = ttk.Entry(addPlants, width=40, textvariable=self.tkPlants.warmth)
        entryWarmth.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(addPlants, image=self.tkImages.bin, command=lambda btnId=4: self.utils.deleteFromEntry(btnId, self.tkPlants.warmth))
        btnDeleteFromEntry.grid(row=7, column=1, pady=5, sticky=tk.W)

        lblSubstrates = ttk.Label(addPlants, text="Substrates:")
        lblSubstrates.grid(row=8, column=0, padx=10, pady=15, sticky=tk.W)

        entrySubstrates = ttk.Entry(addPlants, width=40, textvariable=self.tkPlants.substrates)
        entrySubstrates.grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)
        btnDeleteFromEntry = ttk.Button(addPlants, image=self.tkImages.bin, command=lambda btnId=5: self.utils.deleteFromEntry(btnId, self.tkPlants.substrates))
        btnDeleteFromEntry.grid(row=9, column=1, pady=5, sticky=tk.W)

        errorMessage = ttk.Label(addPlants, textvariable=self.tkPlants.errorMsg)
        errorMessage.grid(row=10, column=0, columnspan=4, padx=10, pady=5, sticky=tk.W)

        btnAddToDB = ttk.Button(addPlants, text="Upload Image", command=lambda: self.uploadImage(addPlants))
        btnAddToDB.grid(row=0, column=2, pady=10, padx=(30, 10), sticky=tk.W)

        btnReset = ttk.Button(addPlants, text="Remove Image", command=self.removeImage)
        btnReset.grid(row=0, column=3, pady=10, padx=10, sticky=tk.W)

        btnSave = ttk.Button(addPlants, text="Save", command=self.addToDB)
        btnSave.grid(row=0, column=4, pady=10, padx=10, sticky=tk.W)

    def uploadImage(self, addPlants):
        self.file = filedialog.askopenfilename(parent=self, title="Choose an image...")
        self.originalImage = Image.open(self.file).resize((150, 250))
        self.tkImage = ImageTk.PhotoImage(self.originalImage)
        self.createLabelImage(self.tkImage, addPlants)

    def createLabelImage(self, tkImage, addPlants):
        self.lblImage = ttk.Label(addPlants, image=tkImage)
        self.lblImage.image = tkImage
        self.lblImage.grid(row=1, rowspan=10, column=2, columnspan=20, pady=10, padx=80, sticky=tk.W)

    def removeImage(self):
        if self.lblImage is not None:
            self.lblImage.destroy()
            #self.lblImage.image.set("")

    def convertToBinaryData(self, image):
        with open(image, 'rb') as file:
            blobData = file.read()
        return blobData

    def addToDB(self):
        plantName = self.tkPlants.plantName.get()
        image = self.convertToBinaryData(self.file)
        humidity = self.tkPlants.humidity.get()
        brightness = self.tkPlants.brightness.get()
        warmth = self.tkPlants.warmth.get()
        substrates = self.tkPlants.substrates.get()

        if plantName == "" and humidity == "" and brightness == "" and warmth == "" and substrates == "": # da se nista ne ispise u DB ako su sva polja prazna
            self.tkPlants.errorMsg.set("All fields are empty, nothing was added!")
            return
        elif plantName == "" or humidity == "" or brightness == "" or warmth == "" or substrates == "":
            self.tkPlants.errorMsg.set("Please check your inputs, all fields should be filled out!")
            return
        else:
            plant = PlantEntity(plant=plantName, image=image, humidity=humidity, brightness=brightness, warmth=warmth, substrates=substrates)
            self.session.add(plant)
            self.session.commit()
            self.tkPlants.errorMsg.set("Successfully added to database!")
            self.removeImage()
            self.tkPlants.plantName.set("")
            self.tkPlants.humidity.set("")
            self.tkPlants.brightness.set("")
            self.tkPlants.warmth.set("")
            self.tkPlants.substrates.set("")