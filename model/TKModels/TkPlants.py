import tkinter as tk

class TkPlants:

    def __init__(self):

        self.plantName = tk.StringVar()
        self.image = tk.StringVar()
        self.humidity = tk.StringVar()
        self.brightness = tk.StringVar()
        self.warmth = tk.StringVar()
        self.substrates = tk.StringVar()
        self.errorMsg = tk.StringVar()