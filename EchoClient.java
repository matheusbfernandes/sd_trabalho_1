import java.io.*;
import java.net.*;
import java.util.Random;
import java.nio.charset.Charset;
import java.util.concurrent.TimeUnit;

public class EchoClient {
    public static void main(String[] args) throws IOException {

        String serverHostname = new String ("192.168.101.40");
		int porta = 3000;

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
		String mensagemAleatoria = "aaaaaoeirudjskcmsndhfjehfjdkslsjdhfjufjdkdlskdjdkskdowkkkkkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
		aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
		aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaappppppppppp
		pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
		pppp";

		System.out.println(mensagemAleatoria.length());
		//String mensagemAleatoria = "oi";
		int number_of_packets = 10;
		long startTime = System.currentTimeMillis();
		while (number_of_packets != 0) {
			out.println(mensagemAleatoria);
			System.out.println(in.readLine() +" "+ number_of_packets);
			number_of_packets--;  
		}
		
        System.out.println("Tempo = " + ((System.currentTimeMillis()) - startTime));
		out.close();
		in.close();
		echoSocket.close();
    }
}
