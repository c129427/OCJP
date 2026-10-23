# Try-with-resources

## Estude

- Interface `AutoCloseable` e fechamento automático de recursos.
- Declaração de um ou mais recursos no cabeçalho do `try`.
- Ordem inversa de fechamento em relação à ordem de abertura.
- Recursos declarados no cabeçalho e referências a variáveis efetivamente finais.
- Bloco `catch` e `finally` opcionais.
- Exceções primárias e exceções suprimidas durante o fechamento (`getSuppressed`).
- Diferenças de comportamento entre fechamento automático e fechamento manual.

## Prática

Use dois recursos que lançam exceções na operação e no fechamento. Identifique qual exceção é primária e quais ficam suprimidas.
