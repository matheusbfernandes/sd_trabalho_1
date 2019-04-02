import time
import socket
import os


def get_time():
    return time.time()


def esperando_resposta(sock, pacotes_perdidos):
    while True:
        try:
            mensagem, _ = sock.recvfrom(1024)

            return str(get_time()), pacotes_perdidos
        except (Exception):
            pacotes_perdidos += 1

            return "ERROR 522", pacotes_perdidos


def enviar_mensagem(sock, mensagem, servidor_endereco, pacotes_perdidos):
    sock.sendto(mensagem, servidor_endereco)

    return esperando_resposta(sock, pacotes_perdidos)


def calcular_media_rtt(media_rtt, rtt):
    if media_rtt == -1.0:
        return rtt

    return media_rtt * 0.8 + rtt * 0.2


def main():
    cliente_ip = "192.168.0.100"
    cliente_porta = 10000
    cliente_endereco = (cliente_ip, cliente_porta)

    servidor_ip = "192.168.0.100"
    servidor_porta = 59330
    servidor_endereco = (servidor_ip, servidor_porta)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)
    sock.bind(cliente_endereco)

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
            tempo_envio = get_time()
            mensagem_recebida, pacotes_perdidos = enviar_mensagem(sock, mensagem, servidor_endereco, pacotes_perdidos)

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
