import java.util.Arrays;
import java.util.Scanner;

class Q1 {
    public static void main(String[] args) {
        Scanner i = new Scanner(System.in);
        int boxes[] = new int[i.nextInt()];
        int x = 0;
        int defferent = 0;
        for (int c = 0; c < boxes.length; c++) {
            boxes[c] = i.nextInt();
        }
        for (int a = 0; a < boxes.length; a++) {
            x = boxes[a] / 5;
            defferent = boxes[a] - x * 5;
            if (defferent <= 2)
                boxes[a] = x * 5;
            else
                boxes[a] = (x + 1) * 5;
        }
        System.out.println(Arrays.toString(boxes));

    }
}