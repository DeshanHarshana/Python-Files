import java.util.Arrays;
import java.util.Scanner;

class Diagonal {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int size=Integer.parseInt(scanner.nextLine());
        int sum1=0;
        int sum2=0;
        for(int i=0; i<size; i++){
            String s[]= scanner.nextLine().split(" ");
            sum1=sum1+Integer.parseInt(s[i]);
            sum2=sum2+Integer.parseInt(s[size-1-i]);
        }
        System.out.println(Math.abs(sum1-sum2));
       
    }
}

/*
 int matrix[][]=new int[size][size];
        for(int i=0; i<size; i++){
            String s[]= scanner.nextLine().split(" ");
            int row[]=new int[s.length];
            for(int k=0; k<row.length;k++){
                row[k]=Integer.parseInt(s[k]);
            }
            for(int j=0; j<row.length; j++){
                matrix[i][j]=row[j];
            }
           
        }
       

        int sumLeft=0;
        int rightLeft=0;

        for(int i=0; i<matrix.length; i++){
            sumLeft=sumLeft+matrix[i][i];
        }
        for(int i=0; i<matrix.length; i++){
            rightLeft=rightLeft+matrix[i][(matrix.length-1)-i];
        }
       
        System.out.println(Math.abs(sumLeft-rightLeft));
        */