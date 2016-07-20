import socket
host = ''
port = 5007
s = socket.socket()
s.connect((host, port))
while True:
    s.send("Hai")
