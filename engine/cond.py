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
compDict={"equal":equal,"less":less,"more":more,"equalles":equalLess,"equalMore":equalMore}

class SmallCond(object):
    def __init__(self,data,dev1,value1,dev2,value2,comp):
        self.data=data
        self.value1=value1
        self.value2=value2
        self.bool=False
        self.dev1=dev1#Const value from value1/2 variable for "Value" else find Devices with name dev1/2
        self.dev2=dev2
        self.comp=comp
    
    def Refresh(self):
        print("Refresh")
        if self.dev1!="Value":
            self.value1=self.data.GetValue(self.dev1)
        if self.dev2!="Value":
            self.value2=self.data.GetValue(self.dev2)
        self.bool=compDict[self.comp](self.value1,self.value2)
    
    def toStr(self):
        string = "Cond = {{"
        string += "\n\t\t1."+str(self.dev1)+" = "+str(self.value1)
        string += "\n\t\t2."+str(self.dev2)+" = "+str(self.value2)
        string += "\n\t\tcomp = "+self.comp
        string += "\n\t\tBool = "+ str(self.bool)
        string += "\n\t}}\n"
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
            if self.falseValue!=-1:
                self.data.SendValue(self.deviceName,self.falseValue)
            ###
        ###
    ###
    def toStr(self):
        string = "Effect = {{"
        string += "\n\t\tDevice Name = "+self.deviceName
        string += "\n\t\ttrueValue = "+ str(self.trueValue)
        string += "\n\t\tfalseValue = "+ str(self.falseValue)
        string += "\n\t\tCurrentValue = "+ str(self.data.GetValue(self.deviceName))
        string += "\n\t}}\n"
        return string
    ###
###



class Cond(object):
    def __init__(self,name,refresh,desc):
        self.name = name
        self.refresh=refresh #sekundy
        self.desc = desc
        self.small=dict() #slownik malych warunkow
        self.effect=dict() #slownik efektow
        self.bool=False
        debug.Log('Cond: Object Added {}, {}, {}'.format(name,refresh,desc))
    ###
    def addEffec(self,data,name,deviceName,trueValue,falseValue):
        self.effect[name]=(Effect(data,deviceName,trueValue,falseValue))
        debug.Log('{}: Effect Added {}, {}, {}, {}'.format(self.name,name,deviceName,trueValue,falseValue))
    ###
    def addSmall(self,data,name,dev1,dev2,comp,value1=0,value2=0):
        self.small[name]=(SmallCond(data,dev1,value1,dev2,value2,comp))
        debug.Log('{}: Cond Added {}, {}, {}, {}, {}, {}'.format(self.name,name,dev1,value1,dev2,value2,comp))
    ###
    def Refresh(self,count,interval):
        if count%(self.refresh//interval)!=0:
            return
        tempBool=0 #Liczy true w small.bool
        for i in self.small.values():
            i.Refresh()
            if i.bool:
                tempBool+=1
            ###
        ###
        if tempBool==len(self.small):
            if self.bool==False:
                debug.Log('{}: bool To True'.format(self.name))
            self.bool=True
        else:
            if self.bool==False:
                debug.Log('{}: bool To False'.format(self.name))
            self.bool=False
        ###
        for i in self.effect.values():
            i.Refresh(self.bool)
        ###
    def toStr(self):
        string = "Condition = {{"
        string += "\n\tname = "+self.name
        string += "\n\tDesc = "+ self.desc
        string += "\n\tRefresh = "+str(self.refresh)
        string += "\n\tBool = "+str(self.bool)
        for i,j in self.small.items():
            string+="\n\t"+i+" "   
            string+=j.toStr()
        ###
        for i,j in self.effect.items():
            string+="\n\t"+i+" "   
            string+=j.toStr()
        ###
        string += "\n}}\n"
        return string
    ###
###
