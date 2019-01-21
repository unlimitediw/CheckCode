public class Person {
    private MaritalState maritalState;

    public Person(String status){
        maritalState = new MaritalState(status);
    }

    public void setMaritalState(String status) {
        maritalState.setStatus(status);
    }

    public String getMaritalState() {
        return maritalState.getStatus();
    }
}
