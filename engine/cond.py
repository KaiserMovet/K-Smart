import sys
import pickle
import devices
import debug

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
    def __init__(self,data,dev1,value1,dev2,value2,comp):
        self.data=data
        self.value1=value1
        self.value2=value2
        self.bool=False
        self.dev1=dev1#Const value from value1/2 variable for "Value" else find Devices with name dev1/2
        self.dev2=dev2
        self.comp=comp
        self.compDict={"equal":equal,"less":less,"more":more,"equalles":equalLess,"equalMore":equalMore}
        debug.Log('SmallCond Added {} {} {} {} {}'.format(dev1,value1,dev2,value2,comp))
    
    def Refresh(self):
        if self.dev1!="Value":
            self.value1=self.data.GetValue(self.dev1,self.data)
        if self.dev2!="Value":
            self.value2=self.data.GetValue(self.dev2,self.data)
        self.bool=self.compDict[self.comp](self.value1,self.value2)
    
    def ToStr(self):
        string = "\tCond = {{"
        string += "\n\t\t1."+str(self.dev1)+" = "+str(self.value1)
        string += "\n\t\t1."+str(self.dev2)+" = "+str(self.value2)
        string += "\n\t\tcomp = "+self.comp
        string += "\n\t\tBool = "+ str(self.bool)
        string += "\n\t}}"
        return string
    ###
###
class Effect(object):
    def __init__(self,data,deviceName,trueValue,falseValue):
        self.deviceName=deviceName
        self.trueValue=trueValue #-1 - nie wysyla wartosci (nic nie robi podczas refreshu)
        self.falseValue=falseValue
        self.data=data
        
    ###
    def Refresh(self,con):
        if con:
            if self.trueValue!=-1:
                self.data.SendValue(self.deviceName,self.trueValue)
            ###
        else:
            if self.trueValue!=-1:
                self.data.SendValue(self.deviceName,self.trueValue)
            ###
        ###
    ###
    def ToStr(self):
        string = "\tEffect = {{"
        string += "\n\t\tDevice Name = "+self.deviceName
        string += "\n\t\ttrueValue = "+ str(self.trueValue)
        string += "\n\t\tfalseValue = "+ str(self.falseValue)
        string += "\n\t\tCurrentValue = "+ str(self.data.GetValue(self.deviceName,self.data))
        string += "\n\t}}"
        return string
    ###
###



class Cond(object):
    def __init__(self,name,refresh,desc):
        self.name = name
        self.refresh=refresh #sekundy
        self.desc = desc
        self.small=list() #lista malych warunkow
        self.effect=list() #lista efektow
        self.bool=False
        debug.Log('Cond: Object Added {} {} {}'.format(name,refresh,desc))
    ###
    def addEffec(self,data,deviceName,trueValue,falseValue):
        self.effect.append(Effect(data,deviceName,trueValue,falseValue))
        debug.Log('{}: Effect Added {} {} {}'.format(self.name,deviceName,trueValue,falseValue))
    ###
    def addCond(self,data,dev1,value1,dev2,value2,comp):
        self.small.append(SmallCond(data,dev1,value1,dev2,value2,comp))
        debug.Log('{}: Cond Added {} {} {} {} {}'.format(self.name,dev1,value1,dev2,value2,comp))
    ###
    def Refresh(self):
        tempBool=0 #Liczy true w small.bool
        for i in self.small:
            i.Refresh()
            if i.bool:
                tempBool+=1
            ###
        ###
        if tempBool==len(self.small):
            self.bool=True
        else:
            self.bool=False
        ###
        for i in self.effect:
            i.Refresh(self.bool)
        ###
    def ToStr(self):
        string = "Condition = {{"
        string += "\n\tname = "+self.name
        string += "\n\tDesc = "+ self.desc
        string += "\n\tRefresh = "+str(self.refresh)
        string += "\n\tBool = "+str(self.bool)
        for i in self.small:
            string+=i.ToStr()
        ###
        string += "\n}}"
        return string
    ###
###
