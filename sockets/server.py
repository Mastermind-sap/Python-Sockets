import socket
import time
import pickle
HEADERSIZE=10

##s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.bind((socket.gethostname(),1234))
##s.listen(5)
##
##while True:
##    clientsocket,address=s.accept()
##    print(f"Connection from {address} has been established!")
##    msg="Welcome to the server!"
##    msg=f"{len(msg):<{HEADERSIZE}}"+msg
##    clientsocket.send(bytes(msg,"utf-8"))
##    #clientsocket.close()
##    while True:
##        time.sleep(3)
##        msg=f"The time is! {time.time()}"
##        msg=f"{len(msg):<{HEADERSIZE}}"+msg
##        clientsocket.send(bytes(msg,"utf-8"))
##


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.bind((socket.gethostname(),1234))
s.bind(("192.168.29.37",1234))
s.listen(5)

while True:
    clientsocket,address=s.accept()
    print(f"Connection from {address} has been established!")
    d={1:"hey",2:"there"}
    msg=pickle.dumps(d)
    #print(msg)

    msg=bytes(f"{len(msg):<{HEADERSIZE}}","utf-8")+msg
    clientsocket.send(msg)
    #clientsocket.close()
    

