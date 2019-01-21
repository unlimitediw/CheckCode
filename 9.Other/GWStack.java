public class GWStack<T> {
    private T t;
    public void set(T t) { this.t = t; }
    public T get() { return t; }

    String cString;

    Integer cInt;


    GWStack next;

    public GWStack(String content) {
        this.cString = content;
    }

    public GWStack(Integer content){
        this.cInt = content;
    }

    public void push(String next_val) {

        push( new GWStack(next_val) );

    }

    public void push(GWStack next_node) {

        GWStack tmp = this;

        while( tmp.next != null ) {

            tmp = tmp.next;

        }

        // tmp now points to the last node

        tmp.next = next_node;

        //return this; // return the last node

    }

    public String toString() {

        String str = "";

        GWStack tmp = this;

        do {

            str = str + " " + tmp.cString;

            tmp = tmp.next;

        } while(tmp != null);



        return str;

    }


    public String pop(){
        GWStack pTmp = this;
        GWStack tmp = pTmp.next;
        if(pTmp.next == null) return pTmp.cString;
        while(tmp.next != null){
            pTmp = tmp;
            tmp = tmp.next;
        }
        pTmp.next = null;
        return tmp.cString;
    }
}
