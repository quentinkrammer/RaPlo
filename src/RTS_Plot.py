# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import time

class RTS_Plot():

    def __init__(self):
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim((0, 10))
        self.ax.set_ylim((0, 10))      
        
    def linePlot(self):        
        hl, = self.ax.plot([], [], "o")                
        for i in range(6):
            self.update_line(hl, [i, i])
            time.sleep(0.5)
        time.sleep(2)
        
    def scatterPlot(self):
        x = [None]
        y = [None] 
        sc = self.ax.scatter(x,y)        
        for i in range(6):
            self.update_scatter(sc, [i, i])            
            time.sleep(0.5)                     
        
    def update_scatter(self, sc, new_data):
        sc.set_offsets(np.c_[new_data[0],new_data[1]])
        self.fig.canvas.draw()  
        
    def update_line(self, hl, new_data):
        hl.set_xdata(new_data[0])
        hl.set_ydata(new_data[1])
        self.fig.canvas.draw()
