package Day21;

class Dp<K, V>{ // Key, Value
    private K name;
    private V grade;

    public Dp() {
    }

    public Dp(K name, V grade) {
        this.name = name;
        this.grade = grade;
    }

    public K getName() {
        return name;
    }

    public void setName(K name) {
        this.name = name;
    }

    public V getGrade() {
        return grade;
    }

    public void setGrade(V grade) {
        this.grade = grade;
    }
}
public class Generic2 {
    public static void main(String[] args) {
        Dp<String, String> s1 = new Dp<>("안준호", "일병");
        Dp<String, Integer> s2 = new Dp<>("안준호", 3);
        Dp<String, String> s3 = new Dp<>("임지섭", "대위");
        Dp<PostBox<String>, String> s4 = new Dp<>( new PostBox<String>("돼지"), "문자열");
        System.out.println(s1.getName() + "의 계급은 "+ s1.getGrade()  +  "입니다.");
        System.out.println(s2.getName() + "의 계급은 "+ s2.getGrade()  +  "입니다.");
        System.out.println(s3.getName() + "의 계급은 "+ s3.getGrade()  +  "입니다.");
        System.out.println(s4.getName() + "의 계급은 "+ s4.getGrade()  +  "입니다.");

    }
}
