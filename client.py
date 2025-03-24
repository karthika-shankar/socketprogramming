import socket

client = socket.socket()
client.connect(("localhost", 12345))
print(client.recv(1024).decode())
client.send("roll".encode())
print(client.recv(1024).decode())
client.close()
