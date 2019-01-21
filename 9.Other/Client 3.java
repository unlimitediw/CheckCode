package KVStoreClient.src.com.hw2.client;

import java.io.BufferedReader;
import java.io.EOFException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Iterator;

import Common.src.com.hw2.common.*;

import javafx.util.Pair;

public class Client {
	public void sendAndRecvMsgs(KVMsg message, int portnum, Socket sock) throws IOException, Exception {
		if (portnum == 5555) {
			// use text protocol
			KVMsgCodec codec = new KVMsgTextCodec();
			byte[] bstream = codec.toBytes(message);
			OutputStream os = sock.getOutputStream();
			os.write(bstream);

			// receive response
			BufferedReader buffer_reader = new BufferedReader(new InputStreamReader(sock.getInputStream()));
			String response = buffer_reader.readLine();
			System.out.println(response);

		} else if (portnum == 6666) {

			// use binary protocol
			KVMsgCodec codec = new KVMsgBinaryCodec();
			byte[] bstream = codec.toBytes(message);
			BinarySendRecvHelper sendrecvHelper = new BinarySendRecvHelper(sock);
			sendrecvHelper.sendBytes(bstream);
			
			byte[] response = sendrecvHelper.readBytes();
			String str_res = new String(response);
			System.out.println(str_res);

		} else {
			System.out.println("Wrong server port");
		}

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		if (args.length < 3) {
			System.out.println(
					"Invalid parameter input, please input parameter:  <server_ip> <server_port> <operation> <key> <value>...\n");
			System.exit(-1);
		}
		
		ArrayList<KVMsg> msgs = new ArrayList<KVMsg>();
		String host = args[0];
		int portnum = Integer.parseInt(args[1]);
		String opt = args[2];

		if (opt.equals("SET")) {
			if (args.length < 5 || (args.length % 2) != 1) {
				System.out.println(
						"Invalid parameter input, please input parameter: <server_ip> <server_port> <operation> <key> <value>...\n");
				System.exit(-1);
			} else {
				for (int i = 3; i < args.length; i+=2) {
					String key = args[i];
					String value = args[i+1];
					msgs.add(new KVMsg(opt, key, value));
				}
			}
		} else if (opt.equals("GET")) {
			if (args.length < 4) {
				System.out.println(
						"Invalid parameter input, please input parameter:  <server_ip> <server_port> <operation> <key> <value>...\n");
				System.exit(-1);
			} else {
				for (int i = 3; i < args.length; i++) {
					String key = args[i];
					msgs.add(new KVMsg(opt, key));
				}
			}
		} else if (opt.equals("STATS")) {
			msgs.add(new KVMsg(opt));
		} else if (opt.equals("MULTISET")) {
			if (args.length < 5 || (args.length % 2) != 1) {
				System.out.println(
						"Invalid parameter input, please input parameter:  <server_ip> <server_port> <operation> <key> <value>...\n");
				System.exit(-1);
			} else {
				ArrayList<Pair<String, String>> key_values = new ArrayList<Pair<String, String>>();
				for (int i = 3; i < args.length; i+=2) {
					String key = args[i];
					String value = args[i+1];
					key_values.add(new Pair<String,String>(key,value));					
				}
				msgs.add(new KVMsg(opt, key_values));
			} 
		} else if (opt.equals("MULTIGET")) {
			if (args.length < 4) {
				System.out.println(
						"Invalid parameter input, please input parameter:  <server_ip> <server_port> <operation> <key> <value>...\n");
				System.exit(-1);
			} else {
				ArrayList<String> keys = new ArrayList<String>();
				for (int i = 3; i < args.length; i++) {
					String key = args[i];
					keys.add(key);
				}
				msgs.add(new KVMsg(keys, opt));
			}
		} else {
			System.out.println("Invalid opteration:" + opt);
			System.exit(-1);
		}
		
		//System.out.println("server:" + host + " port:" + portnum + " opt:" + opt + " key:" + key + " value:" + value);
		//System.out.println("key is " + key);

		// Your code here!
		Socket sock = null;
		Client cl = new Client();
		try {
			sock = new Socket(host, portnum);
			System.out.println("connect to " + host + ":" + portnum + " success\n");
			
			Iterator<KVMsg> it = msgs.iterator();
			while (it.hasNext()) {
				KVMsg msg = it.next();
				//System.out.println("Msg" + i + " opt:" + msg.GetOpt() + " key:" + msg.GetKey() + " value:" + msg.GetValue());
				cl.sendAndRecvMsgs(msg, portnum, sock);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				if (sock != null) {
					sock.close();
					sock = null;
				}
				/*
				 * if (out != null) { out.close(); out = null; }
				 */
				System.out.println("Done\n");
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}

	}
}
