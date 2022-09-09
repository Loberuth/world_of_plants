import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Frame
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from entity.SensorEntity import SensorEntity

class Graphs(Frame):
    def __init__(self, container, session):
        super().__init__(container)
        self.container = container
        self.session = session
        self.toggleShowGraphsWindow = False

    def placeGraphs(self, topWindow):

        self.sensorEntity = self.session.query(SensorEntity).all()
        self.sensorEntityV2 = self.session.query(SensorEntity).all()[-1]
        self.sensorHumidity = self.session.query(SensorEntity.humidity).all()
        self.sensorBrightness = self.session.query(SensorEntity.brightness).all()
        self.sensorphValue = self.session.query(SensorEntity.phValue).all()
        self.sensorSalinity = self.session.query(SensorEntity.salinity).all()
        self.sensorAirTemp = self.session.query(SensorEntity.airTemperature).all()

        if not self.toggleShowGraphsWindow:
            topWindow.geometry("1400x700")

            self.tabs = ttk.Notebook(topWindow, width=600)
            self.tabs.grid(row=0, column=1, rowspan=2, padx=30, pady=30, sticky=tk.N)

            graphOne = ttk.Frame(self.tabs)
            graphTwo = ttk.Frame(self.tabs)
            graphThree = ttk.Frame(self.tabs)

            self.tabs.add(graphOne, text="Line chart")
            self.tabs.add(graphTwo, text="Pie chart")
            self.tabs.add(graphThree, text="Histogram")

            self.createLineChartGraph(graphOne)
            self.createPieChartGraph(graphTwo)
            self.createHistogramGraph(graphThree)
            self.toggleShowGraphsWindow = True
        else:
            self.tabs.destroy()
            topWindow.geometry("800x500")
            self.toggleShowGraphsWindow = False

    def createLineChartGraph(self, frame):

        hours = []
        for e in range(len(self.sensorEntity)):
            hours.append(e + 1)

        humidityList = []
        for value in self.sensorHumidity:
            humidityList.append(int(value[0]))

        brightnessList = []
        for value in self.sensorBrightness:
            brightnessList.append(int(value[0]))

        phValueList = []
        for value in self.sensorphValue:
            phValueList.append(float(value[0]))

        salinityList = []
        for value in self.sensorSalinity:
            salinityList.append(float(value[0]))

        tempList = []
        for value in self.sensorAirTemp:
            tempList.append(int(value[0]))


        figure = Figure(figsize=(6, 6))
        figure_canvas = FigureCanvasTkAgg(figure, frame)
        NavigationToolbar2Tk(figure_canvas, frame)
        axis = figure.add_subplot()
        axis.plot(hours, humidityList, label="Humidity")
        axis.plot(hours, brightnessList, label="Brightness")
        axis.plot(hours, phValueList, label="Ph value")
        axis.plot(hours, salinityList, label="Salinity")
        axis.plot(hours, tempList, label="Air temp")
        axis.set_title("Sensors Data")
        axis.set_xlabel("Sensor values per 1 frequency")
        axis.set_ylabel("Sensor values")
        axis.legend()
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0.5)

    def createPieChartGraph(self, frame):

        y = np.array([self.sensorEntityV2.humidity, self.sensorEntityV2.warmth, self.sensorEntityV2.brightness, self.sensorEntityV2.phValue, self.sensorEntityV2.salinity, self.sensorEntityV2.airTemperature])
        labels = ["Humidity", "Warmth", "Brightness", "Ph", "Salinity", "Air temperature"]
        figure = Figure(figsize=(6, 6))
        figure_canvas = FigureCanvasTkAgg(figure, frame)
        NavigationToolbar2Tk(figure_canvas, frame)
        ax = figure.add_subplot(111)
        ax.pie(y, radius=1, labels=labels, autopct='%0.2f%%')
        chart1 = FigureCanvasTkAgg(figure, frame)
        chart1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    def createHistogramGraph(self, frame):

        height = [self.sensorEntityV2.humidity, self.sensorEntityV2.warmth, self.sensorEntityV2.brightness, self.sensorEntityV2.phValue, self.sensorEntityV2.salinity, self.sensorEntityV2.airTemperature]

        figure = Figure(figsize=(6, 6))
        canvas = FigureCanvasTkAgg(figure, frame)
        NavigationToolbar2Tk(canvas, frame)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

        p = figure.gca()
        p.hist(height, edgecolor="blue", bins=5)
        p.set_xlabel('Median Value', fontsize=10)
        p.set_ylabel('Frequency', fontsize=10)