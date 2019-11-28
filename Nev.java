/**
 * How to compile: javac Nev.java
 * How to run: java Nev
 */
public class Nev{
    public static void main(String[] args) {
        var console = System.console();
        var out = console.writer();

        out.println("Hello world from Java!");
        
        out.print("Mi lenni tied név? ");
        out.flush();
        var nev = console.readLine();
        
        out.println("Hello, "+nev);
        
        out.println("vege");
    }
}