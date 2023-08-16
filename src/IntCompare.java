/*
정수를 문자열로 바꿔서 더한뒤 비교
 */
public class IntCompare {
    public static int solution(int a, int b) {

        // return Math.max(Integer.parseInt(String.valueOf(a)+String.valueOf(b)),2*a*b);

        int answer = 0;

        String first = String.valueOf(a);
        String second = String.valueOf(b);

        String result = "";
        if(Integer.parseInt(first + second) > 2 * a * b){
            answer = Integer.parseInt(first + second);
        } else if (Integer.parseInt(first + second) < 2 * a * b){
            answer = 2 * a * b;
        } else {
            answer = Integer.parseInt(first + second);
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(91,2));
    }
}
