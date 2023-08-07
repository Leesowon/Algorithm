import java.util.Scanner;

class MixString {
    public static String solution(String str1, String str2) {
        String answer = "";
        for(int i=0 ; i<str1.length() ; i++){
            answer += str1.substring(i,i+1) + str2.substring(i,i+1);
        }
        return answer;
    }

    /*
    public String solution(String str1, String str2) {
        String answer = "";

        for(int i = 0; i < str1.length(); i++){
            answer+= str1.charAt(i);
            answer+= str2.charAt(i);
        }

        return answer;
    }
     */

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str1 = sc.nextLine();
        String str2 = sc.nextLine();

        String answer = solution(str1, str2);
        System.out.println(answer);
    }
}