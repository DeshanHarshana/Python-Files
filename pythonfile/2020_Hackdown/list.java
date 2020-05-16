import java.util.ArrayList;
import java.util.List;

public class list {
public static void main(String[] args) {
    List<Integer> lst=new ArrayList<>();
    lst.add(45);
    lst.add(56);
    lst.clear();
    lst.add(43);
    System.out.println(lst);
}
}