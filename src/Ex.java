import java.util.Scanner;

public class Ex {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("이름 : ");
        String username = sc.nextLine();

        System.out.print("생일 : ");
        int birthday = sc.nextInt();

        System.out.printf("%s\t%d", username, birthday);
    }
}
