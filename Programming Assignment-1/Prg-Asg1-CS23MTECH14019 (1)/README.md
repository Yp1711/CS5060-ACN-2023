# Socket Programming in Python: Implementation of Ping using UDP and TCP

This repository provides Python code examples for implementing a simple "ping" functionality using both UDP (User Datagram Protocol) and TCP (Transmission Control Protocol) sockets. The "ping" functionality simulates sending and receiving packets between a client and a server.

## Table of Contents

- [Prerequisites](#prerequisites)
- [UDP Ping Implementation](#udp-ping-implementation)
- [TCP Ping Implementation](#tcp-ping-implementation)
- [Packet Loss Logic](#packet-loss-logic)
- [Usage](#usage)

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed on your system.
- Basic understanding of socket programming concepts.

## UDP Ping Implementation

The UDP ping implementation uses Python's `socket` library to create a simple UDP client and server. The client sends "ping" packets to the server, and the server responds with an acknowledgment. The round-trip time (RTT) is measured to simulate ping behavior.

To run the UDP Ping program:

1. Navigate to the `udp_ping` directory.
2. Run the server:

   ```bash
   python UDPPingerXServer.py
3. In a separate terminal, run the client:

   ```bash
   python UDPPingerXClient.py

## TCP Ping Implementation

The TCP ping implementation also uses Python's socket library to create a simple TCP client and server. The client establishes a connection with the server and sends "ping" requests. The server responds with an acknowledgment, and the RTT is measured.

To run the TCP Ping program:

1. Navigate to the tcp_ping directory.
2. Run the server:

   ```bash
   python TCPPingerXServer.py
3. In a separate terminal, run the client:

   ```bash
   python TCPPingerXClient.py

## Packet Loss Logic

#### 1. Simulation of Packet Loss Logic at Application Level
- Using a simple random number generation code snippet for generating loss
    ```bash
    rand = random.randint(0, 11)
    if rand < 4:
        continue
#### 2. Emulation of Packet loss at NIC Interface
- Using tc-netem utility for generating loss
    ```bash
    sudo tc edisc [add]/[change]/[del]/[rename] dev [dev_name] root netem lost [percentage_loss]

##   Usage

You can use these implementations as a foundation for more advanced network applications or as a learning resource for socket programming in Python.

Feel free to modify and extend the code to suit your specific requirements.

