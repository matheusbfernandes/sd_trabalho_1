import socket
import time


def main():
    servidor_host = "192.168.0.100"
    servidor_porta = 10000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor_endereco = (servidor_host, servidor_porta)
    print("Servidor: %s iniciado. Utilizando a porta: %s" % servidor_endereco)
    sock.bind(servidor_endereco)

    sock.listen(1)

    while True:
        print("Esperando por uma conexao...")
        conexao, endereco_cliente = sock.accept()

        try:
            print("Conectado com:", endereco_cliente)
            dados_bytes = conexao.recv(6)
            dado_inicial = dados_bytes.decode()
            type(dado_inicial)

            if dado_inicial == "INICIO":
                recebendo_dados = True

                total_bytes = 0
                while recebendo_dados:
                    tempo_inicial = time.time()
                    dados_bytes = conexao.recv(1024)
                    total_bytes += len(dados_bytes)

                    if not dados_bytes:
                        tempo_final = time.time()
                        tempo_total = tempo_final - tempo_inicial
                        print(total_bytes)
                        print(tempo_total)
                        recebendo_dados = False

                        print("Sem mais dados para receber de:", endereco_cliente)
            else:
                print("Mensagem inical \"%s\" nao corresponde com o esperado." % dado_inicial)
        finally:
            print("Fechando a conexao...")
            conexao.close()


if __name__ == "__main__":
    main()
