import java.util.Scanner;

class Person {
    private final int IQ = 100;
    private String name;
    static char bloodType = 'A';
    private int age;

    public Person() {
        System.out.println("기본생성자");
    }

    public Person(String name, int age) {
        System.out.println("매개변수 2개인 생성자");
        this.name = name;
        this.age = age;
    }

    public static void display(){
        System.out.printf("bloodType = %c\n", bloodType);
//        System.out.println("name = " + this.name);
    }

    public void talk() {
        System.out.println("이름은 " + this.name + " 나이는 " + this.age);
    }

    public void talk(String nm, int age) {
        System.out.println("열정을 잃은 " + nm + "의 나이는 " + age);
    }

    public void talk(int age, String nm) {
        System.out.println("age = " + age);
        System.out.println("nm = " + nm);
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

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void breathe() {
        System.out.println(this.name + "이 숨을 쉰다.");
    }
}
public class Day11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Person ps = new Person();
        ps.setName("길동");
        ps.setAge(23);
        ps.talk();
        System.out.println(ps.getName());
        ps.breathe();
        System.out.println(ps);
        Person hoDong = new Person("호동", 45);
        System.out.println(hoDong);
        System.out.print("이름 입력 >> ");
        String name = sc.next();
        System.out.print("나이 입력 >> ");
        int age = sc.nextInt();
        Person np = new Person(name, age);
        System.out.println("np = " + np);
        ps.talk("자바", 23);
        ps.talk(24, "오라클");
        Person.display();
    }
}
