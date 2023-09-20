/*
2023-09-19
백준 10871 : X보다 작은 수
정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
이때, A에서 X보다 작은 수를 모두 출력하는 프로그램 작성

정수 N과 X를 받고, N개 만큼의 정수를 받는다.
N개의 정수 중 X보다 작은 정수들 출력
*/

import java.util.*;

public class Baek_10871 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList list_store = new ArrayList<Integer>();
        ArrayList list_answer = new ArrayList<Integer>();
        int n = sc.nextInt();
        int X = sc.nextInt();
        for(int i=0 ; i<n ; i++){
            list_store.add(sc.nextInt()); // 이렇게 값을 받아서 배열에 넣을 수 있나?
            if((int)list_store.get(i)<X){
                list_answer.add(list_store.get(i));
            } else {
                continue;
            }
        }
        for(int i=0 ; i< list_answer.size() ; i++){
            System.out.print(list_answer.get(i)+" ");
        }
    }
}
