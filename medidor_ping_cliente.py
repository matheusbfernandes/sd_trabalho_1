import time
from socket import *
import os


def get_time():
    return int(round(time.time() * 1000))


def esperando_resposta(socket_servidor, pacotes_perdidos):
    while True:
        try:
            mensagem, _ = socket_servidor.recvfrom(4096)
            
            return str(get_time()), pacotes_perdidos
        except Exception as e:
            pacotes_perdidos += 1
            
            return "ERROR 522", pacotes_perdidos


def enviar_mensagem(socket_servidor, mensagem, servidor_endereco, pacotes_perdidos):
    socket_servidor.sendto(mensagem, servidor_endereco)
    
    return esperando_resposta(socket_servidor, pacotes_perdidos)


def calcular_media_rtt(media_rtt, rtt):
    if media_rtt == -1:
        return rtt
    return media_rtt * 0.8 + rtt * 0.2


def main():
    cliente_ip = "192.168.103.21"
    cliente_porta = 1024
    
    servidor_ip = "192.168.103.20"
    servidor_porta = 59330
    
    servidor_endereco = (servidor_ip, servidor_porta)

    socket_servidor = socket(AF_INET, SOCK_DGRAM)
    socket_servidor.settimeout(1.0)
    socket_servidor.bind((cliente_ip, cliente_porta))
    
    num_pings = 10

    num_sequencia = 1
    pacotes_perdidos = 0.0
    total_pacotes = 0.0
    
    media_rtt = -1
    rtt = 0

    mensagem = os.urandom(1024)
    tam_mensagem = len(mensagem)
    
    while num_sequencia <= num_pings:
        tempo_envio = get_time()
        mensagem_recebida, pacotes_perdidos = enviar_mensagem(socket_servidor, mensagem, servidor_endereco, pacotes_perdidos)
        
        if mensagem_recebida == 'ERROR 522':
            print(mensagem_recebida)
        else:
            rtt = int(mensagem_recebida) - tempo_envio
            media_rtt = calcular_media_rtt(media_rtt, rtt)
            
        print(str(tam_mensagem) +'bytes'+ ' rtt=' + str(rtt))
        num_sequencia += 1
        total_pacotes += 1

    print("AVGRTT: " + str(media_rtt))
    print("Packet Loss: " + str(pacotes_perdidos/total_pacotes*100) + "%")


if __name__ == "__main__":
    main()
