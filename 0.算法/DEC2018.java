import java.util.*;

public class DEC2018 {
    // #1
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> keyMemo = new HashMap<>();
        for(int i = 0;i< nums.length;i++){
            if(keyMemo.containsKey(nums[i])){
                return new int[]{keyMemo.get(nums[i]),i};
            }
            else{
                keyMemo.put(target - nums[i],i);
            }
        }
        return null;
    }

    // #2
    // AddTwoNumber simple version
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode resultSet = head;
        int carry = 0;
        while(l1 != null || l2 != null){
            int x, y, sum;
            if(l1 != null)
                x = l1.val;
            else
                x = 0;
            if(l2 != null)
                y = l2.val;
            else
                y = 0;
            sum = carry + x + y;
            carry = sum / 10;
            resultSet.next = new ListNode(sum % 10);
            resultSet = resultSet.next;
            if(l1 != null)
                l1 = l1.next;
            if(l2 != null)
                l2 = l2.next;
        }
        if (carry == 1) {
            resultSet.next = new ListNode(carry);
        }
        return head.next;
    }

    // #2
    // Note1: Carry remain should be taken as a new node.
    // Note2: Be care about condition.
    public GenListNode addTwoNumbers(GenListNode<Integer> l1, GenListNode<Integer> l2) {
        int carry = 0;
        int startVal = l1.val + l2.val;
        if(startVal >= 10) {
            startVal %= 10;
            carry = 1;
        }
        GenListNode result = new GenListNode(startVal);
        GenListNode temp = result;
        while(l1.next != null && l2.next != null){
            l1 = l1.next;
            l2 = l2.next;
            int cur = l1.val + l2.val + carry;
            if(cur >= 10){
                cur %= 10;
                carry = 1;
            }
            else {
                carry = 0;
            }
            GenListNode newNode = new GenListNode(cur);
            temp.next = newNode;
            temp = newNode;
        }
        if(l1.next == null && l2.next == null){
            if(carry == 1){
                temp.next = new GenListNode<Integer>(1);
            }
        }
        if(l1.next != null) singleIter(l1,temp,carry);
        if(l2.next != null) singleIter(l2,temp,carry);
        return result;
    }

    void singleIter(GenListNode<Integer> l, GenListNode<Integer> inherit, int carry){
        while (l.next != null) {
            l = l.next;
            int cur = l.val + carry;
            if (cur >= 10) {
                cur %= 10;
                carry = 1;
            } else {
                carry = 0;
            }
            GenListNode newNode = new GenListNode(cur);
            inherit.next = newNode;
            inherit = newNode;
        }
        if(carry == 1){
            inherit.next = new GenListNode<Integer>(1);
        }
    }

    // #3
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> charMap = new HashMap<>();
        int head = 0;
        int tail = 0;
        int maxLength = 0;
        while(tail < s.length()){
            if(tail - head > maxLength) maxLength = tail - head;
            if(charMap.containsKey(s.charAt(tail))) {
                head = charMap.get(s.charAt(tail)) + 1;
                Set<Character> keys = new HashSet<>(charMap.keySet());
                for(char key : keys){
                    if(charMap.get(key) < head){
                        charMap.remove(key);
                    }
                }
            }
            charMap.put(s.charAt(tail),tail);
            tail++;
        }
        if(tail - head > maxLength) maxLength = tail - head;
        return maxLength;
    }

    // #636 version 1
    public int[] exclusiveTime(int n, List<String> logs) {
        int cur = -1;
        int exist = 0;
        int[] res = new int[n];
        Stack<Integer> memo = new Stack<>();
        for(String log : logs){
            String[] part = log.split(":");
            if(part[1].equals("start")){
                if(memo.isEmpty()){
                    res[exist] += Integer.parseInt(part[2]) - cur - 1;
                    memo.add(Integer.parseInt(part[0]));
                    cur = Integer.parseInt(part[2]);
                }
                else if(Integer.parseInt(part[0]) != memo.peek()){
                    res[memo.peek()] += Integer.parseInt(part[2]) - cur - 1;
                    memo.add(Integer.parseInt(part[0]));
                    cur = Integer.parseInt(part[2]);
                }
            }
            else{
                if(!memo.isEmpty() && Integer.parseInt(part[0]) == memo.peek()){
                    res[memo.peek()] += Integer.parseInt(part[2]) - cur + 1;
                    cur = Integer.parseInt(part[2]);
                    exist = memo.pop();

                }
                else{
                    res[Integer.parseInt(part[0])] += Integer.parseInt(part[2]) - cur;
                    cur = Integer.parseInt(part[2]);
                }
            }
        }
        return res;
    }

    // #636 standard version
    public int[] exclusiveTime1(int n, List<String> logs) {
        int[] res = new int[n];
        Stack<Integer> stack = new Stack<>();
        int prevTime = 0;
        for (String log : logs) {
            String[] parts = log.split(":");
            if (!stack.isEmpty()) res[stack.peek()] +=  Integer.parseInt(parts[2]) - prevTime;
            prevTime = Integer.parseInt(parts[2]);
            if (parts[1].equals("start")) stack.push(Integer.parseInt(parts[0]));
            else {
                res[stack.pop()]++;
                prevTime++;
            }
        }
        return res;
    }
}


