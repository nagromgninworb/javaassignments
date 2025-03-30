import java.util.Scanner;

public class Exercise12_09 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a binary number: ");
        String binaryString = input.nextLine();

        try {
            int decimalValue = bin2Dec(binaryString);
            System.out.println("Decimal value: " + decimalValue);
        } catch (BinaryFormatException e) {
            System.out.println("Not a binary number");
        }

        input.close();
    }

    public static int bin2Dec(String binary) throws BinaryFormatException {
        for (int i = 0; i < binary.length(); i++) {
            char ch = binary.charAt(i);
            if (ch != '0' && ch != '1') {
                throw new BinaryFormatException("Invalid binary character: " + ch);
            }
        }

        return Integer.parseInt(binary, 2);
    }
}
