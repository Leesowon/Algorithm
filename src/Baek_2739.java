/*
2023-09-12
백준 2739 : 구구단
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램 작성
*/
import java.util.*;
public class Baek_2739 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for(int i=1; i<10 ; i++){
            System.out.println(N+" * "+i+" = "+(N*i));
        }
    }
}
