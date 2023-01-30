package Probs;

import java.util.Map;
import java.util.Scanner;

public class Ch03 {
    public static void main(String[] args) {
        System.out.println(factorial(5));
    }

    static int factorial(int n){
        switch (n) {
            case 1 -> {
                return 1;
            }
            default -> {
                return n * factorial(n - 1);
            }
        }
    }

}
