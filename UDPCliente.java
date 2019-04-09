/*
Autor: Matheus Bento Fernandes
*/

import java.net.DatagramSocket;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.io.IOException;
import java.io.InterruptedIOException;

public class UDPCliente extends Thread {
    private static final int TIMEOUT = 250;
    private static final int ENVIOS = 10;

    public static void main(String[] args) throws IOException, InterruptedException {
        InetAddress enderecoServer = InetAddress.getByName("177.44.46.117");
        int portaServer = 59330;

        String mensagem = "exemplo";
        byte[] bytesParaEnviar = mensagem.getBytes();

        DatagramSocket socket = new DatagramSocket();
        socket.setSoTimeout(TIMEOUT);

        DatagramPacket pacoteEnviar = new DatagramPacket(bytesParaEnviar, bytesParaEnviar.length, enderecoServer, portaServer);
        DatagramPacket pacoteReceber = new DatagramPacket(new byte[bytesParaEnviar.length], bytesParaEnviar.length);

        double tempoInicio, tempoFinal, tempoTotal;
        int qtdPerdidos = 0;
        double rttTotal = 0, rttMin = 0, rttMax = 0;

        System.out.println("PING " + enderecoServer.getHostName() + ":" + portaServer + " (" + enderecoServer.getHostAddress()
                + ":" + portaServer + ") com a mensagem: \"" + mensagem + "\"(" + bytesParaEnviar.length + " bytes)\n");

        for (int i = 0; i < ENVIOS; ++i) {
            tempoInicio = System.nanoTime();
            socket.send(pacoteEnviar);

            try {
                socket.receive(pacoteReceber);
                tempoFinal = System.nanoTime();

                tempoTotal = (tempoFinal - tempoInicio) / 1000000;
                rttTotal += tempoTotal;

                if (rttMin == 0) {
                    rttMin = tempoTotal;
                }
                else if (tempoTotal < rttMin) {
                    rttMin = tempoTotal;
                }
                else if (tempoTotal > rttMax) {
                    rttMax = tempoTotal;
                }

                System.out.println(pacoteReceber.getLength() + " bytes recebidos de " + pacoteReceber.getAddress().getHostAddress() + ":" + pacoteReceber.getPort()
                        + ": sequencia de envio=" + (i+1) + ", tempo=" + tempoTotal + " ms");
            }
            catch (InterruptedIOException e) {
                ++qtdPerdidos;
                tempoTotal = 250L;
                System.out.println("Timed out: sequencia de envio=" + (i+1));
            }

           sleep(1000L);
        }

        socket.close();

        System.out.println("\n--- ping " + enderecoServer.getHostName() + ":" + portaServer + " estatisticas ---");
        System.out.println(ENVIOS + " pacotes transmitidos, recebidos=" + (ENVIOS - qtdPerdidos) + ", perdidos=" + qtdPerdidos
                + ", taxa de perdas=" + ((double) qtdPerdidos/(double) ENVIOS * 100) + "%");
        System.out.printf("rtt minimo/medio/maximo = %.3f/%.3f/%.3f ms%n", rttMin, (rttTotal/ENVIOS), rttMax);
    }
}
