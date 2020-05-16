import java.util.HashSet;
import java.util.Set;

class Sets {
public static void main(String[] args) {
    Set<Integer> set=new HashSet<>();
    set.add(34);
    set.add(23);
    set.add(87);
    set.add(34);//duplicate value not add

    set.forEach(System.out::println);
    
}
}