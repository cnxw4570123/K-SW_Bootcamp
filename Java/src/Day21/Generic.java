package Day21;

public class Generic{
    static class Prints{
        //generic method
        public static <T> void PrintArray(T[] arr){
            for(T a : arr) System.out.println(a);
        }
    }

    public static void main(String[] args) {
        Double d1[] = {3.14, 2.71, 9.9};
        String s1[] = {"HI", "HELLO", "GREETING"};
        Integer i1[] = {10, 9, 7};
        Character c1[] = {'A', 'B', 'C'};
        Prints.PrintArray(c1);
        Prints.PrintArray(d1);
        Prints.PrintArray(i1);
        Prints.PrintArray(s1);
//        Prints.<Double>PrintArray(d1);
    }
}
