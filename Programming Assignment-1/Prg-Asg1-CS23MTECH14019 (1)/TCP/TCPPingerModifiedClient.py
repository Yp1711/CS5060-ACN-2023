#TCPPingerModifiedClient.py
# We will need the following packets for socket connecgtion, RTT calculation
from socket import *
from time import *
from datetime import *
from select import *
from math import *

# The following variable are needed for some showing the summary of Ping
min=inf
max=-inf
sum=0
total_packet=0
lost_packet=0
N = int(input("Enter Value of N:"))

# Exception Handling for the client Socket Connection
try:
     
    # Creates TCP Packet
    TCPClientSocket = socket(AF_INET,SOCK_STREAM)
    # Attemps for connection with Server, listining at mentioned address and port number
    TCPClientSocket.connect(('172.31.0.3',12000))
    # Notice the use of below method attaches a upperbound of time on the Socket operation
    TCPClientSocket.settimeout(1)
    # is_ready, _, _ = select([TCPClientSocket],[],[],1)
    # if is_ready:  

    # Loop with iterates around number of packets the user want to send for Ping echo
    for i in range(N):

        # Used to Mark timestamp at which the packet is sent to the server
        datetime_request = datetime.now()
        request_time = datetime_request.strftime("%H:%M:%S:%f")
        message = "ping "+ str(i+1)
        # Sends the Packet
        TCPClientSocket.sendall(str.encode(message))
        total_packet+=1

        # A loops that waits for the packet from the server in case of loss
        while True:
            
            # Exception Handling to wait for the response for one second
            try:

                # Recieves the Packet
                response_message = TCPClientSocket.recv(1024)
                # Used to Mark timestamp at which the packet is recieved by the client
                datetime_response = datetime.now()
                response_time = datetime_response.strftime("%H:%M:%S:%f")
                RTT = (datetime_response - datetime_request).microseconds/1000
                # Prints the Request Timestamp, Resposne Timestamp and RTT for each Ping probe packet
                print(response_message.decode() +" "+ request_time +" "+ response_time + " " + str(RTT))
                # Calculations for summary of entire Ping Utility
                RTT=float(RTT)
                sum=sum+RTT
                if RTT>max:
                    max=RTT
                if RTT<min:
                    min=RTT
                break
    # else:
    #     print("Requested Time Out")

            except timeout:

                # counts the number of packet that got lost along with adding into the total packets that a client sends
                lost_packet+=1
                total_packet+=1
                print("Requested Time Out...Re-transmitting")
                # Overrides new request time
                datetime_request = datetime.now()

except error:
    
    print("Error")

finally:

    # Closes the Client Socket
    TCPClientSocket.close()


# Prints the Summary of Entire Ping Utility i.e. Minimim, Maximum, Average RTT and Packet Loss
print(f"\nMax:{max}\nMin:{min}\nAverage:{sum/(total_packet-lost_packet)}\nPacket Loss:{(lost_packet/total_packet)*100}%")

