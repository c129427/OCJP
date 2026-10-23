import java.sql.Connection;

public class SistemaDeModulosJpmsExample {
    public static void main(String[] args) {
        System.out.println("=== Java Platform Module System (JPMS) ===");
        Module moduloBase = String.class.getModule();
        Module moduloSql = Connection.class.getModule();
        System.out.println("Modulo da classe String: " + moduloBase.getName());
        System.out.println("Modulo da interface java.sql.Connection: " + moduloSql.getName());

        String descritor = """
                module estudos.ocjp {
                    requires java.sql;
                    exports estudos.ocjp.api;
                    opens estudos.ocjp.modelo to framework.reflexivo;
                    uses estudos.ocjp.spi.ProvedorRelatorio;
                    provides estudos.ocjp.spi.ProvedorRelatorio
                        with estudos.ocjp.impl.ProvedorCsv;
                }
                """;

        System.out.println("Descritor conceitual module-info.java:");
        System.out.println(descritor);
        System.out.println("requires declara dependencia; exports permite acesso normal a um pacote.");
        System.out.println("opens permite acesso reflexivo; uses/provides declaram uso e implementacao de servicos.");
        System.out.println("O texto ilustra diretivas: os nomes sao exemplos, nao um modulo pronto para compilar.");
    }
}
