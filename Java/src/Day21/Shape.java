package Day21;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Shape {
    private String type;
    private String color;
    private Double area;

    public Shape() {
    }

    public Shape(String type, String color, Double area) {
        this.type = type;
        this.color = color;
        this.area = area;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public Double getArea() {
        return area;
    }

    public void setArea(Double area) {
        this.area = area;
    }

    @Override
    public String toString() {
        return this.type+"("+this.color+", "+this.area+")";
    }

    public static final List<Shape> shapes = Arrays.asList(
            new Shape("삼각형", "빨간색", 10.5),
            new Shape("사각형", "파란색", 10.5),
            new Shape("원", "파란색", 16.5),
            new Shape("원", "빨간색", 5.3),
            new Shape("원", "노란색", 8.1),
            new Shape("사각형", "파란색", 20.7),
            new Shape("삼각형", "파란색", 3.4),
            new Shape("사각형", "빨간색", 12.6)
    );

    static List<Shape> findShapes(List<Shape> shapes, String type, String color, Double area){
        ArrayList<Shape> result = new ArrayList<Shape>();
        for(Shape shape : shapes) if(shape.getType().equals(type) && shape.getColor().equals(color) && shape.getArea() <= area) result.add(shape);
        return result;
    }

}
