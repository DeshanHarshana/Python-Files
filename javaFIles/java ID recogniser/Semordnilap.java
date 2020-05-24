import java.util.Scanner;

public class Semordnilap {
    public static void main(String[] args) {
        Scanner sn=new Scanner(System.in);
        String s=sn.nextLine().toLowerCase();
        String t=sn.nextLine().toLowerCase();
        String rt="";

        for(int i=t.length()-1; i>=0; i--){
            rt=rt+t.charAt(i);
        }
        if(s.equals(rt)){
            System.out.println("Semordnilap");
        }else{
            System.out.println("Not Semordnilap");
        }
    }
    


}