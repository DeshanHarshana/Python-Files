import java.util.ArrayList;
import java.util.Collection;

class Col{
    public static void main(String[] args) {
        Collection<Integer> value=new ArrayList<Integer>();
        value.add(54);
        System.out.println(value.size());
        A a=new B();
        a.show();
    }
}

interface A{
    void show();
}
class B implements A{

    @Override
    public void show() {
       System.out.println("hello");

    }

}