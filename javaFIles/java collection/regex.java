

import java.util.regex.Pattern;

class r {

    /* driver function to check */
    public static void main(String[] args) {
        String String_We_Want_to_check = ".213.123.23.32";
        if (isValid(String_We_Want_to_check))
            System.out.print("Valid");
        else
            System.out.print("Invalid");
            String t="";
            t.ma
    }

    public static boolean isValid(String email) {
        String Regex = "(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)";

        Pattern pat = Pattern.compile(Regex);
        if (email == null)
            return false;
        return pat.matcher(email).matches();

    }
}