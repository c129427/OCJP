import java.util.ListResourceBundle;
import java.util.Locale;
import java.util.ResourceBundle;

public class LocaleEBundlesExample {
    public static void main(String[] args) {
        System.out.println("=== Locale e ResourceBundle ===");
        for (Locale locale : new Locale[] {
                Locale.forLanguageTag("pt-BR"),
                Locale.US
        }) {
            ResourceBundle mensagens =
                    ResourceBundle.getBundle("LocaleEBundlesExample$Mensagens", locale);
            System.out.println(locale.toLanguageTag() + " -> "
                    + mensagens.getString("saudacao"));
        }
        System.out.println("O bundle pt-BR sobrescreve a saudacao; outros locales usam o bundle base.");
    }

    public static class Mensagens extends ListResourceBundle {
        @Override
        protected Object[][] getContents() {
            return new Object[][] {
                    {"saudacao", "Welcome to Java study"}
            };
        }
    }

    public static class Mensagens_pt_BR extends Mensagens {
        @Override
        protected Object[][] getContents() {
            return new Object[][] {
                    {"saudacao", "Bem-vindo aos estudos de Java"}
            };
        }
    }
}
