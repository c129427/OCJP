# Guia de estudos — Oracle Certified Professional: Java SE 17 Developer

Este repositório organiza os estudos para a certificação **Oracle Certified Professional: Java SE 17 Developer**, exame **1Z0-829**. Os diretórios acompanham os domínios publicados pela Oracle; cada domínio contém um índice e um README por assunto, com tópicos para estudar e atividades de prática.

> O conteúdo é um roteiro de estudos independente, não material oficial da Oracle. Confirme os objetivos e as condições atuais do exame na [página oficial do exame 1Z0-829](https://education.oracle.com/java-se-17-developer/pexam_1Z0-829).

O portal estático de estudos começa em [`index.html`](index.html); o [resumo geral](resumo.html) oferece uma visão rápida do percurso. Para quem está começando, a [trilha inicial](trilha-iniciante.html) começa pelos fundamentos de variáveis, entrada/saída, compilação e execução; depois apresenta uma sequência progressiva, erros frequentes e um projeto incremental com checkpoints compiláveis. A trilha permite marcar o progresso, salvo localmente neste navegador. O [glossário Java](glossario.html) explica termos recorrentes. O [quiz dinâmico](quiz.html) oferece rodadas adaptativas de 12 questões, sem repetir temas na mesma rodada, e indica quais assuntos revisar. Cada capítulo também tem um marco prático de conclusão. As páginas usam o CSS compartilhado `site.css` e podem ser abertas diretamente no navegador.

O [comparativo entre os exames 1Z0-808, 1Z0-829 e 1Z0-830](exames.html) destaca as diferenças de versão Java, nível e foco de estudo, com uma matriz editorial de reaproveitamento por capítulo. As páginas de assunto incluem objetivo de aprendizagem, roteiro curto, atividade prática, checagem com resposta comentada, exemplo Java com comandos de execução e links para conceitos relacionados. O banco do quiz fica em `tools/quiz_questions.py` e `tools/quiz_questions_extra.py`, com questões variadas nos níveis fácil, médio e difícil para cada assunto. O resultado de uma rodada é apenas uma amostra de estudo, não uma medida definitiva de domínio. A ordem do índice de certificação segue os links de assuntos de cada README; a trilha para iniciantes reordena os fundamentos por pré-requisito. Para regenerar todas as páginas, execute `python tools\build_static_site.py`.

## Roteiro por domínio

| Domínio do exame | Conteúdos |
| --- | --- |
| [01. Valores, texto e datas](./01-valores-texto-e-datas/README.md) | Valores primitivos e wrappers, operadores, conversões, `String`, `StringBuilder` e API de data e hora |
| [02. Controle de fluxo](./02-controle-de-fluxo/README.md) | Condicionais, `switch`, laços, métodos e sobrecarga |
| [03. Programação orientada a objetos](./03-poo/README.md) | Classes, objetos, encapsulamento, construtores, herança, interfaces, enums, records, classes seladas e pattern matching |
| [04. Tratamento de exceções](./04-excecoes/README.md) | Hierarquia de exceções, `try`/`catch`/`finally`, multi-catch e try-with-resources |
| [05. Arrays e coleções](./05-arrays-e-colecoes/README.md) | Arrays, generics, Collections Framework, comparações e ordenação |
| [06. Streams e expressões lambda](./06-streams-e-lambdas/README.md) | Interfaces funcionais, lambdas, method references, streams, collectors e `Optional` |
| [07. Java Platform Module System](./07-modulos-java/README.md) | Módulos, diretivas, serviços e execução de aplicações modulares |
| [08. Concorrência](./08-concorrencia/README.md) | Threads, executors, sincronização e APIs concorrentes |
| [09. Entrada e saída (I/O)](./09-io/README.md) | Streams de bytes e caracteres, NIO.2, arquivos e serialização |
| [10. JDBC](./10-jdbc/README.md) | Conexões, statements, resultados, recursos e transações |
| [11. Localização](./11-localizacao/README.md) | `Locale`, bundles de recursos, formatação e parsing localizado |

## Como estudar

1. Se ainda não programa em Java, comece pelos [fundamentos da trilha](trilha-iniciante.html#fundamentos): compile e execute o primeiro exemplo antes de seguir para os assuntos.
2. Em cada assunto, leia o objetivo, execute o exemplo e tente a atividade prática antes de conferir a resposta da checagem.
3. Use o glossário quando encontrar um termo novo e retorne aos tópicos “Estude” e “Verifique se consegue” para aprofundar a revisão.
4. Ao preparar a certificação, siga o índice por domínio e confirme os objetivos oficiais atuais do exame.

Os exemplos ficam em subpastas de `src/`, separadas por domínio e assunto.

## Preferências do Copilot

As preferências persistentes do projeto ficam em [`.github/copilot-instructions.md`](.github/copilot-instructions.md). A skill [`super-memoria`](.github/skills/super-memoria/SKILL.md) orienta como mantê-las; a configuração inicial determina que as respostas sejam sempre em português brasileiro.

## Executar os exemplos

Cada assunto tem uma classe Java independente, com `main` e saída pelo console, organizada em `src/<domínio>/<assunto>/`. O exemplo inicial da trilha fica em `src/java_Basico/FundamentosJava.java`. Para compilá-lo e executá-lo no PowerShell a partir da raiz:

```powershell
New-Item -ItemType Directory -Force target\bin | Out-Null
javac -d target\bin src\java_Basico\FundamentosJava.java
java -cp target\bin FundamentosJava
```

No macOS/Linux:

```sh
mkdir -p target/bin
javac -d target/bin src/java_Basico/FundamentosJava.java
java -cp target/bin FundamentosJava
```

Exemplo de um assunto de certificação no PowerShell:

```powershell
javac -d target\bin src\05-arrays-e-colecoes\arrays\ArraysExample.java
java -cp target\bin ArraysExample
```

Os nomes das pastas dos domínios começam com números ou contêm hífens, que não são válidos em nomes de pacotes Java. Por isso, os exemplos usam o pacote padrão e nomes de classe exclusivos. O arquivo `.classpath` inclui cada pasta de assunto como raiz de código-fonte para que o projeto Eclipse/Java continue reconhecendo esses exemplos.

## Referências

- [Oracle — exame Java SE 17 Developer (1Z0-829)](https://education.oracle.com/java-se-17-developer/pexam_1Z0-829)
- [Documentação da plataforma Java, versão 17](https://docs.oracle.com/en/java/javase/17/)
- [Especificação da linguagem Java, versão 17](https://docs.oracle.com/javase/specs/jls/se17/html/index.html)
- [Especificação da máquina virtual Java, versão 17](https://docs.oracle.com/javase/specs/jvms/se17/html/index.html)
