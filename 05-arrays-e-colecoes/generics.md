# Generics

## Estude

- Classes, interfaces e métodos genéricos; parâmetros de tipo e inferência.
- Tipos parametrizados e invariância, por exemplo, `List<Integer>` não é subtipo de `List<Number>`.
- Limites superiores com `extends` e limites inferiores com `super`.
- Wildcards `?`, `? extends T` e `? super T`; princípio PECS para leitura e escrita.
- Inferência de tipos, operador diamante (`<>`) e métodos genéricos estáticos.
- Apagamento de tipos (type erasure), restrições de tipos genéricos e tipos raw.
- Segurança de tipos, avisos de unchecked e heap pollution.

## Verifique se consegue

- Determinar quais operações de leitura e escrita compilam com cada wildcard.
- Separar erros de compilação de casts que podem falhar durante a execução.
