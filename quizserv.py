import socket, pickle

HOST = 'localhost'
PORT = 5006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
conn, addr = s.accept()
print('Connected by', addr)
work = []
while 1:
    data1 = conn.recv(2048)
    print("receiving")
    data2 = conn.recv(2048)
    print("receiving")
    data11 = pickle.loads(data1)   # decode
    data21 = pickle.loads(data2)
    print(data11)
    print(data21)

    for x in range(4):
        work.append(data11[x])
        work.append(data21[x])

    print("sending:", work)
    datase = pickle.dumps(work)    # encode
    conn.send(datase)


conn.close()
