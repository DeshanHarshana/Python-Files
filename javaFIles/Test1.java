import java.util.Scanner;

class Student {
    private int id = 0;
    private String name = "";
    private int age = 0;

    public Student setName(final String name) {
        this.name = name;
        return this;
    }

    public Student setId(final int id) {
        this.id = id;
        return this;
    }

    public Student setAge(final int age) {
        this.age = age;
        return this;
    }

    @Override
    public String toString() {
        return "Student [age=" + age + ", id=" + id + ", name=" + name + "]";
    }
}

class Test {
    public static void main(final String[] args) {
        final Student student = new Student().setAge(12).setName("Amila").setId(1);
        System.out.println(student.toString());
        final String s = "dfasdas";
        
    }
}