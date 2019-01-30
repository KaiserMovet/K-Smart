import subprocess


def GetValue(ip):
        value=0
        #output = subprocess.check_output("wget -qO- "+ip, shell=True).decode("utf-8") 
        output = subprocess.check_output("cat czujnik", shell=True).decode("utf-8")
        print("Otrzymano wartosc: "+str(output))
        return output
    ###

def SendValue(ip, val):
        subprocess.check_output("echo "+str(val)+" > czujnik", shell=True).decode("utf-8")
        print("Wyslano wartosc: "+str(val))
        return


def main():
    typeName="192.168.43.158"     #args=self.typeName.split(":")
    value=7

if __name__ == "__main__":
    main()

