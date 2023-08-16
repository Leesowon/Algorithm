/*
2023-08-16
Day4-1
 */
public class DoubleNum {
    public static int solution(int num, int n) {
        if(num%n == 0){
            return 1;
        } else{
            return 0;
        }

        // int answer = num % n == 0 ? 1 : 0;
        // return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(98,2));
    }
}
