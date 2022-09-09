import tkinter as tk

class TkPots:

    def __init__(self):

        self.potName = tk.StringVar()
        self.potStatus = tk.IntVar()
        self.plantName = tk.StringVar()
        self.humidity = tk.StringVar()
        self.brightness = tk.StringVar()
        self.warmth = tk.StringVar()
        self.substrates = tk.StringVar()
        self.phValue = tk.StringVar()
        self.salinity = tk.StringVar()
        self.airTemperature = tk.StringVar()
        self.message = tk.StringVar()
        self.comboBoxChoice = tk.StringVar()