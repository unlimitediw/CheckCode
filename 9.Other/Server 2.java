import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket server = new ServerSocket(8080);
        server.setReuseAddress(true);
        System.out.println("Listening for connection on port 8080 ....");
        while(true){
            try(Socket socket = server.accept()){
                OutputStream outstream = socket.getOutputStream();
                Date today = new Date();
                String body = "<html><body>Hello,!!!!!!.</body></html>";
                String httpResponse = "HTTP/1.1 200 OK\r\n\r\n" + body;
                outstream.write(httpResponse.getBytes("UTF-8"));
            }
        }
    }
}


//localhost:8080