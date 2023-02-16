package Day24;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

public class Day24_mission {
    public static void main(String[] args) {
        System.out.println("Server start");
        try(ServerSocket svSck = new ServerSocket(9000);
            Socket client = svSck.accept();
            PrintWriter pw = new PrintWriter(client.getOutputStream())
        ){
            Date date = new Date();
            System.out.println(date.toString());
            pw.println(date.toString());
        }catch (IOException e){}
        System.out.println("Server Closed");
    }
}
