package Day24;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.UnknownHostException;

public class ClientSocket {
    public static void main(String[] args) throws IOException {
        System.out.println("Client generated");
        System.out.println("Client > ipAddress : ");
        BufferedReader brd = new BufferedReader(new InputStreamReader(System.in));
        String a = brd.readLine();

        try(Socket client = new Socket(a, 9000);
            BufferedReader br = new BufferedReader(new InputStreamReader(client.getInputStream()));
        ) {
            System.out.println("Server connected");
            String line;
            while((line = br.readLine())!= null){
                System.out.println(line);
            }
        } catch (UnknownHostException e) {
            throw new RuntimeException(e);
        }
        System.out.println("disconnected");
    }
}
