#UDPPingerClient.py
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
count=0
N = int(input("Enter Value of N:"))
diff=N

# Loop with iterates around number of packets the user want to send for Ping echo
for i in range(N):

    # Client send a word 'ping' to server as part of Probe Packet 
    message = "ping "+ str(i+1)
    # Creates a UDP socket
    # Notice the use of SOCK_DGRAM for UDP Packet
    UDPClientSocket = socket(AF_INET,SOCK_DGRAM)
    # Notice the use of below method attaches a upperbound of time on the Socket operation
    UDPClientSocket.settimeout(1)
    # Used to Mark timestamp at which the packet is sent to the server
    datetime_request = datetime.now()
    request_time = datetime_request.strftime("%H:%M:%S:%f")
    # Sends the Packet
    UDPClientSocket.sendto(str.encode(message), ('172.31.0.3',12000))

    # Exception Handling to wait for the response for one second
    try:
        # is_ready, _, _ = select([UDPClientSocket],[],[],1)
        # if is_ready:    

            # Recieves the packet 
            response_message = UDPClientSocket.recvfrom(1024)
            # Used to Mark timestamp at which the packet is recieved by the client
            datetime_response = datetime.now()
            response_time = datetime_response.strftime("%H:%M:%S:%f")
            RTT = (datetime_response - datetime_request).microseconds/1000
            # Prints the Request Timestamp, Resposne Timestamp and RTT for each Ping probe packet
            print(response_message[0].decode() +" "+ request_time +" "+ response_time + " " + str(RTT))
            RTT=float(RTT)
            # Calculations for summary of entire Ping Utility
            sum=sum+RTT
            if RTT>max:
                max=RTT
            if RTT<min:
                min=RTT
        # else:
        #     print("Requested Time Out")

    except timeout:

        # Counts the number of packet that got lost
        count+=1
        print("Requested Time Out")


if N != count:
     diff = N-count

# Prints the Summary of Entire Ping Utility i.e. Minimim, Maximum, Average RTT and Packet Loss
print(f"\nMax:{max}\nMin:{min}\nAverage:{sum/diff}\nPacket Loss:{((N-diff)/N)*100}%")

