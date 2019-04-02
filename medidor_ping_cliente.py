import time
from socket import *
import os


def get_time():
    return time.time()


def esperando_resposta(sock, pacotes_perdidos):
    while True:
        try:
            mensagem, _ = sock.recvfrom(1024)
            
            return str(get_time()), pacotes_perdidos
        except Exception:
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

    sock = socket(AF_INET, SOCK_DGRAM)
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
                print(mensagem_recebida)
            else:
                rtt = float(mensagem_recebida) - tempo_envio
                print(rtt)
                media_rtt = calcular_media_rtt(media_rtt, rtt)

            print("{:d} bytes, rtt = {:.3f}".format(tam_mensagem, rtt))
            num_sequencia += 1
            total_pacotes += 1
    finally:
        sock.close()

    print("rtt medio: {:.3f}".format(media_rtt))
    print("Pacotes perdidos: {:.2f}%".format(pacotes_perdidos / total_pacotes * 100.0))


if __name__ == "__main__":
    main()
