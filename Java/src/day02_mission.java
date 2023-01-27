import java.util.Scanner;

public class day02_mission {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("이름을 입력하세요!");
        String name = sc.nextLine();
        System.out.println("학과를 입력하세요!");
        String major = sc.next();
        System.out.println("영어 성적을 입력하세요!");
        double eng_score = sc.nextInt();
        System.out.println("수학 성적을 입력하세요!");
        double math_score = sc.nextInt();
        System.out.println("국어 성적을 입력하세요!");
        double kor_score = sc.nextInt();
        System.out.println("주소를 입력하세요!");
        String address = sc.nextLine();
        System.out.println("이름 = " + name + " 학과 = " + major);
        System.out.println("영어 = " + eng_score + " 물리학 = " +math_score + "미적분학 = " + kor_score);
        double total = eng_score + kor_score + math_score;
        System.out.println("총점 = " + total + "평균 = " + total / 3);
        System.out.println("address = " + address);



    }
}
