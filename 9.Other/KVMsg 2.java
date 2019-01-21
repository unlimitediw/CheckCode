import javafx.util.Pair;

import java.util.ArrayList;

public class KVMsg {
    private String key;
    private String value;
    private String opt;
    private ArrayList<String> keys;
    private ArrayList<Pair<String, String>> keyValues;

    public KVMsg(String opt, String key, String value) {
        this.opt = opt;
        this.key = key;
        this.value = value;
        this.keyValues = null;
        this.keys = null;
    }

    public KVMsg(String opt){
        this.opt = opt;
        this.key = null;
        this.value = null;
        this.keys = null;
        this.keyValues = null;
    }

    public KVMsg(String opt,String key){
        this.opt = opt;
        this.key = key;
        this.value = null;
        this.keyValues = null;
        this.keys = null;
    }

    public KVMsg(String opt, ArrayList<Pair<String,String>> keyValues){
        this.opt = opt;
        this.keyValues = keyValues;
        this.key = null;
        this.value = null;
        this.keys = null;
    }

    public KVMsg(ArrayList<String> keys, String opt){
        this.opt = opt;
        this.key = null;
        this.value = null;
        this.keys = keys;
        this.keyValues = null;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public String getOpt() {
        return opt;
    }

    public void setOpt(String opt) {
        this.opt = opt;
    }


    public ArrayList<String> getKeys() {
        return keys;
    }

    public ArrayList<Pair<String, String>> getKeyValues() {
        return keyValues;
    }
}
