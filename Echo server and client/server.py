import socket

host=''
port=12345

s=socket.socket()
s.bind((host,port))
s.listen(1)

conn, addr=s.accept()

print("Connected by ",addr)

while True:
    data=conn.recv(1024)
    if not data:
        break
    conn.send(data)
conn.close()