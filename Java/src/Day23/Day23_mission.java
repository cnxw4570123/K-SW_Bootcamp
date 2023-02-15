package Day23;

import java.util.Arrays;
import java.util.List;

public class Day23_mission {
    public static void main(String[] args) {
        String names[] = {"홍길동", "배장화", "임꺽정", "연흥부", "김선달", "황진이"};
        List<String> nameList = Arrays.asList(names);
        nameList.stream().filter(nm -> nm.charAt(0) < '이').forEach(s -> System.out.print(s + " "));
        System.out.println();
        nameList.stream().sorted().forEach(s -> System.out.print(s + " "));
        System.out.println();
        System.out.println(nameList.stream().findFirst());
        nameList.stream().findFirst().ifPresent(System.out::println);
        System.out.println(nameList.stream().count());

    }
}
