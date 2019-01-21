import java.util.ArrayList;

public class BoundingBox {
    int x,y,width,height;
    boolean infintePixel;
    ArrayList<int[]> overlappingPixel = new ArrayList<>();

    /**
     *
     * (x,y) is the left down corner of the box
     * @param x
     * @param y
     * @param width is the box width
     * @param height is the box height
     */
    public BoundingBox(int x, int y, int width, int height) {

        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;

    }
}
