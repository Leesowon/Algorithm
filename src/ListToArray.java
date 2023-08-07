import java.util.Arrays;

public class ListToArray {
    public static String solution(String[] arr) {
        String answer = String.join("",arr);
        return answer;

        // return String.join("", arr);
    }

    public static void main(String[] args) {
        String [] arr = {"a", "b", "c"};
        String answer = solution(arr);
        System.out.println(answer);
    }
}
