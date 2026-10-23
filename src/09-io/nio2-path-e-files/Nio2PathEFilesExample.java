import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Nio2PathEFilesExample {
    public static void main(String[] args) throws IOException {
        System.out.println("=== NIO.2: Path e Files ===");
        Path arquivoTemporario = Files.createTempFile("estudo-ocjp-", ".txt");
        try {
            String mensagem = "Estudando NIO.2";
            Files.writeString(arquivoTemporario, mensagem);
            System.out.println("Conteudo recuperado do arquivo: " + Files.readString(arquivoTemporario));
            System.out.println("Path aponta para arquivo regular: " + Files.isRegularFile(arquivoTemporario));
            System.out.println("Tamanho em bytes: " + Files.size(arquivoTemporario));
            System.out.println("Caminho normalizado: " + arquivoTemporario.normalize());
        } finally {
            boolean removido = Files.deleteIfExists(arquivoTemporario);
            System.out.println("Arquivo temporario removido: " + removido);
        }
    }
}
