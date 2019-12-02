from Frame import Frame
import wx
import numpy as np
from RTS_Plot import RTS_Plot
import threading
import time
import collections
import statistics
from DGMSegmentParser import DGMSegmentParser

def update():
    parser = DGMSegmentParser()
    initLast5Values = [99, 0, 99, 0, 99]
    lastFiveXValues = collections.deque(initLast5Values, 5)
    lastFiveYValues = collections.deque(initLast5Values, 5)
    
    while True:
        jdl, hd = parser.deparseNextSegment()
        if not jdl:
            break
          
        XData = []#DataJDL.LatPos_m(SelectedSensor); %LatPos_m where logical array == 1
        YData = []#DataJDL.LongPos_m(SelectedSensor);
#         CData = []#DataJDL.Power_dB(SelectedSensor);
#         CData2 = []#DataJDL.CoG_Doppler(SelectedSensor);    
          
        for index, sensor in enumerate(jdl["_NSensor"]):
            if sensor == "2":
                XData.append(float(jdl["_LatPos_m"][index]))
                YData.append(float(jdl["_LongPos_m"][index]))
                #CData.append(float(jdl["_PowerDB"][index]))
                #CData2.append(float(jdl["_CoGDoppler"][index]))
         
        if not XData or not YData:
            continue    
        XMean = statistics.mean(XData)
        YMean = statistics.mean(YData)
         
        lastFiveXValues.append(XMean)
        lastFiveYValues.append(YMean)
         
        XMedian = statistics.median(lastFiveXValues)
        YMedian = statistics.median(lastFiveYValues)  
         
        frame.updateScatter(XMedian, YMedian)
    

app = wx.App(redirect=False)
frame = Frame(None, "moin")
frame.Show()

thread = threading.Thread(target=update, args=(), daemon=True)
thread.start()

app.MainLoop()



