

public class Matrix_Multiple {
    public static void main(String[] args) {
        int x[][]={ {-55,-4,7},
        {4,-55,6},
        {4,5,6},
                       };

        int y[][]={ {1,2,3},
                    {0,1,4},
                    {5,6,0},
                   
                       };

        //print(multiple(x, y));
        //print(transpose(y));
        print(inverse(y));
        
                            
        
    }
    static void print(double z[][]){
        for(int i=0; i<z.length; i++){
            for(int j=0; j<z[0].length; j++){
                System.out.print(z[i][j] + "\t");
            }
            System.out.println("\n");
        }
    }

    static double[][] inverse(int arr[][]){
        int det=
         arr[0][0]*(arr[1][1]*arr[2][2]-arr[2][1]*arr[1][2])
        -arr[0][1]*(arr[1][0]*arr[2][2]-arr[2][0]*arr[1][2])
        +arr[0][2]*(arr[1][0]*arr[2][1]-arr[2][0]*arr[1][1]);

        int trans[][]=transpose(arr);
        int detarr[]=new int[9];
        detarr[0]=1*(trans[1][1]*trans[2][2]-trans[2][1]*trans[1][2]);
        detarr[1]=-1*(trans[1][0]*trans[2][2]-trans[2][0]*trans[1][2]);
        detarr[2]=1*(trans[1][0]*trans[2][1]-trans[2][0]*trans[1][1]);

        detarr[3]=-1*(trans[0][1]*trans[2][2]-trans[2][1]*trans[0][2]);
        detarr[4]=1*(trans[0][0]*trans[2][2]-trans[2][0]*trans[0][2]);
        detarr[5]=-1*(trans[0][0]*trans[2][1]-trans[2][0]*trans[0][1]);
        
        detarr[6]=1*(trans[0][1]*trans[1][2]-trans[1][1]*trans[0][2]);
        detarr[7]=-1*(trans[0][0]*trans[1][2]-trans[1][0]*trans[0][2]);
        detarr[8]=1*(trans[0][0]*trans[1][1]-trans[1][0]*trans[0][1]);

        double adj[][]=new double[3][3];
        int count=0;
        for(int i=0; i<adj.length; i++){
            for(int j=0; j<adj[0].length; j++){
                adj[i][j]=detarr[count];
                count++;
            }
        }

        double inverse[][]=new double[3][3];
        for(int i=0; i<inverse.length; i++){
            for(int j=0; j<inverse[0].length; j++){
                inverse[i][j]=(1/det)*adj[i][j];
            }
        }

       return inverse;
    }

    static int[][] transpose(int arr[][]){
        int trans[][]=new int[arr[0].length][arr.length];
        for(int i=0; i<arr.length; i++){
            for(int j=0; j<arr[0].length; j++){
                trans[j][i]=arr[i][j];
            }
        }
        return trans;
    }

    static int[][] multiple(int arr1[][], int arr2[][]){
        if(arr1[0].length==arr2.length){
            int arr3[][]=new int[arr1.length][arr2[0].length];
            for(int i=0; i<arr3.length; i++){
                for(int j=0; j<arr3[0].length; j++){
                    int sum=0;
                    for(int k=0; k<arr2.length; k++){
                        sum+=arr1[i][k]*arr2[k][j];
                    }
                    arr3[i][j]=sum;
                }
            }
            return arr3;
        }
        else{
            System.out.println("Given Metrix Can't multiple");
            int z[][]=new int[0][0];
            return z;
        }
        
    }
}