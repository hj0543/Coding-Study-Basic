package cond;

public class If2
{
    static void main(String[] args)
    {
        int age = 17;

        if (age >= 18)
        {
            System.out.println("성인입니다"); //참일 때 실행
        } else {
            System.out.println("미성년자입니다"); //만족하는 조건이 없을 때 실행
        }
    }
}
