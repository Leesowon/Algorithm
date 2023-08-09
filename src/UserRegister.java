import java.util.Scanner;

public class UserRegister {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("======================");
        System.out.println("회원 등록");
        System.out.println("======================");

        boolean register = false;

        while(!register){
            System.out.println("회원 가입을 진행하시겠습니까? \ny : 진행    n : 종료");
            System.out.print(">>");
            String register_input = sc.nextLine();

            if(register_input.equalsIgnoreCase("y")){
                register = true;
                System.out.println("======================");
                System.out.println("회원 가입이 진행됩니다.");
                System.out.println("======================");
            }
            else if(register_input.equalsIgnoreCase("n")){
                System.out.println("======================");
                System.out.println("회원 가입을 종료합니다.");
                System.out.println("======================");
                System.exit(0);
            }
            else{
                System.out.println("<<올바른 값을 입력해주세요>>");
            }
        }
    }
}
