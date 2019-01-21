public class SuperLuxuryHouse extends LuxuryHouse{
    int numZoos;
    int numGyms;
    SuperLuxuryHouse(String houseName, int lotsize, int numLevels, int cuantosBaños, int numBedrooms
            , int numGuestHouses, int numPatios, int numZoos, int numGyms){
        super(houseName, lotsize, numLevels, cuantosBaños, numBedrooms,numGuestHouses,numPatios);
        this.numZoos = numZoos;
        this.numGyms = numGyms;
    }
    public void tellMeAboutThisHouse() {

        super.tellMeAboutThisHouse();

        System.out.println("** SuperLuxury ** numZoos: "+ this.numZoos);

        System.out.println("** SuperLuxury ** numGyms:  "+ this.numGyms);

    }
}
