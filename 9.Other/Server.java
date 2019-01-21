package com.hw2;

import java.io.BufferedReader;
import java.io.EOFException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Arrays;
import com.hw2.common.*;

class MsgServerThread extends AbstractServerThread implements Runnable {
	private Socket sock;
	private PrintWriter out = null;
	private BufferedReader in = null;
	private KVMsgCodec codec = null;

	public MsgServerThread(Socket s, KVStorer kvstorer) throws SocketException {
		super(kvstorer);
		this.sock = s;
		s.setReuseAddress(true);
		this.codec = new KVMsgTextCodec();
	}

	public void run() {
		System.out.println("Got connection from " + sock.getInetAddress() + ":" + sock.getPort());
		try {
			out = new PrintWriter(sock.getOutputStream(), true);
			in = new BufferedReader(new InputStreamReader(sock.getInputStream()));
			while (true) {
				String n = in.readLine();
				if (n == null) {
					break;
				}

				KVMsg msg = codec.fromBytes(n.getBytes());
				String response = Process(msg);
				System.out.println(response);
				
				//reply client side
				out.println(response);
				//System.out.println("reply client");
			}
			System.out.println("Client " + sock.getInetAddress() + ":" + sock.getPort() + " closed\n");
		} catch (SocketException se) {
			if (se.toString().contains("Socket closed") || se.toString().contains("Connection reset")
                    || se.toString().contains("Broken pipe")) {
            } else {
                System.out.println("Error occured");
            }
		} catch (IOException e) {
			e.printStackTrace();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			// clean things up
			try {
				out.close();
				in.close();
				sock.close();
			} catch (IOException e1) {
				e1.printStackTrace();
			}
		}

	}
}

class BinaryServerThread extends AbstractServerThread implements Runnable {
	private Socket sock;
	private KVMsgCodec codec = null;

	public BinaryServerThread(Socket s, KVStorer kvstorer) throws SocketException {
		super(kvstorer);
		this.sock = s;
		s.setReuseAddress(true);
		this.codec = new KVMsgBinaryCodec();
	}

	public void run() {
		System.out.println("Got connection from " + sock.getInetAddress() + ":" + sock.getPort());
		try {
			while (true) {
				BinarySendRecvHelper sendrecvHelper = new BinarySendRecvHelper(sock);
				byte[] recvmsg = sendrecvHelper.readBytes();
				KVMsg msg = codec.fromBytes(recvmsg);
				String response = Process(msg);
				System.out.println(response);
				
				//reply client side
				byte[] send_bytes = response.getBytes();
				sendrecvHelper.sendBytes(send_bytes);
			}
		} catch (EOFException e) {
			System.out.println("Client " + sock.getInetAddress() + ":" + sock.getPort() + " closed\n");
		} catch (IOException e) {
			System.out.println("recv IOException");
			e.printStackTrace();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			// clean things up
			try {
				sock.close();
			} catch (IOException e1) {
				e1.printStackTrace();
			}
		}

	}
}

class TextServer implements Runnable {
	private ServerSocket serverSocket = null;
	private KVStorer kvstorer = null;
	
	public TextServer(KVStorer kvstorer) {
		this.kvstorer = kvstorer;
	}

	@Override
	public void run() {
		// TODO Auto-generated method stub
		boolean listening = true;
		try {
			InetAddress addr = InetAddress.getLocalHost();

			// Get IP Address
			byte[] ipAddr = addr.getAddress();

			// Get hostname
			String hostname = addr.getHostAddress();
			System.out.println("Server IP = " + hostname);
		} catch (UnknownHostException e) {
			System.out.println("catch execption " + e);
		}

		try {
			serverSocket = new ServerSocket(5555);
		} catch (IOException e) {
			System.err.println("Could not listen on port: 5555.");
			System.exit(-1);
		}
		System.out.println("Waiting for connections on port 5555...");

		while (listening) {
			try {
				// wait for a connection
				MsgServerThread job = new MsgServerThread(serverSocket.accept(), this.kvstorer);				
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
class BinaryServer implements Runnable {
	private ServerSocket serverSocket = null;
	private KVStorer kvstorer = null;
	
	public BinaryServer(KVStorer kvstorer) {
		this.kvstorer = kvstorer;
	}

	@Override
	public void run() {
		// TODO Auto-generated method stub
		boolean listening = true;
		try {
			InetAddress addr = InetAddress.getLocalHost();

			// Get IP Address
			byte[] ipAddr = addr.getAddress();

			// Get hostname
			String hostname = addr.getHostAddress();
			System.out.println("Server IP = " + hostname);
		} catch (UnknownHostException e) {
			System.out.println("catch execption " + e);
		}

		try {
			serverSocket = new ServerSocket(6666);
		} catch (IOException e) {
			System.err.println("Could not listen on port: 6666.");
			System.exit(-1);
		}
		System.out.println("Waiting for connections on port 6666...");

		while (listening) {
			try {
				// wait for a connection
				BinaryServerThread job = new BinaryServerThread(serverSocket.accept(), this.kvstorer);				
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
public class Server {
	private KVStorer kvstorer = null;

	public Server(KVStorer kvstorer) {
		this.kvstorer = kvstorer;
		Thread t1 = new Thread(new TextServer(kvstorer));
		Thread t2 = new Thread(new BinaryServer(kvstorer));
		t1.start();
		System.out.println("t1 started");
		t2.start();
		System.out.println("t2 started");
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		KVStorer kvstorer = new KVStorer(64, 1024);
		new Server(kvstorer);
	}

}
