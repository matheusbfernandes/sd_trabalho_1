from socket import *


def main():
    servidor_io = "192.168.0.100"
    servidor_porta = 59330
    servidor_endereco = (servidor_io, servidor_porta)

    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(servidor_endereco)

    while True:
        mensagem, cliente_endereco = sock.recvfrom(1024)
        sock.sendto(mensagem, cliente_endereco)


if __name__ == "__main__":
    main()
