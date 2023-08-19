/*
2023-08-19
Day 5-1
문자열 -> 배열
 */

public class StringCode {
    public static String solution(String code) {
        short mode = 0;
        String ret = "";

        char [] codeArr =  code.toCharArray();

        for(int idx=0 ; idx<code.length() ; idx++){
            switch (mode){
                case 0:
                    if(codeArr[idx] != '1'){
                        if(idx%2 == 0){ // 짝수일 때
                            ret += codeArr[idx];
                        }
                    } else{ // codeArr[idx]==1이면
                       mode = 1;
                    }
                    break;
                case 1:
                    if(codeArr[idx] != '1'){
                        if(idx%2 != 0){ // 홀수일 때
                            ret += codeArr[idx];
                        }
                    } else{ // codeArr[idx]==1이면
                        mode = 0;
                    }
                    break;
                default:
                    ret = "EMPTY";
                    break;
            }
        }

        return ret;
    }

    public static void main(String[] args) {
        System.out.println(solution("abc1abc1abc"));
    }
}
