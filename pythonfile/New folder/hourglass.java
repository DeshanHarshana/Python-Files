import java.util.Arrays;
import java.util.Scanner;

public class hourglass {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
		
		int[][] ar = new int[6][6];
		for (int i = 0; i < 6; i++) {
			String[] t = in.nextLine().split(" ");
			for (int j = 0; j < 6; j++) {
				ar[i][j] = Integer.valueOf(t[j]);
			}
		}

        scanner.close();

        int sumarray[] = new int[16];
        
        int z = 0;
        for (int a = 0; a < 4; a++) {
            for (int b = 0; b < 4; b++) {
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        sumarray[z] = sumarray[z] + ar[i+a][j+b];
                    }
                    System.out.println();
                }
                z++;
            }
        }
        Arrays.sort(sumarray);
        System.out.println(sumarray[15]);

    }
}