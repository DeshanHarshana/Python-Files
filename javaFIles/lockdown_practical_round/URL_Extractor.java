import java.util.*;


class URL_Extractor {
    public static void main(final String[] args) {
        Scanner scanner=new Scanner(System.in);
        String path=scanner.nextLine();
        // Split path into segments
        String segments[] = path.split("\\?");
        String otherpart = segments[1];
        Map<String, String> map = new LinkedHashMap<String, String>();
        String subsegment[] = otherpart.split("&");
        
        for (int i = 0; i < subsegment.length; i++) {
            String subsubsegment[] = subsegment[i].split("=");
            map.put(subsubsegment[0], subsubsegment[1]);
        }
        
        for (String key : map.keySet()) {
            String value = map.get(key);
            System.out.println(key + " " + value);
        }
    }
}