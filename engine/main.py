import pickle
import os
import time
import os.path
import debug
import data as DATA
import threading
import serv

isActive=True
isExit=False

def Refresh(data):
    data.timeCount=0
    while not isExit:
        
        if isActive:
            data.Refresh()
            data.dicConst["timeCount"]+=data.dicConst["interval"]
            with open("data.txt","w") as file:
                file.write(data.DataToStr())
            if data.dicConst["timeCount"]>=3600:
                data.dicConst["timeCount"]=0

        time.sleep(data.dicConst["interval"])
        ###
    ###
###


def Init():
    #if os.path.isfile("save.p"):
    #    data=pickle.load( open( "save.p", "rb" ) )
    #else:
    data=DATA.Data()

    isActive=True
    isExit=False
    #start RefreshLoop
    refresh_handler=threading.Thread(target=Refresh,args=(data,))
    refresh_handler.daemon=True
    refresh_handler.start()
    #start server
    server_handler=threading.Thread(target=serv.start,args=(data,2120,))
    server_handler.daemon=True
    server_handler.start()
    return data, refresh_handler,server_handler

def Kill(data,refresh_handler,server_handler):
    #Save data to file
    refresh_handler.join()
    pickle.dump( data, open( "save.p", "wb" ) )
    
###
def main(Const):
    data,refresh_handler,server_handler=Init()
    

    

    Kill(data,refresh_handler,server_handler)
    return
###  
    
print("s")
if __name__ == "__main__":
    # execute only if run as a script
    main("aaa")
    pass
