import debug
import ktypes
import cond
import devices

class Data:

    def __init__(self):
        self.dicTyp=dict()
        self.dicDev=dict()
        self.divCon=dict()
        pass
    ###
    def addType(self,name,desc,isRec):
        self.dicTyp[name]=ktypes.Types(name,desc,isRec)
        
    ###
    def addDev(self,data,name,pos,desc,typeName,refreshTime):
        self.dicDev[name]=devices.Device(data,name,pos,desc,typeName,refreshTime)
    ###
    def printTyp(self):
        for i in self.dicTyp.values():
            print(i.toStr())
    def printDev(self):
        for i in self.dicDev.values():
            print(i.toStr())
    ###
    def TypToStr(self):
        string=""
        for i in self.dicTyp.values():
            string+=(i.toStr())
        return string
    def DevToStr(self):
        string=""
        for i in self.dicDev.values():
            string+=(i.toStr())
        return string
    ###
    ###Get Value from device
    def GetValue(self,name):
        value=self.dicDev[name].value
        return value
    ###
    ###Send Value to device
    def SendValue(self,name,val):
        if(self.dicDev[name].type.isRec):
            self.dicDev[name].value=val
            debug.Log('Data: SendValue {} {} '.format(name,val))
        return

###