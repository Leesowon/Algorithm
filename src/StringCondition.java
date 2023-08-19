/*
2023-08-19
Day 4-4
문자열 비교
==와 equals의 차이

"==" 비교 연산자는 주소값을 비교하고
equlas() 메서드는 내용 자체를 비교 즉, 데이터 값을 비교
 */

public class StringCondition {
    public static int solution(String ineq, String eq, int n, int m) {
        int answer = 0;

        if(ineq.equals((">")) && eq.equals("=")){
            answer = n >= m ? 1 : 0;
        } else if (ineq.equals(("<")) && eq.equals("=")) {
            answer = n <= m ? 1 : 0;
        } else if (ineq.equals((">")) && eq.equals("!")) {
            answer = n > m ? 1 : 0;
        } else if(ineq.equals(("<")) && eq.equals("!")){
            answer = n < m ? 1 : 0;
        }
        return answer;
    }

    /*
    boolean answer = false;
        if (ineq.equals(">") && eq.equals("="))
            answer = n >= m;
        else if (ineq.equals("<") && eq.equals("="))
            answer = n <= m;
        else if (ineq.equals(">") && eq.equals("!"))
            answer = n > m;
        else
            answer = n < m;
        return answer ? 1 : 0;
     */

    public static void main(String[] args) {
        System.out.println(solution(">", "=", 50, 20));

    }

}
