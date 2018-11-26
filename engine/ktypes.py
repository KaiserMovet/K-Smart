import debug


class Types(object):
    def __init__(self,name,desc,isRec):
        self.name = name
        self.desc = desc
        self.isRec=isRec #Is Receiver or Sender
        debug.Log('Types: Object Added {} {} {}'.format(self.name,desc,isRec))
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
