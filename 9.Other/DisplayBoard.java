public class DisplayBoard {
    //used to show fresh board graph in each turn.
    public static void displayBoard(String[][] TTT){
        for (String x[]:TTT) {
            for (String y : x) {
                System.out.printf(y + " ");
            }
            System.out.println();
        }
    }
}
