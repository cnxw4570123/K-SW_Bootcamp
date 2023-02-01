import java.util.Scanner;

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
