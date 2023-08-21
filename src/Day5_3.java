/*
2023-08-20
Day 5-3
https://school.programmers.co.kr/learn/courses/30/lessons/181930
pow 클래스 오버로딩
 */
public class Day5_3 {
    public static int solution(int a, int b, int c) {
        if(a != b && b != c && c != a){
            return a+b+c;
        } else if((a==b&&b!=c)||(b==c&&a!=b)||(a==c&&b!=a)){
            return (a+b+c)*(a*a+b*b+c*c);
        } else { // a==b && b==c
            return (a+b+c)*(a*a+b*b+c*c)*(a*a*a+b*b*b+c*c*c);
        }
    }

    public static void main(String[] args) {
        System.out.println(solution(2,6,1));
        System.out.println(solution(5,3,3));
        System.out.println(solution(4,4,4));
    }
}

/*
class Solution {
    public int solution(int a, int b, int c) {
        int answer = 1;

        int count = 1;
        if(a == b || a == c || b == c) {
            count++;
        }

        if(a == b && b == c) {
            count++;
        }

        for(int i = 1; i <= count; i++) {
            answer *= (pow(a,i)+pow(b,i)+pow(c,i));
        }

        return answer;
    }

    private int pow(int a, int b) {
        if(b == 0) return 1;
        return a * pow(a, b-1);
    }
}

 */
