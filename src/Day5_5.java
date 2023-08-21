/*
2023-08-22
Day 5-5
정수가 담긴 리스트 num_list가 주어집니다.
num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return
 */
public class Day5_5 {
    public static int solution(int[] num_list) {
        String even = "";
        String odd = "";

        for(int i=0 ; i<num_list.length ; i++){
            if(num_list[i]%2 == 0){
                even += String.valueOf(num_list[i]);
                System.out.println(even);
            } else{
                odd += String.valueOf(num_list[i]);
                System.out.println(odd);
            }
        }
        return Integer.valueOf(even)+Integer.valueOf(odd);
    }

    public static void main(String[] args) {
        int [] arr = {5,7,8,3};
        System.out.println(solution(arr)); // 581
    }
}
