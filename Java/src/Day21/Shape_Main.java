package Day21;

import java.util.List;

public class Shape_Main {
    public static void main(String[] args) {
        List<Shape> shapes1 = Shape.findShapes(Shape.shapes, "사각형", "빨간색",  100.0);
        List<Shape> shapes2 = Shape.findShapes(Shape.shapes, "사각형", "파란색",  100.0);
        for(Shape shp: shapes2) shapes1.add(shp);
        shapes2.clear();
        System.out.println("사각형 :"+ shapes1);
        List<Shape> shapes3 = Shape.findShapes(Shape.shapes, "삼각형", "빨간색",  12.0);
        List<Shape> shapes4 = Shape.findShapes(Shape.shapes, "원", "빨간색",  12.0);
        for(Shape shp: shapes4) shapes3.add(shp);
        System.out.println("빨간 도형(면적 <= 12.0) :"+shapes3);

    }
}
