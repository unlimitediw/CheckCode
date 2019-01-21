public class Student {
    int id;//line1
    String name;//line2

    Student(){
        System.out.println("this is a default constructor");
    }
    Student(int id, String name){
        this();
        this.id = id;//to access line1
        this.name = name;//to access line2
    }
    void display(){
        System.out.println(id+name);
    }
}
