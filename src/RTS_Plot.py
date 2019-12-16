# -*- coding: utf-8 -*-
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import wx
import numpy as np
from ConfigHandler import ConfigHandler
import collections


class RTS_Plot(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, size=(700, 400))
        self.config = ConfigHandler(type(self).__name__ )
        self.figure = matplotlib.figure.Figure()
        self.canvas = FigureCanvas(self, -1, self.figure)
        X_Min = int(self.config.getValue("X_Min"))
        X_Max = int(self.config.getValue("X_Max"))
        Y_Min = int(self.config.getValue("Y_Min"))
        Y_Max = int(self.config.getValue("Y_Max"))
        self.X_PriorDataPoints = collections.deque([], int(self.config.getValue("numberOfScatterPoints")))
        self.Y_PriorDataPoints = collections.deque([], int(self.config.getValue("numberOfScatterPoints"))) 
        self.axes = self.figure.add_subplot(111)        
        self.axes.set_xlim((X_Min, X_Max))
        self.axes.set_ylim((Y_Min,Y_Max))
#         self.axes.set_xlabel("_LatPos_m")   
#         self.axes.set_ylabel("_LongPos_m")
        self.axes.grid(True)
        self.axes.spines['left'].set_position('zero')
        self.axes.spines['bottom'].set_position('zero')
        radius = [9, 10, 11]
        self.circleSegments = []
        for r in radius:            
            self.circleSegments.append(matplotlib.patches.Arc((0, 0), r*2, r*2, theta1=30, theta2=150,\
                                                              linewidth=1.5, zorder=0))           
            self.axes.add_patch(self.circleSegments[-1])
        self.lines = []
        maxDistance = radius[-1]
        for i in range(30, 160, 10):
            if i % 30 == 0: 
                self.axes.plot([0, maxDistance * np.cos(np.radians(i))],\
                                       [0,  maxDistance * np.sin(np.radians(i))], "k-", zorder=1)                
            else:
                line = self.axes.plot([0, maxDistance * np.cos(np.radians(i))],\
                                       [0,  maxDistance * np.sin(np.radians(i))], "k--",\
                                       color='#C0C0C0', zorder=1)
        
        self.sc = self.axes.scatter(None,None, zorder=2)        
        self.scPriorDataPoints = self.axes.scatter(None, None)        
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)       
      
    def updateScatter(self, XData, YData):       
        self.scPriorDataPoints.set_offsets(np.c_[self.X_PriorDataPoints,self.Y_PriorDataPoints])
        self.sc.set_offsets(np.c_[XData,YData])
        self.canvas.draw()
        self.X_PriorDataPoints.append(XData)
        self.Y_PriorDataPoints.append(YData)
        
    def updateScatter2(self, offsets):        
        self.sc.set_offsets(offsets)
        self.canvas.draw()
  
        
         

        