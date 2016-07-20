import socket

s = socket.socket()

host = socket.gethostname()
#host = '192.168.0.9'
port = 5007

s.connect((host, port))

#s.send()

print("choices are:")

choice = ["1.full moon", "2.New Moon", "3.Solar Eclipse"]

print(choice)

ip = raw_input('val')

if str(ip) == "1":
    s.send('1')
if str(ip) == "2":
    s.send('2')
if str(ip) == "3":
    s.send('3')


s.close()