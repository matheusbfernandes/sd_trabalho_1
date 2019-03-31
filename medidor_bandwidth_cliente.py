import socket
import os
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('192.168.0.100', 10000)
sock.connect(server_address)

try:
    message = os.urandom(131072)

    inicio = time.time()
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(131072)
        amount_received += len(data)
        print('received "%s"' % data)

    fim = time.time()
    print("taxa de transferencia de:%.2f" % (1 / (fim - inicio)))
finally:
    print('closing socket')
    sock.close()
