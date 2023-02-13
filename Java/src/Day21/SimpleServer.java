package Day21;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class SimpleServer {
    public static void main(String[] args) {
        System.out.println("echo server");
        try (ServerSocket serverSocket = new ServerSocket(6000)){
            System.out.println("Waiting for connection.....");
            Socket clientSocket = serverSocket.accept(); // await connection
            System.out.println("client has been connected");
//            BufferedReader br;
//            PrintWriter out;
            try (
                BufferedReader br = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter pw = new PrintWriter(clientSocket.getOutputStream(), true)
            )  // expires when try block ends
            {
//                BufferedReader br = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
//                PrintWriter pw = new PrintWriter(clientSocket.getOutputStream(), true)
                String line;
                while ((line = br.readLine()) != null) {
                    System.out.println("Message From Client: " + line);

                    pw.println(line); // send to client
                }
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
//            finally {
//              br.close();
//              pw.close();
//            }
        } catch (IOException ex) {
            System.out.println("access Failed!");
        }
    }
}
