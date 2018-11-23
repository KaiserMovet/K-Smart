import sys
import pickle
import devices
dic=dict()

def equal(a,b):
    return (a==b)
def less(a,b):
    return (a<b)
def more(a,b):
    return (a>b)
def equalLess(a,b):
    return (a<=b)
def equalMore(a,b):
    return (a>=b)


class SmallCond(object):
    def __init__(self):
        self.value1=0
        self.value2=0
        self.bool="false"
        self.dev1="Value"#Const value from value1/2 variable for "Value" else find Devices with name dev1/2
        self.dev2="None"
        self.comp=equal
    
    def Refresh(self):
        if self.dev1!="Value":
            self.value1=devices.GetValue(self.dev1)
        if self.dev2!="Value":
            self.value2=devices.GetValue(self.dev2)
        self.bool=self.comp(self.value1,self.value2)

###    
class Cond(object):
    def __init__(self):
        self.name = "None"
        self.refresh=60 #sekundy
        self.desc = "Some Device Type"
        self.small=list() #lista malych warunkow
    



def Load():
    dic = pickle.load( open( "cond.p", "rb" ) )
   
###
def Save():
    pickle.dump( dic, open( "cond.p", "wb" ) )
###
