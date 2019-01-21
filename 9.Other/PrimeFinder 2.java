import java.math.BigInteger;

public class PrimeFinder extends Thread {

    BigInteger bigNum;

    public PrimeFinder(BigInteger bigNum) {
        this.bigNum = bigNum;
    }

    public BigInteger BigIntSqrt(BigInteger x){
        BigInteger div = BigInteger.ZERO.setBit(x.bitLength()/2);
        BigInteger div2 = div;
        while(true) {
            BigInteger y = div.add(x.divide(div)).shiftRight(1);
            if (y.equals(div) || y.equals(div2))
                return y;
            div2 = div;
            div = y;
        }
    }

    public void run() {
        // TODO see if bigNum is a prime number
        if(bigNum.compareTo(new BigInteger("2"))<0){
            System.out.println(bigNum+" is not a prime number");
            return;
        }
        BigInteger bigNumSQRT = BigIntSqrt(bigNum);
        BigInteger zero = new BigInteger("0");
        for(BigInteger i = new BigInteger("2");i.compareTo(bigNumSQRT)<=0;i = i.add(new BigInteger("1"))){
            if(bigNum.mod(i).compareTo(zero) == 0){
                System.out.println(bigNum+" is not a prime number and it can divided by "+ i);
                return;
            }
            //System.out.println("Current iteration number: "+i +" and current test number: "+bigNum);
        }
        System.out.println(bigNum+ " is a prime number");

    }



}