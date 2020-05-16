import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class collection2 {
public static void main(String[] args) {
    Object object[]=new Object[5];
    object[1]="deshan";
    object[2]=23;
    System.out.println(object[1].toString());
    System.out.println(object[2].toString());

    // Collection vlaue=new ArrayList();
    // vlaue.add('e');
    // vlaue.add(23);
    // vlaue.add(34.44);
    Collection<Integer> vlaue=new ArrayList<Integer>();
    vlaue.add(55);
    vlaue.add(554);
    vlaue.add(545);

    // Iterator i=vlaue.iterator();
    // System.out.println(i.next());
    // System.out.println(i.next());
    // System.out.println(i.next());

    // while(i.hasNext()){
    //     System.out.println(i.next());
    // }

    // for(Object i : vlaue){
    //     System.out.println(i.toString());

    // }
    for(int i : vlaue){
         System.out.println(i);

    }
}
}