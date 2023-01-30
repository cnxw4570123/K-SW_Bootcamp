package Probs;

public class Ch03 {
    public static void main(String[] args) {
        double c;
        for (double a = 1; a < 20; a++) {
            for (double b = 1; b < 20; b++) {
                c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
                if (c == (int)c && a + b + c <= 20) { 
                    System.out.println("a = " + a + " b = " + b + " c = " + c);
                }
            }
        }
    }
}
