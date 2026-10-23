# Comparação e ordenação

## Estude

- `Comparable<T>` e a ordem natural implementada por `compareTo`.
- `Comparator<T>` e comparadores criados com `comparing`, `thenComparing` e `reversed`.
- `compareTo`/`compare` devem indicar ordem negativa, zero ou positiva.
- Ordenação de listas e arrays; busca binária exige dados ordenados segundo a mesma ordem.
- Ordenação natural de `TreeSet` e `TreeMap`, comparador fornecido e incompatibilidade de tipos.
- Relação recomendada entre `compareTo` e `equals`.
- Ordenação com lambdas e referências de método.

## Prática

Ordene objetos por dois campos e teste como um comparador que retorna zero afeta a inclusão em `TreeSet`.
