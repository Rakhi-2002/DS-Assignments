// ArithmeticServiceImpl.java
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

//making below class available for remote invocation with the help of UnicastRemoteObject
public class IntfImplement extends UnicastRemoteObject implements Intf {
    public IntfImplement() throws RemoteException {
        super();
    }

    @Override
    //to handle exceptions which can occur while calling methods remotely
    public int add(int a, int b) throws RemoteException {
        return a + b;
    }

    @Override
    public int subtract(int a, int b) throws RemoteException {
        return a - b;
    }

    @Override
    public int multiply(int a, int b) throws RemoteException {
        return a * b;
    }

    @Override
    public double divide(int a, int b) throws RemoteException {
        if (b == 0) {
            throw new RemoteException("Cannot divide by zero");
        }
        return (double) a / b;
    }

    public static void main(String[] args) {
        try {
            int registryPort = 1098; // Use a different port
            Intf arithmeticService = new IntfImplement();
            java.rmi.registry.LocateRegistry.createRegistry(registryPort);
            java.rmi.Naming.rebind("//localhost:" + registryPort + "/ArithmeticService", arithmeticService);
            System.out.println("ArithmeticService is ready on port " + registryPort + ".");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
