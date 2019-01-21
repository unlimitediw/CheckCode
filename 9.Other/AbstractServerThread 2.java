public class AbstractServerThread {
    private KVStorer kvStorer;
    public AbstractServerThread(KVStorer kvStorer){
        this.kvStorer = kvStorer;
    }

    public String Process(){
        return "";
    }
}
