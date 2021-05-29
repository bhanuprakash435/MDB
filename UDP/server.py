import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 4321))


while True:
    data, address = sock.recvfrom(1234)
    print(str(data))
    #message = bytes("Welcome to MSIS").encoding('utf-8')
    #sock.sendto(message, address)
    sock.sendto(bytes("Welcome to Manipal", 'utf-8'), address)    
    