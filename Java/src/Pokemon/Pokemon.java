package Pokemon;


public class Pokemon {
    private String owner;
    private String skills[];
    private static int count = 0;

    public Pokemon(){
        Pokemon.count++;
    }

    public Pokemon(String owner, String skill_list) {
        this.owner = owner;
        this.skills = skill_list.split("/");
        System.out.print("Pokemon generated : ");
        Pokemon.count++;
    }

    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public String[] getSkills() {
        return skills;
    }

    public void setSkills(String[] skills) {
        this.skills = skills;
    }

    public static int getCount() {
        return count;
    }

    public static void setCount(int count) {
        Pokemon.count++;
    }

    public void info(){
        for(int i = 0; i < skills.length; i++)
            System.out.println(i+1 + " : " + skills[i]);
    }

    public void attack(int idx){
        System.out.println(skills[idx] + " excuted");
    }
}
