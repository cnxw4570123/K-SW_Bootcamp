package Day21;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class SimpleServer implements Runnable {
    private static Socket clientSocket;
    public SimpleServer(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }
    @Override
    public void run() {
        System.out.println("[" + Thread.currentThread() + "] 스레드 : ");
        try (BufferedReader br = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
             PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)
        )
        {
            String inputLine;
            while ((inputLine = br.readLine()) != null) {
                System.out.println("[" + Thread.currentThread() + "]"+"클라이언트가 보낸 메시지 : " + inputLine);
                out.println(inputLine);
            }
            System.out.println("[" + Thread.currentThread() + " 클라이언트 종료]");
        } catch (IOException ex) {
            System.out.println("입출력 예외 발생!");
        }
    }

    public static void main(String[] args) {
        ExecutorService eService = Executors.newFixedThreadPool(2); // Thread 개수 제한
        System.out.println("에코 서버 시작됨");
        try (ServerSocket serverSocket = new ServerSocket(6000)) {
            while (true) {
                System.out.println("클라이언트 접속 대기 중.....");
                clientSocket = serverSocket.accept();
                SimpleServer tes = new SimpleServer(clientSocket);
//                new Thread(tes).start();
                eService.submit(tes);
            }
        } catch (IOException ex) {
            System.out.println("문제가 발생했습니다.");
        }
        System.out.println("다중 접속 에코 서버 종료");
        eService.shutdown();
    }


//    public static void main(String[] args) {
//        System.out.println("에코 서버 시작됨");
//        try (ServerSocket serverSocket = new ServerSocket(9900)) {
//            System.out.println("클라이언트 접속 대기 중.....");
//            Socket clientSocket = serverSocket.accept();  // 접속 대기
//            System.out.println("클라이언트 접속됨.");
//
//            try (
//                    BufferedReader br = new BufferedReader(
//                            new InputStreamReader(clientSocket.getInputStream()));
//                    PrintWriter pw =
//                            new PrintWriter(clientSocket.getOutputStream(), true))
//            {
//                Stream
//                        .generate(() -> {
//                            try {
//                                return br.readLine();
//                            } catch (IOException ex) {
//                                return null;
//                            }
//                        })
//                        .peek(text -> {
//                            System.out.println("클라이언트로 부터 받은 메세지 : " + text);
//                            pw.println(text);
//                        })
//                        .allMatch(Objects::nonNull);
//            } catch (IOException e) {
//                throw new RuntimeException(e);
//            }
//        }
//        catch (IOException ex) {
//            System.out.println("접속 실패!");
//        }
//    }
}
