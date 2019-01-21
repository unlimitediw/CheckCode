import java.util.Scanner;

public class MainClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //Create instance.
        HelloGenerator helloGenerator = new HelloGenerator();
        EveryDay everyDay = new EveryDay();

        //Please give command.
        System.out.println("If we want to see Hello please press 1&Enter\n"+
                "If you want to see Everday please press 2&Enter\n" +
                "Press e&Enter to exit\n");
        String command = sc.next();
        while(!command.equals("e")) {
            if (command.equals("1")) {
                helloGenerator.setHelloNum(1000);
                helloGenerator.sayHellow();
            } else if (command.equals("2")) {
                everyDay.printEverday();
            } else if (!command.equals("e")) {
                System.out.println("Wrong command.");
            }
            command = sc.next();
        }


    }
}
