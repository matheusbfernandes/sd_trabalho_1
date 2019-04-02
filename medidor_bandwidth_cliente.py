import socket
import os
import time


def converter(string):
    buf = ""
    for ele in string:
        if ele != ' ':
            buf += ele
    return int(buf)


def main():
    servidor_host = "192.168.0.100"
    servidor_porta = 10000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor_endereco = (servidor_host, servidor_porta)
    sock.connect(servidor_endereco)

    try:
        mensagem_inicio = "INICIO"
        mensagem_para_bytes = mensagem_inicio.encode()
        sock.send(mensagem_para_bytes)

        mensagem = os.urandom(10240)
        for i in range(0, 10):
            sock.sendall(mensagem)

        print("######")
        # dado = sock.recv(10240)

        # mensagem_final = "FIM"
        # mensagem_para_bytes = mensagem_final.encode()
        # sock.sendall(mensagem_para_bytes)
        #
        # tempo_total = converter(dado.decode())
        # print(tempo_total)
    finally:
        print("Fechando socket...")
        sock.close()


if __name__ == "__main__":
    main()
