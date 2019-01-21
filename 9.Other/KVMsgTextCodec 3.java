package Common.src.com.hw2.common;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

import javafx.util.Pair;

public class KVMsgTextCodec extends KVMsgCodec {

	public static final String CHARSET = "US-ASCII";
	public static final String DELIMITER = " ";
	public static final String END = "\n";

	@Override
	public byte[] toBytes(KVMsg msg) throws Exception {
		String opt = msg.GetOpt();
		String key = msg.GetKey();
		String value = msg.GetValue();
		ArrayList<String> keys = msg.GetKeys();
		ArrayList<Pair<String,String>> key_values = msg.GetKeyValues();
		
		String msgString = "";	
		
		if ((opt.equals(SET)) && isKeyValid(key) && isValueValid(value)) {
			msgString = msg.GetOpt() + DELIMITER + msg.GetKey() + DELIMITER + msg.GetValue() + END;
		} else if (opt.equals(GET) && isKeyValid(key)) {
			msgString = msg.GetOpt() + DELIMITER + msg.GetKey() + END;
		} else if (opt.equals(STATS)) {
			msgString = msg.GetOpt() + END;
		} else if (opt.equals(MULTIGET)) {
			Iterator<String> it = keys.iterator();
			msgString += msg.GetOpt();
			while (it.hasNext()) {
				String ikey = it.next();
				msgString += DELIMITER + ikey;
			}
			msgString += END;
		} else if (opt.equals(MULTISET)) {
			msgString += msg.GetOpt();
			Iterator<Pair<String,String>> it = key_values.iterator();
			while(it.hasNext()) {
				Pair<String, String> key_value = it.next();
				msgString += DELIMITER + key_value.getKey() + DELIMITER + key_value.getValue();
 			}
			msgString += END;
		} else {
			throw new Exception("invalid KV message");
		}
	
		byte data[] = msgString.getBytes(CHARSET);
		return data;
	}

	@Override
	public KVMsg fromBytes(byte[] message) throws Exception {
		ByteArrayInputStream msgStream = new ByteArrayInputStream(message);
		Scanner scanner = new Scanner(new InputStreamReader(msgStream, CHARSET));

		String str = null;
		String key = null;
		String value = null;
		String opt = null;
		ArrayList<String> keys = new ArrayList<String>();
		ArrayList<Pair<String,String>> key_values = new ArrayList<Pair<String, String>>();

		try {
			str = scanner.next();
			System.out.println("option is:" + str);
			if (!str.equals(SET) && !str.equals(GET) && !str.equals(STATS) && !str.equals(MULTISET) && !str.equals(MULTIGET)) {
				throw new Exception("Decoding error: not supported operation " + str);
			}
			opt = str;
			
			if (opt.equals(STATS)) {
				return new KVMsg(opt);
			}
			
			if (opt.equals(GET)) {
				str = scanner.next();
				if (!isKeyValid(str)) {
					throw new Exception("Decoding error: key length is invalid");
				}
				key = str;	
				return new KVMsg(opt, key);
			}
				
			if (opt.equals(SET)) {
				str = scanner.next();
				if (!isKeyValid(str)) {
					throw new Exception("Decoding error: key length is invalid");
				}
				key = str;
				str = scanner.nextLine();
				if (str.length() >= 1) {
					str = str.substring(1);
				}
				if (!isValueValid(str)) {
					throw new Exception("Decoding error: value length is invalid");
				}
				value = str;
				return new KVMsg(opt, key, value);
			}
			
			if (opt.equals(MULTISET)) {
				while (scanner.hasNext()) {
					str = scanner.next();
					if (!isKeyValid(str)) {
						throw new Exception("Decoding error: key length is invalid");
					}
					key = str;

					if (scanner.hasNext()) {
						str = scanner.next();
					} else {
						throw new Exception("Decoding error: key and value does not show up together");
					}
					
					if (!isValueValid(str)) {
						throw new Exception("Decoding error: value length is invalid");
					}
					
					value = str;
					key_values.add(new Pair<String,String>(key, value));					
				}
				return new KVMsg(opt, key_values);
			}
			if (opt.equals(MULTIGET)) {
				while (scanner.hasNext()) {
					str = scanner.next();
					if (!isKeyValid(str)) {
						throw new Exception("Decoding error: key length is invalid");
					}
					key = str;
					keys.add(key);				
				}
				return new KVMsg(keys, opt);
			}
			
		} catch (IOException ioe) {
			throw new Exception("Decode KV message failed");
		} finally {
			scanner.close();
		}
		//return new KVMsg(opt, key, value);
		return null;
	}

	@Override
	public byte[] toBytes(ArrayList<KVMsg> msgs) throws Exception {
		// TODO Auto-generated method stub
		Iterator<KVMsg> it = msgs.iterator();
		StringBuffer mBuffer = new StringBuffer();
		while (it.hasNext()) {
			KVMsg msg = it.next();
			if (msg.GetOpt() != SET && msg.GetOpt() != GET && msg.GetOpt() != STATS || msg.GetKey() == null
					|| msg.GetKey().length() > MAXIMUM_KEY_LEN || msg.GetValue() == null || msg.GetValue().length() > MAXIMUM_VALUE_LEN) {
				throw new Exception("invalid KV message");
			}

			String msgString = msg.GetOpt() + DELIMITER + msg.GetKey() + DELIMITER + msg.GetValue() + END;
			mBuffer.append(msgString);
		}
		byte data[] = String.valueOf(mBuffer).getBytes(CHARSET);
		return data;
	}

	@Override
	public ArrayList<KVMsg> fromBytes2(byte[] message) throws Exception {
		ByteArrayInputStream msgStream = new ByteArrayInputStream(message);
		Scanner scanner = new Scanner(new InputStreamReader(msgStream, CHARSET));

		String str;
		String opt;
		String key;
		String value;
		ArrayList<KVMsg> arraylist = new ArrayList<KVMsg>();

		try {
			while (scanner.hasNext()) {
				str = scanner.next();
				if (!str.equals(SET) && !str.equals(GET) && !str.equals(STATS)) {
					throw new Exception("Decoding error: not supported operation");
				}
				opt = str;

				str = scanner.next();
				if (str.length() == 0 || str.length() > MAXIMUM_KEY_LEN) {
					throw new Exception("Decoding error: key length is invalid");
				}
				key = str;

				str = scanner.nextLine();
				if (str.length() == 0 || str.length() > MAXIMUM_VALUE_LEN) {
					throw new Exception("Decoding error: value length is invalid");
				}
				value = str;
				arraylist.add(new KVMsg(opt, key, value));
			}

		} catch (IOException ioe) {
			throw new Exception("Decode KV message failed");
		}
		scanner.close();
		return arraylist;
	}

}
