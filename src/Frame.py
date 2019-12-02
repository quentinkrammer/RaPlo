#import matplotlib
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanas
import wx
from RTS_Plot import RTS_Plot
from RTS_Plot_1D import RTS_Plot_1D

class Frame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)        
        self.rtsPlot = RTS_Plot(self)
        self.doppler = RTS_Plot_1D(self, 0, 5, "_CoGDoppler")      
        
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.rtsPlot, 1, wx.EXPAND)
        self.sizer.Add(self.doppler, 0, wx.EXPAND)
        
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("info text")
        
        self.SetSizerAndFit(self.sizer)
        
    def updateScatter(self, XValue, YValue):
        self.rtsPlot.updateScatter(XValue, YValue)
        
    def updateDoppler(self, data):
        self.doppler.updateData(data)
        
        