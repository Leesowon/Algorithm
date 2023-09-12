/*
2023-08-20
Day5-1
a,d -> 첫 항이 a이고 등차가 d인 등차수열의 배열 생성
이때 길이는 boolean 배열 include의 길이
arithmetic series
1) boolean 배열의 길이 확인
2) 배열 생성
3) boolean 배열 속 true인 index 찾기
4) 해당 index의 등차 배열의 값들 더하기

배열을 따로 만들어줄 필요없이 included 배열을 돌면서 true이면 answer에 해당하는 값 더해가면o

stream으로 한줄 코딩도 가능
 */

public class Day5_2 {
    public static int solution(int a, int d, boolean[] included) {
        int [] arit = new int[included.length];
        int sum = 0;

        for(int i=0 ; i<included.length ; i++){
            arit[i] = a + d*i;
        }

        for(int i=0 ; i<included.length ; i++){
            if(included[i] == true){ // 어차피 안에 들어있는 값이 t/f니까 == true를 쓸 필요xxx
                sum += arit[i];
            }
        }
        return sum;
    }

    /*
    int answer = 0;

        for(int i = 0; i < included.length; i++){
            if(included[i]){
                answer +=  a + (d*i);
            }
        }

        return answer;
     */

    public static void main(String[] args) {
//        boolean [] arr = {true,false,false,true,true};
        boolean [] arr = {false,false,false,true,false,false,false};

//        solution(3,4,arr);
        System.out.println(solution(7,1,arr));
    }
}
