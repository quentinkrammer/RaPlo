# -*- coding: utf-8 -*-

import socket
from ConfigHandler import ConfigHandler

class DGMSegmentFetcher(ConfigHandler):

    def __init__(self):
        #ConfigHandler.__init__(self, type(self).__name__ )
        ConfigHandler.__init__(self )                 
        self.SOURCE = self.getValue("source", "DEFAULT")        
        if self.SOURCE == "local" : 
            self.setSection("DGMSegmentFetcher_Local")                       
            self.file = open(self.getValue("path"))                        
        if self.SOURCE == "remote":
            self.setSection("DGMSegmentFetcher_Remote")
            self.HOST = self.getValue("host")  # The server's hostname or IP address
            self.PORT = int(self.getValue("port"))        # The port used by the server
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.HOST, self.PORT))
            self.file = None
            self.buffer = self.getValue("buffer") #2**19 to match 4e7
        
    def __del__(self):
        if self.SOURCE == "local":
            self.file.close()
        if self.SOURCE == "remote":            
            self.socket.close()
            
    def getNextDGMSegment(self):
        if self.SOURCE == "local":
            return self.getNextDGM()
        if self.SOURCE == "remote":
            return self.getNextDGM_Remote()       
                        
    def getNextDGM_Remote(self):         
        data = self.socket.recv(self.buffer).decode()#data = self.socket.recv(int(4.0E7)
   
        tempFile = open("tempData.txt", 'w')
        tempFile.write(data)
        tempFile.close()                 
        with open("tempData.txt") as self.file:
            segment = self.getNextDGM()          
        return segment
    
    def getNextDGM(self):
        segment = { "Joint Detection" : [],  \
                   "Host Dynamics" : []
            }
        while True:
            line = self.file.readline()
            if not line:
                return (False, False)                        
            if "Joint" in line:
                line = self.getNextLine()                  
                while line:       
                    segment["Joint Detection"].append(line)
                    line = self.getNextLine() 
            if "Host" in line:
                line = self.getNextLine()                  
                while line:       
                    segment["Host Dynamics"].append(line)
                    line = self.getNextLine()
                    if "</DGM>" in line:
                        break
                break                
        return (segment["Joint Detection"], segment["Host Dynamics"] )
                    
    def getNextLine(self):
        l = self.file.readline() 
        l = l.rstrip('\n').strip()
        return l
    
    def writeToFile(self, txt):
        #f = open(".\data\testdatenX.txt", "a")
        f = open("latest_recorded_data.txt", "a")
        f.write(txt)
        f.close()
        
# d = DGMSegmentFetcher()
# print(d.SOURCE)