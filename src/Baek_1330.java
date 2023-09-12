import java.util.Scanner;

/*
2023-09-12
백준 1330 두 수 비교하기
 */
public class Baek_1330 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();

        if(A>B){
            System.out.println(">");
        } else if (A<B) {
            System.out.println("<");
        } else{
            System.out.println("==");
        }
    }
}
