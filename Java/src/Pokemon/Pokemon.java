package Pokemon;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public abstract sealed class Pokemon permits  Pickachu, Ggoboogi, Pairi{
    private String owner;
//    private String skills[];
    private List<String> skills;
    private static int count = 0;

    public Pokemon(){
        Pokemon.count++;
    }

    public Pokemon(String owner, String skill_list) {
        this.owner = owner;
//        this.skills = skill_list.split("/");
        this.skills = new ArrayList<String>();
        StringTokenizer st = new StringTokenizer(skill_list, "/");
        while(st.hasMoreTokens()) this.skills.add(st.nextToken());
        System.out.print("Pokemon generated : ");
        Pokemon.count++;
    }

    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public List<String> getSkills() {
        return skills;
    }

    public void setSkills(String[] skills) {
        this.skills = List.of(skills);
    }

    public static int getCount() {
        return count;
    }

    public static void setCount(int count) {
        Pokemon.count++;
    }

    public void info(){
        System.out.println(this.owner + "'s pokemon can execute");
        for(int i = 0; i < skills.size(); i++)
            System.out.println(i+1 + " : " + skills.get(i));
    }

    public abstract void attack(int idx);
}
