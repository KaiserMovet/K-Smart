


class Types(object):
    def __init__(self,name,desc,isRec):
        self.name = name
        self.desc = desc
        self.isRec=isRec #Is Receiver or Sender
    ###
    def toStr(self):
        string = "Type = {{"
        string += "\n\tname = "+self.name
        string += "\n\tdesc = "+self.desc
        string += "\n\tisRec = "+str(self.isRec)
        string += "\n}}"
        return string
    ###
pass
