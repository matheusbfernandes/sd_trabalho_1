import java.net.DatagramSocket;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.io.IOException;
import java.io.InterruptedIOException;

public class UDPCliente extends Thread {
    private static final int TIMEOUT = 1000;
    private static final int ENVIOS = 10;

    public static void main(String[] args) throws IOException, InterruptedException {
        InetAddress enderecoServer = InetAddress.getByName("ibiza.dcc.ufla.br");
        int portaServer = 7013;

        int tamMensagem = 64;
        byte[] bytesParaEnviar = new byte[tamMensagem];

        DatagramSocket socket = new DatagramSocket();
        socket.setSoTimeout(TIMEOUT);

        DatagramPacket pacoteEnviar = new DatagramPacket(bytesParaEnviar, bytesParaEnviar.length, enderecoServer, portaServer);
        DatagramPacket pacoteReceber = new DatagramPacket(new byte[bytesParaEnviar.length], bytesParaEnviar.length);

        double tempoInicio, tempoFinal, tempoTotal;
        int qtdPerdidos = 0;
        double rttTotal = 0;

        for (int i = 1; i <= ENVIOS; ++i) {
            double rtt = 0;
            tempoInicio = System.nanoTime();
            socket.send(pacoteEnviar);

            try {
                socket.receive(pacoteReceber);
                tempoFinal = System.nanoTime();

                rtt = (tempoFinal - tempoInicio) / 1000000;
                rttTotal += rtt;

                System.out.printf("Enviado %d bytes, num_seq=%d, rtt=%.3f\n",tamMensagem, i, rtt);
            }
            catch (InterruptedIOException e) {
                ++qtdPerdidos;
                System.out.println("timeout, num_seq=" + i);
            }

           sleep(1000L);
        }

        socket.close();

        System.out.printf("rtt medio: %.3f ms%n", (rttTotal/ENVIOS));
        System.out.printf("Pacotes perdidos: %.2f\n", (((double)qtdPerdidos / (double)ENVIOS) * 100.0));
    }
}
