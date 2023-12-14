import socket

host=socket.gethostname()
port=12345

s=socket.socket()
s.connect((host,port))

s.send("Hello ".encode())
data=s.recv(1024)
s.close()
print("Received", data.decode())