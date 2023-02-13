import java.net.InetAddress;
import java.net.UnknownHostException;

public class Day20 {
    public static void main(String[] args) {
        try {
            InetAddress addr = InetAddress.getByName("www.inha.ac.kr");
//            InetAddress addr = InetAddress.getByName("www.kiminha.ac.kr");
//            System.out.println("addr = " + addr);
            System.out.println("addr.CanonicalHostName = " + addr.getCanonicalHostName());
            System.out.println("addr.HostAddress = " + addr.getHostAddress());
            System.out.println("addr.getHostName() = " + addr.getHostName());
            
        } catch (UnknownHostException e) {
//            throw new RuntimeException(e);
            System.out.println("there's no domain for this URL");
        }
    }
}
