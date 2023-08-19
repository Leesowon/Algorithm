/*
2023-08-19
Day 4-5
두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수
 */

public class Flag {
    public static int solution(int a, int b, boolean flag) {
        int answer = 0;
        if(flag){
            return a+b;
        } else{
            return a-b;
        }

        // return flag ? a + b : a - b;
    }

    public static void main(String[] args) {
        System.out.println(solution(20,5,false));
    }
}
