package Day13;

abstract class Mammal{
    protected int typeNum = 1;
    public Mammal(){
        System.out.println("Mammal 생성자 호출");
    }

    public void talk(){
        System.out.println("Mammal.talk");
    }
    public void status(){
        System.out.println("Mammal.status");
    }

    public abstract void moving();
}
abstract class Person extends Mammal{
    public abstract void moving();
    static String words = "hi";
    protected final int IQ = 100;
    protected String name;
    protected int typeNum = 2;
    protected int age;
    static char bloodType = 'A';

    public Person() {
        System.out.println("Person의 기본생성자");
    }
    public void status(){
        super.status();
        System.out.println("Person.status\n");
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

    public void setAge(int age) {
        this.age = age;
    }

    public void breathe() {
        System.out.println(this.name + "이 숨을 쉰다.");
    }
}

class Man extends Person {
    public void moving(){
        System.out.println("Man이 무빙, 하지만 빨랐죠");
    }
    private int money;
    private String job;
    private int typeNum = 3;
    private int IQ = 150;
    public Man(){
        System.out.println("Man의 기본생성자");
    }

    public void getIQ(){
        System.out.println("sub.IQ = " + IQ);
        System.out.println("super.IQ = " + super.IQ+"\n");
    }
    public Man(int money, String job) {
        this.money = money;
        this.job = job;
    }

    public Man(String name, int age, int money, String job) {
        super(name, age);
        this.money = money;
        this.job = job;
    }

    public void status(){
        super.status();
        System.out.printf("""
                --------
                이름은 %s,
                나이는 %d,
                직업은 %s,
                소지금은 %d
                typeNum = %d
                --------
                """, name, age, job, money, typeNum);
    }

    public void setJob(String job) {
        this.job = job;
    }

    public String getJob(){
        return job;
    }
    public void work(){
        System.out.println(name + "이 일한다");
    }
}

public class Day13 {
    public static void main(String[] args) {
//        Man m2 = new Man("유재석", 51, 700_000, "국민MC");
        Mammal m2 = new Man("유재석", 51, 700_000, "국민MC");
        m2.status(); // 오류 발생 Person 타입으로 promotion됐기 때문에 문제가 생김
        m2.talk();
        m2.moving();
    }
}
