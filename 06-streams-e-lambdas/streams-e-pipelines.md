# Streams e pipelines

## Estude

- Criação de streams a partir de coleções, arrays, valores e `Stream.of`.
- Operações intermediárias lazy: `filter`, `map`, `flatMap`, `distinct`, `sorted`, `limit`, `skip` e `peek`.
- Operações terminais: `forEach`, `count`, `min`, `max`, `reduce`, `toArray` e `collect`.
- Streams de objetos e streams primitivos: `IntStream`, `LongStream` e `DoubleStream`.
- `mapToInt`, `boxed`, `average`, `sum`, `summaryStatistics` e operações relacionadas.
- Curto-circuito com `anyMatch`, `allMatch`, `noneMatch`, `findFirst` e `findAny`.
- Streams não são estruturas de armazenamento; não reutilize um stream já consumido.
- Ordem, efeitos colaterais, pipeline vazio e operações paralelas.

## Verifique se consegue

- Identificar quais operações realmente executam o pipeline.
- Calcular o resultado de `map`/`filter`/`reduce` sem confundir transformação com mutação da fonte.
