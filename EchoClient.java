import java.io.*;
import java.net.*;
import java.util.Random;
import java.nio.charset.Charset;
import java.util.concurrent.TimeUnit;

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

	
        int number_of_packets = 1024;
	long startTime = System.currentTimeMillis();
        System.out.println("Tempo inicial: " + startTime);
        
	while (number_of_packets != 0) {
            out.println(mensagemAleatoria);
            System.out.println(in.readLine() +" "+ number_of_packets);
            number_of_packets--;  
	}
        
        long finalTime = System.currentTimeMillis();
        
	System.out.println("Tempo final: " + System.currentTimeMillis());
        System.out.println("Tempo = " + (finalTime - startTime) + "ms");
        double tempoEmSegundos = (finalTime-startTime)/100.0;
        System.out.println("Tempo de envio de 1 MB em segundos: " + (finalTime-startTime)/1000.0 + " segundos ");
        System.out.println("Velocidade de Upload: " + (1024/tempoEmSegundos) + " kBps");
	out.close();
	in.close();
	echoSocket.close();
    }
}
