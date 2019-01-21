import java.sql.*;

public class helloMySQL {
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Connection conn = null;
        Statement stmt = null;
        try {
            conn = DriverManager
                    .getConnection("jdbc:mysql://localhost/hw9?" + "user=root&password=12345678&useSSL=false");

            String sql = "SELECT id, wall_owner_id, author_id, msg, postDate FROM wallMsg";
            stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            // STEP 5: Extract data from result set
            while (rs.next()) {
                // Retrieve by column name
                int id = rs.getInt("id");
                int wall_owner_id = rs.getInt("wall_owner_id");
                int author_id = rs.getInt("author_id");
                String msg = rs.getString("msg");
                String postDate = rs.getString("postDate");

                // Display values
                System.out.println("ID: " + id);
                System.out.println(", wall_owner_id: " + wall_owner_id);
                System.out.println(", author_id: " + author_id);
                System.out.println(", msg: " + msg);
                System.out.println(", postDate: "+postDate);
                System.out.println("");
            }
            rs.close();

        } catch (SQLException ex) {
            // handle any errors
            System.out.println("SQLException: " + ex.getMessage());
            System.out.println("SQLState: " + ex.getSQLState());
            System.out.println("VendorError: " + ex.getErrorCode());
        }
    }

}
