import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ResultSetRecursosETransacoesExample {
    public static void main(String[] args) throws SQLException {
        System.out.println("=== JDBC: ResultSet e transacoes ===");
        if (args.length == 0) {
            System.out.println("Uso: java ResultSetRecursosETransacoesExample <jdbc-url>");
            System.out.println("O exemplo usa SELECT 1; informe uma URL JDBC e inclua o driver do banco.");
            return;
        }

        try (Connection conexao = DriverManager.getConnection(args[0])) {
            conexao.setAutoCommit(false);
            System.out.println("autoCommit desativado: a aplicacao controla a transacao.");
            try (PreparedStatement comando = conexao.prepareStatement("SELECT 1");
                 ResultSet resultados = comando.executeQuery()) {
                if (resultados.next()) {
                    System.out.println("next() avanca o cursor; valor da coluna 1: "
                            + resultados.getInt(1));
                }
                conexao.commit();
                System.out.println("commit() confirma a transacao.");
            } catch (SQLException excecao) {
                try {
                    conexao.rollback();
                } catch (SQLException falhaNoRollback) {
                    excecao.addSuppressed(falhaNoRollback);
                }
                System.out.println("rollback() tentou reverter a transacao.");
                throw excecao;
            }
        }
    }
}
