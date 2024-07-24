# TCPPingerModifiedServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *

# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET, SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind((gethostname(), 12000))

# For contineous listening
while True:

    # Servers listens contineously for clients
    serverSocket.listen()
    # Accepts the connection made by clients i.e. makes TCP pipes
    conn, address = serverSocket.accept()

    try:

        while True:
            
            # Capitalize the message from the client
            data = conn.recv(1024)
            message = data.upper()
            # Breaks the connection with client in case of it doesn't recieves message from client
            if not message:
                break
            # Otherwise, the server responds
            conn.sendall(message)
        
    finally:
        
        # Breaks the connection of client socket i.e. pipe 
        conn.close()