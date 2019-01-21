package Common.src.com.hw2.common;

import java.util.ArrayList;
import java.util.HashMap;

import javafx.util.Pair;

public class KVMsg {
	private String key;
	private String value;
	private String opt;
	private ArrayList<Pair<String, String>> key_values;
	private ArrayList<String> keys;
	
	public KVMsg(String opt, String key, String value) {
		this.opt = opt;
		this.key = key;
		this.value = value;
		this.key_values = null;
		this.keys = null;
	}
	
	public KVMsg(String opt) {
		this.opt = opt;
		this.key = null;
		this.value = null;
		this.keys = null;
		this.key_values = null;
	}
	
	public KVMsg(String opt, String key) {
		this.opt = opt;
		this.key = key;
		this.value = null;
		this.key_values = null;
		this.keys = null;
	}
	
	public KVMsg(String opt, ArrayList<Pair<String, String>> key_values) {
		this.key_values = key_values;
		this.opt = opt;
		this.key = null;
		this.value = null;
		this.keys = null;
	}
	
	public KVMsg(ArrayList<String> keys, String opt) {
		this.key_values = null;
		this.opt = opt;
		this.key = null;
		this.value = null;
		this.keys = keys;
	}
	public String GetKey() {
		return key;
	}
	
	public String GetValue() {
		return value;
	}
	
	public void SetKey(String key) {
		this.key = key;
	}
	
	public void SetValue(String value) {
		this.value = value;
	}
	
	public void SetOpt(String opt) {
		this.opt = opt;
	}
	
	public String GetOpt() {
		return opt;
	}
	
	public ArrayList<String> GetKeys() {
		return keys;
	}
	
	public ArrayList<Pair<String, String>> GetKeyValues() {
		return key_values;
	}
}
