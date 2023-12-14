import socket

host=socket.gethostname()
ip=socket.gethostbyname(host)
port=12345

s=socket.socket()
s.connect((host,port))

send_data=host+ ","+ip

s.send(send_data.encode())
data=s.recv(1024).decode()
d=data.split(",")
s.close()

print("server host : ",d[0])
print("server ip : ",d[1])