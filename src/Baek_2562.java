/*
2023-09-20
백준 2562 최댓값
9개의 서로 다른 자연수 중 최댓값을 찾고 최댓값이 몇번째 수인지 구하라
*/

import java.util.*;

public class Baek_2562 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int [] arr = new int[9];
        int max = Integer.MIN_VALUE;
        int num=0;

        System.out.print("100이하의 9개의 정수를 입력하세요");
        for(int i=0 ; i<9 ; i++){
            arr[i] = sc.nextInt();
        }

        for(int i=0 ; i<9 ; i++){
            if(arr[i]>max){
                max = arr[i];
                num = i;
            }
        }
        System.out.println(max + "\n" + (num+1));
    }
}
