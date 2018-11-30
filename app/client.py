import socket
import pickle

def sendTo(dane):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 2000))
    a=pickle.dumps( dane )
    client.send(a)
    response = client.recv(4096)
    return pickle.loads(response)


def refresh():
    return sendTo("Refresh")
