
import java.io.*;

class q3 {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int A = Integer.parseInt(firstMultipleInput[0]);

        int B = Integer.parseInt(firstMultipleInput[1]);

        int M = Integer.parseInt(firstMultipleInput[2]);

        int max = -100000;
        for (int i = A; i <= B; i++) {

            int rem = i % M;
            if (max <= rem) {
                max = rem;
            }
            
        }
        System.out.println(max);

        bufferedReader.close();
    }

}
