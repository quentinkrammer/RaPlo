from Frame import Frame
import wx
import threading
from DGMSegmentParser import DGMSegmentParser
from DataSmoother import DataSmoother
from ConfigHandler import ConfigHandler
import numpy as np
import math as m

# def update():
#     parser = DGMSegmentParser()
#     while True:
#         jdl, hd = parser.deparseNextSegment()
#         if not jdl:
#             break          
#         XData = []#         CData = []#DataJDL.Power_dB(SelectedSensor);
#         YData = []#         CData2 = []#DataJDL.CoG_Doppler(SelectedSensor);      
#         dopplerData = []       
# #         for index, sensor in enumerate(jdl["_NSensor"]):
# #             if sensor == sensor:
# #                 XData.append(float(jdl["_LatPos_m"][index]))
# #                 YData.append(float(jdl["_LongPos_m"][index]))
# #                 dopplerData.append(float(jdl["_CoGDoppler"][index]))         
#         if not XData or not YData:
#             continue             
#         XMedian =  X_Smoother(XData)
#         YMedian =  Y_Smoother(YData)
#         dopplerMedian =  doppler_Smoother(dopplerData)       
#         frame.updateScatter(XMedian, YMedian)
#         frame.updateDoppler(dopplerMedian)
#     
# 
# config = ConfigHandler("DEFAULT")
# sensor = config.getValue("sensor")
# doppler_Smoother = DataSmoother()
# X_Smoother = DataSmoother()
# Y_Smoother = DataSmoother()
# app = wx.App(redirect=False)
# frame = Frame(None, "RaPlo")
# #
# frame.Show()
# #
# 
# thread = threading.Thread(target=update, args=(), daemon=True)
# thread.start()
# 
# app.MainLoop()

def floatValues(*strValues):
    floatValues = []
    for x in strValues:
        floatValues.append(float(x))
    return floatValues
 
phi = -np.pi/4
rotMat = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])

parser = DGMSegmentParser()
jdl, hd = parser.deparseNextSegment()

xData = floatValues(*jdl["_LatPos_m"])
yData = floatValues(*jdl["_LongPos_m"])
dataPoints = np.array([xData, yData])
#dataPoints = np.array([[-1, 3, 1], [1, 4, 0] ])
rotDataPoints = rotMat.dot(dataPoints)

print(rotMat)
print(dataPoints)
print(rotDataPoints)

# pi = np.pi
# print(pi)
# print(np.cos(pi))
# print(np.sin(pi))



