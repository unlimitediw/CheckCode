import java.util.ArrayList;

public class ArrayListNodeTransform {
    public static <T> GenListNode<T> ATN(T[] array){
        GenListNode head = new GenListNode<>(array[0]);
        GenListNode start = head;
        for(int i = 1;i < array.length; i++){
            GenListNode cur = new GenListNode<>(array[i]);
            start.next = cur;
            start = cur;
        }
        return head;
    }

    public static <T> ArrayList<GenListNode<T>> NTA(GenListNode<T> head){
        ArrayList<GenListNode<T>> result = new ArrayList<>();
        GenListNode<T> countMemo = head;
        while(countMemo != null){
            result.add(countMemo);
            countMemo = countMemo.next;
        }
        return result;
    }



}
