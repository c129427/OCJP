public class TextoStringEStringBuilderExample {
    public static void main(String[] args) {
        System.out.println("=== String imutavel e StringBuilder mutavel ===");
        String original = "Java";
        String novaString = original.concat(" SE 17");
        StringBuilder textoMutavel = new StringBuilder("Estudo");
        textoMutavel.append(" OCJP");
        String textoA = new String("Java");
        String textoB = new String("Java");

        System.out.println("concat devolve uma nova String: " + novaString);
        System.out.println("A String original continua inalterada: " + original);
        System.out.println("append altera o StringBuilder: " + textoMutavel);
        System.out.println("equals compara conteudo: " + textoA.equals(textoB));
        System.out.println("== compara identidade dos objetos: " + (textoA == textoB));
    }
}
