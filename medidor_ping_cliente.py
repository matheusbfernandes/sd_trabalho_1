import time
import socket
import os


def get_cliente_endereco():
    CLIENTE_IP = "192.168.0.100"
    CLIENTE_PORTA = 10000

    return CLIENTE_IP, CLIENTE_PORTA


def get_servidor_endereco():
    SERVIDOR_IP = "186.216.101.172"
    SERVIDOR_PORTA = 59330

    return SERVIDOR_IP, SERVIDOR_PORTA


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)
    sock.bind(get_cliente_endereco())

    num_pings = 10
    num_sequencia = 1
    pacotes_perdidos = 0
    total_pacotes = 0

    media_rtt = 0.0

    mensagem = os.urandom(1024)
    tam_mensagem = len(mensagem)

    try:
        while num_sequencia <= num_pings:
            tempo_envio = time.time()
            sock.sendto(mensagem, get_servidor_endereco())
            try:
                mensagem, _ = sock.recvfrom(1024)
                tempo_chegada = time.time()

                rtt = (tempo_chegada - tempo_envio) * 1000
                media_rtt += rtt

                print("Enviado {:d} bytes, num_seq={:2d}, rtt={:.3f}".format(tam_mensagem, num_sequencia, rtt))
            except Exception:
                print("timeout, num_seq={:2d}".format(num_sequencia))
                pacotes_perdidos += 1

            num_sequencia += 1
            total_pacotes += 1

            time.sleep(1)
    finally:
        sock.close()

    print("rtt medio: {:.3f}".format(media_rtt / num_pings))
    print("Pacotes perdidos: {:.2f}%".format(pacotes_perdidos / total_pacotes * 100.0))


if __name__ == "__main__":
    main()
