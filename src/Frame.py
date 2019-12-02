import wx
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanas
from RTS_Plot import RTS_Plot

class Frame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)        
        self.rtsPlot = RTS_Plot(self)
        self.p2 = wx.Panel(self, style=wx.SUNKEN_BORDER)
        
        
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.rtsPlot, 1, wx.EXPAND)
        self.sizer.Add(self.p2, 0, wx.EXPAND)
        
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("info text")
        
        self.SetSizer(self.sizer)
        
    def updateScatter(self, XValue, YValue):
        self.rtsPlot.updateScatter(XValue, YValue)
        
        