import socket

s = socket.socket()

host = socket.gethostname()
#host = '192.168.0.9'
port = 5007

s.connect((host, port))

#s.send()
data = s.recv(1024)
print("data received is:", data)

choice = []
choice = data.split()
print(choice)

ip = raw_input('val')

if str(ip) == choice[2]:
    s.send('3')
if str(ip) == choice[0]:
    s.send('1')


s.close()
