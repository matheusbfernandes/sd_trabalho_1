import socket


def get_servidor_endereco():
    SERVIDOR_IP = "18.204.102.146"
    SERVIDOR_PORTA = 7013

    return SERVIDOR_IP, SERVIDOR_PORTA


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(get_servidor_endereco())

    print("Iniciando servidor...")
    print("Servidor: {:s} iniciado. Utilizando a porta: {:d}".format(*get_servidor_endereco()))

    try:
        while True:
            mensagem, cliente_endereco = sock.recvfrom(1024)
            sock.sendto(mensagem, cliente_endereco)
    except (KeyboardInterrupt, SystemExit):
        sock.close()
        print("\nServidor esta sendo fechado...")


if __name__ == "__main__":
    main()
