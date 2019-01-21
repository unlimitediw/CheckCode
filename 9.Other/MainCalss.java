import java.util.Arrays;
import java.util.Scanner;

public class MainCalss {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //There are two kinds of game, please follow the instructions. Thank you!

        //Initial Decision Class.
        Decision playerDecision = new Decision();
        AI marine = new AI("X");//emmm...233
        AI zergling = new AI("*");

        //AI&your Reference
        short[] row = new short[3];//record the column value, every "*" in col will make row++, every "X" in col will make row--, if abs(col) = 3, game finish.
        short[] col = new short[3];//same
        short[] cD = new short[2];//same
        User player = new User();
        User AI1 = new User();
        User AI2 = new User();

        //Initial TicTacToe Board
        String[][] TTT = new String[3][3];
        for (String c[]:TTT) {
            Arrays.fill(c,"_");
        }

        //Turn Counter.
        int turn = 1;

        //Tips
        System.out.println("If you want to restart, please press 'r'");
        System.out.println("If you want to end this game, please press 'e'");
        System.out.println("If you want to change mode please press 'c'");
        System.out.println("If you want to go on, please press any other key");
        System.out.println("\nPlease select a mode to start, press 'a' means AI or press 'p' means player");

        //ModeInitialization Player vs AI/ AI vs AI
        boolean AImode = false;
        //To avoid unreasonable input
        boolean selected = false;
        while (!selected) {
            selected = true;
            String selcet = sc.next();
            if (selcet.equals("a")) AImode = true;
            else if (selcet.equals("p")) AImode = false;
            else{
                selected = false;
                System.out.println("Wrong command, please select again");
            }
        }

        //Game Begin.
        while(turn < 10){
            System.out.println("turn: "+turn);


            //Player
            if(!AImode) {
                if (turn % 2 == 1) {
                    System.out.println("Give command: (r: reset, e: end, c: changeMode, otherKeys: goOn)");
                    String a = sc.next();
                    if (a.equals("r")) {
                        turn = Reset.Reset(TTT, row, col, cD, AI1, player);
                    }
                    else if (a.equals("e")) return;
                    else if (a.equals("c")){
                        AImode = true;
                        System.out.println("Game reset, turn to AI mode");
                        turn = Reset.Reset(TTT, row, col, cD, AI1, player)+1;
                        continue;
                    }
                    else {
                        playerDecision.makeDecision(TTT, row, col, cD, player);
                        DisplayBoard.displayBoard(TTT);
                        if (player.isWin()) {
                            System.out.println("You WIN!!!(but it is impossible 2333)");
                            turn = Reset.Reset(TTT, row, col, cD, AI1, player);
                        }
                    }
                }
                //AI second X
                else {
                    marine.makeDecision(TTT, row, col, cD, AI1);
                    System.out.println("AI made a decision.");
                    DisplayBoard.displayBoard(TTT);
                    if (AI1.isWin()) {
                        System.out.println("You lost...");
                        turn = Reset.Reset(TTT, row, col, cD, AI1, player);
                    }
                }
            }
            else{
                System.out.println("Give command: (r: reset, e: end, c: changeMode, otherKeys: goOn)");
                String a = sc.next();
                if (a.equals("r")) {
                    turn = Reset.Reset(TTT, row, col, cD, AI1, player);
                }
                else if (a.equals("e")) return;
                else if (a.equals("c")){
                    AImode = false;
                    System.out.println("Game reset, turn to player mode");
                    turn = Reset.Reset(TTT, row, col, cD, AI1, player) + 1;
                    continue;
                }
                //AI1.
                if(turn% 2==0) {
                    marine.makeDecision(TTT, row, col, cD, AI1);
                    System.out.println("AI1 made a decision.");
                    DisplayBoard.displayBoard(TTT);
                    if (AI1.isWin()) {
                        System.out.println("AI1 Wins the game.");
                        turn = Reset.Reset(TTT, row, col, cD, AI1, player);
                    }
                }
                //AI2
                else{
                    zergling.makeDecision(TTT, row, col, cD, AI2);
                    System.out.println("AI2 made a decision.");
                    DisplayBoard.displayBoard(TTT);
                    if (AI2.isWin()) {
                        System.out.println("AI2 Wins the game.");
                        turn = Reset.Reset(TTT, row, col, cD, AI2, player);
                    }
                }
                if (a.equals("c")){
                    AImode = false;
                    System.out.println("Game reset, turn to player mode");
                    turn = Reset.Reset(TTT, row, col, cD, AI1, player);
                }
            }
            if (turn == 9){
                System.out.println("draw.");
                System.out.println("If you want to reset game, please press 'r'. Else exit.");
                String a = sc.next();
                if(a.equals("r")) turn = Reset.Reset(TTT, row, col, cD, AI1, player);
            }
            turn++;
        }

    }
}
