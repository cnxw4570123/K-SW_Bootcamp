class Person {
    protected final int IQ = 100;
    protected String name;
    protected int age;
//    private char sex;
    static char bloodType = 'A';

    public Person() {
        System.out.println("Person의 기본생성자");
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

class Man extends Person{
    private int money;
    private String job;

    public Man(){
        System.out.println("Man의 기본생성자");
    }
    public void status(){
        System.out.printf("%s\n", name);
        System.out.println("job = " + job);
        System.out.println("money = " + money);
    }
    public void work(){
        System.out.println(name + "이 일한다");
    }
}

public class Day12 {
    public static void main(String[] args) {
        Person chulsu = new Person();
        chulsu.name = "철수";
        System.out.println("chulsu.name = " + chulsu.name);
        Man m1 = new Man();
        m1.setName("원빈");
        m1.work();
        System.out.println("m1.getName() = " + m1.getName());
        System.out.println(sum(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
    }

    public static int sum(int... values){
        int sum =0;
        for(int no : values)
            sum += no;
        return sum;
    }
}
