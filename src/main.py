# -*- coding: utf-8 -*-

from Frame import Frame
import wx
import threading
from DGMSegmentParser import DGMSegmentParser
from DataSmoother import DataSmoother
from ConfigHandler import ConfigHandler
import numpy as np
import math as m
import itertools
import cmath
import datetime
 


def floatValues(*strValues):
    floatValues = []
    for x in strValues:
        floatValues.append(float(x))
    return floatValues

def intValues(*strValues):
    intValues = []
    for x in strValues:
        intValues.append(int(x))
    return intValues

def update():
    
    phi = np.radians(-(45+100))    
    rotMat = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])
#     measurementStarted = False
#     fileIndex = 0    
    while True:
        jdl, hd = parser.deparseNextSegment()
        
        xData = floatValues(*jdl["_LatPos_m"])
        yData = floatValues(*jdl["_LongPos_m"])
        
        dataPoints = np.array([xData, yData])        
        rotDataPoints = rotMat.dot(dataPoints)        
        scatterCoordinates = np.transpose(rotDataPoints)     
        frame.rtsPlot.updateScatter2(scatterCoordinates)        
        
#         for sc in scatterCoordinates:            
#             abs = complex(sc[0],sc[1]);
#             abs = np.absolute(abs)
#             
#             if(abs > 9.7 and abs < 10.3):
#                 if not measurementStarted:
#                     startTime = datetime.datetime.now()
#                     priorInterval = startTime
#                     measurementStarted = True
#                     fileIndex += 1;
#                     file= open("sortedData_"+str(fileIndex)+".txt","w+")                    
#                     continue                                            
#                 
#                 now = datetime.datetime.now()                
#                 TimeBetweenValidData =( now - priorInterval ).microseconds / 1000            
#                 
#                 if (TimeBetweenValidData > 400 ):
#                     file.close()
#                     fileIndex += 1;
#                     file= open("sortedData_"+str(fileIndex)+".txt","w+")   
#                     #print("NEUE MESSUNG")
#                 
#                 file.write(str(sc[0])+","+str(sc[1])+"\n")                
#                 priorInterval = now
#    file.close()             
                            

parser = DGMSegmentParser() 
config = ConfigHandler("DEFAULT")
sensor = config.getValue("sensor")

app = wx.App(redirect=False)
frame = Frame(None, "RaPlo")
frame.Show()
 
thread = threading.Thread(target=update, args=(), daemon=True)
thread.start()
 
app.MainLoop()


