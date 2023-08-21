/*
2023-08-22
Day 5-4
정수가 담긴 리스트 num_list가 주어질 때,
모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수
 */
public class Day5_4 {
    public static int solution(int[] num_list) {
        int sum = 0;
        int mul = 1;

        for(int i=0 ; i<num_list.length ; i++){
            sum += num_list[i];
            mul = mul*num_list[i];
        }
        return mul<sum*sum ? 1 : 0;
    }

    public static void main(String[] args) {
        int [] arr = {7,5,8,3};
        System.out.println(solution(arr));
    }
}
