from Frame import Frame
import wx
import threading
from DGMSegmentParser import DGMSegmentParser
from DataSmoother import DataSmoother

def update():
    parser = DGMSegmentParser()
    while True:
        jdl, hd = parser.deparseNextSegment()
        if not jdl:
            break          
        XData = []#         CData = []#DataJDL.Power_dB(SelectedSensor);
        YData = []#         CData2 = []#DataJDL.CoG_Doppler(SelectedSensor);      
        dopplerData = []       
        for index, sensor in enumerate(jdl["_NSensor"]):
            if sensor == "2":
                XData.append(float(jdl["_LatPos_m"][index]))
                YData.append(float(jdl["_LongPos_m"][index]))
                dopplerData.append(float(jdl["_CoGDoppler"][index]))         
        if not XData or not YData:
            continue             
        XMedian =  X_Smoother(XData)
        YMedian =  Y_Smoother(YData)
        dopplerMedian =  doppler_Smoother(dopplerData)       
        frame.updateScatter(XMedian, YMedian)
        frame.updateDoppler(dopplerMedian)
    

doppler_Smoother = DataSmoother()
X_Smoother = DataSmoother()
Y_Smoother = DataSmoother()
app = wx.App(redirect=False)
frame = Frame(None, "RaPlo")
#
frame.Show()
#

thread = threading.Thread(target=update, args=(), daemon=True)
thread.start()

app.MainLoop()



