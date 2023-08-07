class AddString {
    public static String solution(String my_string, String overwrite_string, int s) {

            String answer = "";

            String str1 = my_string.substring(0,s);
            String str2 = my_string.substring(overwrite_string.length()+ str1.length(), my_string.length());

            answer = str1 + overwrite_string + str2;
            return answer;
    }

    public static void main(String[] args) {
        String result = solution("He11oWor1d", "lloWorl", 2);
        System.out.print(result);
    }
}