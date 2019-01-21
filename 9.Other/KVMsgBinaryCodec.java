package com.hw2.common;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;

import javafx.util.Pair;

public class KVMsgBinaryCodec extends KVMsgCodec {
	@Override
	public byte[] toBytes(KVMsg msg) throws Exception {
		// TODO Auto-generated method stub
		ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
		DataOutputStream out = new DataOutputStream(byteStream);
		
		//Write option code first
		int optcode = 0;
		if (msg.GetOpt().equals(SET)) {
			optcode = SET_CODE;
			out.writeByte(optcode);
			
			if (!isKeyValid(msg.GetKey())) {
				throw new Exception("key length is larger than the maximum");
			} 
			out.writeUTF(msg.GetKey());
			
			if (!isValueValid(msg.GetValue())) {
				throw new Exception("value length is larger than the maximum");
			}
			
			out.writeUTF(msg.GetValue());
			out.flush();
		} else if (msg.GetOpt().equals(GET)) {
			optcode = GET_CODE;
			out.writeByte(optcode);
			
			if (!isKeyValid(msg.GetKey())) {
				throw new Exception("key length is larger than the maximum");
			} 
			out.writeUTF(msg.GetKey());
			out.flush();
		} else if (msg.GetOpt().equals(STATS)) {
			optcode = STATS_CODE;
			out.writeByte(optcode);
			out.flush();
			
		} else if (msg.GetOpt().equals(MULTISET)) {
			optcode = MULTISET_CODE;
			out.writeByte(optcode);
			ArrayList<Pair<String,String>> key_values = msg.GetKeyValues();
			Iterator<Pair<String,String>> it = key_values.iterator();
			while(it.hasNext()) {
				Pair<String, String> key_value = it.next();
				out.writeUTF(key_value.getKey());
				out.writeUTF(key_value.getValue());
 			}
			out.flush();
		} else if (msg.GetOpt().equals(MULTIGET)) {
			optcode = MULTIGET_CODE;
			out.writeByte(optcode);
			ArrayList<String> keys = msg.GetKeys();
			Iterator<String> it = keys.iterator();
			while(it.hasNext()) {
				String key = it.next();
				out.writeUTF(key);		
 			}
			out.flush();
		} else {
			throw new Exception("not supported operation");
		}
				
		byte[] data = byteStream.toByteArray();
		return data;
	}

	@Override
	public byte[] toBytes(ArrayList<KVMsg> msgs) throws Exception {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public KVMsg fromBytes(byte[] message) throws Exception {
		// TODO Auto-generated method stub
		ByteArrayInputStream bs = new ByteArrayInputStream(message);
		DataInputStream in = new DataInputStream(bs);
		
		String opt;
		String key;
		String value;
		ArrayList<Pair<String, String>> key_values = new ArrayList<Pair<String, String>>();
		ArrayList<String> keys = new ArrayList<String>();
		
		int optcode = in.readByte();
		if (optcode == SET_CODE) {
			opt = SET;
			key = in.readUTF();
			if (!isKeyValid(key)) {
				throw new Exception("invalid key");
			}
			value = in.readUTF();
			if (!isValueValid(value)) {
				throw new Exception("invalid value");
			}
			return new KVMsg(opt, key, value);
		} else if (optcode == GET_CODE) {
			opt = GET;
			key = in.readUTF();
			if (!isKeyValid(key)) {
				throw new Exception("invalid key");
			}
			return new KVMsg(opt, key);
		} else if (optcode == STATS_CODE) {
			opt = STATS;
			return new KVMsg(opt);
		} else if (optcode == MULTIGET_CODE) {
			opt = MULTIGET;
			try {
				while(true) {
					String ikey = in.readUTF();
					keys.add(ikey);
				}
			} catch (EOFException ee) {
				
			} catch (IOException ioe) {
				ioe.printStackTrace();
			}
			return new KVMsg(keys, opt);
		} else if (optcode == MULTISET_CODE) {
			opt = MULTISET;
			try {
				while(true) {
					String ikey = in.readUTF();
					String ivalue = in.readUTF();
					key_values.add(new Pair<String, String>(ikey, ivalue));
				}
			} catch (EOFException ee) {
				
			} catch (IOException ioe) {
				//ioe.printStackTrace();
			}
			return new KVMsg(opt, key_values);
		} else {
			throw new Exception("unknown operation code");
		}
	}

	@Override
	public ArrayList<KVMsg> fromBytes2(byte[] input) throws Exception {
		// TODO Auto-generated method stub
		return null;
	}

	
}
