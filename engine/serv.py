import socket
import threading
import pickle
import data as DATA
def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    a=pickle.loads(request)
    print(a)
    client_socket.send('ACK!'.encode())
    client_socket.close()

def start(data,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 2131))
    server.listen(5)  # max backlog of connections



    while True:
        client_sock, address = server.accept()
        print('Accepted connection from {}:{}'.format(address[0], address[1]))
        client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        )
        client_handler.start()

###