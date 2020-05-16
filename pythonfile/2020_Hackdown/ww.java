import java.util.Scanner;

class Solution {
int x=0;   
public static void main(String[] args) {
    Solution s=new Solution();
    Scanner sn=new Scanner(System.in);
    int x=sn.nextInt();
    s.setVal(x);

    printPascal(x-1);
}
public void setVal(int x){
    this.x=x;
}
public int getVal(){
    return this.x;
}
public static int binom(int n, int k)
    {
        if (k==n || k==0)
            return 1;
        else return binom(n-1,k-1) + binom(n-1, k);
    }
public static void printPascal(int n) {
    Solution xc=new Solution();
    boolean upsideDown = true;
    if(!upsideDown)
    {
        if(n < 0)
                return;
            //print the future step first, then print current step
            printPascal(n - 1);
            System.out.println();
            for(int i=0; i<n; i++){
                System.out.print(" ");
            }
            for (int k = 0; k <= n; k++)
            {
                System.out.print(binom(n, k));
            }
            

    }
    if (upsideDown)
    {

            if(n < 0)
                return;
            for(int i=xc.getVal(); n<i; i--){
                System.out.print(" ");
            }
            for (int k = 0; k <= n; k++)
            {
                System.out.print(binom(n, k) + " ");
                
            }
            
           
            System.out.println();
            printPascal(n - 1);

    }
}
}