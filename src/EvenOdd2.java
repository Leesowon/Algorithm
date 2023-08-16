import java.util.ArrayList;

/*
2023-08-16
Day4-3
 */
public class EvenOdd2 {
    public static int solution(int n) {
        int answer = 0;

        if(n%2==0){ // 짝수
            for(int i=n ; i>0 ; i--){
                if(i%2==0){
                    answer += i*i;
                }else{
                    continue;
                }
            }
        }else{ // 홀수
            for(int i=n ; i>0 ; i--){
                if(i%2!=0){
                    answer += i;
                }
            }
        }
        return answer;

        /*
        if (n % 2 == 1) {
            return (n + 1) * (n + 1) / 2 / 2;
        } else {
            return 4 * n/2 * (n/2 + 1) * (2 * n/2 + 1) / 6;
        }
         */
    }


    public static void main(String[] args) {
        System.out.println("7 : " + solution(7));
        System.out.println("10 : " + solution(10));
    }
}
