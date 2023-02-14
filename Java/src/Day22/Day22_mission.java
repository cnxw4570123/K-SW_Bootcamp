package Day22;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Day22_mission {
    public static void main(String[] args) {
        int alphabet = 'a';
        Thread main = Thread.currentThread();
        ExecutorService executorService = Executors.newCachedThreadPool();
        Runnable task = () -> {
                for(int i = 0; i < 5; i++){
                    System.out.println("["+Thread.currentThread().getName()+ "] : " + i);
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                }
        };

        executorService.submit(task);
        for(int i = 0; i < 11; i++){
            System.out.println("["+main.getName()+ "]" + (char)(alphabet + i));
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }

        executorService.shutdown();

    }

}