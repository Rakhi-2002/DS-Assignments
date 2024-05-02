package Assignment6;
import java.util.*;

public class Bully{
    int processes;
    boolean pstatus[];
    int coord;

    public Bully(int maxpro){
        processes = maxpro;
        pstatus = new boolean[maxpro];
        coord = maxpro;

        System.out.println("Creating processes");
        for(int i=0; i<processes; i++){
            pstatus[i] = true;

            System.out.println("P" + (i+1) + " is created");
        }
        System.out.println("Coordinator is P" + coord);
    }

    public void display(){
        for(int i=0; i<processes; i++){
            if(pstatus[i]){
                System.out.println("P" + (i+1) + " is up");
            }
            else{
                System.out.println("P" + (i+1) + " is down");
            }
        }
        System.out.println("Coordinator is P" + coord);
    }

    public void upprocess(int pid){
            if(pstatus[pid - 1]){
                System.out.println("P" + pid + " is up");
            }
            else{
                pstatus[pid - 1] = true;
                System.out.println("P" + pid + " is made up");
            }
    }

    public void downprocess(int pid){
            if(pstatus[pid - 1]){
                pstatus[pid - 1] = false;
                System.out.println("P" + pid + " is made down");
            }
            else{
                System.out.println("P" + pid + " is already down");
            }
    }

    public void runelection(int pid){
        coord = pid;
        boolean keepgoing = true;

        for(int i=pid; i<processes && keepgoing; i++){
            System.out.println("Election msg from " + pid + " process " + (i+1));

            if(pstatus[i]){
                keepgoing = false;
                runelection(i+1);
            }
        }
    }

    public static void main(String[] args) {
        int maxprocess = 0;
        int proid = 0;
        int choice = 0;
        Bully bul = null;

        Scanner sc = new Scanner(System.in);
        while(true){
            System.out.println("1. Create Process");
            System.out.println("2. Display P");
            System.out.println("3. Up process");
            System.out.println("4. Down Process");
            System.out.println("5. Run Election");
            System.out.println("6. Exit");

            System.out.println("Enter your choice: ");
            choice = sc.nextInt();

            switch(choice){
                case 1: 
                    System.out.println("Enter no. of processes ");
                    maxprocess = sc.nextInt();
                    bul = new Bully(maxprocess);
                    break;
                
                case 2:
                    bul.display();
                    break;
                
                case 3:
                    System.out.println("Enter the process id to be up ");
                    proid = sc.nextInt();
                    bul.upprocess(proid);
                    break;
                
                case 4:
                    System.out.println("Enter thee process id to be down ");
                    proid = sc.nextInt();
                    bul.downprocess(proid);
                    break;

                case 5:
                    System.out.println("Enter the prcoess to run the election ");
                    proid = sc.nextInt();
                    bul.runelection(proid);
                    bul.display();
                    break;

                case 6:
                    System.exit(0);
                    break;
            }
        }
    }
}