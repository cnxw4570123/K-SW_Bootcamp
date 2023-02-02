package Day13;

interface Vehicle{

//    public static final int YEAR = 2022;
    int YEAR = 2022;
    void start();
    static class Price{
        int discountRatio = 10;
    }
    default void stop(){
        System.out.println("정지한다.");
    }
    private void show(){
        System.out.println("YEAR = " + YEAR);
    }
    public static void turn(){
        System.out.println("방향전환한다.");
    }
}

abstract class Car implements Vehicle{

}
class Sedan extends Car{
    @Override
    public void start(){
        System.out.println("Sedan drives");
    }
}
public class Day13 {
    public static void main(String[] args) {
        Vehicle s = new Sedan();
        s.start();
        s.stop();
    }
}
