import org.w3c.dom.Text;

import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

class GWServerThread implements Runnable {
    // Core KV

    private Socket sock;
    private HashMap<String, String> KVgw;
    private BufferedReader in;
    private PrintWriter out;


    public GWServerThread(Socket s, HashMap<String, String> KVgw) {
        this.sock = s;
        this.KVgw = KVgw;
    }

    public void run() {
        // receive message
        try {
            out = new PrintWriter(sock.getOutputStream(), true);
            in = new BufferedReader(new InputStreamReader(sock.getInputStream()));
            System.out.println("Got connection from " + sock.getInetAddress());
            // read in the  name and message
            String operation = in.readLine();
            ArrayList<String> msgList = new ArrayList<>();
            while(in.ready()){
                String n = in.readLine();
                msgList.add(n);
            }
            /*
            int count = 0;
            // bufferedReader can not check first line by in.ready()
            while(count < 2){
                if(in.ready()){
                    if (count == 0){
                        key = in.readLine();
                    }
                    else{
                        value = in.readLine();
                    }
                }
                count ++;
            }
            */
            System.out.println("Operation name: " + operation);
            String feedback = "";
            if (operation.equals("SET")) {
                if (KVgw.containsKey(msgList.get(0))) {
                    feedback = "Key is already in KVgw.";
                } else {
                    KVgw.put(msgList.get(0), msgList.get(1));
                    feedback = "Key and Value have been set.";
                }
            } else if (operation.equals("GET")) {
                if (KVgw.containsKey(msgList.get(0))) {
                    feedback = "The value of key " + msgList.get(0) + " is: " + KVgw.get(msgList.get(0)) + ".";
                } else {
                    feedback = "Key is not found.";
                }
            } else if (operation.equals("STATS")) {
                int KVcount = KVgw.size();
                String rep = KVcount > 1 ? "are " : "is ";
                String rep2 = KVcount > 1 ? "mappings " : "mapping ";
                feedback = "There " + rep + KVcount + " key-value " + rep2 + "in KVgw.";
            } else if(operation.equals("MULTISET")){
                ArrayList<String> keySet = new ArrayList<>();
                ArrayList<String> valueSet = new ArrayList<>();
                Boolean findVal = false;
                for(int i = 0;i < msgList.size();i++){
                    if (msgList.get(i).equals("dividedMsg")){
                        findVal = true;
                        continue;
                    }
                    if(!findVal){
                        keySet.add(msgList.get(i));
                    }
                    else{
                        valueSet.add(msgList.get(i));
                    }
                }
                if(keySet.size() != valueSet.size()){
                    System.out.println("Error in MULTISET");
                }
                for(int i = 0;i < keySet.size();i++){
                    System.out.println(keySet.get(i));
                    System.out.println("!");
                    if (KVgw.containsKey(keySet.get(i))) {
                        feedback = "Key" + keySet.get(0) + "is already in KVgw.";
                    }
                    else {
                        System.out.println(keySet.get(i));
                        System.out.println(valueSet.get(i));
                        KVgw.put(keySet.get(i), valueSet.get(i));
                    }
                }
            }else if(operation.equals("MULTIGET")){
                StringBuilder feedbackBuilder = new StringBuilder();
                for(int i = 0;i < msgList.size();i++){
                    System.out.println(msgList.get(i));
                    feedbackBuilder.append(KVgw.get(msgList.get(i)));
                }
                feedback = feedbackBuilder.toString();
            }
            else {
                feedback = "Invalid operation!";
            }
            out.println(feedback);

            // clean things up
            out.close();
            in.close();
            sock.close();

        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e){
            e.printStackTrace();
        } finally {
            try {
                out.close();
                in.close();
                sock.close();
            } catch (IOException e){
                e.printStackTrace();
            }
        }
    }
}

class TextServer implements Runnable{
    private ServerSocket serverSocket;
    private HashMap<String, String> KVgw;

    public TextServer(HashMap<String, String> KVgw){
        this.KVgw = KVgw;
    }
    public void run(){
        boolean listening = true;

        try {
            InetAddress addr = InetAddress.getLocalHost();

            // Get IP Address
            byte[] ipAddr = addr.getAddress();

            // Get hostname
            String hostname = addr.getHostAddress();
        } catch (UnknownHostException e) {

        }

        try {
            serverSocket = new ServerSocket(5555);
        } catch (IOException e) {
            System.err.println("Could not listen on port: 5555.");
            System.exit(-1);
        }

        System.out.println("Waiting for connections on port 5555...");

        while (listening) {
            // scanner.hasNext check whether there is a input in terminal
            try {
                // wait for a connection
                GWServerThread job = new GWServerThread(serverSocket.accept(), KVgw);
                // start a new thread to handle the connection
                Thread t = new Thread(job);
                t.start();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }


        try {
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

// manual end
class InputThread implements Runnable{

    public void run() {
        try{
            Scanner sc = new Scanner(System.in);
            if(sc.hasNext()){
                System.exit(0);
            }
        }
        catch (Exception e) {

        }
    }
}

public class GWServer {
    public GWServer() {
        // terminal check exit thread
        Thread end = new Thread(new InputThread());
        end.start();

        // KVgw HashMap
        HashMap<String, String> KVgw = new HashMap<>();
        Thread t = new Thread(new TextServer(KVgw));
        t.start();
        System.out.println("Server started.");
    }

    public static void main(String[] args) {
        new GWServer();
    }
}
