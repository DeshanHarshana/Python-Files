import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


class q6 {
    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] Input = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
        int numofTeachers = Integer.parseInt(Input[0]);
        int numofStudent = Integer.parseInt(Input[1]);
        int markList[][] = new int[numofStudent][numofTeachers];
        int StudentPoint[] = new int[numofStudent];
        for (int i = 0; i < StudentPoint.length; i++) {
            StudentPoint[i] = 0;
        }
        int count = 2;
        for (int i = 0; i < numofStudent; i++) {
            for (int j = 0; j < numofTeachers; j++) {
                markList[i][j] = Integer.parseInt(Input[count]);
                count++;
            }
        }

        for (int i = 0; i < numofTeachers; i++) {
            int column[] = new int[numofStudent];
            for (int k = 0; k < column.length; k++) {
                column[k] = markList[k][i];
            }
            int max = findMax(column);
            for (int j = 0; j < numofStudent; j++) {
                if (markList[j][i] == max) {
                    StudentPoint[j] = StudentPoint[j] + 1;
                }
            }
        }

        if (isSame(StudentPoint)) {
            System.out.println("0");
        } else {
            System.out.println(findindex(StudentPoint, findMax(StudentPoint)) + 1);

        }

        bufferedReader.close();
    }

    static int findMax(int arr[]) {
        int max = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= max) {
                max = arr[i];
            }
        }
        return max;
    }

    static int findindex(int arr[], int num) {
        int index = 0;
        for (int i = 0; i < arr.length; i++) {
            if (num == arr[i]) {
                index = i;
            }
        }
        return index;
    }

    static boolean isSame(int arr[]) {
        boolean duplicates = false;
        for (int j = 0; j < arr.length; j++) {
            for (int k = j + 1; k < arr.length; k++) {
                if (k != j && arr[k] == arr[j] && arr[k] == findMax(arr)) {
                    duplicates = true;
                }
            }
        }
        return duplicates;
    }
}