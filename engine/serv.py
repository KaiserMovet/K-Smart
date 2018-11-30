import socket
import threading
import pickle
import data as DATA

def inter(client_socket,data,mess):
    print("Otrzymano slownik")
    if mess["exe"]=="addDev":
        data.addDev(mess["name"],mess["desc"],mess["typeName"],mess["refreshTime"],mess["isRec"])   
    if mess["exe"]=="addCon":
        data.addCond(mess["name"],mess["refreshTime"],mess["desc"])   
    if mess["exe"]=="addSmall":
        data.addSmall(mess["conName"],mess["smallName"],mess["dev1"],mess["dev2"],mess["comp"],mess["value1"],mess["value2"])   
    if mess["exe"]=="addEffect":
        data.addEffect(mess["conName"],mess["effectName"],mess["deviceName"],mess["trueValue"],mess["falseValue"])     
    if mess["exe"]=="ChangePos":
        data.ChangePos(mess["name"],mess["pos"])
    if mess["exe"]=="addValue":
        data.addValue(mess["name"],mess["pos"],mess["desc"],mess["value"])   
    

###

def handle_client_connection(client_socket,data,address):
    request = client_socket.recv(1024)
    mess=pickle.loads(request)
    if mess == "Refresh":
        a=data.toDict()
        client_socket.send(pickle.dumps(a))
        
    else:
        inter(client_socket,data,mess)
        client_socket.send(pickle.dumps("Dzieki"))
    client_socket.close()
    print('Closed connection from {}:{}'.format(address[0], address[1]))


def start(data,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(5)  # max backlog of connections



    while True:
        client_sock, address = server.accept()
        print('Accepted connection from {}:{}'.format(address[0], address[1]))
        client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client_sock,data,address,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        )
        client_handler.start()

###