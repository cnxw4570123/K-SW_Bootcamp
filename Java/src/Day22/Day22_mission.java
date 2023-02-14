package Day22;

class Worker extends Thread{
    @Override
    public void run() {
        for(int i = 0; i < 5; i++){
            System.out.printf("[%s] : %d\n", getName(), i);
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
        int alphabet = 'a';
        Thread main = Thread.currentThread();
        Worker w = new Worker();
        w.start();
        for(int i = 0; i < 11; i++){
            System.out.println("["+main.getName()+ "]" + (char)(alphabet + i));
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }

}