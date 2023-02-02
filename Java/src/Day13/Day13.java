package Day13;

interface Vehicle{

    public abstract void fetch();
    int YEAR = 2022;
    void start();
    static class Price{
        int discountRatio = 10;
    }
    void drive();
    default void stop(){
        System.out.println("stops");
    }
    private void show(){
        System.out.println("YEAR = " + YEAR);
    }
    public static void turn(){
        System.out.println("방향전환한다.");
    }
}
class Carrier{
    public void fetch(){
        System.out.println("carries passengers");
    }
}
abstract class Car extends Carrier implements Vehicle{ // Carrier가 첫번째 부모, vehicle이 두번째 부모

}
class Sedan extends Car{
    @Override
    public void drive(){
        System.out.println("Sedan drives");
    }
    public Sedan(){}

    @Override
    public void fetch() {
        System.out.print("Sedan ");
        super.fetch();
    }

    @Override
    public String toString() {
        return super.toString();
    }

    public void stop(){
        System.out.print("Sedan ");
        super.stop();
    }
    @Override
    public void start(){
        System.out.println("Sedan starts");
    }
}

public class Day13 {
    public static void main(String[] args) {
        Vehicle coupe = new Sedan();
        coupe.drive();
        coupe.start();
        coupe.stop();
        coupe.fetch();
        Vehicle.turn();
    }
}
