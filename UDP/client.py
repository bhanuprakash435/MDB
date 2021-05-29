import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter your name")
client_socket.sendto(message.encode('utf-8'), ('localhost', 4321))
data, address = client_socket.recvfrom(1234)
print(str(data))
client_socket.close()
