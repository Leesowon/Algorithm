/*
2023-09-12
백준 2439 : 별찍기-2
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
예제)
    *
   **
  ***
 ****
*****
*/
import java.util.*;
public class Baek_2439 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for(int i=1 ; i<=N ; i++){
            for(int j=N-i ; j>=0 ; j--){
                System.out.println(" ");
            }
            for(int k=0 ; k<i ; k++){
                System.out.println("*");
            }
            System.out.println();
        }
    }
}
