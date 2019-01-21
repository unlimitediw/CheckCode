import java.sql.*;
import java.util.HashMap;

public class wallMsgSQL {
    Connection conn = null;
    Statement stmt = null;
    String s1 = String.format("%1$-" + 15 + "s", "WallOwner");
    String s2 = String.format("%1$-" + 15 + "s", "Author");
    String s3 = String.format("%1$-" + 15 + "s", "Msg");
    String outputString = (s1 + "  " + s2 + "  " + s3 + "\n");
    HashMap<Integer, String> userHash = new HashMap<>();

    wallMsgSQL(int givenID) {
        try {
            conn = DriverManager
                    .getConnection("jdbc:mysql://localhost/hw9?" + "user=root&password=12345678&useSSL=false");


            stmt = conn.createStatement();
            String sql = "SELECT id,scname FROM users";
            ResultSet userRs = stmt.executeQuery(sql);
            // STEP 5: Extract data from result set
            while (userRs.next()) {
                userHash.put(userRs.getInt("id"), userRs.getString("scname"));
            }
            sql = "SELECT id, wall_owner_id, author_id, msg, postDate FROM wallMsg";
            ResultSet rs = stmt.executeQuery(sql);
            while (rs.next()) {
                // Retrieve by column name
                int wall_owner_id = rs.getInt("wall_owner_id");
                if (wall_owner_id != givenID) {
                    continue;
                }
                int author_id = rs.getInt("author_id");
                String msg = rs.getString("msg");

                // Display values
                String ownerIDString = userHash.get(wall_owner_id);
                String authorIDString = userHash.get(author_id);
                ownerIDString = String.format("%1$-" + 15 + "s", ownerIDString);
                authorIDString = String.format("%1$-" + 15 + "s", authorIDString);
                outputString += ownerIDString;
                outputString += "  ";
                outputString += authorIDString;
                outputString += "  ";
                outputString += msg;
                outputString += "\n \n";
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
