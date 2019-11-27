# -*- coding: utf-8 -*-

import socket
import os
from DeparseData import DeparseData
from RTS_Plot import RTS_Plot

rts = RTS_Plot()
parser = DeparseData("local")


jdl, hd = parser.deparseNextSegment()
 
XData = []#DataJDL.LatPos_m(SelectedSensor); %LatPos_m where logical array == 1
YData = []#DataJDL.LongPos_m(SelectedSensor);
CData = []#DataJDL.Power_dB(SelectedSensor);
CData2 = []#DataJDL.CoG_Doppler(SelectedSensor);    
 
for index, sensor in enumerate(jdl["_NSensor"]):
    if sensor == "2":
        XData.append(jdl["_LatPos_m"][index])
        YData.append(jdl["_LongPos_m"][index])
        CData.append(jdl["_PowerDB"][index])
        CData2.append(jdl["_CoGDoppler"][index])

rts.scatterPlot(XData, YData)
# 
# print("ENDE")

# jdl, hd = parser.deparseNextSegment()
# print(jdl)
# print(len(jdl["Version"]))
# jdl, hd = parser.deparseNextSegment()
# print(jdl)
# jdl, hd = parser.deparseNextSegment()
# print(jdl)
# jdl, hd = parser.deparseNextSegment()
# print(jdl)


# rts = RTS_Plot()
# rts.scatterPlot()
# rts.linePlot()









           
    
    