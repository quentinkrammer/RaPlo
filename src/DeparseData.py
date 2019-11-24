from SDSFileHandler import SDSFileHandler


class DeparseData(SDSFileHandler):

    def __init__(self, path):        
        SDSFileHandler.__init__(self, path)
        self.JDL = {}        
        self.HD = {}         
        
    def deparseNextSegment(self):
        JDLStrings, HDStrings = self.getNextDGLSegment()
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
                                  
        return (self.JDL, self.HD)        
         
    def seperateHeaderFromData(self, listOfStrings, listRef):
                               
        headerStrings = listOfStrings[0][:-1].split(",")
        for string in headerStrings:
            listRef[string] = []
        for dataString in listOfStrings[1:]:
            data = dataString[:-1].split(",")            
            for i, string in enumerate(headerStrings):
                listRef[string].append(data[i])
            
            
        
        