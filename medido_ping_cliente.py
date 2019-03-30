# UDPPingClient.py
import time
from socket import *

# What's your IP address and witch port should we use?
recieve_host = '192.168.0.100'
recieve_port = 1024

# What's the remote host's IP address and witch port should we use?
remote_host = '200.141.186.1'
remote_port = 59330

# number of times to ping
num_pings = 10

# Keep track of some things
sequence_number = 1
packets_dropped = 0.0
total_packets = 0.0

# Setup a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.settimeout(1.0)
serverSocket.bind((recieve_host, recieve_port))

def get_time():
    return int(round(time.time() * 1000))

def wait_for_response():
    global packets_dropped
    while True:
        # Receive the client packet along with the address it is coming from
        try:
            message, address = serverSocket.recvfrom(remote_port)
            return str(get_time())
        except Exception as e:
            packets_dropped = packets_dropped + 1
            return 'ERROR 522'

def send_message(message):
    serverSocket.sendto(message, (remote_host, remote_port))
    return wait_for_response()


avgRtt = 0
rtt = 0

while sequence_number <= num_pings:
    # Create message with current sequence_number and time

    matriz = [1]*3000
    message = "teste"
    # message = 'QjhsdfkjahsgdfkjahsgdfkjashdgfkajshdgfkajhsdgfkajshdgfkjahsdgfkjashdgfkjashdgfkjashdgfkjahsdgfkjashgdfjkahsdgfkjashdgfkjahsdgfkjahsdgfkjahsgdfkjahsgdfjkahsgdfkjahsgdfkjahgsdfkjhagsdkfjhagsdkjfhagsdkjfhgasdkjhfgasdkjfgasdkjhfgaksjdhfgakjshdgfkjashdgfkjashdgfkjashdgfkjashdgfkajsdhgfkajdhgfkajsdhgfkajshdgfkajshdgfkajsdhgfkajsdhgfakjsdhgfkajsdhgfakjsdhgfaksjdhfgajksdfhgakjsdhfgajsdhgfkdjhfgaksdjfhgaskjdfhgaksjdhfgWASDFASDFASDFASDFASDFASDFASDFADFASDFASDFASDFASDFASDFADFASDFASDFASDFASDFASFDASDFASDFASDFASDFASDFASDFASDFASDFASDFASDASDFSDFASDFASDFASDFASDASDFASDFASDFASDFASDFASDFASDFADSERQWERQWERQWREQWERQWERQWERQWERQWRQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQWERQERQWTQVWVERTQWFTQ$QCWTQWVQTWRVQTVQWVTQGRWERGERGSDFHSDFGBAGASDFASDFASDFASDFASDFASDFASFASDFASDFASDFASDFASFASDFASFASDFPINGQWERTYUIOPASDFGHJKLMNBVCXASDASDADSASDASDASDASDASDASDASASDFASDFASDFASDFASDFASDFASDFASDFASDFASDFASDFASDFASDFASDFASDFASDFASDFASDFDASDASDASDASDZ'
    # Recieve ping
    message_as_byte = str.encode(message)
    type(message_as_byte)
    sendtime = get_time()
    recieved = send_message(message_as_byte)
    recieved_size = len(message)
    #print recieved_time
    if recieved == 'ERROR 522':
        print(recieved)
    else:
        rtt = int(recieved) - sendtime
        avgRtt = avgRtt + rtt
    print(str(recieved_size) +'bytes'+ ' rtt=' + str(rtt))
    sequence_number = sequence_number + 1
    total_packets = total_packets + 1
# Out of the loop, report running statistics
print("AVGRTT: " + str(avgRtt/10))
print("Packet Loss: " + str(packets_dropped/total_packets*100) + "%")
