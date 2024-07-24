# TCPPingerConcurrentServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
from threading import *

# For Thread Handling
def handle_thread(conn,address):

    try:

        # Loop for handeling a particulat Pipe 
        while True:
                
                # Capitalize the message from the client
                data = conn.recv(1024)
                message = data.upper()
                if not message:
                    break
                # Otherwise, the server responds
                conn.sendall(message)

    finally:
         
        # Breaks the connection of client socket i.e. pipe 
         conn.close()



def main():
    
    # Create a TCP socket
    # Notice the use of SOCK_STREAM for TCP packets
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Assign IP address and port number to socket
    serverSocket.bind((gethostname(), 12000))
    # Listens for a client Connection
    serverSocket.listen()

    # For continuity         
    while True:

        # Accepts the connection made by client i.e. makes TCP pipe
        conn, address = serverSocket.accept()
        # Creates thread 
        thread = Thread(target=handle_thread,args=(conn,address))
        # Starts Thread
        thread.start()



if __name__ == "__main__":
    main()
    