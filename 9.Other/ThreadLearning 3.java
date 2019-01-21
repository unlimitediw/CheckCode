package part5;

public class ThreadLearning {
    public static Account account = new Account();
    public static void main(String[] args) {
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < 10000; i++){
                    //count += 1;
                    account.debit(100);
                }
            }
        });
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < 10000; i++){
                    //count += 1;
                    account.debit(100);
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
        System.out.println(account.getBalance());
    }
}

class Account{
    private int balance = 10000;
    public void debit(int amt){
        if(amt < 0) return;
        synchronized (this){
            balance -= amt;
        }
    }
    public int getBalance(){
        return balance;
    }
}