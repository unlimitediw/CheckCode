package com.hw2;

import java.util.ArrayList;
import java.util.Iterator;

import com.hw2.common.KVMsg;

import javafx.util.Pair;

public abstract class AbstractServerThread {
	private KVStorer kvstorer = null;
	public AbstractServerThread(KVStorer kvstorer) {
		this.kvstorer = kvstorer;
	}
	
	public String Process(KVMsg msg) {
		if (msg.GetOpt().equals("SET")) {
			if (kvstorer.Set(msg.GetKey(), msg.GetValue()) == -1) {
				return new String("SET key:" + msg.GetKey() + " value:" + msg.GetValue() + " failed\n");
			} else {
				return new String("SET key:" + msg.GetKey() + " value:" + msg.GetValue() + " success\n");
			}
		}

		if (msg.GetOpt().equals("GET")) {
			return ("GET key:" + msg.GetKey() + " result is:" +  kvstorer.Get(msg.GetKey()) + "\n");
		}

		if (msg.GetOpt().equals("STATS")) {
			return ("STATS is " + String.valueOf(kvstorer.Stats()) + "\n");
		}

		if (msg.GetOpt().equals("MULTISET")) {
			String response = "";
			ArrayList<Pair<String, String>> key_values = msg.GetKeyValues();
			Iterator<Pair<String,String>> it = key_values.iterator();
			while(it.hasNext()) {
				Pair<String, String> key_value = it.next();
				if (kvstorer.Set(key_value.getKey(), key_value.getValue()) == -1) {
					response += "SET key:value (" + key_value.getKey() + "," + key_value.getValue() + ") failed.";
				} else {
					response += "SET key:value (" + key_value.getKey() + "," + key_value.getValue() + ") success.";
				}
 			}
			return response;
		} 
		
		if (msg.GetOpt().equals("MULTIGET")) {
			String response = "";
			ArrayList<String> keys = msg.GetKeys();
			Iterator<String> it = keys.iterator();
			while(it.hasNext()) {
				String ikey = it.next();
				String ivalue = kvstorer.Get(ikey);			
				response += "GET key:" + ikey + ", value:" + ivalue + ". ";			
 			}
			return response;
		} 
		return new String("Not supported operation:" + msg.GetOpt() + ".");
	}
}
