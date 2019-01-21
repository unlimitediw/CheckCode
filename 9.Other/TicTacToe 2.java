import java.util.Arrays;

public class TicTacToe {
    public static void main(String[] args) {

        //Initialize board
        String[][] TTT = new String[20][20];
        for (String c[]:TTT) {
            Arrays.fill(c,"_");
        }

        //Key value

        int turn = 1;
        while(turn < 400){
            DisplayBoard.displayBoard(TTT);
            turn++;
        }
    }
}
