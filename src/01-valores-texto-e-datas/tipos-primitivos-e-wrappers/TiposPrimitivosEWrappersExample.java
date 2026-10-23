public class TiposPrimitivosEWrappersExample {
    public static void main(String[] args) {
        System.out.println("=== Tipos primitivos e classes wrapper ===");
        System.out.println("int guarda um valor primitivo; Integer e um objeto que representa um int.");

        int quantidade = 42;
        Integer total = quantidade;
        int valorConvertido = total;
        int valorLidoDeTexto = Integer.parseInt("58");

        System.out.println("int quantidade = 42: " + quantidade);
        System.out.println("Integer total = quantidade (autoboxing): " + total);
        System.out.println("int valorConvertido = total (unboxing): " + valorConvertido);
        System.out.println("Integer.parseInt(\"58\") converte texto para int: " + valorLidoDeTexto);
        System.out.println("Use equals para comparar valores de wrappers: "
                + Integer.valueOf(1000).equals(Integer.valueOf(1000)));
    }
}
