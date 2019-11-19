# -*- coding: utf-8 -*-
'''

'''
import socket
import os


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
jointDetecion = []
#file = open("testdaten1.txt")
with open("testdaten1.txt") as file:
    #for line in file:
    for index, line in enumerate(file):    
        content = line.rstrip('\n')
        #print(content)
        if content:
            print("Content: "+repr(content))
            print(index)
            #if "Joint Detection List:" in content:
#                 header = file.readline()
#                 jointDetecion.append(file.readline())
#                 jointDetecion.append(file.readline())
#                 print(jointDetecion)
        
        #if content[-1] == ":":
        #    header = file.readline()
        #    hostDynamics = file.readline()
      
        #print(hostDynamics)
    
    
    file.close() 
           
    
    