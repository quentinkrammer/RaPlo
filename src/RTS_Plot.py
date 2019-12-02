import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import wx
import numpy as np
import time
from ConfigHandler import ConfigHandler

class RTS_Plot(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.config = ConfigHandler(type(self).__name__ )
        self.figure = matplotlib.figure.Figure()
        X_Min = int(self.config.getValue("X_Min"))
        X_Max = int(self.config.getValue("X_Max"))
        Y_Min = int(self.config.getValue("Y_Min"))
        Y_Max = int(self.config.getValue("Y_Max"))
        self.axes = self.figure.add_subplot(111)        
        self.axes.set_xlim((X_Min, X_Max))
        self.axes.set_ylim((Y_Min,Y_Max))          

        self.sc = self.axes.scatter(0,0) 
        self.canvas = FigureCanvas(self, -1, self.figure)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)       
        #self.update("text")  
              
    def updateScatter(self, XData, YData):            
        self.sc.set_offsets(np.c_[XData,YData])
        self.canvas.draw() 
        

        
        