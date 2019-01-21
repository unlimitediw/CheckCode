import javafx.util.Pair;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class KVMsgTextCodec extends KVMsgCodec {
    public static final String CHARSET = "US-ASCII";
    public static final String DELIMITER = " ";
    public static final String END = "\n";

    @Override
    public byte[] toBytes(KVMsg msg) throws Exception {
        String opt = msg.getOpt();
        String key = msg.getKey();
        String value = msg.getValue();
        ArrayList<String> keys = msg.getKeys();
        ArrayList<Pair<String, String>> keyValues = msg.getKeyValues();

        String msgString = "";
        if ((opt.equals(SET)) && isKeyValid(key) && isValueValid(value)) {
            msgString = msg.getOpt() + DELIMITER + msg.getKey() + DELIMITER + msg.getValue() + END;
        } else if (opt.equals(GET) && isKeyValid(key)) {
            msgString = msg.getOpt() + DELIMITER + msg.getKey() + END;
        } else if (opt.equals(STATS)) {
            msgString = msg.getOpt() + END;
        } else if (opt.equals(MULTIGET)) {
            Iterator<String> it = keys.iterator();
            msgString += msg.getOpt();
            while (it.hasNext()) {
                String ikey = it.next();
                msgString += DELIMITER + ikey;
            }
            msgString += END;
        } else if (opt.equals(MULTISET)) {
            msgString += msg.getOpt();
            Iterator<Pair<String, String>> it = keyValues.iterator();
            while (it.hasNext()) {
                Pair<String, String> keyValue = it.next();
                msgString += DELIMITER + keyValue.getKey() + DELIMITER + keyValue.getValue();
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
        ArrayList<String> keys = new ArrayList<>();
        ArrayList<Pair<String, String>> keyValues = new ArrayList<>();

        try {
            str = scanner.next();
            System.out.println("option is: " + str);
            if (!str.equals(SET) && !str.equals(GET) && !str.equals(STATS) && !str.equals(MULTISET) && !str.equals(MULTIGET)) {
                throw new Exception("Decoding error: not supported operation" + str);
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
                    keyValues.add(new Pair<String, String>(key, value));
                }
                return new KVMsg(opt, keyValues);
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
        return null;
    }

    @Override
    public byte[] toBytes(ArrayList<KVMsg> msgs) throws Exception {
        Iterator<KVMsg> it = msgs.iterator();
        StringBuffer mBuffer = new StringBuffer();
        while (it.hasNext()) {
            KVMsg msg = it.next();
            if (msg.getOpt() != SET && msg.getOpt() != GET && msg.getOpt() != STATS || msg.getKey() == null ||
                    msg.getKey().length() > MAXIMUM_KEY_LEN || msg.getValue() == null ||
                    msg.getValue().length() > MAXIMUM_VALUE_LEN) {
                throw new Exception("invalid KV message");
            }
            String msgString = msg.getOpt() + DELIMITER + msg.getKey() + DELIMITER + msg.getValue() + END;
            mBuffer.append(msgString);
        }
        byte data[] = String.valueOf(mBuffer).getBytes(CHARSET);
        return data;
    }

    @Override
    public ArrayList<KVMsg> fromBytes2(byte[] message) throws Exception {
        ByteArrayInputStream msgStream = new ByteArrayInputStream(message);
        Scanner scanner = new Scanner(new InputStreamReader(msgStream,CHARSET));

        String str;
        String opt;
        String key;
        String value;

        ArrayList<KVMsg> arrayList = new ArrayList<KVMsg>();

        try{
            while(scanner.hasNext()){
                str = scanner.next();
                if (!str.equals(SET) && !str.equals(GET) && !str.equals(STATS)){
                    throw new Exception("Decoding error: not supported operation");
                }
                opt = str;
                if(str.length() == 0||str.length() > MAXIMUM_KEY_LEN){
                    throw new Exception("Decoding error: key length is invalid");
                }
                key = str;

                str = scanner.next();
                if(str.length() == 0|| str.length() > MAXIMUM_VALUE_LEN){
                    throw new Exception("Decoding error: value length is invalid");
                }
                value = str;
                arrayList.add(new KVMsg(opt,key,value));
            }
        }catch(IOException ioe){
            throw new Exception("Decode KV message failed");
        }
        scanner.close();
        return arrayList;
    }
}
