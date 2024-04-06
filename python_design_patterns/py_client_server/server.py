""" Simple Python Server 

1. Creates a new socket for a server
2. Binds it to a port and starts listening for incoming connections 
"""
import socket 
import os 
# get ip and hostname
HOSTNAME = socket.gethostname()
IP_ADDR = socket.gethostbyname(socket.gethostname())
PORT_ADDR = 1243 # pick any free port 
print(f"Server at {HOSTNAME}:{IP_ADDR}")

# create socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to port and start listening
server_socket.bind(('0.0.0.0', PORT_ADDR))
server_socket.listen()

# a blocking call; program stops until a request to connect
# from a client is received.
client_socket, client_address = server_socket.accept()

while True:
    print(f"Connected to {client_socket}/{client_address}")
    msg = f"You are connected"
    client_socket.send(msg.encode('utf-8'))
    break