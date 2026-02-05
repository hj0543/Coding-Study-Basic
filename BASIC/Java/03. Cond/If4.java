package cond;

public class If4
{
    static void main(String[] args)
    {
        int age = 5;

        if (age <= 7) //~7: 미취학
        {
            System.out.println("미취학");
        }
        else if (age <= 13) //~13: 초등학생
        {
            System.out.println("초등학생");
        }
        else if (age <= 16) //~16: 중학생
        {
            System.out.println("중학생");
        }
        else if (age <= 19) //~19: 고등학생
        {
            System.out.println("고등학생");
        }
        else //19세 초과
        {
            System.out.println("성인");
        }
    }
}
