import socket
import time

host= socket.gethostname()
port=9999
serversocket=socket.socket()

serversocket.bind((host,port))

serversocket.listen(5)
while True:
    clientsocket, addr=serversocket.accept()

    print("Got a connection from ", str(addr))
    currentTime=time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()



