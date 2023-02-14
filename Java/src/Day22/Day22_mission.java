package Day22;
class Worker extends Thread{
    @Override
    public void run(){
        for(int i = 0; i < 5; i++) {
            System.out.println("작업 스레드 : " + i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
public class Day22_mission {
    public static void main(String[] args) {
        Thread t = new Thread(new Worker());
        t.start();
        int alphabet = 'a';
        for(int i = 0; i < 10; i++) {
            System.out.println("메인 스레드 : "+(char)(alphabet + i));
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }

    }
}