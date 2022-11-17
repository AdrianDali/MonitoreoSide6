import os
import pyqtgraph as pg
import threading
import sys
import time



class Graph():
    def __init__(self):
        #creating a pyqtgraph plot window
        self.window = pg.plot()

        # setting window geometry
        # left = 100, top = 100
        # width = 600, height = 500
        self.window.setGeometry(100, 100, 600, 500)
        self.window.setBackground((245, 240, 225))
        # title for the plot window
        title = "Pantalla Grafica Monitoreo"

        # setting window title to plot window
        self.window.setWindowTitle(title)

        # create list for y-axis
        y1 = [5]

        # create horizontal list i.e x-axis
        x = [1]

        # create pyqt5graph bar graph item
        # with width = 0.6
        # with bar colors = green
        self.bargraph = pg.BarGraphItem(x=x, height=y1, width=1.0, brush='#1e3d59')
        self.bargraph02 = pg.BarGraphItem(x=[3], height=y1, width=1.0, brush='#ff6e40')

        self.window.setXRange(0, 4, padding=0)
        self.window.setYRange(0, 70)

        # add item to plot window
        # adding bargraph item to the window
        self.window.addItem(self.bargraph)
        self.window.addItem(self.bargraph02)

    def show(self):
        self.window.show()

    def update_bar(self, contador):
        time.sleep(2)
        self.bargraph.setOpts(height= contador )
        print("paso hilo")
        