import pickle
import os
import time
import os.path
import signal
import sys
import debug
import data as DATA
import threading
import serv

isActive=True
isExit=False

def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        print('Program will exit soon')
        time.sleep(1)
        print("Press Ctrl+C again to exit immediately")
        signal.signal(signal.SIGINT, original_sigint)
        global isExit
        isExit=True
        
def Refresh(data):
    data.timeCount=0
    while not isExit:
        if isActive:
            data.isUpdating=True
            data.Refresh()
            data.dicConst["timeCount"]+=data.dicConst["interval"]
            data.isUpdating=False
            with open("data.txt","w") as file:
                file.write(data.DataToStr())
            if data.dicConst["timeCount"]>=3600:
                data.dicConst["timeCount"]=0

        time.sleep(data.dicConst["interval"])
        #time.sleep(1)
        ###
    ###
###


def Init():
    if os.path.isfile("save.p"):
        data=pickle.load( open( "save.p", "rb" ) )
    else:
    	data=DATA.Data()

    isActive=True
    isExit=False
    global original_sigint
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal_handler)
    #start RefreshLoop
    refresh_handler=threading.Thread(target=Refresh,args=(data,))
    refresh_handler.daemon=True
    refresh_handler.start()
    #start server
    server_handler=threading.Thread(target=serv.start,args=(data,2000,))
    server_handler.daemon=True
    server_handler.start()
    data.cam.PrepareFiles()
    data.cam.Start()
    return data, refresh_handler,server_handler

def Kill(data,refresh_handler,server_handler):
    #Save data to file
    refresh_handler.join()
    data.cam.Kill()
    print(222)
    pickle.dump( data, open( "save.p", "wb" ) )
    sys.exit()
    
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
