public class LuxuryHouse extends House {
    int numGuestHouses;

    int numPatios;



    public LuxuryHouse(String houseName, int lotsize, int numLevels

            , int cuantosBaños, int numBedrooms

            , int numGuestHouses, int numPatios) {

        super(houseName, lotsize, numLevels, cuantosBaños, numBedrooms);

        this.numGuestHouses = numGuestHouses;

        this.numPatios = numPatios;

    }

    // Overrides House.tellMeAboutThisHouse()

    public void tellMeAboutThisHouse() {

        super.tellMeAboutThisHouse();

        System.out.println("** Luxury ** Guest Houses: "+ this.numGuestHouses);

        System.out.println("** Luxury ** Patios:  "+ this.numPatios);

    }
}
