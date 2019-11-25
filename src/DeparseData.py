from DGMSegmentHandler import DGMSegmentHandler


class DeparseData(DGMSegmentHandler):

    def __init__(self, source):        
        DGMSegmentHandler.__init__(self, source)
        self.JDL = {}        
        self.HD = {}         
        
    def deparseNextSegment(self):
        #JDLStrings = self.getNextDGMSegment()
        
        JDLStrings, HDStrings = self.getNextDGMSegment()
        if not JDLStrings:
            return (False, False)    
#         self.JDL = self.seperateHeaderFromData(JDLStrings, "JDL")
#         self.HD = self.seperateHeaderFromData(HDStrings, "HD")
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
        #return JDLStrings 
                                  
        return (self.JDL, self.HD)
    
    def deparseRemote(self): 
        segment = self.getNextDGLSegment() 
        return segment      
         
    def seperateHeaderFromData(self, listOfStrings, listRef):
                               
        headerStrings = listOfStrings[0][:-1].split(",")
        for string in headerStrings:
            listRef[string] = []
        for dataString in listOfStrings[1:]:
            data = dataString[:-1].split(",")            
            for i, string in enumerate(headerStrings):
                listRef[string].append(data[i])
            
            
        
        