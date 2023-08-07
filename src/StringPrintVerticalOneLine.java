import java.util.Scanner;

public class StringPrintVerticalOneLine {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();

        int length = a.length();

        for(int i=0 ; i<length ; i++){
            System.out.println(a.charAt(i));
        }
        // charAt() : String으로 저장된 문자열 중에서 한 글자만 선택해서 char타입으로 변환해주는 함수


        /*
        char [] c;
        c = a.toCharArray();

        for(int i=0 ; i<a.length() ; i++){
            System.out.println(c[i]);
        }
         */

        /*
        for (char ch : a.toCharArray())
            System.out.println(ch);
         */
    }
}