import socket
import pickle
HEADERSIZE=10

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.connect((socket.gethostname(),1234))
s.connect(("192.168.29.37",1234))

##1
##msg=s.recv(1024)
##print(msg.decode("utf-8"))

##2
##while True:
##    msg=s.recv(8)
##    print(msg.decode("utf-8"))

##3
##full_msg=''
##while True:
##    msg=s.recv(8)
##    if len(msg)<=0:
##        break
##    full_msg+=msg.decode("utf-8")
##
##print(full_msg)


##4
##while True:
##    full_msg=''
##    new_msg=True
##    while True:
##        msg=s.recv(16)
##        if new_msg:
##            print(f"new message length: {msg[:HEADERSIZE]}")
##            msglen=int(msg[:HEADERSIZE])
##            new_msg=False
##            
##        full_msg+=msg.decode("utf-8")
##
##        if len(full_msg)-HEADERSIZE ==msglen:
##            print("full msg recvd")
##            print(full_msg[HEADERSIZE:])
##            new_msg=True
##            full_msg=""
##    print(full_msg)


##5
while True:
    full_msg=b''
    new_msg=True
    while True:
        msg=s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen=int(msg[:HEADERSIZE])
            new_msg=False
            
        full_msg+=msg

        if len(full_msg)-HEADERSIZE ==msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            d=pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            new_msg=True
            full_msg=b""
    print(full_msg)
