import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class q3 {
public static void main(String[] args) {
    ArrayList<String> list=new ArrayList<String>();
    ArrayList<Integer> fibList=new ArrayList<Integer>();
    Scanner s=new Scanner(System.in);
    int count=s.nextInt();
    for(int i=0; i<=count; i++){
    String str = s.nextLine();     
    str = str.replaceAll("[^-?0-9]+", " "); 
    String[] elements = str.split(" ");
    for(String x: elements){
        list.add(x);
    }
    
    
}
    list.remove(0);
    
    for(String i: list){
        if(isFibonacci(Integer.parseInt(i))){
            fibList.add(Integer.parseInt(i));
        }
    }
   
    Collections.sort(fibList);
    System.out.println(fibList.get(fibList.size()-1));




}
static boolean isFibonacci(int n) 
    { 
        // n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
        // is a perfect square 
        return isPerfectSquare(5*n*n + 4) || 
               isPerfectSquare(5*n*n - 4); 
    } 
    static  boolean isPerfectSquare(int x) 
    { 
        int s = (int) Math.sqrt(x); 
        return (s*s == x); 
    } 
}
