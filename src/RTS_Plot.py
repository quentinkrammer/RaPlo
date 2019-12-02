import matplotlib
#from matplotlib.figure import Figure
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
        self.axes.set_xlabel("_LatPos_m")   
        self.axes.set_xlabel("_LongPos_m")        

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
        
         
        

# r = RingBuffer(capacity=4, dtype=np.bool)
# r.append(True)
# r.appendleft(False)
# print(np.array(r))  # array([False, True])
deque = collections.deque([], 3)
deque.append(1)
deque.append(2)
deque.append(3)
deque.append(4)
print(repr(deque))
data = np.c_[deque,deque]
print(repr(data))
        