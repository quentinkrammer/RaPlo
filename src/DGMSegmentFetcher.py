# -*- coding: utf-8 -*-

import socket
from ConfigHandler import ConfigHandler
import collections

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
            self.HOST = self.getValue("host")
            self.PORT = int(self.getValue("port"))     
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.HOST, self.PORT))
            self.file = None
            self.buffer = int(self.getValue("buffer")) #2**19 to match 4e7
            self.dataStorageFile = self.getValue("dataStoragePath") 
        
    def __del__(self):
        if self.SOURCE == "local":
            self.file.close()
        if self.SOURCE == "remote":            
            self.socket.close()
            
    def writeToFile(self, txt):
        f = open(self.dataStorageFile, "a")
        f.write(txt)
        f.close()
            
    def getNextDGMSegment(self):
        if self.SOURCE == "local":
            return self.getNextDGM_Local()
        if self.SOURCE == "remote":
            return self.getNextDGM_Remote2()       
                        
    def getNextDGM_Remote(self):
        dataBytes = self.socket.recv(self.buffer)
        dataStr = dataBytes.decode()
        self.writeToFile(dataStr)   
        tempFile = open(".tempData.txt", 'w')
        tempFile.write(dataStr)
        tempFile.close()                 
        with open(".tempData.txt") as self.file:
            segment = self.getNextDGM_Local()          
        return segment
    
    def getNextDGM_Local(self):
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
    
    def getNextDGM_Remote2(self):
        deque = collections.deque([], 6)
        data = ""
        while True:
            char = self.socket.recv(1).decode()            
            data += char
            deque.append(char)
            terminator = str().join(deque)            
            if terminator == "</DGM>":
                break
        self.writeToFile(data)   
        tempFile = open(".tempData.txt", 'w')
        tempFile.write(data)
        tempFile.close()                 
        with open(".tempData.txt") as self.file:
            segment = self.getNextDGM_Local()          
        return segment
            
        
            
        

