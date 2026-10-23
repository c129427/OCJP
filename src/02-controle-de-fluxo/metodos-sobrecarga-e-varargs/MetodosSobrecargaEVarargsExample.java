public class MetodosSobrecargaEVarargsExample {
    private static String descrever(int valor) {
        return "inteiro " + valor;
    }

    private static String descrever(String valor) {
        return "texto " + valor;
    }

    private static int somar(int... valores) {
        int soma = 0;
        for (int valor : valores) {
            soma += valor;
        }
        return soma;
    }

    public static void main(String[] args) {
        System.out.println("=== Sobrecarga de metodos e varargs ===");
        System.out.println("O compilador escolhe a sobrecarga pelo tipo do argumento:");
        System.out.println("descrever(17) -> " + descrever(17));
        System.out.println("descrever(\"Java\") -> " + descrever("Java"));
        System.out.println("Resultado de somar(1, 2, 3, 4): " + somar(1, 2, 3, 4));
        System.out.println("Varargs tambem aceita zero argumentos: somar() -> " + somar());
        System.out.println("Um array pode ser passado ao parametro varargs: "
                + somar(new int[] {5, 6}));
    }
}
