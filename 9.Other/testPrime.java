import java.math.BigInteger;

public class testPrime {
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        PrimeFinder p1 = new PrimeFinder(new BigInteger("1934829384871234"));
        PrimeFinder p2 = new PrimeFinder(new BigInteger("713124125151127"));
        PrimeFinder p3 = new PrimeFinder(new BigInteger("72235121411142111111111"));
        p1.start();
        p2.start();
        p3.start();

        // prove
        BigInteger a = new BigInteger("713124125151127");
        System.out.println("You can try to prove it by write the divider into the following space: " + a.divide(new BigInteger("61")).multiply(new BigInteger("61")));
    }
}
