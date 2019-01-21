import java.util.HashMap;
import java.util.Hashtable;

public class KVStorer {
    private HashMap<String,String> kvStorer = new HashMap<>();
    private int keyLen = 0;
    private int valueLen = 0;

    public KVStorer(int keyLen,int valueLen){
        this.keyLen = keyLen;
        this.valueLen = valueLen;
    }

    public Boolean Set(String key,String value){
        if(key == null|| value == null){
            System.out.println("key or value is null.");
            return false;
        }
        if (key.length() > keyLen){
            System.out.println("key length is larger than maximum length: " + keyLen);
        }
        if(value.length() > valueLen){
            System.out.println("value length is larger than maximum length: " + valueLen);
        }
        kvStorer.put(key,value);
        return true;
    }

    public String Get(String key){
        return (String) kvStorer.get(key);
    }

    public int Stats(){
        return kvStorer.size();
    }
}
