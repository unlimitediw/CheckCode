import javafx.util.Pair;

import java.io.*;
import java.util.ArrayList;
import java.util.Iterator;

public class KVMsgBinaryCodec extends KVMsgCodec {
    @Override
    public byte[] toBytes(KVMsg msg) throws Exception{
        // TODO Auto-generated method stub
        ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
        DataOutputStream out = new DataOutputStream(byteStream);

        // Write option code first
        int optcode = 0;
        if(msg.getOpt().equals(SET)){
            optcode = SET_CODE;
            out.writeByte(optcode);

            if(!isKeyValid(msg.getKey())){
                throw new Exception("key length is larger than the maximum");
            }
            out.writeUTF(msg.getKey());
            if(!isValueValid(msg.getValue())){
                throw new Exception("value length is larger than the maximum");
            }

            out.writeUTF(msg.getValue());
            out.flush();
        }else if(msg.getOpt().equals(GET)){
            optcode = GET_CODE;
            out.writeByte(optcode);

            if(!isKeyValid(msg.getKey())){
                throw new Exception("key length is larger than the maximum");
            }
            out.writeUTF(msg.getKey());
            out.flush();
        }else if(msg.getOpt().equals(STATS)){
            optcode = STATS_CODE;
            out.write(optcode);
            out.flush();
        }else if(msg.getOpt().equals(MULTISET)){
            optcode = MULTISET_CODE;
            out.writeByte(optcode);
            ArrayList<Pair<String,String>> keyValues = msg.getKeyValues();
            Iterator<Pair<String,String>> it = keyValues.iterator();
            while(it.hasNext()){
                Pair<String,String> keyValue = it.next();
                out.writeUTF(keyValue.getKey());
                out.writeUTF(keyValue.getValue());
            }
            out.flush();
        }else if(msg.getOpt().equals(MULTIGET)){
            optcode = MULTIGET_CODE;
            out.writeByte(optcode);
            ArrayList<String> keys = msg.getKeys();
            Iterator<String> it = keys.iterator();
            while(it.hasNext()){
                String key = it.next();
                out.writeUTF(key);
            }
            out.flush();
        }else{
            throw new Exception("not supported operation");
        }
        byte[] data = byteStream.toByteArray();
        return data;
    }

    @Override
    public byte[] toBytes(ArrayList<KVMsg> msgs) throws Exception{
        return null;
    }

    @Override
    public KVMsg fromBytes(byte[] message) throws Exception{
        ByteArrayInputStream bs = new ByteArrayInputStream(message);
        DataInputStream in = new DataInputStream(bs);

        String opt;
        String key;
        String value;
        ArrayList<Pair<String,String>> keyValues = new ArrayList<>();
        ArrayList<String> keys = new ArrayList<>();

        int optcode = in.readByte();
        //here use isKeyValid
        if(optcode == SET_CODE){
            opt = SET;
            key = in.readUTF();
            if (!isKeyValid(key)) {
                throw new Exception("invalid key");
            }
            value = in.readUTF();
            if(!isValueValid(value)){
                throw new Exception("invalid value");
            }
            return new KVMsg(opt,key,value);
        }else if(optcode == GET_CODE){
            opt = STATS;
            key = in.readUTF();
            if(!isKeyValid(key)){
                throw new Exception("invalid key");
            }
            return new KVMsg(opt,key);
        }else if(optcode == STATS_CODE){
            opt = STATS;
            return new KVMsg(opt);
        }else if(optcode == MULTIGET_CODE){
            opt = MULTIGET;
            try{
                while(true){
                    String ikey = in.readUTF();
                    keys.add(ikey);
                }
            }catch(EOFException ee){

            }catch(IOException ioe){
                ioe.printStackTrace();
            }
            return new KVMsg(keys,opt);
        }else if(optcode == MULTISET_CODE){
            opt = MULTISET;
            try{
                while (true){
                    String ikey = in.readUTF();
                    String ivalue = in.readUTF();
                    keyValues.add(new Pair<String,String>(ikey,ivalue));
                }
            }catch(EOFException ee){

            }catch(IOException ioe){
                //ioe.printStackTrace();
            }
            return new KVMsg(opt,keyValues);
        }else{
            throw new Exception("unknown operation code");
        }
    }

    @Override
    public ArrayList<KVMsg> fromBytes2(byte[] input) throws Exception{
        return null;
    }
}
