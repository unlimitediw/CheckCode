package Common.src.com.hw2.common;

import java.util.ArrayList;

public abstract class KVMsgCodec {
	public static final int MAXIMUM_KEY_LEN = 64;
	public static final int MAXIMUM_VALUE_LEN = 1024;
	public static final String SET = "SET";
	public static final String GET = "GET";
	public static final String STATS = "STATS";
	public static final String MULTISET = "MULTISET";
	public static final String MULTIGET = "MULTIGET";
	
	public static final int SET_CODE = 1;
	public static final int GET_CODE = 2;
	public static final int STATS_CODE = 3;
	public static final int MULTISET_CODE = 4;
	public static final int MULTIGET_CODE = 5;

	public abstract byte[] toBytes(KVMsg msg) throws Exception;

	public abstract byte[] toBytes(ArrayList<KVMsg> msgs) throws Exception;

	public abstract KVMsg fromBytes(byte[] input) throws Exception;

	public abstract ArrayList<KVMsg> fromBytes2(byte[] input) throws Exception;
	
	boolean isKeyValid(String key) {
		if (key != null && key.length() < MAXIMUM_KEY_LEN) {
			return true;
		} else {
			return false;
		}
	}
	
	boolean isValueValid(String value) {
		if (value != null && value.length() < MAXIMUM_VALUE_LEN) {
			return true;
		} else {
			return false;
		}
	}

}
