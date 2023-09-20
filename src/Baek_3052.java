/*
2023-09-20
백준 3052 : 나머지
자연수 10개를 입력받고, 42로 나누어 나머지들을 구했을 때
서로 다른 나머지의 개수 출력
*/

import java.util.*;

public class Baek_3052 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n=10;
        int [] arr = new int[n];
        boolean bl = true;
        int cnt=0;

        System.out.println("정수 10개를 입력하세요");
        for(int i=0 ; i<arr.length ; i++){
            arr[i] = sc.nextInt();
        }

        for(int i=0 ; i<arr.length ; i++){
            for(int j=i+1 ; j<arr.length ; j++){

            }
        }
        System.out.print(cnt);
    }
}
