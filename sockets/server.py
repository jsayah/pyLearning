import socket
import time
import pickle

HEADERSIZE = 10 #set header size

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is IPV4 and SOCK_STREAM is TCP
s.bind((socket.gethostname(), 1234)) #This binds the socket to the localhost in this case on port 1234
s.listen(5) #Set the queue size to 5

while True:
    clientsocket, address = s.accept() #binds the incoming information to clientsocket and address is the IP
    print(f'Connection from {address} has been established!')

    d = {1: 'Hey', 2: 'There'}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg #Typed header that will show the length of the incoming message.

    clientsocket.send(msg) #Gives instructions to encode a response. In this case as utf-8

