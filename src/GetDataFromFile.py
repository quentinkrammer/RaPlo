# -*- coding: utf-8 -*-

class GetDataFromFile():

    def __init__(self, filePath):        
        self.data = self.extractData(filePath)
        
    def getData(self):
        return self.data
        
    def extractData(self, path):        
        dataRaw = []
        dataFinal = []        
        with open(path) as file:            
            for lineRaw in file:
                line = lineRaw.rstrip('\n').strip()                
                dataRaw.append(line)    
            file.close()    
              
        updatedIndex = 0        
        for index, d in enumerate(dataRaw):
            #print(repr(d))
            if d:        
                if "Joint" in d[:5]:
                    dataPair = {}            
                    updatedIndex = index + 1             
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
                    dataPair["Joint Detection"] = tuple(JDLabelValuePairs)
                        
                if "Host" in d[:4]:
                    updatedIndex = index + 1             
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
                    dataPair["Host Dynamics"] = tuple(HDLabelValuePairs)
                    dataFinal.append(dataPair)
        dataFinal = tuple(dataFinal)                         
        return dataFinal