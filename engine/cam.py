import os
import glob
import pickle
import subprocess
import time
import signal



class Cam(object):
    def __init__(self):
        self.cams=list()# (port,name)
        self.subproc=0
    #Add camera to list and create conf files
    
    def Start(self):
        self.subproc=0
        #TODO
        #self.subproc=subprocess.Popen("sudo motion",shell=True, preexec_fn=os.setsid)
    def Kill(self):
        if self.subproc==0:
            return
        os.killpg(os.getpgid(self.subproc.pid), signal.SIGTERM)
        while self.subproc.poll()==None:
            time.sleep(1)
        self.subproc=0
        return
    def Restart(self):
        self.Kill()
        self.Start() 
    
    def AddCam(self,devName):
        self.cams.append(0,devName)
        self.PrepareFiles()
    def RemoveCam(self,devName):
        for i in self.cams:
            if devName==i[1]:
                self.cams.remove(i)
                break
        self.PrepareFiles()


    def __PrepareCam__(self,devName):

        port=8081
        while port in [item[0] for item in self.cams]:
            port+=1

        index=len(self.cams)
        line1="videodevice "+devName+"\n"
        line2="stream_port "+str(port)
        with open('/etc/motion/thread'+str(index)+'.conf','w') as f:
            f.writelines((line1,line2))
        self.cams.append((port,devName))

    def PrepareFiles(self):
        for filename in glob.glob("/etc/motion/thread*.conf"):
            os.remove(filename) 
        oldCams=self.cams.copy()
        self.cams=list()
        for name in [item[1] for item in oldCams]:
            self.__PrepareCam__(name)
        if self.subproc!=0:
            self.Restart()

    def Count(self):
        index=len(self.cams)
        if index==0:
            index=1
        return index

