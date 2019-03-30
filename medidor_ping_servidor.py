# UDPPingServer.py
# We will need the following module to generate randomizedlost packets
import random
from socket import *
import time

# What's your IP address and witch port should we use?
recieve_host = '192.168.0.100'
recieve_port = 59330

# What's the remote host's IP address and witch port should we use?
remote_host = '192.168.0.100'
remote_port = 12000

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind((recieve_host, recieve_port))


def get_time():
    return int(round(time.time() * 1000))

def send_message(message,wait=False):
    message_as_bytes = str.encode(message)
    type(message_as_bytes)
    serverSocket.sendto(message_as_bytes, (remote_host, remote_port))

# Just respond to ping requests
while True:
    # Receive the client packet along with the address it is coming from
    message_as_bytes, address = serverSocket.recvfrom(remote_port)
    message = message_as_bytes.decode()
    type(message)
    # Capitalize the message from the client
    message = message.upper()
    print('Recieve: ' + message)
    message_as_bytes = str.encode(message)
    type(message_as_bytes)
    serverSocket.sendto(message_as_bytes, address)
    print('Send: ' + message)
