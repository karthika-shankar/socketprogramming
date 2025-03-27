import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
server_address = ("localhost", 9999)  

move = input("Enter your move (rock, paper, scissors): ")  
client.sendto(move.encode(), server_address)  

response, _ = client.recvfrom(1024)  
print(response.decode())

client.close()
