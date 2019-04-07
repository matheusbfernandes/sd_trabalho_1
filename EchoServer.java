import java.net.*; 
import java.io.*; 

public class EchoServer extends Thread { 
    protected Socket clientSocket;
    public static void main(String[] args) throws IOException  { 
        ServerSocket serverSocket = null; 

        try { 
            serverSocket = new ServerSocket(7013); 
            System.out.println ("Connection Socket Created");
            try { 
                while (true) {
                    System.out.println ("Waiting for Connection");
                    new EchoServer(serverSocket.accept()); 
                }
            } catch (IOException e) { 
                System.err.println("Accept failed."); 
                System.exit(1); 
            } 
        } catch (IOException e) { 
            System.err.println("Could not listen on port: 7013."); 
            System.exit(1); 
        }  finally {
            try {
                serverSocket.close(); 
            } catch (IOException e) { 
                System.err.println("Could not close port: 7013."); 
                System.exit(1); 
            } 
        }
    }

    private EchoServer (Socket clientSoc) {
        clientSocket = clientSoc;
        start();
    }

    public void run() {
        System.out.println ("New Communication Thread Started");

        try { 
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true); 
            BufferedReader in = new BufferedReader(new InputStreamReader( clientSocket.getInputStream())); 

            String inputLine; 

            int qtdPacotesRecebidos = 0;

            while ((inputLine = in.readLine()) != null) { 
                //System.out.println ("Server: " + inputLine); 
                ++qtdPacotesRecebidos;
                //Enviando para o cliente o numero do pacote recebido
                out.println(qtdPacotesRecebidos); 

                if (inputLine.equals("Bye.")) 
                    break; 
                } 

            out.close(); 
            in.close(); 
            clientSocket.close(); 
            System.out.println ("Thread ended");
                
        } catch (IOException e) { 
            System.err.println("Problem with Communication Server");
            System.exit(1); 
        } 
    }
} 
