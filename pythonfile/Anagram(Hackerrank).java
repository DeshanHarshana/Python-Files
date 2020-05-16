import java.util.*;

class Anagram {
    static boolean isAnagram(String a, String b) {
        boolean isAnagram=false;
        if(a.length()==b.length()){
            for(int i=0; i<a.length(); i++){
                if(count(a, b.charAt(i))==count(b, b.charAt(i))){
                    isAnagram=true;
                }
                else{
                    isAnagram=false;
                }
            }
        }
        return isAnagram;
}
static int count(String word, char letter){
    int count=0;
    for(int i=0; i<word.length(); i++){
        if(word.charAt(i)==letter){
            count++;
        }
    }
    return count;
}

public static void main(String[] args) {
    
    
    Scanner scan = new Scanner(System.in);
    String a = scan.next();
    String b = scan.next();
    scan.close();
    boolean ret = isAnagram(a, b);
    System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    //if ret true print anagrams othrwise print npt anagaram
    
}
}