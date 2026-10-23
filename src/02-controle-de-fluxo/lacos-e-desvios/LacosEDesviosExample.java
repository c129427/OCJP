public class LacosEDesviosExample {
    public static void main(String[] args) {
        System.out.println("=== Lacos, continue e break rotulado ===");
        int soma = 0;
        for (int numero = 1; numero <= 5; numero++) {
            if (numero == 3) {
                System.out.println("continue pula o numero " + numero + ".");
                continue;
            }
            soma += numero;
        }
        System.out.println("Soma dos valores processados (1 + 2 + 4 + 5): " + soma);

        int encontrados = 0;
        busca:
        for (int linha = 1; linha <= 3; linha++) {
            for (int coluna = 1; coluna <= 3; coluna++) {
                System.out.println("Verificando linha " + linha + ", coluna " + coluna);
                if (linha == 2 && coluna == 2) {
                    encontrados++;
                    break busca;
                }
            }
        }
        System.out.println("break busca encerrou os dois lacos; alvo encontrado: " + encontrados);
    }
}
