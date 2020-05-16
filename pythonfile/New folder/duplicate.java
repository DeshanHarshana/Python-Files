import java.util.*;
class duplicate2 {
    public static void main(String[] args) {
        int x[]={2,3,4,4,4,5,6,6,6,7};
       
        int length=removeDuplicateElement(x,x.length);
        for(int i=0; i<length; i++){
            System.out.println(x[i]);
        }
    
    }
        




    public static boolean isDuplicate(int arr[]) {
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

    
    

    public  static int removeDuplicateElement(int arr[], int n) {
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
