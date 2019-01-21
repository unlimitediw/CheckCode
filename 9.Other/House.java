public class House {
    int lotsize;

    int numLevels;

    int numBaths;

    int numBedrooms;

    String houseName;

    public House(int lotsize, int numLevels, int cuantosBaños, int numBedrooms)

    {

        this.lotsize = lotsize;

        this.numLevels = numLevels;

        this.numBaths = cuantosBaños;

        this.numBedrooms = numBedrooms;

    }

    // Overloading House() constructor

    public House(String houseName, int lotsize, int numLevels, int cuantosBaños, int numBedrooms)

    {

        this.lotsize = lotsize;

        this.numLevels = numLevels;

        this.numBaths = cuantosBaños;

        this.numBedrooms = numBedrooms;

        this.houseName = houseName;

    }

    public void TurnOnTheLight() {

        System.out.println("Turned on the light");

        System.out.println("It is very bright");

    }

    public void tellMeAboutThisHouse() {

        if( this.houseName != null ) {

            System.out.println(this.houseName + " --> ");

        }

        System.out.println("  lotsize: " + lotsize);

        System.out.println("  Number of levels: " + numLevels);

        System.out.println("  Cuantos baños: " + numBaths);

        System.out.println("  Number of Bedrooms: " + numBedrooms);

    }
}
