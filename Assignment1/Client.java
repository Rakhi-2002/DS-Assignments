// ArithmeticClient.java
import java.rmi.Naming;

public class Client {
    public static void main(String[] args) {
        try {
            String url = "//localhost:1098/ArithmeticService"; // Use the same port as specified in the server
            Intf arithmeticService = (Intf) Naming.lookup(url);

            int a = 10;
            int b = 5;

            System.out.println("Adding: " + a + " + " + b + " = " + arithmeticService.add(a, b));
            System.out.println("Subtracting: " + a + " - " + b + " = " + arithmeticService.subtract(a, b));
            System.out.println("Multiplying: " + a + " * " + b + " = " + arithmeticService.multiply(a, b));
            System.out.println("Dividing: " + a + " / " + b + " = " + arithmeticService.divide(a, b));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
