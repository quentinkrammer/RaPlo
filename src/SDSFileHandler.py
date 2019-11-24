# -*- coding: utf-8 -*-

class SDSFileHandler():


    def __init__(self, path):
        self.file = open(path)
        
        
    def __del__(self):
        self.file.close()
        
    def getNextDGLSegment(self):
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
            