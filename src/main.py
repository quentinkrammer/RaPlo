from Frame import Frame
import wx
import threading
from DGMSegmentParser import DGMSegmentParser
from DataSmoother import DataSmoother
from ConfigHandler import ConfigHandler
import numpy as np
import math as m

def floatValues(*strValues):
    floatValues = []
    for x in strValues:
        floatValues.append(float(x))
    return floatValues

def update():
    parser = DGMSegmentParser()
    #phi = -np.pi/4
    phi = np.radians(-45)
    rotMat = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])  
    while True:
        jdl, hd = parser.deparseNextSegment()
        
        xData = floatValues(*jdl["_LatPos_m"])
        yData = floatValues(*jdl["_LongPos_m"])
        dataPoints = np.array([xData, yData])        
        rotDataPoints = rotMat.dot(dataPoints)        
        scatterCoordinates = np.transpose(rotDataPoints)     
        frame.rtsPlot.updateScatter2(scatterCoordinates)     

parser = DGMSegmentParser() 
config = ConfigHandler("DEFAULT")
sensor = config.getValue("sensor")

app = wx.App(redirect=False)
frame = Frame(None, "RaPlo")
frame.Show()
 
thread = threading.Thread(target=update, args=(), daemon=True)
thread.start()
 
app.MainLoop()


