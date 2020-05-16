
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Pattern;

class r {

    /* driver function to check */
    public static void main(String[] args) {
        List<String> list=new ArrayList<String>();
        Scanner sn=new Scanner(System.in);
        int num=sn.nextInt();
        for(int i=0; i<num; i++){
            String string=sn.nextLine();
        list.add(string);
        }
        for(int i=0; i<list.size(); i++){
        if (isValid(list.get(i))){
            System.out.println("Valid");
        }
        else{
            System.out.println("Invalid");
        }
    }
            
    }

    public static boolean isValid(String email) {
        String Regex = "^[aA-zZ]\\w{7,29}$";

        Pattern pat = Pattern.compile(Regex);
        if (email == null)
            return false;
        return pat.matcher(email).matches();

    }
}