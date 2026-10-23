public class HerancaSobrescritaEPolimorfismoExample {
    private static class Animal {
        String especie = "animal";

        String emitirSom() {
            return "som generico";
        }
    }

    private static class Cachorro extends Animal {
        String especie = "cachorro";

        @Override
        String emitirSom() {
            return "latido";
        }
    }

    private static class Gato extends Animal {
        @Override
        String emitirSom() {
            return "miado";
        }
    }

    public static void main(String[] args) {
        System.out.println("=== Heranca, sobrescrita e polimorfismo ===");
        Animal[] animais = {new Cachorro(), new Gato()};
        for (Animal animal : animais) {
            System.out.println("Tipo da referencia: Animal; som sobrescrito: " + animal.emitirSom());
        }

        Animal referencia = new Cachorro();
        System.out.println("Campo usa o tipo declarado da referencia: " + referencia.especie);
        System.out.println("Metodo sobrescrito usa o tipo real do objeto: " + referencia.emitirSom());
    }
}
