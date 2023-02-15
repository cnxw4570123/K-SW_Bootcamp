package Day23;

import java.util.Arrays;
import java.util.List;

public class Day23_mission {

    public static void main(String[] args) {
        enum Gender{Man, Women}
        List<String> names = List.of("홍길동", "배장화", "임꺽정", "연흥부", "김선달", "황진이");
        List<Integer> ages = List.of(25, 20, 29, 28, 32, 18);
        List<Gender> genders = List.of(Gender.Man, Gender.Women, Gender.Man, Gender.Man, Gender.Man, Gender.Women);

        System.out.println(ages.stream().reduce(0,(a,b)-> a+b));
        System.out.println(ages.stream().reduce(0, (a,b)-> a > b ? a:b));
        System.out.println((double) ages.stream().reduce(0,Integer::sum)/ages.stream().count());



    }
}
