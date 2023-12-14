import socket

host=socket.gethostname()
ip=socket.gethostbyname(host)
port=12345

s=socket.socket()
s.bind((host, port))
s.listen(1)

conn, addr=s.accept()
print("Connected by ", addr)

while True:
    data=conn.recv(1024).decode()
    d=data.split(",")
    if not data:
        break
    print("Client host ",d[0])
    print("Client ip ", d[1])

    send_data=host + "," + ip
    conn.send(send_data.encode())
    conn.close()