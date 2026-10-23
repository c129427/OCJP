import java.text.NumberFormat;
import java.text.ParseException;
import java.text.ParsePosition;
import java.util.Locale;

public class FormatacaoEParsingExample {
    public static void main(String[] args) throws ParseException {
        System.out.println("=== Formatacao e parsing localizado ===");
        double valor = 12345.67;
        NumberFormat formatoBrasil = NumberFormat.getCurrencyInstance(Locale.forLanguageTag("pt-BR"));
        NumberFormat formatoEua = NumberFormat.getCurrencyInstance(Locale.US);
        NumberFormat parserNumericoBrasil = NumberFormat.getNumberInstance(Locale.forLanguageTag("pt-BR"));
        String valorBrasileiro = "1.234,50";
        ParsePosition posicao = new ParsePosition(0);
        Number valorInterpretado = parserNumericoBrasil.parse(valorBrasileiro, posicao);

        System.out.println("Mesmo valor em moeda brasileira: " + formatoBrasil.format(valor));
        System.out.println("Mesmo valor em moeda dos EUA: " + formatoEua.format(valor));
        if (valorInterpretado == null || posicao.getIndex() != valorBrasileiro.length()) {
            throw new ParseException("Valor invalido para o locale pt-BR.", posicao.getErrorIndex());
        }
        System.out.println("\"" + valorBrasileiro + "\" interpretado no locale pt-BR: "
                + valorInterpretado);
    }
}
