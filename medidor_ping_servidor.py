import socket


def main():
    servidor_io = "192.168.0.100"
    servidor_porta = 59330
    servidor_endereco = (servidor_io, servidor_porta)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(servidor_endereco)

    print("Iniciando servidor...")
    print("Servidor: {:s} iniciado. Utilizando a porta: {:d}".format(*servidor_endereco))

    try:
        while True:
            mensagem, cliente_endereco = sock.recvfrom(1024)
            sock.sendto(mensagem, cliente_endereco)
    except (KeyboardInterrupt, SystemExit):
        sock.close()
        print("\nServidor esta sendo fechado...")


if __name__ == "__main__":
    main()
