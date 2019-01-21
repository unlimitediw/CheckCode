public class HouseListingSuperLuxury {
    public static void main(String[] args) {
        House dogHouse = new House("dogHouse", 4000,5,2,5);
        House catHouse = new House("catHouse", 3000,4,2,7);
        LuxuryHouse chickenHouse = new LuxuryHouse("chickenHouse",3500,2,4,
                5,15,5);
        LuxuryHouse monkeyHouse = new LuxuryHouse("monkeyHouse",3600,2,4,
                4,9,4);
        SuperLuxuryHouse sharkHouse = new SuperLuxuryHouse("sharkHouse",49600,24,43,
                44,97,44,55,12);
        SuperLuxuryHouse dinosaurHouse = new SuperLuxuryHouse("dinosaurHouse",79300,244,343,
                454,971,444,552,123);
        dogHouse.tellMeAboutThisHouse();
        catHouse.tellMeAboutThisHouse();
        chickenHouse.tellMeAboutThisHouse();
        monkeyHouse.tellMeAboutThisHouse();
        sharkHouse.tellMeAboutThisHouse();
        dinosaurHouse.tellMeAboutThisHouse();
    }
}
