import java.util.Arrays;

public class Reset {
    //reset the game
    public static int Reset(String[][] TTT,short[] row, short[] col, short[] cD,User AI,User player){

        for (String c[]:TTT) {
            Arrays.fill(c,"_");
        }
        Arrays.fill(row,(short)0);
        Arrays.fill(col,(short)0);
        Arrays.fill(cD,(short)0);
        player.setWin(false);
        AI.setWin(false);
        System.out.println("Game restart.");
        return 0;
    }
}
