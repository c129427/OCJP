import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class StreamsReadersEWritersExample {
    public static void main(String[] args) throws IOException {
        System.out.println("=== I/O: streams de bytes e de caracteres ===");
        String mensagem = "Java I/O: acao e informacao";
        byte[] dados = mensagem.getBytes(StandardCharsets.UTF_8);
        try (ByteArrayInputStream entrada = new ByteArrayInputStream(dados);
             ByteArrayOutputStream saida = new ByteArrayOutputStream()) {
            saida.write(entrada.readAllBytes());
            String texto = saida.toString(StandardCharsets.UTF_8);
            System.out.println("Streams de bytes copiam bytes; UTF-8 decodifica o texto: " + texto);
        }

        try (BufferedReader leitor = new BufferedReader(new InputStreamReader(
                new ByteArrayInputStream(dados), StandardCharsets.UTF_8))) {
            System.out.println("Reader le caracteres linha a linha: " + leitor.readLine());
        }
    }
}
