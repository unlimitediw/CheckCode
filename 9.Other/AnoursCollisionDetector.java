public class AnoursCollisionDetector implements CollisionDetector {

    public boolean collided(BoundingBox b1, BoundingBox b2){

        if((b2.x <= b1.x+b1.width&& b1.x <= b2.x+b2.width)&&(b2.y <= b1.y+b1.height&&b1.y <= b2.y+b2.height)){
            return true;
        }
        else{
            return false;
        }
    }
}
