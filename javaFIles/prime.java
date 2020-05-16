import java.math.BigInteger;
import java.util.Scanner;
  
class GFG { 
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) 
    { 
        String n = scanner.nextLine();

  
        
        boolean result; 
  
        // Creates one BigInteger object 
        BigInteger a= new BigInteger(n); 
  
        // When certainty is one, 
        // it will check number for prime or composite 
        result = a.isProbablePrime(1); 
        if(result){
            System.out.println("prime");
        }
        else{
            System.out.println("not prime");
        }
  
        
    } 
}