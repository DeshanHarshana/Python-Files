import java.io.*;
import java.util.*;

class ArrayListEXapmle {

    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> listOfLists = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> sublist1=new ArrayList<>();
        ArrayList<Integer> sublist2=new ArrayList<>();
        sublist1.add(34);
        sublist1.add(12);
        sublist2.add(87);
        sublist2.add(12);
        listOfLists.add(sublist1);
        listOfLists.add(sublist2);
        listOfLists.get(0).add(211);
        System.out.println(listOfLists.get(1).get(0));
        listOfLists.clear();
        System.out.println(listOfLists);
    }
}