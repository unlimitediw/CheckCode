import java.util.Scanner;

public class MainClass {
    public static void main(String[] args) {
        //Preset
        Scanner sc = new Scanner(System.in);

        String maze ="|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n" +
                "|                                   |                 |                         |\n" +
                "| | ||||||| ||| ||||||| ||| ||| ||| | ||||||| ||| ||||| ||||||||||||||||||| ||| |\n" +
                "| | |     |   | |       | | | | | |           | | |         |             | | | |\n" +
                "| | | ||| ||| | ||||||||| ||| ||| ||| | ||| ||| | ||||| ||||| ||||||| ||||| | | |\n" +
                "| | | | |   |         |             | |   | |   |     | |     |     | |     | | |\n" +
                "| | ||| ||| | | | ||| ||| ||| ||| ||| ||| ||| ||| ||| | ||||| | | ||| ||||| | | |\n" +
                "| |       | | | | | |   |     | | |     |           | |       | | |       | | | |\n" +
                "| | ||||| | ||| | | ||| | ||| | ||| ||||| ||||||| ||| ||||||||| | ||||||| ||| |||\n" +
                "| |   |   |     | |   |   | | |       |   |     | |                   | |       |\n" +
                "| ||| ||| ||||| | | | ||||| ||| ||||| | | | ||||| | ||||||||||| ||| ||| ||| ||| |\n" +
                "|   |   |     | |   |           | | | | | |           |     | | | | |     |   | |\n" +
                "| ||||||| ||| ||||| ||||| | ||| | | ||||| ||||||| ||| | ||||| ||| ||| ||| | |||||\n" +
                "| |       |       |     | | | | |               | | | |               |   | |   |\n" +
                "| ||||| | ||||||||| ||| | ||| | ||||||||||| ||| ||| | ||||||||||| ||| ||||| ||| |\n" +
                "|     | |       |     | |     |           | | |     |   |     |   | | |         |\n" +
                "| ||||| ||| ||| | ||| | ||||| | | ||||||| ||| | ||| ||| | ||| ||| | | ||| ||||| |\n" +
                "| |       | | | |   | |     | | | |     |     |   |   |   | |   | |     | |   | |\n" +
                "| ||||| ||| | | ||||| ||||||| ||| | ||||| ||| | ||| | ||| | ||| ||| ||||| | | |||\n" +
                "|   | | |   | | |       |       | |       | | |   | | | |     |     |   | | |   |\n" +
                "| ||| ||| | | | | ||| |||   ||||| | ||||||| | | ||| | | ||| | ||||| ||| | ||| | |\n" +
                "| | |       | |   | |       |     | |       |   |   | |   | |     |   | |     | |\n" +
                "| | ||| ||| | ||| | ||||||||| | ||| ||||||| ||||| | ||| ||| ||||| ||| | | ||| | |\n" +
                "| |       | |   | |           | |         |       |                 | |     | | |\n" +
                "| ||||| | | | | ||| ||| ||| ||| | ||| ||| ||||| | ||| ||||| ||||||||| | ||| ||| |\n" +
                "|     | | | | |     | | |       | | | | |     |     | |   |           | | |     |\n" +
                "| ||||| ||| ||| ||||| | ||| ||||| | | | ||| ||| ||| ||| ||||||||||||| ||| | ||| |\n" +
                "|     |         |     |     |     |   |   | |   | |           |     |       | | |\n" +
                "| ||||||||| ||| | | | | ||||| ||||| | ||| | | | | | | ||||||| ||| | | ||||||| | |\n" +
                "| |         | | | | | | |     |     |   |   | | | | | |     |   | | | |   | | | |\n" +
                "| ||||| ||||| | | | | | | ||| | ||| ||| ||||| | | | ||| ||||| ||||| | ||| | | | |\n" +
                "|     | |       | | | |   |   | | |   |         | | |   |     | |   |     |   | |\n" +
                "| ||| | | | ||| ||| ||| ||| ||| | ||| ||||||||| | |||   | ||||| ||| | ||| | | | |\n" +
                "|   | | | | | |         |   |       |       | | |       |         |   | | | | | |\n" +
                "| ||| ||||||| ||| | | ||| ||| ||| ||| ||||| | ||| ||||| | ||||||||||| | | | ||| |\n" +
                "| |             | | | | | |   | | |     | | |     |   | | |         | |   |     |\n" +
                "| ||||||| ||| | ||| ||| | ||||| ||| ||||| | | ||||| | | ||| ||||| ||| | ||||| | |\n" +
                "|       | | |           |         | |       |     | | |     |     |   | | | | | |\n" +
                "| ||||||| | ||| | ||||| | ||||||| | ||||||| ||| ||| | | ||||| ||| ||||| | | ||| |\n" +
                "| |       |   | | | | |   |     |       |     | |   | | |     | |         |   | |\n" +
                "| ||||||| ||| | | | | | ||| | ||||| ||| ||| | | ||| | | | ||| | ||| | ||||| ||| |\n" +
                "|       |     | | | | | |   | |   | | |   | | |   | | | | | | |   |   |         |\n" +
                "| ||||| | ||||| | | | | ||||| ||| | | ||||| | | | ||| | | | | ||| ||| ||||||||| |\n" +
                "| |   |   | |   | |   |         |   |   |     | |     |   | |   |   |         | |\n" +
                "| ||| | ||| ||||| ||| ||||| ||| ||||| | | ||| | | ||| ||||| | | ||| ||||||||| | |\n" +
                "|   | | |       |   |       | |         |   | |   |         | |   |         | | |\n" +
                "| ||| | ||| ||| | | | ||| ||| ||| | ||| ||| | ||||| ||| ||| ||| ||||||||| ||| | |\n" +
                "| |       |   | | | |   | |     | | | |   | |   |   | | |     |         | |   | |\n" +
                "| | ||||||| | ||| | ||||| | ||| ||| | ||| | ||| ||| | | ||||||| ||||| ||| ||||| |\n" +
                "| | |       |             | | |   |   |   |   |   |   |         |     |       | |\n" +
                "| | ||||||| | ||||||||| ||| | | ||||| ||| ||| ||||||| | ||||||| ||| ||||| ||||| |\n" +
                "| |     | |   | |     | |   |   |   |   |   |       | |   |   | |   |   |       |\n" +
                "| | ||||| ||| | ||| ||| ||| ||||| ||| | | |||   ||| ||||| ||| | ||||| ||||||||| |\n" +
                "| |         | |         | |       |       |     |       |   |         |       | |\n" +
                "| ||||| ||||| | ||||| ||| |||     | | ||||| ||| | ||||| | | ||||||| ||| ||| | | |\n" +
                "|     | |     | |   |       |     | | |       | | |   | | |       |     | | | | |\n" +
                "| ||||| | ||| ||| ||||| ||| | ||||| | | | ||||| ||| ||||| ||| | ||||||||| | ||| |\n" +
                "| |     | | |     |   | | | | | |     | | |         |       | | |         |   | |\n" +
                "| ||||| | | | ||| ||| | | | | | ||| ||| | ||||||| ||| | ||||| | ||| | ||| ||||| |\n" +
                "| |   |   |     |   | | | | | |   | |         | |   | | | |     | | | | |       |\n" +
                "| | ||||| ||||||| ||| ||| ||| | ||| | ||||||| | ||| ||| | | ||| | ||| | | ||| | |\n" +
                "| | |   |         |           | |   | |     |           | |   |     | | |   | | |\n" +
                "| | ||| | ||||||| | ||| ||||| | ||| | | ||| ||| | ||||| | ||| | | | ||| ||||| | |\n" +
                "| |   | | |     |   | | |   | |   | | | | |   |   |   | | | | | | |           | |\n" +
                "| | ||| ||| ||| ||||| | | ||| | | | | | | ||| | | ||| ||| | ||| | | ||||||||| | |\n" +
                "| | |                   | |   | | | | | |   | | |   |     |     | | |       | | |\n" +
                "| | ||||||||||| ||| ||| | ||||| ||| ||| | | ||| ||| ||||| ||||| | | ||| ||||| | |\n" +
                "| |   |     | | | | | |                 | |       | |   | |     |             | |\n" +
                "| ||| ||||| | ||| | | ||||||||||| ||||||| | ||||||| | | | ||||| ||||| ||||| ||| |\n" +
                "|       | |         |           |   |     | |       | | | |   |     | |   | |   |\n" +
                "| ||||||| ||| ||||| ||||| ||||| | ||| ||||| | ||||||| ||| ||| ||| ||| ||| | |||||\n" +
                "| |         | |   | |   | |   | | |   |     | | |               | |     | |     |\n" +
                "| ||| ||||| ||| ||| ||| ||| ||| ||| | ||| ||| | | ||||| ||||||||| ||||| | ||||| |\n" +
                "| | |     |     |     |     |           | |   |   |     |             |       | |\n" +
                "| | ||||| | ||| | ||||| ||| ||||| | ||| | ||| ||| ||||||| ||| ||||| | | ||| | | |\n" +
                "| |     | | | | |               | | | | |   |   |       | | | |     | | | | | | |\n" +
                "| ||| ||| ||| | | ||||||| ||| | | ||| ||||| | | | ||||| | | | ||| ||| ||| | | | |\n" +
                "| |   | |     |   |     | | | | |     |   | | | | |     | | |   | |       |   | |\n" +
                "| ||| | ||||| ||||||||| ||| ||| ||||||| ||| ||| ||| ||||| | | ||| ||||||| ||||| |\n" +
                "|                                                         |   |                 |\n" +
                "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n";

        //For convenience of array building.
        maze = maze.replaceAll("\n","");

        //[i] i means rowPosition.
        //[i][j] j means colPosition.
        //[i][j][direction] direction means:0 positionValue, 1 upDirValue, 2 downDirValue,
        //                                  3 leftDirValue, 4 rightDirValue, 5.pathMemoValue
        int[][][] mazeArray = new int[81][81][6];

        //initialize mazeArrayPositionValue.
        for(int i = 0; i < 81; i++){
            for(int j = 0; j < 81; j++){
                if(maze.charAt(i*81 +j) =='|'){
                    mazeArray[i][j][0] = 1;
                }
                else {
                    mazeArray[i][j][0] = 0;
                }
            }
        }

        //initialize directionValue.
        for(int i = 0; i < 81; i++){
            for(int j = 0; j < 81; j++){
                if(mazeArray[i][j][0] == 0){
                    if(mazeArray[i-1][j][0] == 1) mazeArray[i][j][1] = 1;
                    if(mazeArray[i+1][j][0] == 1) mazeArray[i][j][2] = 1;
                    if(mazeArray[i][j-1][0] == 1) mazeArray[i][j][3] = 1;
                    if(mazeArray[i][j+1][0] == 1) mazeArray[i][j][4] = 1;
                }
            }
        }

        //printArray will memo the non trackBack path, which can be both used in some function or print the final result.
        int[][] printArray = new int[81][81];
        for(int i = 0; i < 81; i++){
            for(int j = 0; j < 81; j++){
                if(mazeArray[i][j][0] == 0) {
                    printArray[i][j] = 0;
                }
                else printArray[i][j] = 1;
            }
        }

        //Input after initialization
        int x=0,y=0;//starting position.
        int fx=0,fy=0;//ending position.
        boolean correctInput = false;
        while (!correctInput){
            System.out.print("Please input x: ");
            x = sc.nextInt();
            System.out.print("Please input y: ");
            y = sc.nextInt();
            System.out.print("Please input fx: ");
            fx = sc.nextInt();
            System.out.print("Please input fy: ");
            fy = sc.nextInt();
            if((x>0 && x< 80&&y>0&&y<80&&fx>0&&fx<80&&fy>0&&fy<80&&printArray[x][y] ==0&&printArray[fx][fy]==0)) {
                correctInput = true;
                break;
            }
            else System.out.println("Wrong command, please input again.");
        }

        while(x != fx || y!= fy){

            int choice = 0;
            //Priority set(when choices are more than one)
            //To most maze game, it will make the AI work more efficiently.
            int xOffset = x- fx;
            int yOffset = y- fy;
            int prior = -81;
            int[] priority = new int[4];
            //up
            priority[0] = xOffset;
            //down
            priority[1] = -xOffset;
            //left
            priority[2] = yOffset;
            //right
            priority[3] = -yOffset;

            for(int i = 1; i<5; i++){
                if(mazeArray[x][y][i] == 0 && i != mazeArray[x][y][5]){
                    //Let AI make a reasonable choice~
                    if(priority[i-1] > prior) {
                        prior = priority[i-1];
                        choice = i;

                    }
                }
            }
            //对于没有访问过的路径，访问的同时标记后路, 如果出现循环，视为撞墙并返回
            //To unvisited path, record backPath which is mazeArray[x][y][5], like a double linkedList
            if(choice != 0 ){
                mazeArray[x][y][choice] = 1;
                int viceChoice;
                if(choice == 1){
                    x--;
                    viceChoice =2;
                }
                else if(choice == 2){
                    x++;
                    viceChoice =1;
                }
                else if(choice == 3){
                    y--;
                    viceChoice = 4;
                }
                else{
                    y++;
                    viceChoice =3;
                }
                //"printArray[x][y] == 2" means that if there is a Loop, please take this point as a '|' and do backtracking
                if(printArray[x][y] == 2){
                    //lock loop;
                    mazeArray[x][y][viceChoice] = 1;
                    if(viceChoice == 1){
                        x--;
                    }
                    else if(viceChoice == 2){
                        x++;
                    }
                    else if(viceChoice == 3){
                        y--;
                    }
                    else{
                        y++;
                    }
                }
                else{
                    mazeArray[x][y][5] = viceChoice;
                    printArray[x][y] = 2;
                }
                //test________
            }
            if(choice == 0){
                //对于返回（即走backPath），封死走过的返回路径(like backTracking algorithm)
                //When move in backPath way, lock the backPath.back which is "mazeArray[x][y][viceChoice] =1".
                if(mazeArray[x][y][5] != 0){
                    int viceChoice;
                    printArray[x][y] = 0;
                    if(mazeArray[x][y][5] == 1){
                        x--;
                        viceChoice =2;
                    }
                    else if(mazeArray[x][y][5] == 2){
                        x++;
                        viceChoice =1;
                    }
                    else if(mazeArray[x][y][5] == 3){
                        y--;
                        viceChoice = 4;
                    }
                    else{
                        y++;
                        viceChoice =3;
                    }
                    mazeArray[x][y][viceChoice] =1;
                }
                else{
                    //If there are no path either backPath which means that the AI have tried all possible position but can not find fx,fy
                    System.out.println("No!");
                    return;
                }
            }
            System.out.println(x + " " + y);
        }
        System.out.println("yes");
        //print out the final solution graph.
        for(int i = 0; i < 81; i++){
            for(int j = 0; j < 81; j++){
                if(printArray[i][j] == 0){
                    System.out.print(" ");
                }
                else if(printArray[i][j] == 1){
                    System.out.print("|");
                }
                else System.out.print("*");
            }
            System.out.println();
        }
    }

}
