/*
2023-08-19
Day 5-1
문자열 -> 배열
break vs continue
null vs 빈값
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
                    continue;
                case 1:
                    if(codeArr[idx] != '1'){
                        if(idx%2 != 0){ // 홀수일 때
                            ret += codeArr[idx];
                        }
                    } else{ // codeArr[idx]==1이면
                        mode = 0;
                    }
                    continue;
                }
        }
        if(ret.length()==0){
            return ret = "EMPTY";
        }
        return ret;
    }

    public static void main(String[] args) {
        System.out.println(solution("111"));
    }
}

/*
class Solution {
    public String solution(String code) {
        StringBuilder answer = new StringBuilder();
        int mode = 0;
        for (int i = 0; i < code.length(); i++) {
            char current = code.charAt(i);
            if (current == '1') {
                mode = mode == 0 ? 1 : 0;
                continue;
            }

            if (i % 2 == mode) {
                answer.append(current);
            }
        }
        return answer.length() == 0 ? "EMPTY" : answer.toString();
    }
}
 */
