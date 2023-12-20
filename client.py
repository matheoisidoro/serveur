import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5004
BUFFER_SIZE = 1024 #default
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode(str))
data = s.recv(BUFFER_SIZE)
s.close()
print ("received data:", data)