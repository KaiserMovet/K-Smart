import sys
import pickle

dic=dict()

class Types(object):
    yaml_tag=u'!Types'
    def __init__(self):
        self.name = "None"
        self.maxValue = 255
        self.desc = "Some Device Type"
        self.isRec="false"#Is Receiver or Sender
    
    

def Load():
    dic = pickle.load( open( "types.p", "rb" ) )
    
###
def Save():
    pickle.dump( dic, open( "types.p", "wb" ) )
###




