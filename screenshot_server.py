import socket
import pickle
import threading

#def Main():


def RetrFile(name, s):

    filename = s.recv(1024)
    data = s.recv(1024)
    if data[:6] == 'EXISTS':
        filesize = long(data[6:])
        #filesize = long(data[6:])
        print("File receiving " + "File size:" + str(filesize) + "  starting download")

    f = open('new1_'+filename, 'wb')
    data = s.recv(1024)
    totalRecv = len(data)
    f.write(data)
    while totalRecv < filesize:
        data = s.recv(1024)
        totalRecv += len(data)
        f.write(data)
        print "{0:.2f}".format((totalRecv/float(filesize))*100) + "% Done"
    print "Download Complete!"
    f.close()
    s.close()


def Main():
    host = '127.0.0.1'
    port = 5008
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    #c, addr = s.accept()

    print "Server Started."
    #while True:
    c, addr = s.accept()
    print "client connedted ip:<" + str(addr) + ">"
    ############

    ####################
    t = threading.Thread(target=RetrFile, args=("RetrThread", c))
    t.start()

    #s.close()

if __name__ == '__main__':
    Main()
