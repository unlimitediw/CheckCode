package com.hw2.test;

import java.io.IOException;
import java.net.BindException;
import java.net.ConnectException;
import java.net.InetSocketAddress;
import java.net.SocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.ClosedChannelException;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.SocketChannel;
import java.util.ArrayList;

import java.util.Iterator;
import java.util.Random;
import java.util.Set;

import com.hw2.common.KVMsg;
import com.hw2.common.KVMsgBinaryCodec;
import com.hw2.common.KVMsgCodec;
import com.hw2.common.KVMsgTextCodec;

class StatisticHelper {
	public long start_time = 0;
	public int total_clients = 0;
	public int total_success_conn = 0;
	public int total_failed_conn = 0;
	public long total_connect_latency = 0;
	public long total_request_latency = 0;
	public int total_success_requests = 0;
	public int total_failed_requests = 0;
	public long total_sendbytes = 0;
	public long total_recvbytes = 0;
	public long max_connect_latency = 0;
	public long min_connect_latency = Long.MAX_VALUE;
	public long max_request_latency = 0;
	public long min_request_latency = Long.MAX_VALUE;
	
	StatisticHelper(int total_clients) {
		this.total_clients = total_clients;
		this.start_time = System.currentTimeMillis();
	}

	void ProduceReport() {
		try {
			double total_time_cost = System.currentTimeMillis() - start_time;
			long avarage_connection_latency = total_connect_latency / total_success_conn;
			long avarage_success_request_latency = total_request_latency / total_success_requests;
			System.out.println("Performance Test Report:");
			System.out.println("Total Time Cost:" + total_time_cost + "(ms)");
			System.out.println("Tried " + total_clients + " times");
			System.out.println("Success Connections:" + total_success_conn);
			System.out.println("Failed Connections:" + total_failed_conn);
			System.out.println("Number of Requests per second:" + total_success_requests / (total_time_cost / 1000));
			System.out.println("Average Connection Established Latency:" + avarage_connection_latency + "(ms)");
			System.out.println("Maximum Connection Established Latency:" + max_connect_latency+ "(ms)");
			System.out.println("Minimum Connection Established Latency:" + min_connect_latency + "(ms)");
			System.out.println("Success Requests:" + total_success_requests);
			System.out.println("Failed Requests:" + total_failed_requests);
			System.out.println("Average Request Latency:" + avarage_success_request_latency + "(ms)");
			System.out.println("Maximum Request Latency:" + max_request_latency + "(ms)");
			System.out.println("Minimum Request Latency:" + min_request_latency + "(ms)");
			System.out.println("Total Send Bytes:" + total_sendbytes + "Bytes");
			System.out.println("Total Recv Bytes:" + total_recvbytes + "Bytes");
			
		} catch (ArithmeticException ae) {
			System.out.println("Error: divied by zero");
		}
	}

	void ByteRecved(int len) {
		total_recvbytes += len;
	}

	void ByteWritten(int len) {
		total_sendbytes += len;
	}

	void SuccessOneConn() {
		total_success_conn++;
	}

	void FailedOneConn() {
		total_failed_conn++;
	}

	void SuccessOneRequest() {
		total_success_requests++;
	}

	void FailedOneRequest() {
		total_failed_requests++;
	}

	void ConnectLatency(long duration) {
		if (duration > max_connect_latency) {
			max_connect_latency = duration;
		} 
		if (duration < min_connect_latency) {
			min_connect_latency = duration;
		}
		
		total_connect_latency += duration;
	}

	void RequestLatency(long duration) {
		if (duration > max_request_latency) {
			max_request_latency = duration;
		} 
		
		if (duration < min_request_latency) {
			min_request_latency = duration;
		}
		
		total_request_latency += duration;
	}
}

class Client {
	public static final String allChar = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	public long conn_begin_time = 0;
	public long request_begin_time = 0;
	public SocketChannel sc = null;
	public StatisticHelper sh = null;
	private ByteBuffer bytebuffer = null; // buffer used to write data
	private ByteBuffer recvBuffer = ByteBuffer.allocate(1000); // buffer used to recv data
	private Selector selector = null;
	private int send_bytes = 0;
	private boolean finish4BytesLenthRead = false;
	private int content_length = 0;
	private String recv_text_content = "";

	Client(SocketChannel sc, StatisticHelper sh, Selector selector) {
		this.sc = sc;
		this.conn_begin_time = System.currentTimeMillis();
		this.sh = sh;
		this.selector = selector;
	}

