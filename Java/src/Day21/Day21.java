package Day21;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;

public class Day21 {
    public static void main(String[] args) {

        try {
            URL url = new URL("https://www.inha.ac.kr");
            URLConnection urlConnection = url.openConnection();
            BufferedReader br = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }

        }catch (MalformedURLException e){
            e.printStackTrace();
        } catch (IOException ex) {
            System.out.println("test");
        }
    }
}
