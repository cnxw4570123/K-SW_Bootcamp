package Day22;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Date;

public class MulticastServer {
    public static void main(String args[]) {
        System.out.println("멀티 캐스트 타임 서버");
        DatagramSocket serverSocket = null;  // UDP
        try {
            serverSocket = new DatagramSocket();
            while (true) {
                String dateText = new Date().toString();
                byte[] buffer = new byte[256];
                buffer = dateText.getBytes();
                InetAddress group = InetAddress.getByName("224.0.0.7");
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length, group, 10_000);
                serverSocket.send(packet);
                System.out.println("전송된 시간 : " + dateText);
                try {
                    Thread.sleep(1000); // 1초단위로 delay
                } catch (InterruptedException ex) {
                    //Handle Exception
                }
            }
        } catch (IOException ex) {

        }
    }
}

