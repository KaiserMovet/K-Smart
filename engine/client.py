import socket
import pickle
hostname, sld, tld, port = 'www', 'integralist', 'co.uk', 80
target = '{}.{}.{}'.format(hostname, sld, tld)

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect(('localhost', 2131))

# send some data (in this case a HTTP GET request)
message=dict()
message[0]="Aa"
message[1]="b"
a=pickle.dumps( message )

client.send(a)



# receive the response data (4096 is recommended buffer size)
response = client.recv(4096)

print(response)