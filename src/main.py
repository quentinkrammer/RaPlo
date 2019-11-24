# -*- coding: utf-8 -*-
'''

'''
import socket
import os
from GetDataFromFile import GetDataFromFile
from SDSFileHandler import SDSFileHandler
from DeparseData import DeparseData
import matplotlib.pyplot as plt
import numpy as np

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


# path = r"C:\\Users\\Divalu\\git\\RaPlo\\data\\testdaten1.txt"
# print(path)

# d = GetDataFromFile("test2.txt")
# data = d.getData()
# #print(data)
# 
# 
# x = []
# y = []
# 
# for bracket in data:
#     for dataPoint in bracket["Joint Detection"]:
#         x.append( dataPoint["_LatPos_m"] )
#         y.append( dataPoint["_LongPos_m"] )
#     
# 
# plt.plot(x, y, marker="x")
# 
# plt.xlabel('_LatPos_m')
# plt.ylabel('_LongPos_m')
# 
# plt.title("Simple Plot")
# 
# plt.legend()
# 
# plt.show()


# fh = SDSFileHandler("testdaten1.txt")
# segment  = fh.getNextDGLSegment()
# segment2  = fh.getNextDGLSegment()
# segment3  = fh.getNextDGLSegment()
# segment4  = fh.getNextDGLSegment()
# print("ENDE")


parser = DeparseData("testdaten1.txt")
jdl, hd = parser.deparseNextSegment()
jdl, hd = parser.deparseNextSegment()
jdl, hd = parser.deparseNextSegment()
jdl, hd = parser.deparseNextSegment()
print("ENDE")






           
    
    