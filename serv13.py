import socket
import threading
from Tkinter import *

s = socket.socket()
# SO_REUSEADDR is used to make the port reusable
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 5007

s.bind((host, port))
s.listen(5)

fw = open('sample1.txt', 'w')
fw.write('A 300\n')
fw.write('B 200\n')
fw.write('C 100\n')
fw.write('D 400\n')
fw.close()


def worker():

    c, addr = s.accept()
    print("connection from:", addr)
    #root = Tk()
    #TheLabel = Label(root, text="connection from:" + str(addr))
    #TheLabel.pack()
    #TheLabel = Label(root, text="sending:" + str(data))
    #TheLabel.pack()
    #root.mainloop()

    c.send('1 2 3 4')

    #choice sent by server

    data = c.recv(1024)
    print("from connected user", str(data))
    #c.send(data)

    if str(data) == '3':

        with open('sample1.txt') as f:
            lines = f.readlines()

        print(lines)
        data1 = []

        for x in range(len(lines)):
            text = lines[x].split()
            data1.append(text)
        for i in range(len(data1)):
            for j in range(len(data1)-1):
                if data1[j][1] > data1[j+1][1]:
                    temp = data1[j]
                    data1[j] = data1[j+1]
                    data1[j+1] = temp
        print(data1)
    if str(data) == '1':
        fw = open('sample1.txt', 'a')
        fw.write('E 500\n')
        fw.close()
    c.close()
    #root = Tk()
    #TheLabel = Label(root, text="connection from:" + str(addr))
    #TheLabel.pack()
    #root.mainloop()

z = 0

for z in range(5):
    t = threading.Thread(target=worker)
    t.start()



