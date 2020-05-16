
import java.util.*;
class duplicate2 {
    public static void main(final String[] args) {
        int arr[]={2,3,4,4,4,5,6,6,6,7};
        findduplicate(arr);
        
    }
    public static void findduplicate(int my_array[]){
        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < my_array.length-1; i++)
        {
            for (int j = i+1; j < my_array.length; j++)
            {
                if ((my_array[i] == my_array[j]) && (i != j))
                {
                    System.out.println("Duplicate Element : "+my_array[j]);
                    list.add(my_array[j]);
                }
            }
        }
        System.out.println(list.toString());
    }    

}

class Test {
    public boolean isDuplicate(int arr[]) {
        boolean check = false;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == arr[j] & i != j) {
                    check = true;
                    break;
                }
            }
        }
        return check;
    }

    
    

    public  int removeDuplicateElement(int arr[], int n) {
        if (n == 0 || n == 1)
            return n;

        final int[] temp = new int[n];
        int j = 0;
        for (int i=0; i<n-1; i++)
            if (arr[i] != arr[i+1])
                temp[j++] = arr[i];
         
        temp[j++] = arr[n-1];   
         
        // Changing original array
        for (int i=0; i<j; i++)
            arr[i] = temp[i];
      
        return j;
    }
     
    
}