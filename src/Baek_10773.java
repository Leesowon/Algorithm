/*
2023-10-06
백준 10773 : 제로
스택 응용
*/

import java.util.Stack;
import java.util.Scanner;

public class Baek_10773 {
    public static void main(String[] args) {
        Stack<Integer> money = new Stack<>(); // int
        Scanner sc = new Scanner(System.in);

        int k = sc.nextInt();

        for(int i=0 ; i<k ; i++){
            int value = sc.nextInt();
            if(value == 0){
                money.pop();
            } else{
                money.push(value);
            }
        }

        int sum=0;

        while(!money.empty()){ // 데이터가 남아있으면 반복
            sum += money.pop();
        }

        System.out.println(sum);
        sc.close();
    }
}
