/*
2023-09-12
백준 10952 : A+B - 5
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
*/

import java.util.*;
public class Beak_10952 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A,B; // 변수 선언

        while(true){
            A = sc.nextInt();
            B = sc.nextInt();
            if((A==0)&&(B==0)){
                break;
            }else{
                System.out.println(A+B);
            }
        }
    }
}