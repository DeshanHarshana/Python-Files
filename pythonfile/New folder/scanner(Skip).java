import java.util.Scanner;
import java.util.regex.Pattern;

class scanner_Skip {
public static void main(String[] args) {
    /*
        Scanner scan = new Scanner("Hello World! SSSIT 102 Hindi100 150 123");  
        //Skip the word that matches the specified pattern  
        scan.skip(Pattern.compile("..llo"));  
        System.out.println("Left String: " +scan.nextLine());  
        scan.close();  
        */
        String str = "JavaTpoint 102 131 150 123";  
       //Initialize Scanner object  
       Scanner scan = new Scanner(str);  
       //Initialize the String pattern  
       String pattern = "[a-zA-Z]*";  //skip letters
       //Printing the tokenized Strings  
       while(scan.hasNext()){  
           //Skipping first occurrence of the Pattern  
           scan.skip(pattern);  
           System.out.println(scan.next());  
       }  
       scan.close();  
}
}

/*
The skip() is a method of Java Scanner class which skips input that matches the specified pattern, ignoring delimiters. There are two different types of Java Scanner skip() method which can be differentiated depending on its parameter. These are:

Java Scanner skip(String pattern) Method
Java Scanner skip(Pattern pattern) Method
*/