import java.io.*;
import java.util.*;


class ArrayList2D {
    public static void main(String[] args) throws IOException {

        ArrayList<ArrayList<Integer>> mainList = new ArrayList<ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> nameList = new ArrayList<ArrayList<Integer>>();
        Scanner sn = new Scanner(System.in);
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int size1 = Integer.parseInt(bufferedReader.readLine());

        for (int i = 0; i < size1; i++) {
            ArrayList<Integer> x = new ArrayList<>();
            nameList.add(x);
        }

        for (int i = 0; i < size1; i++) {

            String[] Input = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            for (int j = 0; j < Input.length; j++) {
                int p = Integer.parseInt(Input[j]);
                nameList.get(i).add(p);

            }
            mainList.add(nameList.get(i));

        }
        
        
        ArrayList<String> result=new ArrayList<>();
        int size=Integer.parseInt(bufferedReader.readLine());
        for(int i=0; i<size; i++){
            String[] finds = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
            int listnum=Integer.parseInt(finds[0])-1;
            int index=Integer.parseInt(finds[1]);
            
            try{
                int x=mainList.get(listnum).get(index);
                result.add(String.valueOf(x));

            }catch(Exception e){
                result.add("ERROR!");
            }
        }
        result.forEach(System.out::println);
    }
    
    
}