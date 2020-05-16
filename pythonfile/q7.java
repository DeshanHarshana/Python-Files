import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class q7 {
    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] Input = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
        System.out.println(Arrays.toString(Input));
        Arrays.sort(Input, Collections.reverseOrder());
        System.out.println(Arrays.toString(Input));
        
        
        
        String firstElementarr[]=new String[3];
        int indexArray[]=new int[3];
        for(int i=0; i<firstElementarr.length; i++){
            if(isNumeric(Input[i])){
                firstElementarr[i]=Input[i];
            }
        }
        System.out.println(Arrays.toString(firstElementarr));
        bufferedReader.close();
    }
    public static boolean isNumeric(String str)
{
    return str.matches("[+-]?\\d*(\\.\\d+)?");
}
}