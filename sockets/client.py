import socket
import pickle
#SOCKET MUST BE PRESENT IN BOTH
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is IPV4 and SOCK_STREAM is TCP
s.connect((socket.gethostname(), 1234))

while True:

    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)#Recieves the clientsocket.send() abd sets the data buffer
        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')#will get length of message by calling the static header for the info
            msglen = int(msg[:HEADERSIZE]) #converts the header to int len
            new_msg = False


        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen: #calculates the message length to check if the message is fully recieved
            print('full msg recvd')
            print(full_msg[HEADERSIZE:])

            d = pickle.loads(full_msg[HEADERSIZE:])#pickle decoding the utf-8 stream
            print(d)

            new_msg = True
            full_msg = b'' #b used to convert to bytes
    print(full_msg)#This decodes the utf-8 bytestream sent via clientsocket.send()