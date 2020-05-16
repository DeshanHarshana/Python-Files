import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

class Arraylist_Vs_Linked_list {
    public static void main(String[] args) {
        List<Integer> list=new LinkedList<Integer>();
        list.add(39);
        list.add(42);
        list.add(36);
        list.add(44);
        list.add(27);

        Comparator com=new Comparator<Integer>() {

            @Override
            public int compare(Integer o1, Integer o2) {

                if(o1%10>o2%10){
                    return 1;
                }
                
                //if(o1<o2){ if we want to normal sort
                    //return 1;
                //}
                return -1;
            }

        };


        Collections.sort(list,com);
        list.forEach(System.out::println);
    }

}