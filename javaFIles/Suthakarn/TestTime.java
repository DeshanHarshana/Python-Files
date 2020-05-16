
public class TestTime {
    public static void main(String[] args) {
        Time time = new Time(6, 20, 50);
       
        // time.setHour(0);
        // time.setMinute(40);
        // time.setSecond(54);
        // System.out.println("hour = " + time.getHour() + " = " + " minute : " + time.getMinute() + " = " + " second : "
        //         + time.getSecond());
        
        time.setTime(1, 0, 59);
        time.nextSecond();
        System.out.println(time.toString());

        time.setTime(1, 0, 0);
        time.previousSecond();
        System.out.println(time.toString());
    }
}
class Time {
    private int hour = 0;
    private int minute = 0;
    private int second = 0;
    public Time(int hour, int minute, int second) {
        
            this.hour = hour;
            this.minute = minute;
            this.second = second;
        
    }
    public int getHour() {
        return hour;
    }
    public void setHour(int hour) {
        if (hour >= 24) {
            System.out.println("time error");
        } else {
            this.hour = hour;
        }
    }
    public int getMinute() {
        return minute;
    }
    public void setMinute(int minute) {
        if (hour >= 60) {
            System.out.println("time error");
        } else {
            this.minute = minute;
        }
    }
    public int getSecond() {
        return second;
    }
    public void setSecond(int second) {
        if (hour >= 60) {
            System.out.println("time error");
        } else {
            this.second = second;
        }
    }
    public void setTime(int hour, int minute, int second) {
        
            this.hour = hour;
            this.minute = minute;
            this.second = second;
        
    }
    public Time nextSecond() {
        second++;
        if (second == 60) {
            second = 0;
            minute++;
            if (minute == 60) {
                minute = 0;
                hour++;
                if (hour == 24) {
                    hour = 0;
                    minute = 0;
                    second = 0;
                    
                }
            }
        }
        return this;
    }
    public Time previousSecond() {
        second--;
        if (second < 0) {
            second = 59;
            minute--;
            if (minute < 0) {
                minute = 59;
                hour--;
                if (hour < 0) {
                    hour = 0;
                    minute = 0;
                    second = 0;
                   
                }
            }
        }
        return this;
    }
    public String reMake(int i){
        String newNum="";
        if(i>9){
            newNum=String.valueOf(i);
        }
        else{
            String x=String.valueOf(i);
            newNum="0"+x;
        }
        return newNum;
    }
    public String toString() {
        return "Time [hour=" + reMake(hour) + ", minute="
                + reMake(minute) + ", second=" + reMake(second) + "]";
    }

}