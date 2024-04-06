""" Simple Python Client 

1. Creates a new socket for a client 
2. Configures it to talk to a server
"""
import socket 
import os 
# get ip and hostname of the server 
# but since server it on the local machine as well
HOSTNAME = socket.gethostname()
IP_ADDR = socket.gethostbyname(HOSTNAME)
PORT_ADDR = 1243 # server port addr

# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to the server 
client_socket.connect(('0.0.0.0', PORT_ADDR))
data_recieved = client_socket.recv(1000)
print(data_recieved)