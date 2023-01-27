package Probs;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Ch03 {
    public static void main(String[] args) {

        try{
        if(new Scanner(System.in).nextInt() >= 19){
            System.out.println("성년");
        } else{
            System.out.println("미성년");
        }
        } catch(InputMismatchException e){
            System.out.println("숫자를 입력해주세요");
        } catch (IndexOutOfBoundsException e1){
            System.out.println("인덱스 문제");
        }
    }
}
