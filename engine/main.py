import pickle
import ktypes
import devices
#import cond
import os.path
import debug
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

def Init():
    #if os.path.isfile("save.p"):
    #    data=pickle.load( open( "save.p", "rb" ) )
    #else:
    data=Data()
    ###
    return data

def Kill(data):
    pickle.dump( data, open( "save.p", "wb" ) )
def Testy(data):
    data.addType("Swiatlo","zarowka led",1)
    data.addDev(data,"Swiatlo 1",(1,1),"Swiatlo w duzym pokoju","Swiatlo",60)
    data.printTyp()
    data.printDev()
###
def main(Const):
    data=Init()
    Testy(data)
    print(Const)
    Kill(data)
    return
###  
    
  
if __name__ == "__main__":
    # execute only if run as a script
    main("aaa")
    pass
