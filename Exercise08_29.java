import java.util.Scanner;

public class Exercise08_29 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Create two 3x3 arrays
        int[][] matrix1 = new int[3][3];
        int[][] matrix2 = new int[3][3];

        // Prompt user to enter first matrix
        System.out.print("Enter m1 (a 3-by-3 matrix) row by row: ");
        for (int i = 0; i < matrix1.length; i++) {
            for (int j = 0; j < matrix1[i].length; j++) {
                matrix1[i][j] = input.nextInt();
            }
        }

        // Prompt user to enter second matrix
        System.out.print("Enter m2 (a 3-by-3 matrix) row by row: ");
        for (int i = 0; i < matrix2.length; i++) {
            for (int j = 0; j < matrix2[i].length; j++) {
                matrix2[i][j] = input.nextInt();
            }
        }

        // Display result
        if (equals(matrix1, matrix2)) {
            System.out.println("The two arrays are identical");
        } else {
            System.out.println("The two arrays are not identical");
        }
    }

    // Method to check if two 2D arrays are identical
    public static boolean equals(int[][] m1, int[][] m2) {
        for (int i = 0; i < m1.length; i++) {
            for (int j = 0; j < m1[i].length; j++) {
                if (m1[i][j] != m2[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
}

