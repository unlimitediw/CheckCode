public class User {
    //I am a beginner in java, do not know how to use reference of boolean like in method(boolean win). emmm.. so use this way.
    //It does not work same as function(bool& win) in c++, so sad...
    public boolean isWin() {
        return win;
    }

    public void setWin(boolean win) {
        this.win = win;
    }

    private boolean win = new Boolean(false);

}
