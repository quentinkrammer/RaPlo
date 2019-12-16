# -*- coding: utf-8 -*-
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import wx

class RTS_Plot_1D(wx.Panel):

    def __init__(self, parent, dataMin, dataMax, label=""):
        wx.Panel.__init__(self, parent, -1, size=(180, -1))        
        self.figure = matplotlib.figure.Figure()
        self.canvas = FigureCanvas(self, -1, self.figure)        
        self.axes = self.figure.add_subplot(111)        
        self.axes.set_xlim((0, 1))
        self.axes.set_ylim((dataMin,dataMax))
        self.axes.set_xticklabels([])
        self.axes.set_xlabel(label)          

        self.marker,  = self.axes.plot([0, 1], [None, None])
        
        
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)            
              
    def updateData(self, data):            
        self.marker.set_ydata([data, data])
        self.canvas.draw()
        
         
        