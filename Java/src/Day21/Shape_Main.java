package Day21;

public class Shape_Main {
    public static void main(String[] args) {
        System.out.println("사각형 : "+Shape.findShapesByType(Shape.shapes, "사각형"));
        System.out.println("빨간 도형(면적 <= 12.0) :"+Shape.findShapesByColorNArea(Shape.shapes, "빨간색", 12.0));
    }
}
