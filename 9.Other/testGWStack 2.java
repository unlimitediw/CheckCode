import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class testGWStack {
    public static void main(String[] args) {
        // TODO Auto-generated method stub

        GWStack<String> s = new GWStack<String>("apple");

        s.push("mango");

        s.push("cherry");

        GWStack<Integer> is = new GWStack<Integer>(1);

        System.out.println("Created a stack");

        System.out.println("Content of the stack: " + s);

        // cherry mango apple
        System.out.println("First time pop() value: " + s.pop());
        System.out.println("Second time pop() value: " + s.pop());
        System.out.println("Third time pop() value: " + s.pop());

        // apple mango cherry

    }
}
