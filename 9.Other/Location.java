public class Location {
    double lng;

    double lat;

    Location next = null;


    public Location(double lng, double lat) {

        this.lng = lng;

        this.lat = lat;

    }

    public Location add(Location next_node) {

        Location tmp = this;

        while (tmp.next != null) {

            tmp = tmp.next;

        }

        // tmp is the last node

        tmp.next = next_node;

        return this; // return the last node

    }

    @Override

    public String toString() {

        String str = "";

        Location tmp = this;

        do {

            str += "Location(" + tmp.lng + ", " + tmp.lat + "), ";

            tmp = tmp.next;

        }

        while (tmp.next != null);

        str += "Location(" + tmp.lng + ", " + tmp.lat + "), ";


        return str;

        //return super.toString();

    }

}
