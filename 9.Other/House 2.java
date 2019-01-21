public class House {
    int id;
    int lotsize;
    int numLevels;
    int numBaths;
    int numBedrooms;

    House(int id,int lotsize,int numLevels,int numBaths,int numBedrooms){
        this.id = id;
        this.lotsize = lotsize;
        this.numLevels = numLevels;
        this.numBaths = numBaths;
        this.numBedrooms = numBedrooms;
        print();
    }

    void print(){
        System.out.println("House " + id + ":");
        System.out.println("  lotsize: " + lotsize);
        System.out.println("  Number of levels: " + numLevels);
        System.out.println("  Number of Bathrooms: " + numBaths);
        System.out.println("  Number of Bedrooms: " + numBedrooms);
    }
}
