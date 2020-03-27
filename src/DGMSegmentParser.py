# -*- coding: utf-8 -*-

from DGMSegmentFetcher import DGMSegmentFetcher

class DGMSegmentParser(DGMSegmentFetcher):

    def __init__(self):        
        DGMSegmentFetcher.__init__(self)
        self.JDL = {}        
        self.HD = {}         
        
    def deparseNextSegmentRaw(self):        
        JDLStrings, HDStrings = self.getNextDGMSegment()
        if not JDLStrings:
            return (False, False)    
        headerStrings = JDLStrings[0][:-1].split(",")
        for string in headerStrings:
            self.JDL[string] = []
        for dataString in JDLStrings[1:]:
            data = dataString[:-1].split(",")            
            for i, string in enumerate(headerStrings):
                self.JDL[string].append(data[i])  
                 
        headerStrings = HDStrings[0][:-1].split(",")
        for string in headerStrings:
            self.HD[string] = []
        for dataString in HDStrings[1:]:
            data = dataString[:-1].split(",")            
            for i, string in enumerate(headerStrings):
                self.HD[string].append(data[i])                                  
        return (self.JDL, self.HD)
    
    def deparseNextSegmentFiltered(self):
        JDLStrings = self.getNextDGMSegmentFiltered()
        if len(JDLStrings) == 1:
            return False
        headerStrings = JDLStrings[0].split(",")
        for string in headerStrings:
            self.JDL[string] = []
        for dataString in JDLStrings[1:]:
            data = dataString.split(",")            
            for i, string in enumerate(headerStrings):
                self.JDL[string].append(data[i])
        return self.JDL
        
#     def deparseRemote(self): 
#         segment = self.getNextDGLSegment() 
#         return segment    