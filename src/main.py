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

dataRaw = []
dataFinal = []

with open("testdaten1.txt") as file:
    #for line in file:        
    #linesRaw=file.readlines()
    for lineRaw in file:
        line = lineRaw.rstrip('\n').strip()
        #if line:
        dataRaw.append(line)    
    file.close()
    
      
updatedIndex = 0        
for index, d in enumerate(dataRaw):
    print(repr(d))
    if d:        
        if "Joint" in d[:5]:
            dataPair = {}            
            updatedIndex = index + 1#             
            JDLabel = dataRaw[updatedIndex][:-1].split(",")
            updatedIndex = updatedIndex + 1 
            JDLabelValuePairs = []                      
            while dataRaw[updatedIndex]:
                JDLabelValuePair = {}                
                JDValues = dataRaw[updatedIndex][:-1].split(",")
                for i, label in enumerate(JDLabel):
                    JDLabelValuePair[label] = JDValues[i]
                JDLabelValuePairs.append(JDLabelValuePair)                                                    
                updatedIndex = updatedIndex + 1
            dataPair["Joint Detection"] = JDLabelValuePairs
                
        if "Host" in d[:4]:
            updatedIndex = index + 1#             
            HDLabel = dataRaw[updatedIndex][:-1].split(",")
            updatedIndex = updatedIndex + 1 
            HDLabelValuePairs = []          
            while not "</DGM>" in dataRaw[updatedIndex]:
                HDLabelValuePair = {}                
                HDValues = dataRaw[updatedIndex][:-1].split(",")
                for i, label in enumerate(HDLabel):
                    HDLabelValuePair[label] = HDValues[i]
                HDLabelValuePairs.append(HDLabelValuePair)                                                    
                updatedIndex = updatedIndex + 1
            dataPair["Host Dynamics"] = HDLabelValuePairs
            dataFinal.append(dataPair)      
        
                
print(repr(dataFinal))
                         
                
        
            
                   
    
    
#     for index, line in enumerate(file):    
#         content = line.rstrip('\n').strip()
#         #print(content)
#         if content:
#             if content[-1] == ":":
#                 #jdl = line[]
#                 print("Content: "+repr(content))
#                 print(index)
                
                
            #if "Joint Detection List:" in content:
#                 header = file.readline()
#                 jointDetecion.append(file.readline())
#                 jointDetecion.append(file.readline())
#                 print(jointDetecion)
        
        #if content[-1] == ":":
        #    header = file.readline()
        #    hostDynamics = file.readline()
      
        #print(hostDynamics)

           
    
    