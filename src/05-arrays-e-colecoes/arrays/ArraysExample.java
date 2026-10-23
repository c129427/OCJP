import java.util.Arrays;

public class ArraysExample {
    public static void main(String[] args) {
        System.out.println("=== Arrays ===");
        System.out.println("Um array tem tamanho fixo e recebe valores padrao ao ser criado.");
        int[] notas = {8, 10, 7};
        int[] valoresPadrao = new int[3];
        int[][] matrizIrregular = {{1, 2}, {3}};
        Arrays.sort(notas);

        System.out.println("Tamanho do array (propriedade length): " + notas.length);
        System.out.println("Elementos apos a ordenacao: " + Arrays.toString(notas));
        System.out.println("Novo int[] inicia com zeros: " + Arrays.toString(valoresPadrao));
        System.out.println("Matriz e array de arrays; segunda linha tem tamanho "
                + matrizIrregular[1].length + ".");
        System.out.println("Busca binaria da nota 8 (array ordenado): "
                + Arrays.binarySearch(notas, 8));
    }
}
