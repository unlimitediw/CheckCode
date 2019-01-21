import java.util.Random;
import java.util.Scanner;
public class MyFirstClass {

    public static  void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        System.out.println(average(3,5,8.0));

        LearnClass myInfo = new LearnClass(4,"z",23,"I am....");
        LearnClass frInfo = new LearnClass(7,"aaa",17,"nanasaki");
        System.out.println(myInfo.toString());

        LearnClass encap = new LearnClass();
        System.out.println(encap.getId() +encap.getName() + encap.getAge() + encap.getBio());

        LearnClass myInfoDefault = new LearnClass();
        myInfo.setId(14);
        myInfo.setAge(24);
        myInfo.setName("killer");
        myInfo.setBio("hacker");

        System.out.println(myInfo.getId()+""+myInfo.getAge()+myInfo.getName() +myInfo.getBio());

        Constructor avr = new Constructor();
        System.out.println(avr.average());
        Constructor avr2 = new Constructor(1,2,41);
        System.out.println(avr2.average());

        SKeyword.Sword();

        Student s1 = new Student(1,"kira");
        Student s2 = new Student(2,"aslan");

        System.out.println(s1.id+s1.name);
        Programmer me = new Programmer();
        System.out.println("Programmer Salary is: "+ me.salary);
        System.out.println("Programmer Bonus is: " +me.bonus);

        Mycalculation myC = new Mycalculation();
        myC.addition(1,2);
        myC.division(7,3);

        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt();
        System.out.println(i);
    }

    public static void myMethod(int t){
        System.out.println("emmmm..." +t);
    }

    public static double average(int x, int y, int z){
        return (x+y+z)/3;
    }

    public static double average(double x,double y,double z){
        return (x+y+z)/3;
    }

}
