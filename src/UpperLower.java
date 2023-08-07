/*
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
 */

import java.util.Scanner;

public class UpperLower {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();

        char [] exchange = a.toCharArray();
        char [] result = new char [a.length()];

        for(int i=0 ; i<a.length() ; i++){
            if(Character.isUpperCase(exchange[i])){
                result[i] = Character.toLowerCase(exchange[i]);
            }
            else{
                result[i] = Character.toUpperCase(exchange[i]);
            }
            System.out.print(result[i]);
        }
    }
}

/*

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String answer = "";

        //Stack <Character> stack = new Stack <> ();

        for(Character c : a.toCharArray()){
            if(Character.isUpperCase(c)){
                //stack.push(Character.toLowerCase(c));
                answer += Character.toLowerCase(c);
            }
            else if(Character.isLowerCase(c)){
                //stack.push(Character.toUpperCase(c));
                answer += Character.toUpperCase(c);
            }
        }
        System.out.println(answer);
    }
}

 */