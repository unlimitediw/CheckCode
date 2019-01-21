import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        DEC2018 check = new DEC2018();
        /*
        // #1
        int[] result = check.twoSum(new int[]{2,7,11,15},9);
        for(int i = 0; i< result.length;i++){
            System.out.println(result[i]);
        }
         */
        /* #2
        ListNode l1 = new ListNode<Integer>(2);
        ListNode l2 = new ListNode<Integer>(5);
        l1.next = new ListNode<Integer>(4);
        l2.next = new ListNode<Integer>(6);
        l1.next.next = new ListNode<Integer>(3);
        l2.next.next = new ListNode<Integer>(4);
        ListNode k = Calculator.addTwoNumbers(l1,l2);
        System.out.println(k.next.next.val);
        // easy array to list than check function
        Integer[] a1 = {9,8};
        Integer[] a2 = {1};
        GenListNode<Integer> l1 = ArrayListNodeTransform.ATN(a1);
        GenListNode<Integer> l2 = ArrayListNodeTransform.ATN(a2);
        GenListNode k = Calculator.addTwoNumbers(l1,l2);
        System.out.println(k.next.val);
        */
        // #3
        /*
        int a = check.lengthOfLongestSubstring(
                "abba");
        System.out.println(a);
        */
        // #636
        List<String> data = Arrays.asList("0:start:0",
                "1:start:2",
                "1:end:5",
                "0:end:6");

        int[] res = check.exclusiveTime(2,data);
        for(int log : res){
            System.out.println(log);
        }

    }
}
