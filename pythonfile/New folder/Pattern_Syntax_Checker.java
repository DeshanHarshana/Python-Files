import java.util.Scanner;
import java.util.regex.*;

class Solution
{
      public static void main(String[] args){
      Scanner in = new Scanner(System.in);
      int testCases = Integer.parseInt(in.nextLine());
      while(testCases>0){
        String pattern = in.nextLine();
        if(pattern != null && !pattern.equals("")){
            try{
                Pattern.compile(pattern);
                System.out.println("Valid");
            }catch(PatternSyntaxException e){
                System.out.println("Invalid");
            }
        }
        testCases--;
        //Write your code
     }
  }
 }