import java.util.Scanner;

public class ListaTarefas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite uma tarefa:");
        String descricao = scanner.nextLine();

        System.out.println("Tarefa adicionada: " + descricao);
    }
}
