public class Exercise09_09 {
    public static void main(String[] args) {
        // Using no-arg constructor
        RegularPolygon poly1 = new RegularPolygon();

        // Using constructor with 6 sides and side length 4
        RegularPolygon poly2 = new RegularPolygon(6, 4);

        // Using constructor with 10 sides, side length 4, center at (5.6, 7.8)
        RegularPolygon poly3 = new RegularPolygon(10, 4, 5.6, 7.8);

        // Print perimeter and area of each polygon
        System.out.println("Polygon 1: ");
        System.out.println("Perimeter = " + poly1.getPerimeter());
        System.out.println("Area = " + poly1.getArea());

        System.out.println("\nPolygon 2: ");
        System.out.println("Perimeter = " + poly2.getPerimeter());
        System.out.println("Area = " + poly2.getArea());

        System.out.println("\nPolygon 3: ");
        System.out.println("Perimeter = " + poly3.getPerimeter());
        System.out.println("Area = " + poly3.getArea());
    }
}

class RegularPolygon {
    private int n;          // Number of sides
    private double side;    // Length of each side
    private double x;       // x-coordinate of center
    private double y;       // y-coordinate of center

    // No-arg constructor
    public RegularPolygon() {
        n = 3;
        side = 1;
        x = 0;
        y = 0;
    }

    // Constructor with number of sides and side length
    public RegularPolygon(int n, double side) {
        this.n = n;
        this.side = side;
        this.x = 0;
        this.y = 0;
    }

    // Constructor with all parameters
    public RegularPolygon(int n, double side, double x, double y) {
        this.n = n;
        this.side = side;
        this.x = x;
        this.y = y;
    }

    // Getters
    public int getN() {
        return n;
    }

    public double getSide() {
        return side;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    // Setters
    public void setN(int n) {
        this.n = n;
    }

    public void setSide(double side) {
        this.side = side;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    // Perimeter
    public double getPerimeter() {
        return n * side;
    }

    // Area formula
    public double getArea() {
        return (n * side * side) / (4 * Math.tan(Math.PI / n));
    }
}
