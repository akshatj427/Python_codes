import socket
import threading
import os
from PIL import Image
from PIL import ImageGrab
import time
import numpy

import pickle


def Main():
    host = '127.0.0.1'
    #host = '192.168.0.7'
    port = 5008
    sock = socket.socket()
    sock.connect((host, port))
    #############

    sd = os.getcwd()

    img = ImageGrab.grab()
    imgarr = numpy.asarray(img)
    #print(imgarr)
    img2 = Image.fromarray(numpy.uint8(imgarr))
    sec = time.time()
    lc = time.localtime(sec)
    t = time.asctime(lc)
    print(t)
    saveas = os.path.join(sd, 'Screen_shot' + '.jpg')

    #####img.save(saveas)

    img2.save(saveas)
    print("run successful")

    filename = 'Screen_shot.jpg'
    ######
    sock.send(filename)
    ######
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        #userResponse = sock.recv(1024)
        #if userResponse[:2] == 'OK':
        with open(filename, 'rb') as f:
            bytesToSend = f.read(1024)
            sock.send(bytesToSend)
            while bytesToSend != "":
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
    else:
        sock.send("ERR ")

    sock.close()

if __name__ == '__main__':
    Main()
