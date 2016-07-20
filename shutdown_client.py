from Tkinter import *
import os
import socket
import pickle

root = Tk()


def createclient(event):
    s = socket.socket()
    #host = '192.168.43.10'
    host = socket.gethostname()
    port = 5010
    s.connect((host, port))
    print("conn established")
    print (s.recv(1024))
    data = s.recv(1024)
    if data == "shutdown":
        print("shutting down")
        #os.system("cmd")
        os.system("shutdown /s")
        #cwd = os.getcwd()
        #listdir = os.listdir(cwd)
        #print(listdir)
        #data_string = pickle.dumps(listdir)
        #s.send(data_string)
   
button_1 = Button(root, text="create client")
button_1.bind("<Button-1>", createclient)
button_1.pack()

root.mainloop()
