import java.util.Random;

public class testCollision {
    public static void main(String[] args) {

        CollisionDetector d = new AnoursCollisionDetector();

        /**
         * Suppose our scene is 2D
         * the domain of left-down corner of box is x(0,10),y(0,10)
         * the domains of size of width and height are width(0,2) and height(0,2)
         * We use 2000 random instances to test the collision rate
         */

        /**
         * Test case 1: overlapping as pictured is generated automatically in the output as you can see
         * Test case 2 and 3 can be finished in the same principle but we can simply show several instance examples
         *
         * Example1:
         * Test case    Detail                                                      Expected    actual
         * Test case 1: b1{(3,0),height-4,width-5} b2{(6,1),height-6,width-5}       true        true
         * Test case 2: interact at (6,4) and (7,4)                                 true        true
         * Test case 3: not overlapping on line                                     false       false
         *
         * Example2:
         * Test case    Detail                                                      Expected    actual
         * Test case 1: b1{(6,4),height-4,width-6} b2{(8,1),height-5,width-3}       true        true
         * Test case 2: interact at (8,4) and (11,4)                                true        true
         * Test case 3: not overlapping on line                                     false       false
         */

        int i = 0;
        float n = 2000;
        float hit = 0;
        Random rand = new Random();

        while (i < n) {
            BoundingBox b1 = new BoundingBox(rand.nextInt(10), rand.nextInt(10), rand.nextInt(7), rand.nextInt(7));

            BoundingBox b2 = new BoundingBox(rand.nextInt(10), rand.nextInt(10), rand.nextInt(7), rand.nextInt(7));

            if (d.collided(b1, b2)) {
                hit++;
                System.out.println("Collides!");
                System.out.println("Test case 1: ");
                System.out.println("    coordinate: (" + b1.x + ", " + b1.y + ") and height: " + b1.height + " and width: " + b1.width);
                System.out.println("    coordinate: (" + b2.x + ", " + b2.y + ") and height: " + b2.height + " and width: " + b2.width);
            } else {
                System.out.println("Does not collide");
            }
            i++;
        }
        System.out.println("Hit rate: " + String.format("%.2f", 100. * hit / n) + "%");
    }

}


