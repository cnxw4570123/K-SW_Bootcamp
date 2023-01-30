package Probs;

import java.util.Map;
import java.util.Scanner;

public class Ch03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("철수 : ");
        char cs = sc.next().charAt(0);
        System.out.print("영희 : ");
        char yh = sc.next().charAt(0);
        if(cs == yh) {
            System.out.println("무승부");
        }else if(cs == 'p'){ // p r s
            if(yh == 'r')
                System.out.println("철수, 승!");
            else
                System.out.println("영희, 승!");
        } else if (cs == 'r') {
            if(yh == 's')
                System.out.println("철수, 승!");
            else
                System.out.println("영희, 승!");
        } else {
            if(yh == 'p')
                System.out.println("철수, 승!");
            else
                System.out.println("영희, 승!");
        }
    }
}
