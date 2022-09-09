import tkinter as tk

class TkSensors:

    def __init__(self):

        self.humidity = tk.StringVar()
        self.brightness = tk.StringVar()
        self.warmth = tk.StringVar()
        self.phValue = tk.StringVar()
        self.salinity = tk.StringVar()
        self.airTemperature = tk.StringVar()
        self.errorMsg = tk.StringVar()