/*
2023-09-20
백준 1475 : 방번호
방 번호에 필요한 플라스틱 세트 최소 개수 구하기
6/9 호환 가능
*/

import java.util.*;

public class Baek_1475 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int room;
        int cnt=0; // 필요한 플라스틱 수
        int cnt_69=0;

        // 1. 방번호 입력
        System.out.print("방번호를 입력하세요 : ");
        room = sc.nextInt();
        
        // 2. 방번호 자릿수 확인 : num
        int num = (int)(Math.log10(room)+1);

        // 3. 자리수만큼 배열 생성 >> 배열에 넣기
        int [] arr = new int[num];
        // int를 문자열로 변환
        String room_String = Integer.toString(room);

        // 숫자별 배열 생성
        for(int i=0 ; i<arr.length ; i++){
            arr[i] = room_String.charAt(i)-'0';
        }

        // 4. 자리수마다 비교하여 필요한 플라스틱 수 구하기
        boolean bl = false;
        for(int i=0 ; i<arr.length ; i++){
            for(int j=i+1 ; j<arr.length ; j++){
                if(arr[i] == arr[j]){
                    cnt_69=1;
                    if(arr[i]==6 || arr[i]==9){
                        cnt_69++;
                        System.out.println("cnt_69 : " + cnt_69);
                    } else{
                        cnt++;
                        System.out.println("cnt : " + cnt);
                    }
                    break;
                }
            }
        }
    }
}
