import socket

s = socket.socket()

print("Socket Created")

s.bind(('localhost', 4321))
s.listen(3)

print('waiting for connections')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with", addr, name)
    c.send(bytes("Welcome to Manipal", 'utf-8'))
    c.close()