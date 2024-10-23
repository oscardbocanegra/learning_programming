import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        byte age = 18;
        int bigNumber = 1000;
        System.out.println(age);
        System.out.println(bigNumber);
        System.out.println("Hello world!");

        // Arrays
        int[] numbers = {0, 1, 2, 3, 4};
        System.out.println("\n Arrays");
        System.out.println(Arrays.toString(numbers));

        // Operadores aritmeticos

        int a = 2 + 2;
        int b = 3 - 1;
        int c = 2 * 2;
        float d = 10f / 3f;
        int e = 4 % 3;
        System.out.println("\nOperators");
        System.out.println("This is the result of 2 + 2 = " + a);
        System.out.println("This is the result of 3 - 1 = " + b);
        System.out.println("This is the result of 2 * 2 = " + c);
        System.out.println("This is the result of 10 / 3 = " + d);
        System.out.println("This is the result of 4 % 3 = " + e);



    }
}