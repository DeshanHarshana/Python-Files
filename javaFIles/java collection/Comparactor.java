import java.util.*;

public class Comparactor {
public static void main(String[] args) {
    List<Student>list=new ArrayList<Student>();
    list.add(new Student(1,23));
    list.add(new Student(2,76));
    list.add(new Student(3,25));
    list.add(new Student(4,77));
    list.add(new Student(5,43));

    Comparator com=new Comparator<Student>() {

        @Override
        public int compare(Student o1, Student o2) {

            if(o1.marks>o2.marks){
                return -1;
            }
            else if(o1.marks>o2.marks){
                return 1;
            }
            else{
                return 0;
            }
            
            //if(o1<o2){ if we want to normal sort
                //return 1;
            //}
            
        }

    };

    
    Collections.sort(list,com);







    for (Student student : list) {
        System.out.println(student);
    }
}
}
class Student{
    int rollNum;
    int marks;

    public Student(int rollNum, int marks) {
        this.rollNum = rollNum;
        this.marks = marks;
    }

    @Override
    public String toString() {
        return "Student [marks=" + marks + ", rollNum=" + rollNum + "]";
    }
    
}