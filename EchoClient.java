import java.io.*;
import java.net.*;
import java.util.Random;
import java.nio.charset.Charset;
import java.util.concurrent.TimeUnit;
import java.text.DecimalFormat;

public class EchoClient {
    public static void main(String[] args) throws IOException {

        String serverHostname = new String ("18.204.102.146");
	int porta = 7013;

	System.out.println ("Attemping to connect to host " + serverHostname + " on port " + porta + ".");

        Socket echoSocket = null;
        PrintWriter out = null;
        BufferedReader in = null;

        try {
            echoSocket = new Socket(serverHostname, porta );
            
            out = new PrintWriter(echoSocket.getOutputStream(), true);
            in = new BufferedReader(new InputStreamReader(echoSocket.getInputStream()));

	} catch (UnknownHostException e) {
            System.err.println("Don't know about host: " + serverHostname);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to: " + serverHostname);
            System.exit(1);
        }
		
        //byte[] array = new byte[1024];
        //new Random().nextBytes(array);
        //String mensagemAleatoria = new String(array,Charset.forName("UTF-8"));
        
        //Mensagem de 1024 bytes (10 mensagens = 10kB)
        String mensagemAleatoria = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                + "aaaaaaaaaaaaaaaaaaaaa";

	
        int number_of_packets = 1;
	long startTime = System.currentTimeMillis();
        System.out.println("Tempo inicial: " + startTime);
        
	while (number_of_packets < 1024) {
            out.println(mensagemAleatoria);
            progressivePercentage(number_of_packets, 1024);
            String resp = in.readLine();
            //System.out.println(in.readLine() +" "+ number_of_packets);
            number_of_packets++;  
	}
        
        long finalTime = System.currentTimeMillis();
        DecimalFormat df = new DecimalFormat("0.000");
	//System.out.println("Tempo final: " + System.currentTimeMillis());
        System.out.println("Tempo = " + (finalTime - startTime) + "ms");
        double tempoEmSegundos = (finalTime-startTime)/100.0;
        System.out.println("Tempo de envio de 1 MB em segundos: " + df.format((finalTime-startTime)/1000.0) + " segundos ");
        System.out.println("Velocidade de Upload: " + (1024/tempoEmSegundos) + " kBps");
	out.close();
	in.close();
	echoSocket.close();
    }

    public static void progressivePercentage(int progresso, int qtdDadosEnviados) {
        //tamanho da barra
        int tamMaxBarra = 50;
        
        //quanto porcento já foi concluido do total
        double dPorcentagemConcluida = (progresso*100)/(double)qtdDadosEnviados;        
        int iPorcentagemConcluida = (int)dPorcentagemConcluida;

        char defaultChar = '-';
        String icon = "*";
        

        //cria uma barra do tipo "--------------------------------------------------]"
        String barra = new String(new char[tamMaxBarra]).replace('\0', defaultChar) + "]";
        
        StringBuilder barraConcluida = new StringBuilder();
        barraConcluida.append("[");
        for (int i = 0; i < iPorcentagemConcluida/2; i++) {
            barraConcluida.append(icon);
        }

        DecimalFormat df = new DecimalFormat("0.00");
        String barraRestante = barra.substring((iPorcentagemConcluida/2), barra.length());
        System.out.print("\r" + barraConcluida + barraRestante + " " + df.format(dPorcentagemConcluida) + "% (" + (progresso) + "kB)");
        if (progresso == qtdDadosEnviados) {
            //String barraC = new String(new char[tamMaxBarra]).replace('\0', defaultChar) + "]";
            //System.out.print("\r" + barraConcluida + barraRestante + " " + df.format(dPorcentagemConcluida) + "% (" + (progresso) + "kB)");
            System.out.print("\n");
        }

    }
}
