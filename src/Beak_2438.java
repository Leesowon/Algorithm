/*
2023-09-12
백준 2438 : 별찍기-1
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
예제)
*
**
***
****
*****
*/
import java.util.*;
public class Beak_2438 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for(int i=1 ; i<=N ; i++){
            for(int j=0 ; j<i ; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
