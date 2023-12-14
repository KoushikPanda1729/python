import socket

host= socket.gethostname()
port=9999


s=socket.socket()

s.connect((host,port))
time=s.recv(1024)
s.close()

print("the time got from the sever is--------- ",time.decode('ascii'))



