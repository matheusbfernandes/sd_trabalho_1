import time
import socket
import os


def get_cliente_endereco():
    CLIENTE_IP = "192.168.0.100"
    CLIENTE_PORTA = 10000

    return CLIENTE_IP, CLIENTE_PORTA


def get_servidor_endereco():
    SERVIDOR_IP = "192.168.0.100"
    SERVIDOR_PORTA = 59330

    return SERVIDOR_IP, SERVIDOR_PORTA


def esperando_resposta(sock, pacotes_perdidos):
    while True:
        try:
            mensagem, _ = sock.recvfrom(1024)

            return str(time.time()), pacotes_perdidos
        except (Exception):
            pacotes_perdidos += 1

            return "ERROR 522", pacotes_perdidos


def enviar_mensagem(sock, mensagem, pacotes_perdidos):
    sock.sendto(mensagem, get_servidor_endereco())

    return esperando_resposta(sock, pacotes_perdidos)


def calcular_media_rtt(media_rtt, rtt):
    if media_rtt == -1.0:
        return rtt

    return media_rtt * 0.8 + rtt * 0.2


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)
    sock.bind(get_cliente_endereco())

    num_pings = 10
    num_sequencia = 1
    pacotes_perdidos = 0
    total_pacotes = 0

    media_rtt = -1.0
    rtt = 0.0

    mensagem = os.urandom(1024)
    tam_mensagem = len(mensagem)

    try:
        while num_sequencia <= num_pings:
            tempo_envio = time.time()
            mensagem_recebida, pacotes_perdidos = enviar_mensagem(sock, mensagem, pacotes_perdidos)

            if mensagem_recebida == "ERROR 522":
                print("{:s}, num_seq={:d}".format(mensagem_recebida, num_sequencia))
            else:
                rtt = (float(mensagem_recebida) - tempo_envio) * 1000
                media_rtt = calcular_media_rtt(media_rtt, rtt)

            print("Enviado {:d} bytes, num_seq={:3d}, rtt={:.3f}".format(tam_mensagem, num_sequencia, rtt))
            num_sequencia += 1
            total_pacotes += 1
    finally:
        sock.close()

    print("rtt medio: {:.3f}".format(media_rtt))
    print("Pacotes perdidos: {:.2f}%".format(pacotes_perdidos / total_pacotes * 100.0))


if __name__ == "__main__":
    main()
