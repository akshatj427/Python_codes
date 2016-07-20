from PyQt4 import QtCore, QtGui
import socket
import threading
import os
import pickle

def RetrFile2(name, s):

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



def RetrFile(name, sock):

    #############
    cwd = os.getcwd()
    listdir = os.listdir(cwd)
    print(listdir)
    data_string = pickle.dumps(listdir)
    sock.send(data_string)
    #############
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR ")

    sock.close()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(108, 128, 255);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 129, 181, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)


        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 401, 61))


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def File_Sharing(self):
        print("button clicked")
        host = '127.0.0.1'
        port = 5006

        s = socket.socket()
        s.bind((host, port))

        s.listen(5)


        print("Server Started.")
        #MainWindow.update()



        while True:
            c, addr = s.accept()
            print("client connedted ip:<" + str(addr) + ">")
            ############

            ####################
            t = threading.Thread(target=RetrFile, args=("RetrThread", c))
            t.start()

        s.close()


    def Shutdown(self):

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

    def Screenshot(self):

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
        t = threading.Thread(target=RetrFile2, args=("RetrThread", c))
        t.start()

    def Restart(self):
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

    def logoff(self):
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


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        self.pushButton_2.setText("File_Sharing ")
        self.pushButton_3.setText("Shutdown")
        self.pushButton_5.setText("Restart")
        self.pushButton_4.setText("LogOff")
        self.pushButton.setText("Screenshot")
        #self.plainTextEdit.setPlainText("MainWindow")

        #input_var = ""

        #self.plainTextEdit.appendPlainText(input_var)

        #print(input_var)

        #mytext = self.plainTextEdit.toPlainText()
        #print(mytext)

        self.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Remote Desktop Administrator</span></p></body></html>")

        self.pushButton_2.clicked.connect(self.File_Sharing)
        self.pushButton_3.clicked.connect(self.Shutdown)
        self.pushButton_5.clicked.connect(self.Restart)
        self.pushButton_4.clicked.connect(self.logoff)
        self.pushButton.clicked.connect(self.Screenshot)


from PyQt4 import QtDeclarative

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

