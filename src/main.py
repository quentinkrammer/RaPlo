# -*- coding: utf-8 -*-
import math
import statistics
import collections 
import socket
import os
from DeparseData import DeparseData
from RTS_Plot import RTS_Plot

rts = RTS_Plot()
parser = DeparseData("local")

initLast5Values = [99, 0, 99, 0, 99]
lastFiveXValues = collections.deque(initLast5Values, 5)
lastFiveYValues = collections.deque(initLast5Values, 5)

# jdl, hd = parser.deparseNextSegment()
# print(jdl)
# jdl, hd = parser.deparseNextSegment()
# print(jdl)
# jdl, hd = parser.deparseNextSegment()
# print(jdl)
# jdl, hd = parser.deparseNextSegment()
# print(jdl)
XMin = None
XMax = None
YMin = None
YMax = None
while True:
    jdl, hd = parser.deparseNextSegment()
    if not jdl:
        break
      
    XData = []#DataJDL.LatPos_m(SelectedSensor); %LatPos_m where logical array == 1
    YData = []#DataJDL.LongPos_m(SelectedSensor);
    CData = []#DataJDL.Power_dB(SelectedSensor);
    CData2 = []#DataJDL.CoG_Doppler(SelectedSensor);    
      
    for index, sensor in enumerate(jdl["_NSensor"]):
        if sensor == "0":
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
    
#     if not XMin:        
#         XMin =  XMedian
#     if not YMin:        
#         YMin =  YMedian
#     if not XMax:        
#         XMax =  XMedian
#     if not YMax:        
#         YMax =  YMedian
#     if XMedian < XMin:
#         XMin = XMedian
#     if YMedian < YMin:
#         YMin = YMedian
#     if XMedian > XMax:
#         XMax = XMedian
#     if YMedian > YMax:
#         YMax = YMedian
#     print("X: "+str(XMin)+" to "+str(XMax))   
#     print("Y: "+str(YMin)+" to "+str(YMax))  
    
#     arg =  math.sqrt(XMedian**2+YMedian**2)
#     print(arg)
     
    rts.scatterPlot(XMedian, YMedian)



           
    
    