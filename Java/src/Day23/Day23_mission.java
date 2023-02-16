package Day23;

import java.net.Socket;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

enum Gender{MAN, WOMEN}
class Member{

    String name;
    Gender gender;
    int age;

    public Member() {
    }

    public Member(Gender gender) {
        this.gender = gender;
    }

    public Member(String name, Gender gender, int age) {
        this.name = name;
        this.gender = gender;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public Gender getGender() {
        return gender;
    }

    public int getAge() {
        return age;
    }

    @Override
    public String toString() {
        return "Member(" +
                 name +
                ", " +gender +
                ", " + age +
                ')';
    }
}
public class Day23_mission {

//    Socket
    static int idx = 0;
    public static void main(String[] args) {
        List<String> names = List.of("홍길동", "배장화", "임꺽정", "연흥부", "김선달", "황진이");
        List<Integer> ages = List.of(25, 20, 29, 28, 32, 18);
        List<Gender> genders = List.of(Gender.MAN, Gender.WOMEN, Gender.MAN, Gender.MAN, Gender.MAN, Gender.WOMEN);
        System.out.println("[Member 스트림 원소]");
        names.stream()
                .map(nm -> new Member(nm, genders.get(idx), ages.get(idx++))).forEach(System.out::println);
        System.out.println("\n[Member 스트림을 성별로 그룹핑]");
        idx = 0;
        System.out.println( names.stream()
                .map(nm -> new Member(nm, genders.get(idx), ages.get(idx++)))
                .collect(Collectors.groupingBy(Member::getGender)));



    }
}
