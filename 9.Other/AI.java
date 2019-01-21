import java.util.Random;

public class AI {
    private String chess = "";
    private boolean AI1 = false;

    AI(String chess){
        this.chess = chess;
        if(chess.equals("X")) this.AI1 = true;
    }

    public void makeDecision(String[][] TTT,short[] row, short[] col, short[] cD,User AI){

        //There is the priority of AI action, AI will follow it in any situation.
        //Level -2>-1>0>1>2>3>4
        //Level P will not affect other level but should be obeyed.

        //Level -2: Let first input be a random position to make AI vs AI more interesting.
        //Level -1：如果中心没点 落中心 If there is no point in center, insert center.(space = 1)
        //Level 0；如果自己能3就3. If AI can win, win it.(space = 9)
        //Level 1：如果*colCount = 2||*rowCount = 2|| *centerDiagonalCount = 2 下count剩余点。(space = 9)
        //         If Player will win in next step, prevent it.
        //Level 2: 如果有一个点的col,row,cd中的任意两个同时为1下那个点
        //         avoid the situation of double two value of enemy. e.g. to TTT[i][j], both col[j]&row[i]=2 avoid it
        //Level 3：如果中心有点 落角 If no space is center, insert in corners.(space = 4)
        //Level 4：如果中心有点 角都有点 落边 If no space in center&corners, insert edge.(space = 4)
        //Level P：在满足落点的情况下，下能让自己col、row、centerDiagonal到2的。
        //         (Sync)In any situation, if other situation is satisfied find the way to let AI win.

        int x;
        int y;
        int[] sol = {-1,-1};
        int one = -1, two = -2;
        //Initialize AI standard
        if(!AI1){
            one = 1;
            two = 2;
            //Level -2
            if(TTT[1][1] == "_"){
                Random rand = new Random();
                int i = rand.nextInt(2);
                int j = rand.nextInt(2);
                insert(TTT,row,col,cD,i,j,AI);
                return;
            }
        }

        //Level -1.
        if(TTT[1][1] == "_"){
            insert(TTT,row,col,cD,1,1,AI);
            return;
        }

        //Level 0.
        for(int i =0; i<3;i++){
            if(row[i] == two){
                for(int j =0;j<3;j++){
                    if(TTT[i][j] == "_"){
                        insert(TTT,row,col,cD,i,j,AI);
                        return;
                    }
                }
            }
            else if(col[i] == two){
                for(int j =0;j<3;j++){
                    if(TTT[j][i] == "_"){
                        insert(TTT,row,col,cD,j,i,AI);
                        return;
                    }
                }
            }
            else if(cD[0] == two){
                if (TTT[i][i] == "_") {
                    insert(TTT,row,col,cD,i,i,AI);
                    return;
                }
            }
            else if(cD[1] == two){
                if (TTT[i][2-i] == "_") {
                    insert(TTT,row,col,cD,i,2-i,AI);
                    return;
                }
            }
        }

        //Level 1.
        for(int i =0; i<3;i++){
            if(row[i] == -two){
                for(int j =0;j<3;j++){
                    if(TTT[i][j] == "_"){
                        insert(TTT,row,col,cD,i,j,AI);
                        return;
                    }
                }
            }
            else if(col[i] == -two){
                for(int j =0;j<3;j++){
                    if(TTT[j][i] == "_"){
                        sol[0] = j;
                        sol[1] = i;
                        insert(TTT,row,col,cD,j,i,AI);
                        return;
                    }
                }
            }
            else if(cD[0] == -two){
                if (TTT[i][i] == "_") {
                    insert(TTT,row,col,cD,i,i,AI);
                    return;
                }
            }
            else if(cD[1] == -two){
                if (TTT[i][2-i] == "_") {
                    insert(TTT,row,col,cD,i,2-i,AI);
                    return;
                }
            }
        }

        //Level 2.
        for(int i = 0;i<3;i++) {
            if (row[i] == -one) {
                for (int j = 0; j < 3; j++) {
                    if (TTT[i][j] == "_") {
                        //avoid the situation of double two Level D.
                        if (col[j] == -one || (cD[0] == -one) && (i == j) || (cD[1] == -one) && (i == 2 - j)) {
                            insert(TTT, row, col, cD, i, j,AI);
                            return;
                        }
                    }
                }
            }
            if (col[i] == -one) {
                for (int j = 0; j < 3; j++) {
                    if (TTT[j][i] == "_") {
                        //avoid the situation of double two Level D.
                        if ((cD[0] == -one) && (i == j) || (cD[1] == -one) && (i == 2 - j)) {
                            insert(TTT, row, col, cD, i, j,AI);
                            return;
                        }
                    }
                }
            }
        }

        //Level 3.
        for(int i =0;i< 3;i+=2) {
            for (int j = 0; j < 3; j += 2) {
                if (TTT[i][j] == "_") {
                    sol[0] = i;
                    sol[1] = j;
                    if (row[i] == one || col[j] == one || ((cD[0] == one) && (i == i)) || ((cD[1] == one) && (i == 2 - i)))//Level P.
                        i = 3;
                    break;
                }
            }
        }
        if(sol[0] != -1){
            insert(TTT,row,col,cD,sol[0],sol[1],AI);
            return;
        }

        //Level 4.
        for(int i=0;i< 3;i+=2){
            if (TTT[i][1] == "_") {
                sol[0] = i;
                sol[1] = 1;
                if(row[i] ==one || col[1] == one)//Level P.
                    i = 3;
                break;
            }
        }
        for(int j=0;j< 3;j+=2){
            if (TTT[1][j] == "_") {
                sol[0] = 1;
                sol[1] = j;
                if(row[1] ==one || col[j] == one)//Level P.
                    j = 3;
                break;
            }
        }
        if(sol[0] != -1) insert(TTT,row,col,cD,sol[0],sol[1],AI);
        else System.out.println("Draw~");
    }

    //Insert AI's chess.
    public void insert(String[][] TTT,short[] row, short[] col, short[] cD,int i,int j, User AI){
        TTT[i][j] = chess;
        if(AI1) {
            row[i]--;
            col[j]--;
            if (i == j) {
                cD[0]--;
            }
            if (i == 2 - j) {
                cD[1]--;
            }
        }
        else{
            row[i]++;
            col[j]++;
            if (i == j) {
                cD[0]++;
            }
            if (i == 2 - j) {
                cD[1]++;
            }
        }
        if(row[i] == -3||col[j] == -3||cD[0] == -3||cD[1] == -3)  AI.setWin(true);
    }

}
