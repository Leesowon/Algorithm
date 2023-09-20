/*
2023-09-20
백준 : 1546
*/

import java.util.*;

public class Baek_1546 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num=0;
        double sum=0;
        double avg=0;
        double max = Double.MIN_VALUE;

        System.out.print("시험과목 수 : ");
        num = sc.nextInt();
        double [] arr = new double[num];
        for(int i=0 ; i<arr.length ; i++){
            arr[i] = sc.nextInt();
        }

        // 최고 점수 구하기
        for(int i=0; i<arr.length ; i++){
            if(max<arr[i]){
                max = arr[i];
            } else{
                continue;
            }
        }
        System.out.println("최고점수는 : " + max);

        // 다른 점수 바꾸기
        for(int i=0 ; i<arr.length ; i++){
            System.out.println("기존 arr[i]" + arr[i]);
            arr[i] = (arr[i]/max)*100;
            System.out.println("arr[i] : " + arr[i]);
            sum += arr[i];
        }
        System.out.print((double)sum/num);
    }
}
