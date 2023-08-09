import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class UserRegister {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("======================");
        System.out.println("회원 등록을 시작합니다.");
        System.out.println("======================");

        boolean register = false;

        while(!register){
            System.out.println("회원 가입을 진행하시겠습니까? \ny : 진행    n : 종료");
            System.out.print(">> ");
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

        ArrayList users = new ArrayList<>(); // 가입된 회원 저장

        while (true){
            HashMap user = new HashMap(); // 한명의 유저에 대한 정보를 담는 hashmap

            // ID
            System.out.print("ID : ");
            String username = sc.nextLine();

            // pw
            String pw = "";
            while (true) {
                System.out.print("pw : ");
                pw = sc.nextLine();

                System.out.print("pw 확인 : ");
                String pw_confirm = sc.nextLine();

                if(pw.equals(pw_confirm)){
                    break;
                } else {
                    System.out.println("======================");
                    System.out.println("비밀번호가 일치하지 않습니다.");
                    System.out.println("비밀번호를 다시 입력해주세요");
                    System.out.println("======================");
                }
            }

            // 이름
            System.out.print("이름 : ");
            String name = sc.nextLine();

            // 생년월일(6자리)
            String birth = ""; // 바깥에서 참조해야 하기 때문에 외부에서 선언 후 while 실행
            while (true){
                System.out.print("생년월일(6자리) : ");
                birth = sc.nextLine();
                if(birth.length() == 6){
                    break;
                } else {
                    System.out.println("======================");
                    System.out.println("생년월일 자릿수가 올바르지 않습니다..");
                    System.out.println("생년월일을 다시 입력해주세요");
                    System.out.println("======================");
                }
            }

            // e-mail
            System.out.print("email : ");
            String email = sc.nextLine();

            user.put("name", name);
            user.put("username", username);
            user.put("pw", pw);
            user.put("birth", birth);
            user.put("email", email);

            users.add(user);

            System.out.println("======================");
            System.out.println(user.get("name")+" 님, 회원가입이 완료되었습니다.");
            System.out.println("ID는 " + user.get("username") + "입니다.");
            System.out.println("======================");

            System.out.println("회원가입을 추가로 진행하시겠습니까? \ny : 진행    n : 종료");
            System.out.print(">> ");
            String register_again = sc.nextLine();

            if(register_again.equalsIgnoreCase("y")){
            } else if (register_again.equalsIgnoreCase("n")){
                System.exit(0);
            }
        }
    }
}
