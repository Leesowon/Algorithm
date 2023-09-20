/*
2023-09-19
백준 10807 : 개수 세기
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램 작성
*/

import java.util.*;

public class Baek_10807 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("정수 입력(1 <= N <= 100) : ");
        int N = sc.nextInt();
        int [] n = new int[N]; // N 크기만큼의 배열 생성
        
        // 정수 n만큼 반복하면서 입력받기
        for(int i=0 ; i<N ; i++){
            n[i] = sc.nextInt();
        }

        int v;
        int cnt=0;
        System.out.print("찾으려는 정수는? : ");
        v = sc.nextInt();

        for(int i=0 ; i<N ; i++){
            if(n[i]==v){
                cnt++;
            } else{
                continue;
            }
        }
        System.out.println(cnt);
    }
}
