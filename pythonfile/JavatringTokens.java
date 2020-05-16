import java.io.*;
import java.util.*;

class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        
        String[] tokensVal = s.split("[ !,?\\.\\_'@]+");
        if(s.isEmpty())
	    	   System.out.println("0");
        System.out.println(tokensVal.length);
        for(int i=0; i<tokensVal.length  && tokensVal[i] != null; i++){
            System.out.println(tokensVal[i]);
        }
        
        // Write your code here.
        scan.close();
    }
}

