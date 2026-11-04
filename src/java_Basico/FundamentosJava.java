import java.util.Scanner;

public class FundamentosJava {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Qual é seu nome?");
        String nome = scanner.nextLine();

        System.out.println("Qual é sua idade?");
        int idade = scanner.nextInt();

        int proximaIdade = idade + 1;
        System.out.println("Olá, " + nome + "! No próximo ano você terá " + proximaIdade + ".");
    }
}
