import PlayHelper.*;

import java.util.Scanner;
import java.util.List;
import java.util.Date;
import java.text.SimpleDateFormat;

public class TicTacToe {

    public static void main(String[] args) throws Exception {
        int m = 5;                       // m is the target number
        int n = 12;                       // n is the row/column number of the board
        String teamId1 = "1052";     // Our teamId
        String teamId2;              // Opponent TeamID
        PlayHelper ph;               // Help to connect to the server
        AI newAI;
        // AI VS AI
        AI newAI2;
        newAI = new AI(10, 0.1, 1, 15, 0.6, 1.2, n, m, 4);
        newAI2 = new AI(10, 0.15, 1, 15, 0.6, 1.2, n, m, 4);
        int turn = 1;
        long t = 0;
        while (turn < newAI.n * newAI.n + 1) {
            //the first step if the user do the first step
            if (turn == 1) {
                newAI.Play(n/2,n/2, turn, newAI);
                turn++;
                //DisplayBoard.displayBoard(newAI.TTT, newAI);
            }
            else if (turn % 2 == 1) {
                newAI2.PlayMinMax(newAI2,newAI.optX,newAI.optY,turn);
                turn ++;
                DisplayBoard.displayBoard(newAI2.TTT, newAI2);
            } else {//the opponent's steps
                newAI.PlayMinMax(newAI,newAI2.optX,newAI2.optY,turn);
                turn ++;
                //DisplayBoard.displayBoard(newAI.TTT, newAI);
            }
        }
    }
}