package com.hw2.common;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class BinarySendRecvHelper {
	private Socket socket;
	public BinarySendRecvHelper(Socket socket) {
		this.socket = socket;
	}
	
	public void sendBytes(byte[] byteArray) throws IOException {
		sendBytes(byteArray, 0, byteArray.length);
	}
	
	public void sendBytes(byte[] byteArray, int offset, int len) throws IOException, EOFException {
		if (len == 0) {
			return;
		}
	    if (len < 0) {
	        throw new IOException("Sending length is negative");
	    }
	    
	    if (offset < 0 || offset >= byteArray.length) {
	        throw new IOException("Sending length is larger than data length");
	    }
	    
	    OutputStream os = socket.getOutputStream(); 
	    DataOutputStream dos = new DataOutputStream(os);

	    dos.writeInt(len);
	    dos.write(byteArray, offset, len);	    
	}
	
	
	public byte[] readBytes() throws IOException, EOFException {	
		InputStream in = socket.getInputStream();
	    DataInputStream dis = new DataInputStream(in);

	    int len = dis.readInt();
	    byte[] data = new byte[len];
	    
	    if (len > 0) {
	        dis.readFully(data);
	    }
	    return data;
	}
}
