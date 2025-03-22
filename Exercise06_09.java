public class Exercise06_09 {
    public static void main(String[] args) {
        System.out.println("Feet    Meters     |     Meters    Feet");
        System.out.println("------------------------------------------");

        double feet = 1.0;
        double meters = 20.0;

        for (int i = 0; i < 10; i++) {
            double metersFromFeet = footToMeter(feet);
            double feetFromMeters = meterToFoot(meters);

            System.out.printf("%-8.1f%-12.3f|     %-10.1f%.3f\n",
                              feet, metersFromFeet, meters, feetFromMeters);

            feet++;
            meters += 5.0;
        }
    }

    public static double footToMeter(double foot) {
        return 0.305 * foot;
    }

    public static double meterToFoot(double meter) {
        return 3.279 * meter;
    }
}
