
class Data:

    def Const(self):
        self.dicConst["interval"]=15
        self.dicConst["timeCount"]=0

    def __init__(self):
    #   self.dicTyp=dict()
        self.dicDev=dict()
        self.dicCon=dict()

        self.dicConst=dict()
        self.Const()
        pass
    ###
    #def addType(self,name,desc,isRec):
    #    self.dicTyp[name]=ktypes.Types(name,desc,isRec)
        
    ###
    def addDev(self,name,pos,desc,typeName,refreshTime,isRec):
        self.dicDev[name]=devices.Device(name,pos,desc,typeName,refreshTime,isRec)
    ###
    def addValue(self,name,pos,desc,value):
        self.dicDev[name]=devices.Value(name,pos,desc,value)
    ###
    def changePos(self,name,pos):
        self.dicDev[name].pos=pos
    ###
    def addCond(self,name,refresh,desc):
        self.dicCon[name]=cond.Cond(name,refresh,desc)
    ###
    def addSmall(self,conName,smallName,dev1,dev2,comp,value1=0,value2=0):
        self.dicCon[conName].addSmall(self,smallName,dev1,dev2,comp,value1,value2)
    ###
    def addEffect(self,conName,effectName,deviceName,trueValue,falseValue):
        self.dicCon[conName].addEffec(self,effectName,deviceName,trueValue,falseValue)
    ###
   
    def printDev(self):
        for i in self.dicDev.values():
            print(i.toStr())
    ###
   
    def DevToStr(self):
        string=""
        for i in self.dicDev.values():
            string+=(i.toStr())
        return string
    def ConToStr(self):
        string=""
        for i in self.dicCon.values():
            string+=(i.toStr())
        return string
    ###
    def DataToStr(self):
        string=""
        string+=str(self.dicConst)+"\n"
        string+=self.DevToStr()
        string+=self.ConToStr()
        return string
    ###Get Value from device
    def GetValue(self,name):
        value=self.dicDev[name].value
        return value
    ###
    ###Send Value to device
    def SendValue(self,name,val):
        if(self.dicDev[name].isRec):
            self.dicDev[name].value=val
            debug.Log('Data: SendValue {} {} '.format(name,val))
        return
    ###
    def Refresh(self):
        for i in self.dicDev.values():
            i.Refresh(self.dicConst["timeCount"],self.dicConst["interval"])
        for i in self.dicCon.values():
            i.Refresh(self.dicConst["timeCount"],self.dicConst["interval"])
        

###
