import java.util.Arrays;

public class AI {
    int col[][] = new int[20][2];
    int row[][] = new int[20][2];
    int rD[][] = new int[39][2];
    int lD[][] = new int[39][2];

    String[][] TTT = new String[20][20];

    AI(boolean first){
        for (String c[]:TTT) {
            Arrays.fill(c,"_");
        }
    }

    public int[] makeDecision(){
        int result[] = new int[2];
        result[0] = 10;
        result[1] = 10;
        col[result[0]-1][0] = 1;
        row[result[1]-1][0] = 1;
        rD[result[0]+20-result[1]][0] = 1;
        lD[result[0]+result[1]-2][0] = 1;
        return result;
    }

    public int[] makeDecision(int x,int y){
        int result[] = new int[2];
        int posX = x-1;
        int posY = y-1;
        TTT[posX][posY] = "O";
        TTT[result[0]-1][result[1]-1] = "X";
        return result;
    }

    //Reset Col&Row winWeight at (posX,posY)
    int[] winWeightResetRC(int posX,int posY,int mode,String[][] TTT){
        //0 means my weightValue, 1 means opponent's weightValue.
        int memo0 = 0;
        int memo1 = 0;
        int max[] = new int[2];
        int distance0 = 0;
        int distance1 = 1;
        for(int i =0;i<20;i++){
            int x = 0;
            int y = 0;
            switch (mode) {
                case 1://col
                    x = posX;
                    y = i;
                    break;
                case 2://row
                    x = i;
                    y = posY;
                    break;
            }
            if(TTT[x][y] == "X"){
                memo0++;
                memo1 = 0;
                distance1 = 0;
            }
            else if(TTT[x][y] == "O"){
                memo1++;
                memo0 = 0;
                distance0 = 0;
            }
            else{
                distance0++;
                distance1++;
            }
            if(memo0 - distance0 > max[0]) max[0] = memo0 - distance0;
            else if(memo0 - distance0 <= 0) {
                memo0 = 0;
                distance0 = 0;
            }
            if(memo1 - distance1 > max[1]) max[1] = memo1 - distance1;
            else if(memo1 - distance1 <= 0) {
                memo1 = 0;
                distance1 = 0;
            }
        }
        return max;
    }

    //Reset right diagonal winWeight at (PosX,posY)
    int[] winWeightResetRD(int posX,int posY,String[][] TTT){
        int max[] = new int[2];
        if((posX+posY+1 < 8)||(posX+posY+1>32)) return max;
        int memo0 = 0;
        int memo1 = 0;
        int distance0 = 0;
        int distance1 = 1;
        int offset = posX-posY;
        for(int i = 0; i< 20-Math.abs(offset);i++){
            int x = 0;
            int y = 0;
            if(offset >= 0){
                x = offset +i;
                y = i;
            }
            else{
                x = i;
                y = i-offset;
            }
            if(TTT[x][y] == "X"){
                memo0++;
                memo1 = 0;
                distance1 = 0;
            }
            else if(TTT[x][y] == "O"){
                memo1++;
                memo0 = 0;
                distance0 = 0;
            }
            else{
                distance0++;
                distance1++;
            }
            if(memo0 - distance0 > max[0]) max[0] = memo0 - distance0;
            else if(memo0 - distance0 <= 0) {
                memo0 = 0;
                distance0 = 0;
            }
            if(memo1 - distance1 > max[1]) max[1] = memo1 - distance1;
            else if(memo1 - distance1 <= 0) {
                memo1 = 0;
                distance1 = 0;
            }
        }
        return max;
    }

    //Reset left diagonal winWeight at (PosX,posY)
    int[] winWeightResetLD(int posX,int posY,String[][] TTT){
        int max[] = new int[2];
        if((20-posY + posX < 8)||(20-posY + posX>32)) return max;
        int memo0 = 0;
        int memo1 = 0;
        int distance0 = 0;
        int distance1 = 1;
        int offset = 19 - posX - posY;
        for(int i = 0; i< 20-Math.abs(offset);i++){
            int x = 0;
            int y = 0;
            if(offset >= 0){
                x = i;
                y = 19 - offset -i;
            }
            else{
                x = i - offset;
                y = 19 - i;
            }
            if(TTT[x][y] == "X"){
                memo0++;
                memo1 = 0;
                distance1 = 0;
            }
            else if(TTT[x][y] == "O"){
                memo1++;
                memo0 = 0;
                distance0 = 0;
            }
            else{
                distance0++;
                distance1++;
            }
            if(memo0 - distance0 > max[0]) max[0] = memo0 - distance0;
            else if(memo0 - distance0 <= 0) {
                memo0 = 0;
                distance0 = 0;
            }
            if(memo1 - distance1 > max[1]) max[1] = memo1 - distance1;
            else if(memo1 - distance1 <= 0) {
                memo1 = 0;
                distance1 = 0;
            }
        }
        return max;
    }

}
