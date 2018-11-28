import debug
import threading

class Types(object):
    def __init__(self,name,desc,isRec):
        self.name = name
        self.desc = desc
        self.isRec=isRec #Is Receiver or Sender
        debug.Log('Types: Object Added {}, {}, {},'.format(self.name,desc,isRec))
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

def me(a):
    a.name="www"

def ma(a):
    a.name="gggg"

def main():
    a=Types("a","a",0)
    ma(a)
    print(a.name)
    w=threading.Thread(target=me,args=(a,))
    w.start()
    w.join()
    print(a.name)

main()