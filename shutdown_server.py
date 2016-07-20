from Tkinter import *
import os
import socket
import pickle

root = Tk()

def createserver(event):
    s = socket.socket()
    host = socket.gethostname()
    port = 5010
    s.bind((host, port))
    print("server started")
    s.listen(5)
    while True:
        c, addr = s.accept()
        print('Got connection from ', addr)
        c.send("thank you for connecting")
        c.send("shutdown")
        #receiving list of files
        #data = c.recv(4096)
        #data1 = pickle.loads(data)   # encode
        #print(data1)
        c.close()
   
button_1 = Button(root, text="create server")
button_1.bind("<Button-1>", createserver)
button_1.pack()

root.mainloop()
