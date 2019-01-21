public class Constructor {
    int x,y,z;

    public double average()
    {
        return (x*y*z)/3.0;
    }

    Constructor()
    {
        x= 10; y=10; z=10;
        System.out.println("this is Constructor");
    }
    Constructor(int a,int b, int c){
        x= a; y = b; z =c;
    }
}
