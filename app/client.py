import socket
import pickle
import app.data

def send(dane):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 2021))
    a=pickle.dumps( dane )
    client.send(a)
    response = client.recv(4096)
    return pickle.loads(response)

def test(count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    # client.connect((target, port))
    client.connect(('localhost', 2121))

    # send some data (in this case a HTTP GET request)
    mess=dict()
    if count == 1:
        mess["exe"]="addDev"
        mess["name"]="Ala"
        mess["pos"]=(1,1)
        mess["desc"]="Swiatlo"
        mess["typeName"]="Swiatlo"
        mess["refreshTime"]=15
        mess["isRec"]=1
    if count == 2:
        mess["exe"]="addDev"
        mess["name"]="Ola"
        mess["pos"]=(1,1)
        mess["desc"]="Czujnik"
        mess["typeName"]="Czujnik"
        mess["refreshTime"]=15
        mess["isRec"]=0
    if count == 3:
        mess["exe"]="addCon"
        mess["name"]="War1"
        mess["refreshTime"]=15
        mess["desc"]="Warunek ein"
    if count == 4:
        mess["exe"]="addSmall"
        mess["conName"]="War1"
        mess["smallName"]="Malu1"
        mess["dev1"]="Value"
        mess["value1"]=0
        mess["dev2"]="Ola"
        mess["value2"]=0
        mess["comp"]="equal" 
    if count == 5:
        mess["exe"]="addEffect"
        mess["conName"]="War1"
        mess["effectName"]="Ef1"
        mess["deviceName"]="Ala"
        mess["trueValue"]=100
        mess["falseValue"]=200

    if count == 6:
        mess["exe"]="addSmall"
        mess["conName"]="War1"
        mess["smallName"]="Malu1"
        mess["dev1"]="Value"
        mess["value1"]=10
        mess["dev2"]="Ola"
        mess["value2"]=0
        mess["comp"]="equal" 





    # receive the response data (4096 is recommended buffer size)
    

    print(response)
###
def refresh():
    return send("Refresh")
