import java.util.*;

class Comparitor_Interface {
    public static void main(String[] args) {
        List<Student1>list=new ArrayList<Student1>();
        list.add(new Student1(1,23));
        list.add(new Student1(2,76));
        list.add(new Student1(3,25));
        list.add(new Student1(4,77));
        list.add(new Student1(5,43));
    
       
      
    
        Collections.sort(list);
    
    
        for (Student1 student : list) {
            System.out.println(student);
        }
    }
    }
    class Student1 implements Comparable<Student1>{
        int rollNum;
        int marks;
    
        public Student1(int rollNum, int marks) {
            this.rollNum = rollNum;
            this.marks = marks;
        }
    
        @Override
        public String toString() {
            return "Student [marks=" + marks + ", rollNum=" + rollNum + "]";
        }

        
        @Override
        public int compareTo(Student1 o) {
            if(this.marks>o.marks){
                return -1;
            }
            else if(this.marks<o.marks){
                return 1;
            }
            else{
                return 0;
            }
            
        }
        
    }