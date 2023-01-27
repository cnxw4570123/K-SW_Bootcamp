import java.util.Scanner;

public class day03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Java 점수 입력(0 ~ 100) :");
        int java_score = sc.nextInt();

        if (java_score >= 90 && java_score <= 100){
            if(java_score >= 95) System.out.println("최우수 학생");
            System.out.println("A학점");
        } else if(java_score >= 80) {
            System.out.println("B학점");
        } else if (java_score >= 70) {
            System.out.println("C학점");
        } else{
            System.out.println("F학점");
        }
    }
}
