public class Client {
    public static void main(String[] args) {
        Person Tom = new Person("married");
        System.out.println("Get Tom's married Status: " + Tom.getMaritalState());
        System.out.println("Set Tom's married status to widow.");
        System.out.println("result: ");
        Tom.setMaritalState("widow");
        System.out.println(Tom.getMaritalState());
        System.out.println("Set Tom's married status to Single.");
        System.out.println("result: ");
        Tom.setMaritalState("single");
        System.out.println("Get Tom's married Status: " + Tom.getMaritalState());
    }
}
