import javax.crypto.spec.PSource;

public class StringAdd {
    public static int solution(int a, int b) {
        int answer = 0;
        String a2 = Integer.toString(a);
        String b2 = Integer.toString(b);

        if(Integer.parseInt(a2+b2) > Integer.parseInt((b2+a2))){
            answer = Integer.parseInt(a2+b2);
        }
        else{
            answer = Integer.parseInt((b2+a2));
        }
        return answer;
    }

    /*
    String strA = String.valueOf(a);
        String strB = String.valueOf(b);
        String strSum1 = strA + strB;
        String strSum2 = strB + strA;
        return Math.max(Integer.valueOf(strSum1), Integer.valueOf(strSum2));
     */

    public static void main(String[] args) {
        System.out.println(solution(89,9));
    }
}
