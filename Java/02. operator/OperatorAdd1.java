package operator;

public class OperatorAdd1 {
    static void main() {
        int a = 0;

        a = a + 1;
        System.out.println("a = " + a); //1

        a = a + 1;
        System.out.println("a = " + a); //2

        //증감 연산자
        ++a; //a = a +1
        System.out.println("a = " + a); //3
        ++a; //a = a +1
        System.out.println("a = " + a); //4
    }
}
