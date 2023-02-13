package Day21;

public class Generic{
    static class Prints{
        //generic method
        public static <T extends Number> void PrintArray(T[] arr){
            for(T a : arr) System.out.println(a);
        }
        public static <T> T getFirst(T[] arr){
            return arr[0];
        }
    }

    public static void main(String[] args) {
        Double d1[] = {3.14, 2.71, 9.9};
        String s1[] = {"HI", "HELLO", "GREETING"};
        Integer i1[] = {10, 9, 7};
        Character c1[] = {'A', 'B', 'C'};
        Prints.PrintArray(d1);
        Prints.PrintArray(i1);
        System.out.println(Prints.getFirst(c1));
//        Prints.PrintArray(c1);
//        Prints.PrintArray(s1);
//        Prints.<Double>PrintArray(d1);
    }
}
