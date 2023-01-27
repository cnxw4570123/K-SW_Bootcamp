package Probs;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Ch03 {
    public static void main(String[] args) {
        System.out.print("등수를 입력해주세요 > ");
        switch(new Scanner(System.in).nextInt()){
            case 1 -> System.out.println("아주 잘했습니다");
            case 2, 3 -> System.out.println("잘했습니다");
            case 4, 5, 6 -> System.out.println("보통입니다");
            default -> System.out.println("노력해야겠습니다");
        }
    }
}
