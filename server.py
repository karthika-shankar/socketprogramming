import socket
import threading
import random

players = {}  
lock = threading.Lock()

def handle_client(conn, addr):
    global players
    conn.send("Welcome to the Dice Game! \n".encode())

   
    msg = conn.recv(1024).decode().strip()
    if msg.lower() == "roll":
        dice_roll = random.randint(1, 6)  
        with lock:
            players[addr] = dice_roll
        conn.send(f"You rolled a {dice_roll}! Waiting for others...\n".encode())
    else:
        conn.send("Invalid command. Type 'roll' to play.\n".encode())
    
    conn.close()

def start_server():
    server = socket.socket()
    server.bind(("localhost", 12345))
    server.listen(5)
    print("Server started. Waiting for players...")

    while len(players) < 2: 
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

   
    winner = max(players, key=players.get)
    print(f"\nGame Over! Winner is {winner} with a roll of {players[winner]}!")

    server.close()

start_server()
