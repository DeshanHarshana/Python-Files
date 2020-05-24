
public class ID {
    String id;
    int month[] = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };//we conside feb as 29
    boolean isNewFormat = false;
    String sex = "";

    public ID() {
        this.id = "972890480v";
        if (this.id.length() == 12) {
            isNewFormat = true;
        }
    }

    public String getYear() {
        if (isNewFormat) {
            return this.id.substring(0, 4);
        } else {
            return "19" + this.id.substring(0, 2);
        }
    }

    public int getDays() {
        int days;
        if (isNewFormat) {
            days = Integer.parseInt(this.id.substring(4, 7));
        } else {
            days = Integer.parseInt(this.id.substring(2, 5));
        }
        if (days > 500) {
            sex = "Female";
            return (days - 500);

        } else {
            sex = "Male";
            return (days);
        }
    }

    public void getMonth() {
        int m = 0;
        int d = 0;
        int days = getDays();

        for (int i = 0; i < month.length; i++) {
            if (days < month[i]) {
                m = i+1;
                d = days;
                break;
            } else {
                days = days - month[i];
            }
        }
        System.out.println("/" + m + "/" + d);
    }

    public static void main(String[] args) {
        ID id = new ID();
        System.out.print(id.getYear());
        id.getMonth();
        System.out.println(id.sex);
    }
}