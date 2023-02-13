package Pokemon;

public non-sealed class Pairi extends Pokemon{
    private String name;

    public Pairi(){
        super();
    }

    public Pairi(String owner, String skill_list){
        super(owner, skill_list);
        this.name = "Pairi";
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
        System.out.println("[Pai!]"+ getOwner()+"'s Pokemon "+getName() + "excutes (fire)" + getSkills().get(idx - 1));
    }
}
