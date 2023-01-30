package Probs;

import java.util.Map;
import java.util.Scanner;

public class Ch03 {
    public static void main(String[] args) {
        foo("안녕", 1);
        foo("안녕하세요", 1, 2);
        foo("잘 있어");
    }
    static void foo(String val1){
        System.out.println(val1);
    }
    static void foo(String val1, int val2){
        System.out.println(val1 + " " + val2);
    }

    static void foo(String val1, int val2, int val3){
        System.out.println(val1+ " " + val2 + " " + val3);
    }
}
