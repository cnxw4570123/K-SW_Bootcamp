package Day01;

public class day1_mission {
    public static void main(String[] args) {
        byte var1 = 127;
        int var3 = 128;
        var1 = (byte)var3;
        System.out.println("var1 = " + var1);
        float var5 = 123456.789123f;
        System.out.println("var5 = " + var5);
        double var6 = 123456.789123;
        var5 = (float) var6;
        System.out.println("var5 = " + var5);
    }
}
