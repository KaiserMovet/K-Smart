import sys
import pickle
import types
dic=dict()

class Device(object):
    def __init__(self):
        self.name = "None"
        self.pos=(1,1)
        self.desc = "Some Device"
        self.typeName="None"
        self.value=0
        self.trueValue=-1
        self.type=types.dic[self.typeName]
        self.refresh=60 #sekundy
    def refresh():
        if self.type.isRec
            if self.value!=self.trueValue
                self.trueValue=self.value
                SetDevValue()
                return
            pass
        pass
        GetDevValue()
    
    def GetDevValue():
        #TODO
        pass
    ###
    def SetDevValue():
        #TODO
        pass
    ###


def Load():
    dic = pickle.load( open( "devices.p", "rb" ) )

###
def Save(lista):
    pickle.dump( dic, open( "devices.p", "wb" ) )
###

def GetValue(name):
    value=dic[name].value
    return value
###

def SendValue(name,val):
    if(dic[name].type.isRec):
        dic[name].value=val
    return