	public void handleRead(boolean isBinaryProtocol) throws IOException {
		// recv response
		if (!isBinaryProtocol) {
			try {
				recvBuffer.clear();
				int readBytes = sc.read(recvBuffer);
				if (readBytes > 0) {
					recvBuffer.flip();
					byte[] bytes = new byte[recvBuffer.remaining()];
					recvBuffer.get(bytes);
					recv_text_content += new String(bytes);			
					if (recv_text_content.endsWith("\n")) {
						sh.RequestLatency(System.currentTimeMillis() - this.request_begin_time);
						sc.close();
						sh.SuccessOneRequest();
						sh.ByteRecved(recv_text_content.length());
						sh.ByteWritten(this.send_bytes);
						//System.out.println("success one request");
						System.out.println(recv_text_content);
					} else {
						System.out.println("Uncomplete message");
					}
				} else if (readBytes < 0) {
					sc.close();
					sh.FailedOneRequest();
					System.out.println("server close the connection");
				} else {
					System.out.println("not enough buffer capacity");
					sc.close();
					sh.FailedOneRequest();
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				sc.close();
				sh.FailedOneRequest();
			}

		} else {
			try {
				int readBytes = sc.read(recvBuffer);
				String content = "";
				if (readBytes > 0) {
					if (!finish4BytesLenthRead && readBytes < 4) {
						return;
					} else if (!finish4BytesLenthRead) {
						recvBuffer.flip();
						byte[] length = new byte[4];
						recvBuffer.get(length);
						ByteBuffer wrapped = ByteBuffer.wrap(length);
						content_length = wrapped.getInt();
						finish4BytesLenthRead = true;
					} 
					
					if (finish4BytesLenthRead) {
						// finish 4 bytes length read
						int remainLen = recvBuffer.remaining();
						if (content_length == remainLen) {
							byte[] bytes = new byte[remainLen];
							recvBuffer.get(bytes);
							content += new String(bytes);
							System.out.println(content);

							sh.RequestLatency(System.currentTimeMillis() - this.request_begin_time);
							sc.close();
							sh.SuccessOneRequest();
							sh.ByteRecved(content_length + 4);
							sh.ByteWritten(this.send_bytes);
							// System.out.println("success one request");
						}
					}
				} else if (readBytes < 0) {
					sc.close();
					sh.FailedOneRequest();
					System.out.println("server close the connection");
				} else {
					System.out.println("not enough buffer capacity");
					sc.close();
					sh.FailedOneRequest();
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				sc.close();
				sh.FailedOneRequest();
			}
		}

	}

	public void handleWrite() throws IOException {
		try {
			sc.write(bytebuffer);
			if (bytebuffer.hasRemaining()) {
				sc.register(selector, SelectionKey.OP_WRITE, this);
			}
		} catch (IOException ioe) {
			ioe.printStackTrace();
			sc.close();
			sh.FailedOneRequest();
		}

		// System.out.println("Sent msg to server success");
	}

	public void sendMsg(String opt, boolean isBinaryProtocol) throws IOException {
		if (opt.equals("SET")) {
			String key = generateString(5);
			String value = generateString(10);
			KVMsg msg = new KVMsg("SET", key, value);
			sendMsg(msg, isBinaryProtocol);
		} else if (opt.equals("GET")) {
			String key = generateString(5);
			KVMsg msg = new KVMsg("GET", key);
			sendMsg(msg, isBinaryProtocol);
		} else if (opt.equals("STATS")) {
			KVMsg msg = new KVMsg("STATS");
			sendMsg(msg, isBinaryProtocol);
		} else if (opt.equals("MULTISET")) {
			System.out.println("Not supported test");
		} else if (opt.equals("MULTIGET")) {
			String key1 = generateString(5);
			String key2 = generateString(5);
			String key3 = generateString(5);

			ArrayList<String> keys = new ArrayList<String>();
			keys.add(key1);
			keys.add(key2);
			keys.add(key3);
			KVMsg msg = new KVMsg(keys, "MULTIGET");
			sendMsg(msg, isBinaryProtocol);
		}
	}

	public void sendMsg(KVMsg msg, boolean isBinaryProtocol) throws IOException {
		// send msgs
		if (!isBinaryProtocol) {
			try {
				KVMsgCodec codec = new KVMsgTextCodec();
				byte[] bstream = codec.toBytes(msg);
				bytebuffer = ByteBuffer.allocate(bstream.length);
				bytebuffer.put(bstream);
				bytebuffer.flip();
				this.request_begin_time = System.currentTimeMillis();
				sc.write(bytebuffer);
				if (bytebuffer.hasRemaining()) {
					sc.register(selector, SelectionKey.OP_WRITE, this);
				}
				this.send_bytes += bstream.length;
				// System.out.println("Sent msg to server success");
			} catch (IOException ioe) {
				ioe.printStackTrace();
				sc.close();
				sh.FailedOneRequest();
			} catch (Exception e) {
				e.printStackTrace();
				sc.close();
				sh.FailedOneRequest();
			}
		} else {
			try {
				KVMsgCodec codec = new KVMsgBinaryCodec();
				byte[] bstream = codec.toBytes(msg);
				bytebuffer = ByteBuffer.allocate(4 + bstream.length);
				bytebuffer.putInt(bstream.length);
				bytebuffer.put(bstream);
				bytebuffer.flip();
				this.request_begin_time = System.currentTimeMillis();
				sc.write(bytebuffer);
				if (bytebuffer.hasRemaining()) {
					sc.register(selector, SelectionKey.OP_WRITE, this);
				}
				this.send_bytes += 4 + bstream.length;
				// System.out.println("Sent msg to server success");
			} catch (IOException ioe) {
				ioe.printStackTrace();
				sc.close();
				sh.FailedOneRequest();
			} catch (Exception e) {
				e.printStackTrace();
				sc.close();
				sh.FailedOneRequest();
			}
		}

	}

	public void handleConnected() {

	}

	public static String generateString(int length) {
		StringBuffer sb = new StringBuffer();
		Random random = new Random();
		for (int i = 0; i < length; i++) {
			sb.append(allChar.charAt(random.nextInt(allChar.length())));
		}
		return sb.toString();
	}
}

public class PerformanceTestClient {

	public void doTest(int server_port, String server_ip, String opt, int requests) {
		Selector selector = null;
		try {
			boolean isBinaryProtocol = server_port == 5555 ? false : true;

			if (opt.equals("MULTISET")) {
				System.out.println(
						"Not supported command test\n");
				System.exit(-1);
			}
			StatisticHelper sh = new StatisticHelper(requests);
			SocketAddress server_addr = new InetSocketAddress(server_ip, server_port);
			selector = Selector.open();

			// create 100 clients
			for (int i = 0; i < requests; i++) {
				SocketChannel channel = SocketChannel.open();
				channel.socket().setReuseAddress(true);
				Client cl = new Client(channel, sh, selector);
				channel.configureBlocking(false);
				if (channel.connect(server_addr)) {
					SelectionKey sk = channel.register(selector, SelectionKey.OP_READ, cl);
					sh.ConnectLatency(System.currentTimeMillis() - cl.conn_begin_time);
					sh.SuccessOneConn();
					// System.out.println("Connect to server success");
					cl.sendMsg(opt, isBinaryProtocol);
				} else {
					SelectionKey sk = channel.register(selector, SelectionKey.OP_CONNECT, cl);
				}
			}
			int i = 0;
			while (!selector.keys().isEmpty()) {
				i++;
				selector.select(100);
				Set<SelectionKey> keys = selector.selectedKeys();
				Iterator<SelectionKey> it = keys.iterator();
				SelectionKey key = null;
				while (it.hasNext()) {
					key = it.next();
					it.remove();
					Client cl = (Client) key.attachment();
					try {
						if (key.isConnectable()) {
							if (cl.sc.finishConnect()) {
								// connection is created
								sh.ConnectLatency(System.currentTimeMillis() - cl.conn_begin_time);
								sh.SuccessOneConn();
								cl.sc.register(selector, SelectionKey.OP_READ, cl);
								// System.out.println("Connected to server");
								cl.sendMsg(opt, isBinaryProtocol);
							} else {
								System.out.println("connect to server failed");
								sh.FailedOneConn();
							}
						} else if (key.isReadable()) {
							// System.out.println("Readable");
							cl.handleRead(isBinaryProtocol);
						} else if (key.isWritable()) {
							// System.out.println("Writable");
							cl.handleWrite();
						}
					} catch (ConnectException ce) {
						System.out.println("connection exception:" + ce.getMessage());
						sh.FailedOneConn();
						cl.sc.close();
					} catch (BindException eb) {
						eb.printStackTrace();
						sh.FailedOneConn();
						cl.sc.close();
					}
				}

			}

			sh.ProduceReport();
			System.out.println("Finish performance test");
		} catch (ConnectException ce) {
			ce.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {

		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		if (args.length < 4) {
			System.out.println(
					"Invalid parameter input, please input parameter:  <server_ip> <server_port> <operation> <requests>...\n");
			System.exit(-1);
		}

		int server_port = Integer.parseInt(args[1]);
		String server_ip = args[0];
		String opt = args[2];
		int requests = Integer.parseInt(args[3]);

		PerformanceTestClient ptc = new PerformanceTestClient();
		ptc.doTest(server_port, server_ip, opt, requests);

	}

}
