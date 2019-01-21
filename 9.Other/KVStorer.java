package com.hw2;

import java.util.Hashtable;

public class KVStorer {
	private Hashtable kvstorer = new Hashtable();
	private int keyLen = 0;
	private int valueLen = 0;

	public KVStorer(int keyLen, int valueLen) {
		this.keyLen = keyLen;
		this.valueLen = valueLen;
	}
	
	public Integer Set(String key, String value) {
		if (key == null || value == null) {
			System.out.println("key or value is null");
			return -1;
		} 
		
		if (key.length() > keyLen) {
			System.out.println("key length is larger than the maximum");
			return -1;
		}
		if (value.length() > valueLen) {
			System.out.println("value length is larger than the maximum");
			return -1;
		}
		
		String ori = (String) kvstorer.put(key, value);
		return 0;
	}
	
	public String Get(String key) {
		return (String) kvstorer.get(key);
	}
	
	public int Stats() {
		return kvstorer.size();
	}
	
}
