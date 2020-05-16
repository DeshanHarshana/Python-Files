import java.util.Scanner;

class JavaExample {
    static int fact(int num) {
        int factorial;

        for (factorial = 1; num > 1; num--) {
            factorial *= num;
        }
        return factorial;
    }

    static int ncr(int n, int r) {
        return fact(n) / (fact(n - r) * fact(r));
    }

    public static void main(String args[]) {
        int i, j, k;

        // getting number of rows from user
        System.out.println("Enter number of rows:");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        char c = 'r';
        int num=1;
        System.out.println("Pascal Triangle:");
        for (i = n; i >= 1; i--) {
            int number = 1;
            for (k = 0; k <= (n - i); k++)
                System.out.print(" ");

            for (j = i; j <= (2 * i) - 1; j++)
                System.out.print(num);
                

            for (j = 1; j <= (i - 1); j++)
                System.out.print(num);
                
            System.out.println();
        }
    }
}