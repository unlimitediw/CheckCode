public class HelloGenerator {
    private int hellowNum;

    public void setHelloNum(int helloNum) {
        this.hellowNum = helloNum;
    }

    public void sayHellow(){
        for(int i = 1; i<=hellowNum;i++){
            System.out.println("Hello, "+i);
        }
    }

    HelloGenerator(){
        hellowNum = 0;
    }
}
