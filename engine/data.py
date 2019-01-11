import debug
import cond
import devices
from cam import Cam
from time import sleep
class Data:

    def Wait(self):
        while self.isUpdating:
            sleep(1)

    def Const(self):
        self.dicConst["interval"]=15
        self.dicConst["timeCount"]=0

    def __init__(self):
    #   self.dicTyp=dict()
        self.cam=Cam()

        self.dicDev=dict()
        self.dicCon=dict()
        self.isUpdating=False#when Refresh is active
        self.dicConst=dict()
        self.Const()
        pass
    ###
    def toDict(self):
        wynik=dict()
        wynik["dicConst"]=self.dicConst.copy()
        wynik["camCount"]=self.cam.Count()
        wynik["dicDev"]=dict()
        wynik["dicCon"]=dict()
        wynik["possibleCond"]=list(cond.compDict.keys())
        for i in self.dicDev.keys():
            wynik["dicDev"][i]=self.dicDev[i].__dict__.copy()
        for i in self.dicCon.keys():
            wynik["dicCon"][i]=self.dicCon[i].__dict__.copy()
            a=dict()
            for j in self.dicCon[i].small.keys():
                a[j]=self.dicCon[i].small[j].__dict__.copy()
                a[j].pop("data")

            b=dict()
            for j in self.dicCon[i].effect.keys():
                b[j]=self.dicCon[i].effect[j].__dict__.copy()
                b[j].pop("data")
            wynik["dicCon"][i]=self.dicCon[i].__dict__.copy()

            wynik["dicCon"][i]["small"]=a
            wynik["dicCon"][i]["effect"]=b
        return wynik
    ###
    def addDev(self,name,desc,typeName,refreshTime,isRec,pos=(-1,-1)):
        self.Wait()
        self.dicDev[name]=devices.Device(name,pos,desc,typeName,refreshTime,isRec)
        print("Dodano")
        print(self.dicDev[name].toStr())
    ###
    def addValue(self,name,pos,desc,value):
        self.Wait()
        self.dicDev[name]=devices.Value(name,pos,desc,value)
    ###
    def changePos(self,name,pos):
        self.Wait()
        self.dicDev[name].pos=pos
    ###
    def addCond(self,name,refresh,desc):
        self.Wait()
        self.dicCon[name]=cond.Cond(name,refresh,desc)
    ###
    def addSmall(self,conName,smallName,dev1,dev2,comp,value1=0,value2=0):
        if conName in self.dicCon:
            self.Wait()
            self.dicCon[conName].addSmall(self,smallName,dev1,dev2,comp,value1,value2)
    ###
    def addEffect(self,conName,effectName,deviceName,trueValue,falseValue):
        if conName in self.dicCon:
            self.Wait()
            self.dicCon[conName].addEffec(self,effectName,deviceName,trueValue,falseValue)
    ###
    def addCam(self,name):
        self.cam.AddCam(name)
    def remCam(self,name):
        self.cam.RemoveCam(name)
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
        if name not in self.dicCon:
            return -1
        value=self.dicDev[name].value
        return value
    ###
    ###Send Value to device
    def SendValue(self,name,val):
        if name not in self.dicDev.keys():
            return
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