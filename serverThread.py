import socket, threading
host = ''
port = 5007
s = socket.socket()
s.bind((host, port))
s.listen(5)


def handleclient(conn):
    for i in range(5):
        data = conn.recv(1024)
        print(data)
        if not data:
            break
while True:
    conn, addr = s.accept()
    print('connected to ', addr)
    #threading._start_new_thread(handleclient, (conn,))
    t = threading.Thread(target=handleclient, args=(conn,))
    t.start()

