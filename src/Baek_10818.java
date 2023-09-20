/*
2023-09-20
백준 10818 : 최대, 최소
N개의 정수가 주어졌을 때 최댓값과 최솟값을 구하라
*/

import java.util.*;

public class Baek_10818 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [] arr = new int[n];
//        int max = Integer.MIN_VALUE;
//        int min = Integer.MAX_VALUE;
        int max = -1000000;
        int min = 1000000;
        for(int i=0 ; i<n ; i++){
            arr[i] = sc.nextInt();
        }

        for(int i=0 ; i<n ; i++){
            if(max<arr[i]){
                max = arr[i];
            } else if (min>arr[i]) {
                min = arr[i];
            } else{
                continue;
            }
        }
        System.out.print(min + " " + max);
    }
}
