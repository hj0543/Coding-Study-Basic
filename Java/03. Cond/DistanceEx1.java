package cond.ex;

public class DistanceEx
{
    static void main(String[] args)
    {
        int distance = 70;

        if (distance <= 1)
        {
            System.out.println("도보를 이용하세요.");
        }
        else if (distance <= 10)
        {
            System.out.println("자전거를 이용하세요.");
        }
        else if (distance <= 100)
        {
            System.out.println("자동차를 이용하세요.");
        }
        else
        {
            System.out.println("비행기를 이용하세요.");
        }
    }
}
