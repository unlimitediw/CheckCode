public class EveryDay {
    String[] everyDay = new String[7];

    public void printEverday(){
        System.out.println(everyDay[0]+"\n"+
                everyDay[1]+"\n"+
                everyDay[2]+"\n"+
                everyDay[3]+"\n"+
                everyDay[4]+"\n"+
                everyDay[5]+"\n"+
                everyDay[6]+"\n");
    }

    EveryDay(){
        everyDay[0] = "Sunday";
        everyDay[1] = "Monday";
        everyDay[2] = "Tuesday";
        everyDay[3] = "Wednesday";
        everyDay[4] = "Thursday";
        everyDay[5] = "Friday";
        everyDay[6] = "Saturday";
    }
}
