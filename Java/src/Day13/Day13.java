package Day13;

interface Vehicle{

//    public static final int YEAR = 2022;
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

abstract class Car implements Vehicle{

}
class Sedan extends Car{
    @Override
    public void drive(){
        System.out.println("Sedan drives");
    }
    public Sedan(){}

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

interface Zerg{
    int POPULATION = 10;
    default public void zergAtk(){
        System.out.println("Zerg attacks");
    }
    public abstract void display();
}

interface Terran{
    public abstract void terranAtk();
}
interface Protos{
    public abstract void protosAtk();
}
interface Game extends Zerg, Terran, Protos{
    void goodGame();
}

class StarCraft implements Game{
    @Override
    public void goodGame() {
        System.out.println("GG");
    }

    @Override
    public void display() {
        System.out.println("Zerg pop disp = " + POPULATION);
    }

    @Override
    public void terranAtk() {
        System.out.println("Terran attacks");
    }

    @Override
    public void protosAtk() {
        System.out.println("Porotos attacks");
    }
}

public class Day13 {
    public static void main(String[] args) {
        Game s1 = new StarCraft();
        s1.zergAtk();
        s1.display();
        s1.goodGame();
//         Vehicle iob = new Vehicle();
//        Vehicle s = new Sedan();
//        Sedan coupe = new Sedan();
//        Vehicle coupe = new Sedan();
        Vehicle coupe = new Sedan();
//        ((Sedan)coupe).drive();  // 다운 캐스팅 사용
        coupe.drive();
        coupe.start();
        coupe.stop();
        Vehicle.turn();
    }
}
