package Day03;

public class day03 {
    public static void main(String[] args) {
        for(int i = 2; i < 10; i++){
//            if (i == 6)
//                break;
            for(int j = 1; j < 10; j++){
                if(j == 4)
                    break;
                System.out.println(i + " * " + j + " = " + i*j);
            }
            System.out.println("----------");
        }
    }
}