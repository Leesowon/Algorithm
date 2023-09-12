/*
https://wikidocs.net/229
 */
public class Exception {

    public static void main(String[] args) {
        int a = 0;
        int b = 10;
        int c;
        int d = 30;

        try{ // try 문장을 실행하는 도중 예외가 발생한다면
            c = d/b;
        } catch (java.lang.Exception e){ // 예외에 해당되는 catch문 실행
//            예외가 발생한다면 해당 문장 실행
            c = -1;
            System.out.println(c);
        } finally {
            // 예외가 발생하더라도 반드시 실행되어야 하는 부분
            System.out.println("finish");
        }
    }
}
