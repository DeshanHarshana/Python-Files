import java.util.Vector;

public class VectorExample {
public static void main(String[] args) {
    Vector v=new Vector<>();
    v.add(4);
    v.add(4);
    v.add(4);
    System.out.println(v.capacity());
    //default capasiti is 10 if we add mre than 10 it will become 20 30 40 likethis
    v.forEach(System.out::println);
}
}