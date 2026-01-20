package cond.ex;

public class CondOpEx
{
    static void main(String[] args) {
        int a = 10;
        int b = 20;

        String status = (a > b) ? "a" : "b";
        System.out.println("더 큰 숫자는" + status + "입니다.");
        /*
        int max = (a > b) ? a : b;
        System.out.println("더 큰 숫자는" + status + "입니다.");
         */
    }
}
