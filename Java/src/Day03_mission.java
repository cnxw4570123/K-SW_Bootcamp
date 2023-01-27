import java.util.Scanner;

public class Day03_mission {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("소수구하기 프로그램");
        System.out.print("소수를 구할 정수 한개 입력: ");
        int number = sc.nextInt();
        int prime_count = 0;
        for(int i = 2; i <= number; i++){
            int count = 0;
            for(int j = 2; j < i; j++){ // i % j == 0 이면 소수 아님
                if( i % j == 0) {
                    count++;
                    break;
                }
            }
            if(count == 0){
                prime_count++;
                System.out.println(i + "은(는) 소수이다.");
            }
        }
        System.out.println("1~"+number+" 사이의 소수 개수 = " + prime_count);
    }
}
