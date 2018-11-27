import debug




class Device(object):
    def __init__(self,data,name,pos,desc,typeName,refreshTime):
        self.data=data
        self.name = name
        self.pos=pos
        self.desc = desc
        self.typeName=typeName
        self.value=0
        self.trueValue=-1
        self.type=data.dicTyp[typeName]
        self.refreshTime=refreshTime #sekundy
        debug.Log('Device: Object Added {}, {}, {}, {}, {}'.format(name,pos,desc,typeName,refreshTime))
    ###
    def toStr(self):
        string = "Device = {{"
        string += "\n\tname = "+self.name
        string += "\n\tpos = "+ str(self.pos)
        string += "\n\tdesc = "+self.desc
        string += "\n\ttypeName = "+self.typeName
        string += "\n\tvalue = "+str(self.value)
        string += "\n\ttrueValue = "+ str(self.trueValue)
        string += "\n\trefreshTime = "+str(self.refreshTime)
        string += "\n}}"
        return string

    ###    
    def GetDevValue(self):
        #TODO
        debug.Log('{}: GetDevValue {} '.format(self.name,self.value))
        pass
    ###
    def SetDevValue(self):
        #TODO
        debug.Log('{}: SetDevValue {} '.format(self.name,self.value))
        pass
    ###

    def refresh(self):
        if self.type.isRec:
            if self.value!=self.trueValue:
                self.trueValue=self.value
                self.SetDevValue()
                return
            pass
        pass
        self.GetDevValue()
    





