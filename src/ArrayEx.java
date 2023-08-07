import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;

public class ArrayEx {
    public static void main(String[] args) {
//        ArrayList list_1 = new ArrayList();
//        list_1.add(100);
//        list_1.add("sowon");
//        list_1.add('s');
//
//        for(int i=0 ; i<list_1.size() ; i++){
//            System.out.println(list_1.get(i));
//        }
//
//        ArrayList<Integer> list_2 = new ArrayList<Integer>(3);

//        HashMap map = new HashMap();
//
//        map.put("name", "sowon");
//        map.put("age", 24);
//
//        System.out.println(map.get("name"));

        HashMap<String, Integer> ages = new HashMap<>();

        ages.put("a", 10);
        ages.put("b", 20);
        ages.put("c", 30);
        System.out.println(ages.get("b"));
    }
}
