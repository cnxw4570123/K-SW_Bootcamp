import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Day19 {
    public static void main(String[] args) {
        List<Integer> dataArr = new ArrayList<Integer>();
        dataArr.add(188);
        dataArr.add(162);
        dataArr.add(168);

        for(Integer data: dataArr)
            System.out.println(data);
//        System.out.println(dataArr.get(0));
        dataArr.sort(Comparator.naturalOrder());
        System.out.println();
        for(Integer data: dataArr)
            System.out.println(data);


    }
}
