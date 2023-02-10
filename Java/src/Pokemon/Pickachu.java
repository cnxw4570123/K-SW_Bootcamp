package Pokemon;

public class Pickachu extends Pokemon{
    private String name;

    public Pickachu(){
        super();
    }

    public Pickachu(String owner, String skill_list){
        super(owner, skill_list);
        this.name = "Pickachu";
        System.out.println(this.name);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public void attack(int idx) {
        System.out.println("[Pika~!]"+ this.getOwner()+"'s Pokemon "+getName() + " excutes (electric)" + getSkills()[idx - 1]);
    }

}
