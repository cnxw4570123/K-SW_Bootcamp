import java.util.Scanner;

public class day03 {
    public static void main(String[] args) {
        whoIsIt("호랑이");
        whoIsIt("사자");
        whoIsIt("독수리");
        whoIsIt("참새");
        whoIsIt("고등어");
        whoIsIt("곰팡이");
    }

    public static void whoIsIt(String bio){
        String kind = "";
        switch (bio){
            case "사자":
            case "호랑이":
                kind = "포유류";
                break;
            case "독수리":
            case "참새":
                kind = "조류";
                break;
            case "고등어":
            case "참치":
            case "새우":
                kind = "어류";
                break;
            default:
                System.out.print("어이쿠! ");
                kind = "...";
        }
        System.out.printf("%s는 %s이다.\n" ,bio, kind);
    }
}
