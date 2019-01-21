
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class MaritalState {
    private Map<String,HashSet<String>> statusMap = new HashMap<>();
    private String status = null;

    public MaritalState(String status){
        // relationship initialization
        statusMap.put("single",new HashSet<>());
        statusMap.put("married",new HashSet<>());
        statusMap.put("divorced",new HashSet<>());
        statusMap.put("widow",new HashSet<>());
        statusMap.get("single").add("married");
        statusMap.get("married").add("divorced");
        statusMap.get("married").add("widow");
        statusMap.get("divorced").add("married");
        statusMap.get("widow").add("married");
        if(statusMap.containsKey(status)) {
            this.status = status;
        }
        else{
            System.out.println("Invalid initialization");
        }
    }

    public void setStatus(String status) {
        if(status != null){
            if(statusMap.get(this.status).contains(status)) {
                this.status = status;
            }
            else{
                System.out.println("Invalid status.");
            }
        }
        else{
            System.out.println("State not init yet.");
        }
    }

    public String getStatus() {
        if(status != null){
            return status;
        }
        else{
            System.out.println("State not init yet.");
            return "";
        }
    }

}
