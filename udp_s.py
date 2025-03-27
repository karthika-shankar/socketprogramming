import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
server.bind(("localhost", 9999))  

print("UDP Rock-Paper-Scissors Server started. Waiting for players...")

while True:
    data, addr = server.recvfrom(1024)  
    player_move = data.decode().strip().lower()

    if player_move not in ["rock", "paper", "scissors"]:
        server.sendto("Invalid move! Choose rock, paper, or scissors.".encode(), addr)
        continue

    server_move = random.choice(["rock", "paper", "scissors"])  

    win_conditions = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if player_move == server_move:
        result = f"Server chose {server_move}. It's a tie!"
    elif win_conditions[player_move] == server_move:
        result = f"Server chose {server_move}. You win!"
    else:
        result = f"Server chose {server_move}. You lose!"

    server.sendto(result.encode(), addr)  