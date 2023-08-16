/*
2023-08-16
Day4-1
 */
public class DoubleNum {
    public static int solution(int number, int n, int m) {
        return number % n == 0 && number % m == 0 ? 1 : 0;

        // int answer = num % n == 0 ? 1 : 0;
        // return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(60,2,3));
    }
}
