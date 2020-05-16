
import java.util.*;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class DuplicateWords {

    public static void main(String[] args) {
        List<String> list=new ArrayList<String>();
        String regex = "(\\s|^)([a-z]+)(\\s+\\2)+(?=(?:\\s|$))";
        Scanner sn=new Scanner(System.in);
        int num=sn.nextInt();
        for(int i=0; i<num+1; i++){
            String input = sn.nextLine();
            String result = input.replaceAll(regex, "");
            list.add(result);
        }
        for(String i:list){
            System.out.println(i);
        }
    }
}