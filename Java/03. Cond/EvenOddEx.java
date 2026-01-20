package cond.ex;

public class EvenOddEx
{
    static void main(String[] args)
    {
        int x = 161;
        String result = (x % 2 ==0) ? "짝수" : "홀수";
        System.out.println("x=" + x + ", " + result);
    }
}
