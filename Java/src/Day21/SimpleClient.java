package Day21;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.util.Scanner;
import java.util.function.Supplier;

public class SimpleClient {
    public static void main(String[] args) {
        System.out.println("echo client starts");
        try {
            InetAddress localAddress = InetAddress.getLocalHost();
            Socket clientSocket = null;
            PrintWriter pw = null;
            BufferedReader br = null;
            try {
                clientSocket = new Socket(localAddress, 9900);
//                clientSocket = new Socket("165.246.116.122", 9900);
                pw = new PrintWriter(clientSocket.getOutputStream(), true);
                br = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                System.out.println("Connected to server");
                Scanner sc = new Scanner(System.in);

                while (true) {
                    System.out.print("Enter text: ");
                    String line = sc.nextLine();
                    if ("EXIT".equalsIgnoreCase(line)) {
                        break;  // 종료 조건
                    }
                    pw.println(line);  // 서버로 전송
                    System.out.println("Echo from server: " + br.readLine()); // 서버로부터 수신 받은 객체의 라인단위로 문자열 리턴
                }

            } catch (IOException ex) {
                System.out.println("IOexception");
            } finally { // 자원 해제
                clientSocket.close();
                pw.close();
                br.close();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}