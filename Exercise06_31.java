import java.util.Scanner;

public class Exercise06_31 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a credit card number as a long integer: ");
        long number = input.nextLong();

        if (isValid(number)) {
            System.out.println(number + " is valid");
        } else {
            System.out.println(number + " is invalid");
        }
    }

    /** Return true if the card number is valid */
    public static boolean isValid(long number) {
        int size = getSize(number);
        boolean correctPrefix = prefixMatched(number, 4) || prefixMatched(number, 5) ||
                                prefixMatched(number, 37) || prefixMatched(number, 6);
        int total = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number);
        return (size >= 13 && size <= 16) && (total % 10 == 0) && correctPrefix;
    }

    /** Get the result */
    public static int sumOfDoubleEvenPlace(long number) {
        int sum = 0;
        String numStr = Long.toString(number);
        for (int i = numStr.length() - 2; i >= 0; i -= 2) {
            int digit = Character.getNumericValue(numStr.charAt(i));
            sum += getDigit(digit * 2);
        }
        return sum;
    }

    /** Return this number if it is a single digit, otherwise return the sum of the two digits */
    public static int getDigit(int number) {
        if (number < 10)
            return number;
        return number / 10 + number % 10;
    }

    /** Return sum of odd-place digits in number */
    public static int sumOfOddPlace(long number) {
        int sum = 0;
        String numStr = Long.toString(number);
        for (int i = numStr.length() - 1; i >= 0; i -= 2) {
            int digit = Character.getNumericValue(numStr.charAt(i));
            sum += digit;
        }
        return sum;
    }

    /** Return true if the number d is a prefix for number */
    public static boolean prefixMatched(long number, int d) {
        int prefixSize = getSize(d);
        return getPrefix(number, prefixSize) == d;
    }

    /** Return the number of digits in d */
    public static int getSize(long d) {
        return Long.toString(d).length();
    }

    /** Return the first k number of digits from number. If number has fewer digits, return number */
    public static long getPrefix(long number, int k) {
        String numStr = Long.toString(number);
        if (numStr.length() < k) {
            return number;
        }
        return Long.parseLong(numStr.substring(0, k));
    }
}
