public class inheri {
    public static void main(String[] args) {
        A1 b=new B1();
        b.printName();
    }
}
class A1{
    void printName(){
        System.out.println('A');
    }

}
class B1 extends A1{
    void printName(){
        System.out.println('A');
    }
    void sum(){
        System.out.println("sum");
    }

}