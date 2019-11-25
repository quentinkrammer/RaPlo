# -*- coding: utf-8 -*-

import socket
import os
from DeparseData import DeparseData
from RTS_Plot import RTS_Plot


parser = DeparseData("local")
jdl, hd = parser.deparseNextSegment()
print(jdl)
print(len(jdl["Version"]))

jdl, hd = parser.deparseNextSegment()
print(jdl)
jdl, hd = parser.deparseNextSegment()
print(jdl)
jdl, hd = parser.deparseNextSegment()
print(jdl)


# rts = RTS_Plot()
# rts.scatterPlot()
# rts.linePlot()









           
    
    