import java.util.Scanner;

public class day03 {
    public static void main(String[] args) {
        whoIsIt("호랑이");
        whoIsIt("사자");
        whoIsIt("독수리");
        whoIsIt("참새");
        whoIsIt("고등어");
        whoIsIt("곰팡이");
        String temp = f1(40);
        System.out.println("temp = " + temp);
    }
    public static String f1(int n){
        return switch (n){
            case 1 -> "한개";
            case 2 -> "두개";
            default -> "많이";
        };
    }
    public static void whoIsIt(String bio){
        String kind = switch (bio){
            case "사자","호랑이" -> { yield "포유류"; }
            case "독수리", "참새" -> { yield "조류"; }
            case "고등어", "참치", "새우" -> { yield "어류"; }
            default -> {
                System.out.print("어이쿠! ");
                yield "...";
            }
        };
        System.out.printf("%s는 %s이다.\n" ,bio, kind);
    }
}
