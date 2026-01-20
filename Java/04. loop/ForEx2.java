package loop;

public class ForEx2
{
    static void main(String[] args)
    {
        for (int num = 2, count = 1; count <= 10; num += 2, count++)
        {
            System.out.println(num);
        }
    }
    {
        /*
        int num =2;
        for (int count = 1; count <= 10; count++)
        {
            System.out.println(num);
            num += 2;
        }
        이게 더 깔끔하다..*/
    }
}
