public class MulString {
    public static String solution(String my_string, int k) {
        String answer = "";
//        for(int i=0 ; i<k ; i++){
//            answer += my_string;
//        }
        answer = my_string.repeat(3);
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution("Hello", 3));
    }
}
