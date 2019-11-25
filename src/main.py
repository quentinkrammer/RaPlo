# -*- coding: utf-8 -*-

import socket
import os
from DeparseData import DeparseData
from RTS_Plot import RTS_Plot


# def writeToFile(txt):
#     f = open(".\data\testdatenX.txt", "a")
#     f.write(txt)
#     f.close()
# 
# if __name__ == '__main__':
#     
# 
#     HOST = '127.0.0.1'  # The server's hostname or IP address
#     PORT = 1337        # The port used by the server
#     
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((HOST, PORT))
#         #s.sendall(b'Hello, world')
#         while(True):
#             data = s.recv(int(4.0E7))
#             writeToFile(data.decode())
#path = os.path.realpath('..')# + "\\data\\testdaten1.txt"

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


# print(jdl)
# print("----------------ENDE----------------")
# jdl = parser.deparseNextSegment()
# print(jdl)
# 
# print("----------------ENDE----------------")
# jdl = parser.deparseNextSegment()
# print(jdl)
# 
# print("----------------ende----------------")
# jdl = parser.deparseNextSegment()
# print(jdl)


# rts = RTS_Plot()
# rts.scatterPlot()
# rts.linePlot()









           
    
    