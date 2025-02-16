# UDPPingerModifiedServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind((gethostname(), 12000))

while True:
    
# Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

# Capitalize the message from the client
    message = message.upper()

# Otherwise, the server responds
    serverSocket.sendto(message, address)
    