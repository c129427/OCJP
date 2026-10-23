import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class SerializacaoExample {
    private static class Estudante implements Serializable {
        private static final long serialVersionUID = 1L;

        private final String nome;
        private final int modulo;
        private transient String senhaTemporaria;

        Estudante(String nome, int modulo, String senhaTemporaria) {
            this.nome = nome;
            this.modulo = modulo;
            this.senhaTemporaria = senhaTemporaria;
        }

        @Override
        public String toString() {
            return "Estudante{nome='" + nome + "', modulo=" + modulo
                    + ", senhaTemporaria=" + senhaTemporaria + "}";
        }
    }

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        System.out.println("=== Serializacao de objetos ===");
        System.out.println("Somente objetos Serializable podem ser gravados; transient nao e persistido.");
        Estudante original = new Estudante("Alex", 3, "nao-serializar");
        byte[] bytes;
        try (ByteArrayOutputStream buffer = new ByteArrayOutputStream();
             ObjectOutputStream saida = new ObjectOutputStream(buffer)) {
            saida.writeObject(original);
            bytes = buffer.toByteArray();
        }

        try (ObjectInputStream entrada =
                     new ObjectInputStream(new ByteArrayInputStream(bytes))) {
            Estudante recuperado = (Estudante) entrada.readObject();
            System.out.println("Objeto original: " + original);
            System.out.println("Objeto recuperado: " + recuperado);
            System.out.println("A senha temporaria foi restaurada como null por ser transient.");
        }
    }
}
