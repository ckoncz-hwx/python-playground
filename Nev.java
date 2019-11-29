/**
 * How to compile: javac Nev.java
 * How to run: java Nev
 */
public class Nev{
    public static void main(String[] args) {
        var name = System.console().readLine("What is your name? ");
        System.console().writer().println("Hello, "+name);
    }
}