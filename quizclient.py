import socket, pickle

HOST = 'localhost'
PORT = 5006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

lists = []

class Integers:
    def __init__(self, name, lists ):
        self.name = name
        self.lists = lists

List1 = Integers('List1', [1, 3, 5, 7])
List2 = Integers('List2', [2, 4, 6, 8])

print(List1.lists)

data_string1 = pickle.dumps(List1.lists)
data_string2 = pickle.dumps(List2.lists)
s.send(data_string1)
print("sending")
s.send(data_string2)
print("sending")

data = s.recv(1024)
data_arr = pickle.loads(data)
s.close()
print('Received', repr(data_arr))
