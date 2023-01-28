package Probs;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Ch03 {
    public static void main(String[] args) {
        int sum = 0;
        int input = 0;
        do{
            System.out.print("양의 정수를 입력하세요: ");
            input = new Scanner(System.in).nextInt();
            if(input % 2 == 0)
                sum += input;
        } while (input != -1);
        System.out.println("입력한 양의 정수 중에서 짝수의 합은 " + sum);
    }
}
