import java.io.*;
import java.util.*;
class findDuplicate {
public static void main(String[] args) {
    int listarray[]={2,4,6,5,7,7,6};
    find_duplicate(listarray);
}
static void find_duplicate(int x[]){
    List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < x.length-1; i++)
        {
            for (int j = i+1; j < x.length; j++)
            {
                if ((x[i] == x[j]) && (i != j))
                {
                    System.out.println("Duplicate Element : "+x[j]);
                    list.add(x[j]);
                }
            }
        }
        System.out.println(list.toString());
    }    
}
