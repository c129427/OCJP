# Records, classes seladas e pattern matching

## Estude

- Records como portadores de dados: componentes, campos finais, acessores, `equals`, `hashCode` e `toString` gerados.
- Construtor canônico, compacto e construtores adicionais de um record.
- Restrições de records: são implicitamente finais e não estendem outra classe.
- Classes e interfaces `sealed`, `non-sealed` e `final`; lista `permits` e subclasses diretas autorizadas.
- Pattern matching para `instanceof` e escopo da variável de padrão.
- Diferença entre imutabilidade da referência/componente e imutabilidade profunda de um objeto mutável contido.
- Recursos de linguagem disponíveis no Java 17; distinguir funcionalidades finais de funcionalidades em preview.

## Prática

Crie um record com validação no construtor compacto e uma hierarquia sealed com subclasses permitidas. Identifique quais declarações não compilam.
