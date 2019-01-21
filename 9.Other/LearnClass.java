public class LearnClass {
    private int id  = 4;
    private String name = "z";
    private int age = 23;
    private String bio = "emmmmm....";

    LearnClass(){

    }
    LearnClass(int id, String name, int age,String bio){
        this.setId(id);
        this.setName(name);
        this.setAge(age);
        this.setBio(bio);
    }

    @Override
    public String toString() {
        return "my id: " + getId() + "\n My name is: " + getName() + " age " + getAge() + " bio " + getBio();
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getBio() {
        return bio;
    }

    public void setBio(String bio) {
        this.bio = bio;
    }
}
