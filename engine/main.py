import pickle
import os
import time
import os.path
import debug
import data as DATA
import multiprocessing
import serv

def Init():
    #if os.path.isfile("save.p"):
    #    data=pickle.load( open( "save.p", "rb" ) )
    #else:
    data=DATA.Data()
    ###
    #start server
    server_handler=multiprocessing.Process(target=serv.start,args=(data,2131))
    server_handler.daemon=True
    server_handler.start()
    return data, server_handler

def Kill(data,server_handler):
    #Save data to file
    pickle.dump( data, open( "save.p", "wb" ) )
    
def Testy(data):
    data.addType("Swiatlo","zarowka led",1)
    data.addDev(data,"Swiatlo 1",(1,1),"Swiatlo w duzym pokoju","Swiatlo",60)
    data.printTyp()
    data.printDev()
###
def main(Const):
    data,server_handler=Init()
    
    Testy(data)

    server_handler=threading.Thread(target=serv.start,args=(data,2131))

    Kill(data,server_handler)
    return
###  
    
print("s")
if __name__ == "__main__":
    # execute only if run as a script
    main("aaa")
    pass
