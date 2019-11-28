import java.util.Scanner;

public class Nev{
    public static void main(String[] args) {
        System.out.println("Hello world from Java!");
        System.out.print("Mi lenni tied név? ");
        var scanner = new Scanner(System.in);
        var nev = scanner.nextLine();
        System.out.println("Hello, "+nev);
        System.out.println("vege");
    }
}