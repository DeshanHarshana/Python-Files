import java.util.*;

public class ListExample {
public static void main(String[] args) {
    List<Integer> newList=new ArrayList<Integer>();
    newList.add(33);
    newList.add(56);
    newList.add(456);
    newList.add(1,678);
    Collections.sort(newList);
    for(Object i:newList){
        System.out.println(i);
    }
    Integer [] foos = newList.toArray(new Integer[newList.size()]);
    System.out.println(Arrays.toString(foos));//help to convert Integer type collection to array
    newList.forEach(System.out::println);
}
}