import socket, pickle

def insertionSort(data1):
   for index in range(1, len(data1)):

     currentvalue = data1[index]
     position = index

     while position > 0 and data1[position-1] > currentvalue:
         data1[position] = data1[position-1]
         position = position-1

     data1[position] = currentvalue

#alist = [54,26,93,17,77,31,44,55,20]
#insertionSort(alist)
#print(alist)



HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(4096)
    data1 = pickle.loads(data)   # decode
    print("received", data1)
    #data1.append(11)
    #data1[0] = 777
    #assc = sorted(data1)     ## sorting

    insertionSort(data1)

    #### File
    fw = open('data1.txt', 'w')
    fw.write(str(data1))
    fw.close()
    ####
    print("sending:", data1)
    if not data1:
        break
    data = pickle.dumps(data1)    # encode
    conn.send(data)
conn.close()
