import debug
import connector



class Device(object):
    def __init__(self,name,pos,desc,typeName,refreshTime,isRec):
        
        self.name = name
        self.pos=pos
        self.desc = desc
        self.typeName=typeName
        self.value=0
        self.trueValue=-1
        self.isRec=isRec
        self.refreshTime=refreshTime #sekundy

        debug.Log('Device: Object Added {}, {}, {}, {}, {}, {}'.format(name,pos,desc,typeName,refreshTime,isRec))
    ###
    def toStr(self):
        string = "Device = {{"
        string += "\n\tname = "+self.name
        string += "\n\tpos = "+ str(self.pos)
        string += "\n\tdesc = "+self.desc
        string += "\n\ttypeName = "+self.typeName #Dev ip !!!
        string += "\n\tvalue = "+str(self.value)
        string += "\n\ttrueValue = "+ str(self.trueValue)
        string += "\n\trefreshTime = "+str(self.refreshTime)
        string += "\n\tisRec = "+str(self.isRec)
        string += "\n}}\n"
        return string

    ###    
    def GetDevValue(self):
        #TODO
        self.value=connector.GetValue(self.typeName)
        debug.Log('{}: GetDevValue {} '.format(self.name,self.value))
        pass
    ###
    def SetDevValue(self):
        #TODO
        connector.SendValue(self.typeName, self.value)
        debug.Log('{}: SetDevValue {} '.format(self.name,self.value))
        pass
    ###

    def Refresh(self,count,interval):
        if count%(self.refreshTime//interval)!=0:
            return
        if self.isRec:
            if self.value!=self.trueValue:
                self.trueValue=self.value
                self.SetDevValue()
                return
            pass
        pass
        self.GetDevValue()
    

class Value(object):
    def __init__(self,name,pos,desc,value):
        self.name = name
        self.pos=pos
        self.desc = desc
        self.value=value

    def Refresh(self,count,interval):
        pass

    def toStr(self):
        string = "Value = {{"
        string += "\n\tname = "+self.name
        string += "\n\tpos = "+ str(self.pos)
        string += "\n\tdesc = "+self.desc
        string += "\n\tvalue = "+str(self.value)
        string += "\n}}\n"
        return string

    ###    

