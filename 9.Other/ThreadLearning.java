package part4;

public class ThreadLearning {
    private static int count = 0;
    // Use synchronized method here to avoid count access overlap
    public static synchronized void inccount(){
        count++;
    }
    public static void main(String[] args) {
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < 10000; i++){
                    //count += 1;
                    inccount();
                }
            }
        });
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < 10000; i++){
                    //count += 1;
                    inccount();
                }
            }
        });
        t1.start();
        t2.start();
        boolean withJoin = true;
        if (withJoin){
            try {
                t1.join();
                t2.join();
            } catch (InterruptedException e){
                e.printStackTrace();
            }
        }
        // print 87, sout will not wait for t1 and t2 end
        // If with Thread.join(), print 11428
        System.out.println(count);
        System.out.println();
    }
}
