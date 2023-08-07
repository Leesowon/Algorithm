class AddString {
    public static String solution(String my_string, String overwrite_string, int s) {
        char[] origin = my_string.toCharArray();
        char[] over = overwrite_string.toCharArray();
//        char[] result = new char[my_string.length()];

        for (int i = s ; i < s + overwrite_string.length() ; i++) {
            for (int j = 0 ; j < overwrite_string.length() ; j++) {
                origin[i] = over[j];
            }
        }
            String answer = String.valueOf(origin);
            return answer;
    }

    public static void main(String[] args) {
        String result = solution("He11oWor1d", "lloWorl", 2);
        System.out.print(result);
    }
}