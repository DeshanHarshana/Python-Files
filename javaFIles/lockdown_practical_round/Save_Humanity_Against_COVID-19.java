import java.io.*;

import java.util.*;
class Save_Humanity {
public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

    String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

    List<Integer> sumlist = new ArrayList<Integer>();
    int total=0;
    for(String i : firstMultipleInput){
        total=total+Integer.parseInt(i);
    }
    if(firstMultipleInput.length<=1000){
        if(firstMultipleInput.length>3){
            for(int i=0; i<firstMultipleInput.length; i++){
                for(int j=0; j<firstMultipleInput.length; j++){
                    for(int k=0; k<firstMultipleInput.length; k++){
                        if((j!=k)&(k!=i)&(i!=j)){
                            int x=total-(Integer.parseInt(firstMultipleInput[i])+Integer.parseInt(firstMultipleInput[j])+Integer.parseInt(firstMultipleInput[k]));
                            sumlist.add(x);
                        }
                    }
                }
                
            }
        
        }
        else if(firstMultipleInput.length==3){
            sumlist.add(total-(Integer.parseInt(firstMultipleInput[0])+Integer.parseInt(firstMultipleInput[1])+Integer.parseInt(firstMultipleInput[2])));
        }
        else if(firstMultipleInput.length==2){
            sumlist.add(total-(Integer.parseInt(firstMultipleInput[0])+Integer.parseInt(firstMultipleInput[1])));
        }
        else if(firstMultipleInput.length==1){
            sumlist.add(total-(Integer.parseInt(firstMultipleInput[0])));
        }
    }
    Collections.sort(sumlist);
    System.out.println(sumlist.get(sumlist.size()-1));
}
}