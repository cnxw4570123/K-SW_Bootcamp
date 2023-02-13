package Day21;

public class Generic{
    public static void main(String[] args) {
//         Generic<String> postBox = new Generic<String>();
        PostBox<String> postBox1 = new PostBox<String>(); // 현재는 생략 불가
//        PostBox<int> postBox2 = new PostBox<Integer>(); // Primitive Type은 올 수 없고 Wrapper 클래스만 와야한다.
        PostBox<Integer> postBox2 = new PostBox<Integer>();
        postBox1.setItem("소포");
//         postBox1.setItem(77);  // Type MisMatch
         postBox2.setItem(77);
        System.out.println(postBox1.getItem());
        System.out.println(postBox2.getItem());
    }
}
