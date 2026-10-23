import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ConexoesEComandosExample {
    public static void main(String[] args) throws SQLException {
        System.out.println("=== JDBC: Connection, PreparedStatement e ResultSet ===");
        if (args.length == 0) {
            System.out.println("Uso: java ConexoesEComandosExample <jdbc-url>");
            System.out.println("A URL e o driver dependem do banco utilizado.");
            return;
        }

        String sql = "SELECT ?";
        try (Connection conexao = DriverManager.getConnection(args[0]);
             PreparedStatement comando = conexao.prepareStatement(sql)) {
            comando.setInt(1, 42);
            System.out.println("Conexao aberta; parametro JDBC ? preenchido com 42.");
            try (ResultSet resultados = comando.executeQuery()) {
                if (resultados.next()) {
                    System.out.println("next() posicionou o cursor; coluna 1: "
                            + resultados.getInt(1));
                }
            }
        }
    }
}
