import java.util.Scanner;

public class Decision {
    //Translate player's instruction into board.
    public void makeDecision(String[][] TTT,short[] row, short[] col, short[] cD,User player){
        boolean successCommand = false;
        while(!successCommand) {
            Scanner sc = new Scanner(System.in);
            System.out.printf("x: ");
            int x = sc.nextInt();
            System.out.printf("y: ");
            int y = sc.nextInt();
            if (x > 3 || x < 1 || y > 3 || y < 1) {
                System.out.println("(x,y) must be int 3*3 box, please input again.");
                continue;
            } else if (TTT[x-1][y-1] != "_") {
                System.out.println("Please select an empty area, input again.");
                continue;
            }
            TTT[x-1][y-1] = "*";
            row[x-1] ++;
            col[y-1]++;
            if(x==y){
                cD[0]++;
            }
            else if(x == 2-y){
                cD[1]++;
            }
            if(row[x-1] ==3||col[y-1] ==3|| cD[0]==3||cD[1]==3){
                player.setWin(true);
            }
            successCommand = true;
        }
    }
}
