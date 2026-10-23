import java.io.IOException;

public class HierarquiaETiposDeExcecaoExample {
    private static int converter(String texto) throws IOException {
        try {
            return Integer.parseInt(texto);
        } catch (NumberFormatException excecao) {
            throw new IOException("O texto nao contem um inteiro valido.", excecao);
        }
    }

    public static void main(String[] args) {
        System.out.println("=== Excecoes verificadas e nao verificadas ===");
        System.out.println("NumberFormatException e unchecked; IOException e checked.");
        try {
            System.out.println("Texto convertido: " + converter("Java"));
        } catch (IOException excecao) {
            System.out.println("Excecao checked capturada: " + excecao.getClass().getSimpleName());
            System.out.println("Causa original preservada: "
                    + excecao.getCause().getClass().getSimpleName());
        }
    }
}
