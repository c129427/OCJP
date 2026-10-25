# Guia de estudos — Oracle Certified Professional: Java SE 17 Developer

Este repositório organiza os estudos para a certificação **Oracle Certified Professional: Java SE 17 Developer**, exame **1Z0-829**. Os diretórios acompanham os domínios publicados pela Oracle; cada domínio contém um índice e um README por assunto, com tópicos para estudar e atividades de prática.

> O conteúdo é um roteiro de estudos independente, não material oficial da Oracle. Confirme os objetivos e as condições atuais do exame na [página oficial do exame 1Z0-829](https://education.oracle.com/java-se-17-developer/pexam_1Z0-829).

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

1. Siga os domínios e assuntos na ordem do roteiro, ou use o índice para revisar um tema específico.
2. Leia o README do assunto e escreva pequenos programas para testar cada item da lista.
3. Antes de consultar a saída do programa, preveja o resultado e explique as regras envolvidas.
4. Revise os casos-limite indicados nos assuntos: eles são especialmente úteis para questões de múltipla escolha.
5. Use as listas de tópicos e os desafios dos READMEs para acompanhar seu progresso.

Os exemplos ficam em subpastas de `src/`, separadas por domínio e assunto.

## Preferências do Copilot

As preferências persistentes do projeto ficam em [`.github/copilot-instructions.md`](.github/copilot-instructions.md). A skill [`super-memoria`](.github/skills/super-memoria/SKILL.md) orienta como mantê-las; a configuração inicial determina que as respostas sejam sempre em português brasileiro.

## Executar os exemplos

Cada assunto tem uma classe Java independente, com `main` e saída pelo console, organizada em `src/<domínio>/<assunto>/`. Por exemplo, para compilar e executar o exemplo de arrays no PowerShell:

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
