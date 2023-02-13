package Day21;

import java.util.List;

public class Shape_Main {
    public static void main(String[] args) {
        System.out.println("사각형 : "+Shape.findShapes(Shape.shapes, shp -> shp.getType().equals("사각형")));
    System.out.println("빨간 도형(면적 <= 12.0) : "+Shape.findShapes(Shape.shapes, shp -> shp.getColor().equals("빨간색") && shp.getArea() <= 12.0));

    }
}
