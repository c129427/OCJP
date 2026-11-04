#!/usr/bin/env python3
"""Generate static study pages from the repository's existing Markdown notes."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

from quiz_questions import QUIZ_BANK
from quiz_questions_extra import QUIZ_QUESTION_VARIANTS


ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIRS = sorted(path for path in ROOT.iterdir() if re.match(r"\d{2}-", path.name))

LEARNING_GUIDES = {
    "data-e-hora-java-time": (
        "Escolher entre data civil, horário local, instante e horário associado a fuso; reconhecer operações imutáveis.",
        "Por que adicionar um mês com `Period` não equivale sempre a somar 30 dias com `Duration`?",
        "`Period` opera em unidades do calendário e respeita a duração variável dos meses; `Duration` mede tempo em segundos e unidades menores.",
    ),
    "operadores-expressoes-e-conversoes": (
        "Rastrear precedência, conversões e tipo resultante antes de calcular o valor de uma expressão.",
        "Qual é o tipo de `byte + byte` e por que a atribuição direta de volta a `byte` não compila?",
        "A promoção numérica binária converte ambos para `int`; o resultado é `int` e exige cast explícito para voltar a `byte`.",
    ),
    "texto-string-e-stringbuilder": (
        "Distinguir identidade de referência, igualdade de conteúdo e operações mutáveis ou imutáveis.",
        "Depois de `String s = \"Java\"; s.concat(\" 17\");`, qual é o valor de `s`?",
        "`s` continua sendo `Java`: `String` é imutável e `concat` devolve uma nova string que precisa ser atribuída.",
    ),
    "tipos-primitivos-e-wrappers": (
        "Diferenciar valores primitivos, wrappers, inicialização de variáveis e conversões boxing/unboxing.",
        "O que ocorre ao atribuir um wrapper `null` a uma variável primitiva?",
        "O unboxing tenta obter o valor primitivo e lança `NullPointerException`; uma variável local também precisa estar inicializada antes do uso.",
    ),
    "condicionais-e-switch": (
        "Rastrear os caminhos de `if` e `switch`, distinguindo instruções de expressões que produzem valor.",
        "Uma expressão `switch` com um bloco `case` pode usar `break` para devolver o resultado?",
        "Não. Um bloco de uma expressão `switch` usa `yield` para produzir valor; os caminhos precisam ser exaustivos.",
    ),
    "lacos-e-desvios": (
        "Simular inicialização, condição, corpo e atualização de laços, inclusive desvios rotulados.",
        "Em um laço aninhado, o que `continue externo` faz?",
        "Interrompe a iteração atual do laço identificado por `externo` e segue para a próxima iteração desse laço.",
    ),
    "metodos-sobrecarga-e-varargs": (
        "Prever a resolução de overloads a partir dos tipos declarados e distinguir passagem por valor de mutação do objeto.",
        "A escolha do overload usa o tipo real do objeto passado ou o tipo declarado da expressão?",
        "Usa os tipos conhecidos em compilação; referências são passadas por valor, então reatribuir o parâmetro não reatribui a variável do chamador.",
    ),
    "classes-objetos-e-encapsulamento": (
        "Entender referências, estado, escopo e limites de acesso de objetos e membros.",
        "Se `b = a`, a atribuição copia o objeto ou a referência?",
        "Copia a referência: `a` e `b` passam a apontar para o mesmo objeto; mudanças no estado observável por uma delas aparecem pela outra.",
    ),
    "construtores-e-inicializacao": (
        "Rastrear a ordem de inicialização e o encadeamento dos construtores de uma hierarquia.",
        "O compilador sempre fornece um construtor sem argumentos?",
        "Não. O construtor padrão só é fornecido quando a classe não declara nenhum construtor.",
    ),
    "heranca-sobrescrita-e-polimorfismo": (
        "Separar despacho dinâmico de métodos sobrescritos de acesso a campos definido pelo tipo declarado.",
        "Uma chamada a método sobrescrito depende do tipo declarado da referência ou da classe real do objeto?",
        "O método sobrescrito é escolhido pelo tipo real do objeto; campos não são despachados dinamicamente e dependem da referência usada.",
    ),
    "interfaces-e-enums": (
        "Aplicar contratos de interfaces, resolver métodos `default` e usar enums como tipos fechados de constantes.",
        "O que a classe deve fazer quando duas interfaces implementadas fornecem o mesmo método `default`?",
        "Fornecer uma implementação explícita que resolva o conflito, podendo delegar a uma das interfaces com `Interface.super.metodo()`.",
    ),
    "records-sealed-e-pattern-matching": (
        "Reconhecer os contratos e restrições de records e hierarquias sealed disponíveis no Java 17.",
        "Um record pode estender uma classe definida pelo usuário?",
        "Não. Um record é implicitamente final e estende `java.lang.Record`; funcionalidades em preview devem ser diferenciadas das finais no Java 17.",
    ),
    "hierarquia-e-tipos-de-excecao": (
        "Identificar exceções checked e unchecked e decidir quando declarar, capturar ou propagar.",
        "Qual é a diferença entre `throw` e `throws`?",
        "`throw` lança uma instância no fluxo de execução; `throws` declara no método tipos de exceções que podem ser propagadas.",
    ),
    "try-catch-finally-e-multicatch": (
        "Prever o fluxo de captura, propagação e execução de `finally` sem ocultar a exceção original.",
        "Por que evitar `return` ou lançar outra exceção dentro de `finally`?",
        "Esse fluxo pode substituir o retorno ou a exceção pendente, ocultando o resultado ou a falha original.",
    ),
    "try-with-resources": (
        "Aplicar fechamento automático e interpretar a ordem de fechamento e as exceções suprimidas.",
        "Se a operação e `close()` falham, qual falha fica como exceção principal?",
        "A falha da operação é principal; a falha do fechamento é suprimida e pode ser consultada com `getSuppressed()`.",
    ),
    "arrays": (
        "Distinguir arrays de primitivos e de referências, índices, covariância e utilitários de busca/ordenação.",
        "Por que `Arrays.binarySearch` pode retornar um resultado incorreto se o array não estiver ordenado?",
        "A busca binária pressupõe dados ordenados segundo a mesma ordem usada na busca; sem esse requisito, o resultado não é confiável.",
    ),
    "comparacao-e-ordenacao": (
        "Definir uma ordem natural ou externa e prever como comparadores influenciam coleções ordenadas.",
        "O que significa `compare(a, b) == 0` para um `TreeSet`?",
        "Os elementos são equivalentes segundo a ordenação; o conjunto não os mantém como elementos distintos, mesmo que `equals` diga o contrário.",
    ),
    "generics": (
        "Ler limites e wildcards para preservar segurança de tipos e saber quais operações são válidas.",
        "Em `List<? extends Number>`, é seguro adicionar um `Integer`?",
        "Não: o tipo exato da lista pode ser `List<Double>`. A referência permite leitura como `Number`, mas restringe inserções (princípio PECS).",
    ),
    "interfaces-e-colecoes": (
        "Escolher estruturas de coleção conforme ordem, duplicatas, acesso, mutabilidade e contrato de igualdade.",
        "Quais contratos devem ser consistentes para uma chave usada em `HashMap`?",
        "`equals` e `hashCode`: objetos iguais devem ter o mesmo hash; mudar campos usados nesses métodos enquanto a chave está no mapa compromete a consulta.",
    ),
    "collectors-e-optional": (
        "Agrupar e reduzir dados com collectors e escolher operações de `Optional` conforme o comportamento desejado.",
        "Qual é a diferença de avaliação entre `orElse(valor)` e `orElseGet(supplier)`?",
        "`orElse` avalia o argumento mesmo quando o valor existe; `orElseGet` só chama o supplier quando o `Optional` está vazio.",
    ),
    "interfaces-funcionais-lambdas-e-referencias": (
        "Associar lambdas e method references ao tipo funcional esperado e aplicar composição de funções.",
        "Uma lambda pode modificar uma variável local capturada?",
        "Não pode reatribuí-la: uma variável local capturada deve ser final ou efetivamente final, embora isso não torne automaticamente imutável o objeto referenciado.",
    ),
    "streams-e-pipelines": (
        "Montar pipelines sem confundir operações intermediárias lazy com operações terminais.",
        "Um `filter` executa o pipeline assim que é chamado?",
        "Não. `filter` é intermediária e lazy; uma operação terminal dispara a avaliação. Um stream já consumido não pode ser reutilizado.",
    ),
    "sistema-de-modulos-jpms": (
        "Declarar dependências e distinguir exposição de API pública de abertura para reflexão.",
        "Qual é a diferença entre `exports` e `opens`?",
        "`exports` torna acessíveis tipos públicos de um pacote; `opens` permite acesso reflexivo profundo ao pacote conforme as regras do sistema de módulos.",
    ),
    "apis-concorrentes-e-colecoes": (
        "Escolher entre locks, atomics e coleções concorrentes, reconhecendo os limites de atomicidade.",
        "`ConcurrentHashMap` torna atômica qualquer sequência de duas chamadas?",
        "Não. Use operações compostas próprias, como `computeIfAbsent`; duas chamadas separadas não viram uma transação atômica por estarem no mapa concorrente.",
    ),
    "sincronizacao-e-visibilidade": (
        "Diferenciar visibilidade, exclusão mútua e atomicidade no acesso a estado compartilhado.",
        "Uma variável `volatile` torna `contador++` atômico?",
        "Não. `volatile` garante propriedades de visibilidade e ordenação, mas incremento é leitura-modificação-escrita; use sincronização ou um tipo atômico.",
    ),
    "threads-e-executors": (
        "Distinguir criação de threads, execução de tarefas, resultados futuros e encerramento de executors.",
        "Qual é a diferença entre chamar `start()` e chamar `run()` diretamente?",
        "`start()` agenda a execução em uma nova thread; uma chamada direta a `run()` é apenas uma chamada de método na thread atual.",
    ),
    "nio2-path-e-files": (
        "Usar `Path` para representar caminhos e `Files` para executar operações e tratar seus erros.",
        "Criar um objeto `Path` confirma que o arquivo existe?",
        "Não. `Path` representa um caminho; existência, permissões e operações são verificadas separadamente com `Files`.",
    ),
    "serializacao": (
        "Rastrear o estado serializado de objetos e reconhecer riscos de compatibilidade e segurança.",
        "Um campo `static` faz parte do estado serializado de cada objeto?",
        "Não como estado da instância: `static` pertence à classe. Campos `transient` também são excluídos da serialização padrão; dados não confiáveis não devem ser desserializados sem proteção.",
    ),
    "streams-readers-e-writers": (
        "Escolher entre I/O de bytes e caracteres, definir charset e fechar recursos corretamente.",
        "Para copiar uma imagem, deve-se decodificar os dados com `Reader`?",
        "Não. Uma imagem é dado binário: use streams de bytes. `Reader` e `Writer` são abstrações para caracteres e codificação.",
    ),
    "conexoes-e-comandos": (
        "Executar comandos JDBC com parâmetros e administrar conexões e statements como recursos.",
        "A partir de que índice são definidos os parâmetros de um `PreparedStatement`?",
        "A partir de 1. Prefira `PreparedStatement` com parâmetros para valores em vez de concatenar esses valores no SQL.",
    ),
    "resultset-recursos-e-transacoes": (
        "Ler resultados respeitando o cursor e identificar quando a transação foi confirmada ou revertida.",
        "Onde começa o cursor de um `ResultSet` e o que fazer antes de ler uma linha?",
        "Antes da primeira linha. Chame `next()` e leia colunas somente quando o método retornar `true`; confirme ou reverta a transação conforme o resultado.",
    ),
    "formatacao-e-parsing": (
        "Formatar e interpretar números e datas com locale explícito e tratar entradas incompatíveis.",
        "Por que o mesmo padrão de formatação pode produzir texto diferente em dois locales?",
        "Símbolos e convenções regionais (como separadores decimais e de agrupamento) variam; informe explicitamente o `Locale` para resultados previsíveis.",
    ),
    "locale-e-bundles": (
        "Separar idioma de região e prever a resolução de bundles e o fallback de recursos.",
        "O que acontece se não houver bundle para o locale mais específico solicitado?",
        "`ResourceBundle` procura alternativas mais gerais e o bundle base conforme as regras de busca; uma chave ausente pode resultar em `MissingResourceException`.",
    ),
}

BEGINNER_STAGES = [
    (
        "1. Primeiros programas",
        "Aprenda a ler e escrever pequenos programas antes de estudar APIs maiores.",
        [
            "tipos-primitivos-e-wrappers",
            "operadores-expressoes-e-conversoes",
            "texto-string-e-stringbuilder",
            "condicionais-e-switch",
            "lacos-e-desvios",
            "metodos-sobrecarga-e-varargs",
        ],
    ),
    (
        "2. Organize o código com objetos",
        "Modele dados e responsabilidades em classes e entenda como os objetos são criados.",
        [
            "classes-objetos-e-encapsulamento",
            "construtores-e-inicializacao",
            "interfaces-e-enums",
            "heranca-sobrescrita-e-polimorfismo",
        ],
    ),
    (
        "3. Trabalhe com dados e falhas",
        "Guarde coleções de dados, restrinja seus tipos e trate situações inesperadas.",
        [
            "arrays",
            "interfaces-e-colecoes",
            "generics",
            "hierarquia-e-tipos-de-excecao",
            "try-catch-finally-e-multicatch",
        ],
    ),
    (
        "4. Use APIs do dia a dia",
        "Aplique os fundamentos para transformar dados, usar arquivos e lidar com datas.",
        [
            "interfaces-funcionais-lambdas-e-referencias",
            "streams-e-pipelines",
            "nio2-path-e-files",
            "data-e-hora-java-time",
        ],
    ),
]

PRACTICE_TASKS = {
    "tipos-primitivos-e-wrappers": "Declare uma quantidade como `int`, converta-a para `Integer` e imprima os dois valores. Depois, tente converter o texto `\"abc\"` com `Integer.parseInt` e observe a exceção.",
    "operadores-expressoes-e-conversoes": "Calcule o total de dois preços inteiros e mostre também o resultado de uma divisão inteira e de uma divisão decimal.",
    "texto-string-e-stringbuilder": "Monte uma frase com `StringBuilder`, altere uma palavra e compare o resultado com uma concatenação de `String`.",
    "data-e-hora-java-time": "Crie uma data fixa com `LocalDate.of`, some sete dias e imprima as duas datas para observar que a original não mudou.",
    "condicionais-e-switch": "Leia ou defina uma nota numérica e use `if` para classificá-la em aprovado ou não aprovado; teste os limites da condição.",
    "lacos-e-desvios": "Percorra os números de 1 a 10, imprima apenas os pares e some os valores impressos.",
    "metodos-sobrecarga-e-varargs": "Crie um método que receba dois números e devolva a soma; faça uma sobrecarga que receba três e compare as chamadas.",
    "classes-objetos-e-encapsulamento": "Crie uma classe `Tarefa` com descrição e estado concluído privados; instancie uma tarefa e imprima seus dados por métodos públicos.",
    "construtores-e-inicializacao": "Adicione à classe `Tarefa` um construtor que receba a descrição e imprima a ordem em que campos e construtor são executados.",
    "heranca-sobrescrita-e-polimorfismo": "Crie duas subclasses que sobrescrevam um método `descrever`; chame o método por variáveis do tipo da superclasse.",
    "interfaces-e-enums": "Defina um enum para os estados de uma tarefa e use `switch` para imprimir uma mensagem para cada estado.",
    "records-sealed-e-pattern-matching": "Crie um `record` simples para representar uma categoria e teste os métodos `toString` e `equals` gerados.",
    "hierarquia-e-tipos-de-excecao": "Escreva um método que valide uma descrição vazia e lance `IllegalArgumentException`; capture a exceção e mostre a mensagem.",
    "try-catch-finally-e-multicatch": "Converta um texto em número dentro de `try` e trate uma entrada inválida com uma mensagem compreensível.",
    "try-with-resources": "Grave uma linha em um arquivo usando um recurso `AutoCloseable` dentro de try-with-resources.",
    "arrays": "Armazene cinco notas em um array, calcule a média e imprima o maior valor.",
    "generics": "Crie uma `List<String>`, adicione três nomes e percorra a lista sem casts.",
    "interfaces-e-colecoes": "Guarde nomes em `ArrayList` e `HashSet`; adicione um nome repetido e compare os tamanhos.",
    "comparacao-e-ordenacao": "Ordene uma lista de tarefas pela descrição usando `Comparator.comparing`.",
    "interfaces-funcionais-lambdas-e-referencias": "Use um `Predicate<String>` para selecionar descrições maiores que cinco caracteres.",
    "streams-e-pipelines": "Filtre uma lista de números pares, transforme-os em seus quadrados e imprima o resultado após uma operação terminal.",
    "collectors-e-optional": "Agrupe tarefas por estado com `Collectors.groupingBy` e conte quantas existem em cada grupo.",
    "sistema-de-modulos-jpms": "Escreva um `module-info.java` mínimo com uma dependência `requires` e um pacote exposto por `exports`.",
    "threads-e-executors": "Submeta duas tarefas curtas a um `ExecutorService`, aguarde os resultados e encerre o executor.",
    "sincronizacao-e-visibilidade": "Use duas threads para atualizar um contador compartilhado; compare o resultado sem sincronização e com uma seção `synchronized`.",
    "apis-concorrentes-e-colecoes": "Conte ocorrências de palavras em um `ConcurrentHashMap` usando `merge` ou `computeIfAbsent`.",
    "streams-readers-e-writers": "Leia um arquivo de texto com charset explícito e feche o leitor automaticamente.",
    "nio2-path-e-files": "Crie um arquivo temporário com `Files`, grave duas linhas, leia-as e apague o arquivo.",
    "serializacao": "Torne uma classe simples serializável, grave uma instância e leia-a de volta; observe um campo `transient`.",
    "conexoes-e-comandos": "Com um banco de teste configurado, execute uma consulta parametrizada usando `PreparedStatement`.",
    "resultset-recursos-e-transacoes": "Percorra um `ResultSet` chamando `next()` antes de ler cada coluna e confirme ou reverta uma transação.",
    "locale-e-bundles": "Crie dois arquivos de recursos para idiomas diferentes e carregue uma mensagem usando `ResourceBundle`.",
    "formatacao-e-parsing": "Formate o mesmo valor monetário para dois `Locale` explícitos e compare separadores e símbolos.",
}

GLOSSARY_ITEMS = [
    ("Compilar", "Converter arquivos-fonte `.java` em bytecode com o compilador `javac`; erros de sintaxe e de tipos aparecem nesta etapa."),
    ("Executar", "Iniciar o programa compilado com `java`; erros que dependem dos valores ou do estado podem ocorrer durante a execução."),
    ("Primitivo e wrapper", "Um primitivo guarda diretamente um valor simples, como `int`; um wrapper, como `Integer`, é uma classe que representa esse valor como objeto."),
    ("Boxing e unboxing", "Boxing converte um primitivo em wrapper; unboxing extrai o primitivo do wrapper. Fazer unboxing de `null` causa `NullPointerException`."),
    ("Referência", "Uma variável de tipo de classe guarda uma referência a um objeto, não uma cópia automática do objeto."),
    ("Sobrecarga (overload)", "Métodos com o mesmo nome e parâmetros diferentes; o compilador escolhe qual chamar com base nos tipos conhecidos em compilação."),
    ("Sobrescrita (override)", "Uma subclasse fornece sua implementação de um método herdado; a chamada de instância pode depender da classe real do objeto."),
    ("Exceção checked", "Uma exceção verificada pelo compilador, que em geral precisa ser capturada ou declarada com `throws`."),
    ("Generics e wildcard", "Generics associam tipos a classes e métodos; `?` representa um tipo desconhecido e pode restringir o que é seguro inserir."),
    ("Interface funcional", "Uma interface com um único método abstrato, que pode ser implementada com lambda quando o tipo esperado é conhecido."),
    ("Stream lazy", "Operações intermediárias de stream descrevem transformações; a execução ocorre quando uma operação terminal é chamada."),
    ("Atomicidade e visibilidade", "Atomicidade trata uma operação como indivisível; visibilidade garante que uma thread veja alterações feitas por outra. São propriedades diferentes."),
    ("JDK, JRE e JVM", "JDK é o kit de desenvolvimento que inclui ferramentas como `javac`; JVM executa bytecode. JRE é o conjunto de componentes de execução, que nem sempre é distribuído como instalação separada."),
]

CROSS_REFERENCES = {
    "data-e-hora-java-time": ["formatacao-e-parsing", "locale-e-bundles"],
    "operadores-expressoes-e-conversoes": ["tipos-primitivos-e-wrappers", "metodos-sobrecarga-e-varargs"],
    "texto-string-e-stringbuilder": ["arrays", "formatacao-e-parsing"],
    "tipos-primitivos-e-wrappers": ["operadores-expressoes-e-conversoes", "arrays"],
    "condicionais-e-switch": ["interfaces-e-enums", "records-sealed-e-pattern-matching"],
    "lacos-e-desvios": ["arrays", "streams-e-pipelines"],
    "metodos-sobrecarga-e-varargs": ["interfaces-funcionais-lambdas-e-referencias", "generics"],
    "classes-objetos-e-encapsulamento": ["construtores-e-inicializacao", "heranca-sobrescrita-e-polimorfismo"],
    "construtores-e-inicializacao": ["classes-objetos-e-encapsulamento", "records-sealed-e-pattern-matching"],
    "heranca-sobrescrita-e-polimorfismo": ["interfaces-e-enums", "records-sealed-e-pattern-matching"],
    "interfaces-e-enums": ["condicionais-e-switch", "records-sealed-e-pattern-matching"],
    "records-sealed-e-pattern-matching": ["condicionais-e-switch", "heranca-sobrescrita-e-polimorfismo"],
    "hierarquia-e-tipos-de-excecao": ["try-catch-finally-e-multicatch", "try-with-resources"],
    "try-catch-finally-e-multicatch": ["hierarquia-e-tipos-de-excecao", "try-with-resources"],
    "try-with-resources": ["streams-readers-e-writers", "resultset-recursos-e-transacoes"],
    "arrays": ["generics", "interfaces-e-colecoes"],
    "comparacao-e-ordenacao": ["interfaces-e-colecoes", "streams-e-pipelines"],
    "generics": ["interfaces-e-colecoes", "comparacao-e-ordenacao"],
    "interfaces-e-colecoes": ["comparacao-e-ordenacao", "streams-e-pipelines"],
    "collectors-e-optional": ["streams-e-pipelines", "interfaces-funcionais-lambdas-e-referencias"],
    "interfaces-funcionais-lambdas-e-referencias": ["streams-e-pipelines", "comparacao-e-ordenacao"],
    "streams-e-pipelines": ["collectors-e-optional", "interfaces-funcionais-lambdas-e-referencias"],
    "sistema-de-modulos-jpms": ["conexoes-e-comandos", "streams-readers-e-writers"],
    "apis-concorrentes-e-colecoes": ["threads-e-executors", "interfaces-e-colecoes"],
    "sincronizacao-e-visibilidade": ["threads-e-executors", "apis-concorrentes-e-colecoes"],
    "threads-e-executors": ["sincronizacao-e-visibilidade", "apis-concorrentes-e-colecoes"],
    "nio2-path-e-files": ["streams-readers-e-writers", "try-with-resources"],
    "serializacao": ["streams-readers-e-writers", "classes-objetos-e-encapsulamento"],
    "streams-readers-e-writers": ["nio2-path-e-files", "try-with-resources"],
    "conexoes-e-comandos": ["resultset-recursos-e-transacoes", "try-with-resources"],
    "resultset-recursos-e-transacoes": ["conexoes-e-comandos", "hierarquia-e-tipos-de-excecao"],
    "formatacao-e-parsing": ["locale-e-bundles", "data-e-hora-java-time"],
    "locale-e-bundles": ["formatacao-e-parsing", "data-e-hora-java-time"],
}

CHAPTER_EXAM_NOTES = {
    "01-valores-texto-e-datas": (
        "Fundamentos reaproveitáveis; valide APIs e objetivos específicos de Java 8.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; confira as APIs e mudanças de linguagem em Java 21.",
    ),
    "02-controle-de-fluxo": (
        "Fundamentos reaproveitáveis; `switch` moderno não é sintaxe Java 8.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; revise pattern matching para `switch` em Java 21.",
    ),
    "03-poo": (
        "POO básica é reaproveitável; records e sealed não existem em Java 8.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; revise recursos de linguagem e regras de Java 21.",
    ),
    "04-excecoes": (
        "Fundamentos reaproveitáveis; confirme a profundidade no exame específico.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; valide o escopo do blueprint para Java 21.",
    ),
    "05-arrays-e-colecoes": (
        "Fundamentos reaproveitáveis; confira versão e APIs cobradas em Java 8.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; revise também Sequenced Collections no Java 21.",
    ),
    "06-streams-e-lambdas": (
        "Lambdas e streams surgem no Java 8; confirme se pertencem ao exame-alvo.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; valide as APIs e o escopo atualizado de Java 21.",
    ),
    "07-modulos-java": (
        "JPMS foi introduzido após Java 8; não aplique este capítulo como conteúdo Java 8.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; confira o objetivo e as regras de módulos da prova Java 21.",
    ),
    "08-concorrencia": (
        "Fundamentos reaproveitáveis; confira APIs disponíveis e objetivos de Java 8.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; revise virtual threads e APIs Java 21 aplicáveis.",
    ),
    "09-io": (
        "Fundamentos reaproveitáveis; valide APIs e objetivos específicos de Java 8.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; confira APIs e requisitos atualizados de Java 21.",
    ),
    "10-jdbc": (
        "Conceitos JDBC podem ser úteis; confirme se estão no escopo do exame escolhido.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; confirme driver, APIs e objetivos do exame Java 21.",
    ),
    "11-localizacao": (
        "Conceitos de locale são reaproveitáveis; valide objetivos específicos de Java 8.",
        "Base de estudo deste portal; confirme o mapeamento com o blueprint vigente.",
        "Conceitos úteis; confira APIs e objetivos vigentes de Java 21.",
    ),
}

CHAPTER_MILESTONES = {
    "01-valores-texto-e-datas": "Escreva um programa que calcule um total, formate uma mensagem e trabalhe com uma data sem alterar o valor original.",
    "02-controle-de-fluxo": "Implemente um menu de console com métodos, decisões e um laço que continue até a opção de saída.",
    "03-poo": "Modele uma tarefa com estado encapsulado e demonstre como construtores, interfaces e sobrescrita organizam o comportamento.",
    "04-excecoes": "Trate uma entrada inválida e garanta que o recurso aberto seja fechado mesmo quando ocorrer uma falha.",
    "05-arrays-e-colecoes": "Armazene itens em uma coleção tipada, evite duplicatas quando necessário e ordene os resultados.",
    "06-streams-e-lambdas": "Filtre e transforme uma coleção com stream e produza um resultado sem alterar a coleção original.",
    "07-modulos-java": "Separe uma aplicação em dois módulos, declare a dependência e exponha somente o pacote necessário.",
    "08-concorrencia": "Execute tarefas com um executor e proteja um estado compartilhado contra atualizações concorrentes.",
    "09-io": "Grave e leia um arquivo de texto com charset explícito e fechamento automático dos recursos.",
    "10-jdbc": "Execute uma consulta parametrizada, percorra os resultados e confirme ou reverta uma transação.",
    "11-localizacao": "Exiba uma mensagem, data e valor monetário usando recursos apropriados a dois locales explícitos.",
}


def page_title(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def first_paragraph(markdown: str) -> str:
    lines = markdown.splitlines()
    started = False
    content = []
    for line in lines:
        if not started:
            if (
                not line.strip()
                or line.startswith("#")
                or re.match(r"^\s*(?:[-*+]|\d+\.)\s+", line)
                or line.lstrip().startswith((">", "|", "```"))
            ):
                continue
            started = True
        if (
            not line.strip()
            or line.startswith("#")
            or re.match(r"^\s*(?:[-*+]|\d+\.)\s+", line)
            or line.lstrip().startswith((">", "|", "```"))
        ):
            break
        content.append(line.strip())
    return " ".join(content)


def first_study_item(markdown: str) -> str:
    in_study_section = False
    for line in markdown.splitlines():
        heading = re.match(r"^##\s+(.+)$", line)
        if heading:
            in_study_section = heading.group(1).strip().lower() == "estude"
            continue
        if in_study_section:
            item = re.match(r"^\s*[-*+]\s+(.+)$", line)
            if item:
                return item.group(1).strip()
    return ""


def output_target(source: Path, destination: Path, url: str) -> str:
    local_path, separator, fragment = url.partition("#")
    if local_path:
        target = (source.parent / local_path).resolve()
        if target.suffix.lower() == ".md":
            target = target.with_name("index.html" if target.name.lower() == "readme.md" else f"{target.stem}.html")
        if target.exists() or target.suffix.lower() in {".html", ".svg", ".java"}:
            relative = Path(__import__("os").path.relpath(target, destination.parent)).as_posix()
        else:
            relative = local_path
    else:
        relative = ""
    return relative + (separator + fragment if separator else "")


def inline(markdown: str, source: Path, destination: Path) -> str:
    text = html.escape(markdown, quote=False)
    code_tokens: list[str] = []

    def preserve_code(match: re.Match[str]) -> str:
        code_tokens.append(f"<code>{match.group(1)}</code>")
        return f"@@CODE{len(code_tokens) - 1}@@"

    text = re.sub(r"`([^`]+)`", preserve_code, text)

    def render_link(match: re.Match[str]) -> str:
        label = match.group(1)
        url = html.unescape(match.group(2))
        target = output_target(source, destination, url) if not re.match(r"^(?:https?:|mailto:|#)", url) else url
        safe_target = html.escape(target, quote=True)
        external = ' target="_blank" rel="noopener noreferrer"' if target.startswith(("https://", "http://")) else ""
        return f'<a href="{safe_target}"{external}>{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", render_link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    for index, value in enumerate(code_tokens):
        text = text.replace(f"@@CODE{index}@@", value)
    return text


def inline_markup(value: str) -> str:
    escaped = html.escape(value)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)


def is_table_divider(line: str) -> bool:
    return bool(re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line)) and "-" in line


def render_table(lines: list[str], source: Path, destination: Path) -> str:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    head = "".join(f"<th>{inline(cell, source, destination)}</th>" for cell in rows[0])
    body = []
    for row in rows[1:]:
        cells = "".join(f"<td>{inline(cell, source, destination)}</td>" for cell in row)
        body.append(f"<tr>{cells}</tr>")
    return '<div class="table-wrap"><table><thead><tr>' + head + "</tr></thead><tbody>" + "".join(body) + "</tbody></table></div>"


def markdown_to_html(markdown: str, source: Path, destination: Path) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    index = 0

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{inline(' '.join(part.strip() for part in paragraph), source, destination)}</p>")
            paragraph.clear()

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            flush_paragraph()
            index += 1
            continue

        fence = re.match(r"^\s*```([\w+-]*)\s*$", line)
        if fence:
            flush_paragraph()
            language = fence.group(1)
            index += 1
            code = []
            while index < len(lines) and not re.match(r"^\s*```\s*$", lines[index]):
                code.append(lines[index])
                index += 1
            class_name = f' class="language-{html.escape(language, quote=True)}"' if language else ""
            output.append(f"<pre><code{class_name}>{html.escape(chr(10).join(code))}</code></pre>")
            index += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            output.append(f"<h{level}>{inline(heading.group(2), source, destination)}</h{level}>")
            index += 1
            continue

        if line.lstrip().startswith("|"):
            flush_paragraph()
            table_lines = []
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                if not is_table_divider(lines[index]):
                    table_lines.append(lines[index])
                index += 1
            if len(table_lines) > 1:
                output.append(render_table(table_lines, source, destination))
            continue

        if re.match(r"^\s*>\s?", line):
            flush_paragraph()
            quote_lines = []
            while index < len(lines) and re.match(r"^\s*>\s?", lines[index]):
                quote_lines.append(re.sub(r"^\s*>\s?", "", lines[index]))
                index += 1
            quote_content = markdown_to_html("\n".join(quote_lines), source, destination)
            output.append(f"<blockquote>{quote_content}</blockquote>")
            continue

        list_match = re.match(r"^\s*(?:([-*+])|(\d+)\.)\s+(.+)$", line)
        if list_match:
            flush_paragraph()
            ordered = list_match.group(2) is not None
            tag = "ol" if ordered else "ul"
            items = []
            while index < len(lines):
                item_match = re.match(r"^\s*(?:([-*+])|(\d+)\.)\s+(.+)$", lines[index])
                if not item_match or (item_match.group(2) is not None) != ordered:
                    break
                items.append(f"<li>{inline(item_match.group(3), source, destination)}</li>")
                index += 1
            output.append(f"<{tag}>{''.join(items)}</{tag}>")
            continue

        if re.match(r"^\s*(?:---+|___+|\*\*\*+)\s*$", line):
            flush_paragraph()
            output.append("<hr>")
            index += 1
            continue

        paragraph.append(line)
        index += 1

    flush_paragraph()
    return "\n".join(output)


def relative_link(destination: Path, target: Path) -> str:
    return Path(__import__("os").path.relpath(target, destination.parent)).as_posix()


def shell_header(destination: Path) -> str:
    root_index = ROOT / "index.html"
    root_summary = ROOT / "resumo.html"
    css = relative_link(destination, ROOT / "site.css")
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#123b70">
  <link rel="stylesheet" href="{css}">
"""


def write_html(destination: Path, content: str) -> None:
    normalized = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    destination.write_text(normalized, encoding="utf-8")


def page_shell(destination: Path, title: str, content: str, description: str = "") -> str:
    description_meta = html.escape(description[:155], quote=True)
    header = shell_header(destination)
    index_href = relative_link(destination, ROOT / "index.html")
    summary_href = relative_link(destination, ROOT / "resumo.html")
    exams_href = relative_link(destination, ROOT / "exames.html")
    beginner_href = relative_link(destination, ROOT / "trilha-iniciante.html")
    glossary_href = relative_link(destination, ROOT / "glossario.html")
    quiz_href = relative_link(destination, ROOT / "quiz.html")
    return f"""{header}  <title>{html.escape(title)} | Guia de estudos OCJP</title>
  <meta name="description" content="{description_meta}">
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="{index_href}">Java SE 17 <span aria-hidden="true">·</span> Guia OCJP</a>
      <nav class="site-nav" aria-label="Navegação principal">
        <a href="{index_href}">Índice</a>
        <a href="{summary_href}">Resumo</a>
        <a href="{beginner_href}">Começar</a>
        <a href="{quiz_href}">Quiz</a>
        <a href="{exams_href}">Comparar exames</a>
        <a href="{glossary_href}">Glossário</a>
      </nav>
    </div>
  </header>
  <nav class="exam-strip" aria-label="Comparação entre exames">
    <span>Compare:</span>
    <a href="{exams_href}#1z0-808">1Z0-808 · Java 8</a>
    <a href="{exams_href}#1z0-829">1Z0-829 · Java 17</a>
    <a href="{exams_href}#1z0-830">1Z0-830 · Java 21</a>
  </nav>
  <div class="page-shell">
    <main class="content-card">
{content}
    </main>
  </div>
  <footer class="site-footer">Guia independente de estudos para a certificação Java SE 17 Developer · Exame 1Z0-829</footer>
</body>
</html>
"""


def hero(title: str, description: str, eyebrow: str, badges: list[str], actions: str = "") -> str:
    badge_html = "".join(f'<li class="badge">{html.escape(item)}</li>' for item in badges)
    title_html = inline_markup(title)
    description_html = inline_markup(description)
    return f"""      <div class="hero">
        <div class="hero-content">
          <p class="eyebrow">{html.escape(eyebrow)}</p>
          <h1>{title_html}</h1>
          <p class="hero-description">{description_html}</p>
          <ul class="badges" aria-label="Detalhes do conteúdo">{badge_html}</ul>
          {actions}
        </div>
      </div>"""


def article(content: str) -> str:
    return f'      <article class="markdown-body">\n{content}\n      </article>'


def progress_checkbox(identifier: str, label: str) -> str:
    return (
        f'<label class="progress-check"><input type="checkbox" data-progress-id="{html.escape(identifier, quote=True)}" '
        f'aria-label="{html.escape(label, quote=True)}"><span class="sr-only">{html.escape(label)}</span></label>'
    )


def chapter_data(directory: Path) -> tuple[str, str, list[Path]]:
    source = directory / "README.md"
    markdown = source.read_text(encoding="utf-8")
    title = page_title(markdown, directory.name)
    description = first_paragraph(markdown)
    if not description:
        description = f"Conteúdos de estudo do domínio {title}, organizados em assuntos e objetivos de revisão."
    topics = []
    for _, target in re.findall(r"\[([^\]]+)\]\(([^)]+\.md)(?:#[^)]*)?\)", markdown):
        candidate = (directory / target).resolve()
        if candidate.parent == directory.resolve() and candidate.name.lower() != "readme.md":
            if candidate.exists() and candidate not in topics:
                topics.append(candidate)
    remaining = sorted(path for path in directory.glob("*.md") if path.name.lower() != "readme.md")
    topics.extend(path for path in remaining if path not in topics)
    return title, description, topics


def related_topic_links(source: Path, destination: Path) -> str:
    links = []
    for slug in CROSS_REFERENCES.get(source.stem, []):
        target = next(
            (directory / f"{slug}.md" for directory in CHAPTER_DIRS if (directory / f"{slug}.md").exists()),
            None,
        )
        if target:
            title = page_title(target.read_text(encoding="utf-8"), target.stem.replace("-", " ").title())
            href = relative_link(destination, target.with_suffix(".html"))
            links.append(f'<a class="related-link" href="{href}">{inline_markup(title)} <span aria-hidden="true">→</span></a>')
    if not links:
        return ""
    return f'<section class="related-topics"><h2>Conecte com outros assuntos</h2><div class="related-grid">{"".join(links)}</div></section>'


def study_path_hint(source: Path, destination: Path) -> str:
    ordered_slugs = [slug for _, _, slugs in BEGINNER_STAGES for slug in slugs]
    if source.stem in ordered_slugs:
        index = ordered_slugs.index(source.stem)
        if index:
            previous = next(
                directory / f"{ordered_slugs[index - 1]}.md"
                for directory in CHAPTER_DIRS
                if (directory / f"{ordered_slugs[index - 1]}.md").exists()
            )
            previous_title = page_title(previous.read_text(encoding="utf-8"), previous.stem)
            previous_step = f'<a href="{relative_link(destination, previous.with_suffix(".html"))}">{inline_markup(previous_title)}</a>'
        else:
            previous_step = f'<a href="{relative_link(destination, ROOT / "trilha-iniciante.html")}#fundamentos">Fundamentos iniciais</a>'

        if index + 1 < len(ordered_slugs):
            following = next(
                directory / f"{ordered_slugs[index + 1]}.md"
                for directory in CHAPTER_DIRS
                if (directory / f"{ordered_slugs[index + 1]}.md").exists()
            )
            following_title = page_title(following.read_text(encoding="utf-8"), following.stem)
            next_topic = f'<a href="{relative_link(destination, following.with_suffix(".html"))}">{inline_markup(following_title)}</a>'
        else:
            next_topic = f'<a href="{relative_link(destination, ROOT / "trilha-iniciante.html")}#projeto">Projeto incremental</a>'
    else:
        previous_step = f'<a href="{relative_link(destination, ROOT / "trilha-iniciante.html")}#fundamentos">Fundamentos para iniciantes</a>'
        related = CROSS_REFERENCES.get(source.stem, [])
        target = next(
            (directory / f"{related[0]}.md" for directory in CHAPTER_DIRS if related and (directory / f"{related[0]}.md").exists()),
            None,
        )
        if target:
            next_title = page_title(target.read_text(encoding="utf-8"), target.stem)
            next_topic = f'<a href="{relative_link(destination, target.with_suffix(".html"))}">{inline_markup(next_title)}</a>'
        else:
            next_topic = f'<a href="{relative_link(destination, ROOT / "index.html")}">Índice de assuntos</a>'

    return f'<p class="study-meta"><strong>Etapa anterior sugerida:</strong> {previous_step}<br><strong>Próximo recomendado:</strong> {next_topic}</p>'


def learning_guide(source: Path, destination: Path, topic_title: str) -> str:
    objective, question, answer = LEARNING_GUIDES[source.stem]
    practice_task = PRACTICE_TASKS[source.stem]
    source_dir = ROOT / "src" / source.parent.name / source.stem
    java_files = sorted(source_dir.glob("*.java")) if source_dir.exists() else []
    example_html = ""
    if java_files:
        java_source = java_files[0]
        source_href = relative_link(destination, java_source)
        source_path = java_source.relative_to(ROOT).as_posix()
        run_instructions = (
            "Este exemplo JDBC também precisa de uma URL de conexão e do driver do banco no classpath."
            if source.parent.name == "10-jdbc"
            else "A execução imprime o resultado no console para você comparar com sua previsão."
        )
        code = html.escape(java_source.read_text(encoding="utf-8"))
        example_html = f"""<section class="example-panel">
          <div class="example-heading"><div><p class="eyebrow-dark">EXEMPLO DE CONSOLE</p><h2>Veja a regra em execução</h2></div><a class="button-link" href="{source_href}" target="_blank" rel="noopener noreferrer">Abrir arquivo Java ↗</a></div>
          <p>Antes de executar, anote sua previsão. Compile o exemplo com o JDK e compare a saída observada com as regras deste assunto.</p>
          <details class="run-command"><summary>Comandos para compilar e executar</summary><pre><code>javac -d target/bin {html.escape(source_path)}
java -cp target/bin {html.escape(java_source.stem)}</code></pre><p>{html.escape(run_instructions)}</p></details>
          <details class="source-code"><summary>Consultar código-fonte: {html.escape(java_source.name)}</summary><pre><code class="language-java">{code}</code></pre></details>
        </section>"""

    beginner_slugs = {slug for _, _, slugs in BEGINNER_STAGES for slug in slugs}
    study_mode = (
        '<p class="study-mode"><strong>Primeiro contato:</strong> aprenda o conceito e pratique antes de consultar os detalhes de prova. '
        f'<a href="{relative_link(destination, ROOT / "trilha-iniciante.html")}#fundamentos">Voltar aos fundamentos</a> se algum termo ainda for novo.</p>'
        if source.stem in beginner_slugs
        else '<p class="study-mode"><strong>Aprofundamento e revisão 1Z0-829:</strong> use esta página depois dos fundamentos. Os tópicos de prova complementam a trilha inicial e não são pré-requisitos para começar a programar.</p>'
    )
    setup_note = {
        "sistema-de-modulos-jpms": "Aprofundamento opcional: experimente este assunto depois de compilar classes Java comuns; a prática modular usa diretórios e comandos de compilação próprios.",
        "conexoes-e-comandos": "Aprofundamento opcional: para executar a prática JDBC, configure um banco de teste, uma URL de conexão e o driver JDBC; não é necessário para concluir a trilha inicial.",
    }.get(source.stem, "")
    setup_html = f'<p class="setup-note">{html.escape(setup_note)}</p>' if setup_note else ""

    return f"""<section class="learning-guide">
        <div class="learning-objective"><span>OBJETIVO DE APRENDIZAGEM</span><p>{inline_markup(objective)}</p></div>
        {study_mode}
        {setup_html}
        <p class="study-meta"><strong>Ritmo sugerido:</strong> 20–30 minutos · leia, execute o exemplo e tente a atividade antes de consultar referências.</p>
        {study_path_hint(source, destination)}
        <ol class="lesson-routine" aria-label="Roteiro da microaula">
          <li>Leia o objetivo e localize a ideia principal no conteúdo abaixo.</li>
          <li>Preveja o resultado, compile e execute o exemplo.</li>
          <li>Faça a atividade sem copiar a solução e confira a checagem comentada.</li>
        </ol>
        {example_html}
        <section class="practice-task">
          <p class="eyebrow-dark">PRATIQUE AGORA</p>
          <h2>Faça uma pequena alteração por conta própria</h2>
          <p>{inline_markup(practice_task)}</p>
          <p class="task-check">Concluído quando: o programa compilar, produzir o resultado esperado e você conseguir explicar a regra aplicada.</p>
        </section>
        <section class="quick-check">
          <p class="eyebrow-dark">CHECAGEM RÁPIDA · {inline_markup(topic_title)}</p>
          <h2>{inline_markup(question)}</h2>
          <details class="answer-key"><summary>Conferir resposta comentada</summary><p>{inline_markup(answer)}</p></details>
        </section>
        <p class="glossary-link"><a href="{relative_link(destination, ROOT / "glossario.html")}">Consulte o glossário de termos Java ↗</a></p>
      </section>"""


def chapter_exam_callout(directory: Path, destination: Path) -> str:
    notes = CHAPTER_EXAM_NOTES[directory.name]
    rows = []
    for code, label, note in zip(
        ("1Z0-808", "1Z0-829", "1Z0-830"),
        ("Java 8", "Java 17", "Java 21"),
        notes,
    ):
        rows.append(
            f'<div class="exam-fit"><span class="exam-version">{code} · {label}</span><p>{html.escape(note)}</p></div>'
        )
    return f"""<section class="chapter-exam-fit">
        <h2>Como este capítulo se relaciona com cada exame</h2>
        <div class="exam-fit-grid">{"".join(rows)}</div>
        <p class="matrix-note">Orientação editorial sobre reaproveitamento do material; não representa objetivos oficiais nem garante cobertura do exame. Consulte o <a href="{relative_link(destination, ROOT / "exames.html")}">comparativo e as fontes da Oracle</a>.</p>
      </section>"""


def generate_topic_pages() -> int:
    total = 0
    chapter_pages = []
    beginner_slugs = {slug for _, _, slugs in BEGINNER_STAGES for slug in slugs}
    for chapter_number, directory in enumerate(CHAPTER_DIRS, start=1):
        title, description, topics = chapter_data(directory)
        topic_links = []
        for topic_index, source in enumerate(topics):
            markdown = source.read_text(encoding="utf-8")
            topic_title = page_title(markdown, source.stem.replace("-", " ").title())
            destination = source.with_suffix(".html")
            topic_description = first_paragraph(markdown)
            if topic_description == topic_title:
                topic_description = ""
            if not topic_description:
                topic_description = first_study_item(markdown)
            if not topic_description:
                topic_description = f"Assunto do domínio {title}, com tópicos para estudo, prática e revisão."
            body_markdown = re.sub(r"^#\s+.+(?:\n|$)", "", markdown, count=1)
            rendered = markdown_to_html(body_markdown, source, destination)

            map_source = source.with_suffix(".svg")
            map_html = ""
            if map_source.exists():
                map_href = relative_link(destination, map_source)
                map_html = f"""<a class="map-link" href="{map_href}">
          <img src="{map_href}" alt="Miniatura do mapa mental: {html.escape(topic_title, quote=True)}">
          <span>Ver mapa mental deste assunto</span>
        </a>"""

            previous = source.with_name(topics[topic_index - 1].stem + ".html") if topic_index > 0 else directory / "index.html"
            next_page = source.with_name(topics[topic_index + 1].stem + ".html") if topic_index + 1 < len(topics) else None
            chapter_index = directory / "index.html"
            nav = f"""<nav class="chapter-nav" aria-label="Navegação entre assuntos">
          <a href="{relative_link(destination, previous)}">← {"Assunto anterior" if topic_index > 0 else "Capítulo"}</a>
          {"<a href='" + relative_link(destination, next_page) + "'>Próximo assunto →</a>" if next_page else '<a href="' + relative_link(destination, chapter_index) + '">Voltar ao capítulo →</a>'}
        </nav>"""

            study_level = "Fundamento essencial" if source.stem in beginner_slugs else "Aprofundamento"
            content = hero(topic_title, topic_description, f"Capítulo {chapter_number:02d} · {title}", [study_level, "Base: Java 17", "1Z0-829"])
            content += "\n" + article(
                map_html
                + "\n"
                + learning_guide(source, destination, topic_title)
                + "\n"
                + rendered
                + "\n"
                + chapter_exam_callout(directory, destination)
                + "\n"
                + related_topic_links(source, destination)
                + "\n"
                + nav
            )
            write_html(destination, page_shell(destination, topic_title, content, topic_description))
            topic_links.append((topic_title, destination, topic_description))
            total += 1

        card_items = "".join(
            f'<a class="topic-card" href="{relative_link(directory / "index.html", page)}"><h3>{html.escape(topic_title)}</h3><span>{html.escape(topic_description)}</span></a>'
            for topic_title, page, topic_description in topic_links
        )
        map_source = next((path for path in (directory / f"{directory.name}.svg", directory / "mapa-mental-revisao.svg") if path.exists()), None)
        map_html = ""
        if map_source:
            map_href = relative_link(directory / "index.html", map_source)
            map_html = f'<a class="map-link" href="{map_href}"><img src="{map_href}" alt="Miniatura do mapa mental do capítulo {chapter_number:02d}: {html.escape(title, quote=True)}"><span>Abrir mapa mental do capítulo</span></a>'
        chapter_content = hero(title, description, f"Capítulo {chapter_number:02d} · Roteiro OCJP", [f"{len(topics)} assuntos", "Base: Java 17", "1Z0-829"])
        milestone = CHAPTER_MILESTONES[directory.name]
        chapter_article = f"""<p>Escolha um assunto para abrir as notas de estudo. Os mapas mentais complementam o conteúdo como material de revisão.</p>
        {map_html}
        <section class="chapter-milestone"><p class="eyebrow-dark">MARCO DE CONCLUSÃO</p><p>{inline_markup(milestone)}</p></section>
        {chapter_exam_callout(directory, directory / "index.html")}
        <div class="topic-cards">{card_items}</div>
        <p><a href="{relative_link(directory / "index.html", ROOT / "index.html")}">← Voltar ao índice geral</a></p>"""
        chapter_content += "\n" + article(chapter_article)
        destination = directory / "index.html"
        write_html(destination, page_shell(destination, title, chapter_content, description))
        chapter_pages.append((chapter_number, title, description, destination, topic_links))
    return total, chapter_pages


def generate_index(chapters: list[tuple]) -> None:
    chapter_cards = []
    topic_count = sum(len(chapter[4]) for chapter in chapters)
    for number, title, description, destination, topics in chapters:
        topic_links = "".join(
            f'<li><a href="{relative_link(ROOT / "index.html", topic_page)}">{html.escape(topic_title)}</a></li>'
            for topic_title, topic_page, _ in topics
        )
        chapter_cards.append(
            f"""<section class="chapter-card" id="capitulo-{number:02d}">
          <div class="chapter-topline"><span class="chapter-number">CAPÍTULO {number:02d}</span><h3><a href="{relative_link(ROOT / "index.html", destination)}">{inline_markup(title)}</a></h3></div>
          <p>{inline_markup(description)}</p>
          <details class="chapter-details">
            <summary>Ver {len(topics)} assuntos</summary>
            <ul class="topic-list">{topic_links}</ul>
          </details>
        </section>"""
        )
    actions = '<div class="hero-actions"><a href="trilha-iniciante.html">Começar do zero</a><a href="quiz.html">Fazer quiz</a><a href="#capitulos">Explorar capítulos</a></div>'
    content = hero(
        "Seu roteiro de estudos Java SE 17",
        "Um portal organizado para revisar os objetivos da certificação Oracle Certified Professional: Java SE 17 Developer (1Z0-829), com notas, mapas mentais e exemplos.",
        "Guia de estudos · OCJP",
        [f"{len(chapters)} capítulos", "Java SE 17", f"{topic_count} assuntos"],
        actions,
    )
    content += "\n" + article(
        '<section class="beginner-callout"><div><strong>Está começando em Java?</strong><span>Aprenda a compilar, executar, ler entradas e usar variáveis antes dos capítulos de certificação.</span></div><a href="trilha-iniciante.html#fundamentos">Começar pelos fundamentos →</a></section>'
        '<p class="glossary-link"><a href="glossario.html">Consultar glossário de termos Java ↗</a> · <a href="quiz.html">Praticar com quiz de 12 perguntas ↗</a></p>'
        '<section class="exam-callout"><div><strong>Este material tem como base a 1Z0-829 (Java SE 17).</strong><span>A 1Z0-808 é uma prova de fundamentos para Java 8; a 1Z0-830 é profissional, para Java 21. Compare versões, nível e escopo antes de escolher seu roteiro.</span></div><a href="exames.html#matriz">Ver matriz de estudo →</a></section>'
        '<h2 id="capitulos">Roteiro por capítulo</h2>'
        '<p>Abra um capítulo para consultar a visão geral ou expanda a lista para acessar diretamente cada assunto.</p>'
        f'<div class="chapter-grid">{"".join(chapter_cards)}</div>'
        '<blockquote><p>Material independente de estudo. Consulte os objetivos e as condições atuais do exame na <a href="https://education.oracle.com/java-se-17-developer/pexam_1Z0-829">página oficial da Oracle</a>.</p></blockquote>'
    )
    write_html(
        ROOT / "index.html",
        page_shell(ROOT / "index.html", "Índice", content, "Portal estático de estudos para a certificação Oracle Java SE 17 Developer."),
    )


def generate_beginner_guide(chapters: list[tuple]) -> None:
    topics = {
        page.stem: (title, page, description)
        for _, _, _, _, chapter_topics in chapters
        for title, page, description in chapter_topics
    }
    beginner_topic_count = sum(len(stage[2]) for stage in BEGINNER_STAGES)
    stage_sections = []
    for stage_title, stage_description, slugs in BEGINNER_STAGES:
        items = []
        for index, slug in enumerate(slugs, start=1):
            title, page, description = topics[slug]
            items.append(
                f'<li><span class="step-number">{index:02d}</span><div><a href="{relative_link(ROOT / "trilha-iniciante.html", page)}">{inline_markup(title)}</a><p>{inline_markup(description)}</p></div>{progress_checkbox(f"topic-{slug}", f"Marcar {title} como concluído")}</li>'
            )
        stage_sections.append(
            f"""<section class="learning-stage">
          <h3>{html.escape(stage_title)}</h3>
          <p>{html.escape(stage_description)}</p>
          <ol class="learning-steps">{"".join(items)}</ol>
          <p class="stage-completion"><strong>Marco:</strong> explique um conceito sem copiar e faça uma pequena alteração no exemplo.</p>
        </section>"""
        )

    project_milestones = [
        ("1. Capturar e mostrar uma tarefa", "Leia uma descrição com `Scanner` e mostre uma confirmação. Esta primeira versão deve compilar e funcionar sem classes adicionais.", "Entrada: estudar Java. Saída esperada: Tarefa adicionada: estudar Java.", ["tipos-primitivos-e-wrappers", "texto-string-e-stringbuilder"]),
        ("2. Guardar várias tarefas", "Troque a variável única por `ArrayList<String>`. Permita adicionar mais de uma tarefa e listar todas com um laço.", "Adicione duas tarefas; ao listar, as duas aparecem na ordem de inclusão.", ["arrays", "interfaces-e-colecoes", "lacos-e-desvios"]),
        ("3. Criar um menu", "Adicione opções para incluir, listar e sair. Separe ações em métodos e repita o menu até a opção de saída.", "Escolha sair: o programa termina sem imprimir o menu novamente.", ["metodos-sobrecarga-e-varargs", "condicionais-e-switch", "lacos-e-desvios"]),
        ("4. Modelar cada tarefa", "Substitua `String` por uma classe `Tarefa`, com descrição e estado concluído encapsulados.", "Crie uma tarefa e consulte a descrição e o estado por métodos públicos.", ["classes-objetos-e-encapsulamento", "construtores-e-inicializacao"]),
        ("5. Concluir e validar", "Permita concluir uma tarefa pela posição. Verifique a posição antes de acessar a lista e mostre uma mensagem se não for válida.", "Teste a primeira posição, a última posição e uma posição inexistente; nenhuma entrada inválida deve encerrar o programa.", ["condicionais-e-switch", "hierarquia-e-tipos-de-excecao"]),
        ("6. Salvar em arquivo (opcional)", "Quando as etapas anteriores estiverem funcionando, grave e carregue as tarefas em arquivo local com recursos fechados corretamente.", "Feche e reabra o programa: as tarefas salvas continuam disponíveis.", ["nio2-path-e-files", "try-with-resources"]),
    ]
    milestone_sections = []
    for index, (title, description, expected, slugs) in enumerate(project_milestones, start=1):
        links = " · ".join(
            f'<a href="{relative_link(ROOT / "trilha-iniciante.html", topics[slug][1])}">{html.escape(topics[slug][0])}</a>'
            for slug in slugs
        )
        starter_link = ' · <a href="src/java_Basico/ListaTarefas.java">Abrir código inicial</a>' if index == 1 else ""
        milestone_sections.append(
            f'<li><div class="project-milestone-heading"><strong>{html.escape(title)}</strong>{progress_checkbox(f"project-{index}", f"Marcar etapa {index} como concluída")}</div><p>{inline_markup(description)}</p><p class="project-expected"><strong>Teste de conclusão:</strong> {inline_markup(expected)}</p><span>Revise: {links}{starter_link}</span></li>'
        )

    foundation_source = ROOT / "src" / "java_Basico" / "FundamentosJava.java"
    foundation_code = html.escape(foundation_source.read_text(encoding="utf-8"))
    foundation_path = foundation_source.relative_to(ROOT).as_posix()
    project_starter = ROOT / "src" / "java_Basico" / "ListaTarefas.java"
    project_starter_code = html.escape(project_starter.read_text(encoding="utf-8"))
    project_starter_path = project_starter.relative_to(ROOT).as_posix()
    progress_script = """<script>
      (() => {
        const key = "ocjp-study-progress-v1";
        const status = document.getElementById("progress-status");
        const controls = [...document.querySelectorAll("[data-progress-id]")];
        const clearButton = document.getElementById("clear-progress");
        let saved;
        try {
          saved = JSON.parse(localStorage.getItem(key) || "{}");
          if (!saved || typeof saved !== "object" || Array.isArray(saved)) saved = {};
        } catch (error) {
          status.textContent = "O navegador não permitiu acessar o armazenamento local; as marcações não serão salvas.";
          controls.forEach((control) => { control.disabled = true; });
          clearButton.disabled = true;
          return;
        }
        const updateStatus = () => {
          const completed = controls.filter((control) => control.checked).length;
          status.textContent = `${completed} de ${controls.length} etapas marcadas como concluídas neste navegador.`;
        };
        controls.forEach((control) => {
          control.checked = saved[control.dataset.progressId] === true;
          control.addEventListener("change", () => {
            saved[control.dataset.progressId] = control.checked;
            try {
              localStorage.setItem(key, JSON.stringify(saved));
              updateStatus();
            } catch (error) {
              status.textContent = "Não foi possível salvar o progresso; libere espaço ou habilite o armazenamento local.";
            }
          });
        });
        clearButton.addEventListener("click", () => {
          try {
            localStorage.removeItem(key);
            saved = {};
            controls.forEach((control) => { control.checked = false; });
            status.textContent = "Progresso apagado.";
          } catch (error) {
            status.textContent = "Não foi possível apagar o progresso salvo.";
          }
        });
        updateStatus();
      })();
      </script>"""

    body = f"""<section class="beginner-callout"><div><strong>Como usar esta trilha</strong><span>Comece pelos fundamentos, estude na ordem e escreva o código você mesmo. A trilha complementa, mas não substitui, o roteiro completo da certificação.</span></div><a href="index.html">Ver roteiro 1Z0-829 →</a></section>
        <section class="progress-tools" aria-label="Progresso da trilha">
          <p id="progress-status" role="status" aria-live="polite">Carregando seu progresso...</p>
          <button class="progress-clear" id="clear-progress" type="button">Limpar progresso salvo</button>
        </section>
        <h2 id="fundamentos">Fundamentos antes da trilha</h2>
        <p>Se esta é sua primeira experiência com Java, faça esta aula antes de estudar tipos e operadores. Você vai escrever um programa que lê uma resposta, guarda valores em variáveis e mostra um resultado.</p>
        <ol class="foundation-objectives">
          <li>Identificar a classe e o método <code>main</code> que iniciam um programa.</li>
          <li>Declarar variáveis, atribuir valores e usar tipos como <code>String</code> e <code>int</code>.</li>
          <li>Exibir mensagens, ler texto pelo console, compilar com <code>javac</code> e executar com <code>java</code>.</li>
        </ol>
        <h2>Prepare o ambiente</h2>
        <ol>
          <li>Instale um JDK 17 e abra um terminal na pasta em que vai praticar.</li>
          <li>Confirme a instalação executando <code>java -version</code> e <code>javac -version</code>.</li>
        </ol>
        <p>Se o terminal não reconhecer <code>java</code> ou <code>javac</code>, revise a instalação e a configuração do PATH do sistema antes de avançar.</p>
        <h3>Seu primeiro programa com variáveis e entrada</h3>
        <p>Abra o arquivo <a href="src/java_Basico/FundamentosJava.java"><code>FundamentosJava.java</code></a>. Ele contém o programa completo; o nome do arquivo corresponde à classe pública. A variável <code>nome</code> guarda texto, <code>idade</code> guarda um inteiro, e a atribuição guarda em <code>proximaIdade</code> o resultado de uma expressão.</p>
        <details class="source-code" open><summary>Exemplo completo</summary><pre><code class="language-java">{foundation_code}</code></pre></details>
        <p>No PowerShell, compile e execute a partir da raiz do repositório:</p>
        <pre><code>New-Item -ItemType Directory -Force target\\bin | Out-Null
javac -d target\\bin {html.escape(foundation_path)}
java -cp target\\bin FundamentosJava</code></pre>
        <p>No macOS/Linux, use o terminal:</p>
        <pre><code>mkdir -p target/bin
javac -d target/bin {html.escape(foundation_path)}
java -cp target/bin FundamentosJava</code></pre>
        <p>Digite <code>Ana</code> e depois <code>20</code>. A saída esperada será:</p>
        <pre><code>Qual é seu nome?
Qual é sua idade?
Olá, Ana! No próximo ano você terá 21.</code></pre>
        <p><code>System.out.print</code> mantém o cursor na mesma linha; <code>System.out.println</code> termina a linha. <code>Scanner.nextLine</code> lê o nome digitado. O método <code>main</code> é o ponto de entrada; <code>javac</code> compila o arquivo e <code>java</code> executa a classe compilada.</p>
        <section class="practice-task">
          <p class="eyebrow-dark">PRATIQUE AGORA</p>
          <h3>Faça uma alteração e teste</h3>
          <p>Troque a pergunta para “Qual linguagem você está aprendendo?” e imprima uma segunda confirmação. Depois informe outros valores e verifique a saída.</p>
          <p class="task-check">Concluído quando: o arquivo compilar, ler as duas entradas e imprimir uma resposta com o valor informado.</p>
        </section>
        <section class="quick-check">
          <p class="eyebrow-dark">CHECAGEM RÁPIDA</p>
          <h3>O que a variável <code>idade</code> guarda depois de <code>int idade = 20;</code>?</h3>
          <details class="answer-key"><summary>Conferir resposta comentada</summary><p>Guarda o valor inteiro <code>20</code>. A declaração cria a variável e a atribuição inicializa seu valor; em Java, variáveis locais precisam receber valor antes do uso.</p></details>
        </section>
        <aside class="beginner-callout"><div><strong>Erro comum</strong><span>Se o compilador disser que a classe pública deve estar em outro arquivo, confira se o nome é exatamente <code>FundamentosJava.java</code>. Java diferencia maiúsculas de minúsculas.</span></div></aside>
        <h2>Erros comuns no começo</h2>
        <div class="table-wrap"><table><thead><tr><th>Mensagem</th><th>Causa comum</th><th>O que conferir</th></tr></thead><tbody>
          <tr><td><code>error: cannot find symbol</code></td><td>Nome de variável, método ou classe digitado de forma diferente, ou símbolo fora do escopo.</td><td>Confira maiúsculas/minúsculas, grafia e onde o símbolo foi declarado.</td></tr>
          <tr><td><code>class OlaJava is public, should be declared in a file named OlaJava.java</code></td><td>O nome do arquivo não corresponde ao nome da classe pública.</td><td>Salve a classe pública <code>OlaJava</code> no arquivo <code>OlaJava.java</code>.</td></tr>
          <tr><td><code>error: ';' expected</code></td><td>Uma instrução está sem ponto e vírgula ou há um erro de sintaxe próximo.</td><td>Confira o fim da instrução e a linha indicada pelo compilador.</td></tr>
          <tr><td><code>NullPointerException</code></td><td>O programa tentou usar uma referência que está <code>null</code>.</td><td>Verifique onde o objeto deveria ser criado e trate o caso ausente antes de chamar métodos.</td></tr>
        </tbody></table></div>
        <h2>Trilha passo a passo</h2>
        <p>Os capítulos completos continuam organizados por domínio do exame; aqui os fundamentos essenciais vêm primeiro e os assuntos estão reordenados por dependência. Os detalhes de prova ficam para a seção de aprofundamento.</p>
        <div class="learning-stages">{"".join(stage_sections)}</div>
        <h2 id="projeto">Projeto incremental: lista de tarefas</h2>
        <p>Construa uma aplicação de console sem frameworks. Cada checkpoint parte do anterior e precisa compilar antes de avançar. Salvar em arquivo é uma etapa opcional de aprofundamento.</p>
        <section class="project-starter">
          <h3>Ponto de partida compilável</h3>
          <p>O primeiro checkpoint já tem uma versão mínima executável. Abra <a href="src/java_Basico/ListaTarefas.java"><code>ListaTarefas.java</code></a>, compile, execute e digite uma descrição antes de fazer alterações.</p>
          <details class="source-code"><summary>Ver código inicial</summary><pre><code class="language-java">{project_starter_code}</code></pre></details>
          <p>No PowerShell, crie a pasta de saída e execute o programa:</p>
          <pre><code>New-Item -ItemType Directory -Force target\\bin | Out-Null
javac -d target\\bin {html.escape(project_starter_path)}
java -cp target\\bin ListaTarefas</code></pre>
          <p>Digite <code>estudar Java</code>. A saída esperada é:</p>
          <pre><code>Digite uma tarefa:
Tarefa adicionada: estudar Java</code></pre>
        </section>
        <ol class="project-milestones">{"".join(milestone_sections)}</ol>
        <h2>Como saber se pode avançar</h2>
        <ul>
          <li>Consegue explicar o objetivo do código com suas próprias palavras.</li>
          <li>Compila e executa o exemplo sem copiar uma solução completa.</li>
          <li>Consegue alterar uma entrada e prever como o resultado muda.</li>
          <li>Resolveu o marco da etapa; anote dúvidas e retorne ao assunto se precisar consultar a resposta toda vez.</li>
        </ul>
        <p>O glossário explica os termos usados nas páginas; quando estiver confortável com os fundamentos, use o <a href="index.html">índice completo</a> e consulte os tópicos de revisão para o exame.</p>
        {progress_script}"""
    content = hero(
        "Comece a programar em Java",
        "Uma sequência prática para quem está começando, com ambiente, conceitos essenciais e um projeto que cresce junto com os estudos.",
        "Trilha para iniciantes · Java SE 17",
        ["Fundamentos + 4 etapas", f"{beginner_topic_count} assuntos", "20–30 min por assunto"],
    ) + "\n" + article(body)
    page = ROOT / "trilha-iniciante.html"
    write_html(
        page,
        page_shell(page, "Trilha para iniciantes", content, "Percurso progressivo para começar a programar em Java 17 e praticar com um projeto incremental."),
    )


def generate_glossary() -> None:
    entries = "".join(
        f'<div class="glossary-entry"><dt>{html.escape(term)}</dt><dd>{inline_markup(definition)}</dd></div>'
        for term, definition in GLOSSARY_ITEMS
    )
    body = f"""<p>Definições curtas dos termos que aparecem nas aulas. Use este glossário como apoio; cada página de assunto continua sendo a referência para as regras e exemplos completos.</p>
        <dl class="glossary-list">{entries}</dl>
        <p><a href="trilha-iniciante.html">← Voltar à trilha para iniciantes</a></p>"""
    content = hero(
        "Glossário de Java",
        "Termos essenciais explicados em linguagem direta para facilitar a leitura dos assuntos.",
        "Referência rápida · Java SE 17",
        [f"{len(GLOSSARY_ITEMS)} termos", "Definições breves"],
    ) + "\n" + article(body)
    page = ROOT / "glossario.html"
    write_html(
        page,
        page_shell(page, "Glossário Java", content, "Glossário breve de termos Java usados no guia de estudos."),
    )


def generate_quiz(chapters: list[tuple]) -> None:
    topics = {
        page.stem: title
        for _, _, _, _, chapter_topics in chapters
        for title, page, _ in chapter_topics
    }
    if set(QUIZ_BANK) != set(topics):
        missing = sorted(set(topics) - set(QUIZ_BANK))
        unknown = sorted(set(QUIZ_BANK) - set(topics))
        raise ValueError(f"Banco do quiz desalinhado. Sem questões: {missing}; temas desconhecidos: {unknown}")

    question_data = {}
    question_count = 0
    merged_bank = {
        slug: [*questions, *QUIZ_QUESTION_VARIANTS.get(slug, [])]
        for slug, questions in QUIZ_BANK.items()
    }
    if set(QUIZ_QUESTION_VARIANTS) - set(topics):
        raise ValueError(f"Variantes do quiz para temas desconhecidos: {sorted(set(QUIZ_QUESTION_VARIANTS) - set(topics))}")
    for slug, title in topics.items():
        levels = {"facil": [], "medio": [], "dificil": []}
        seen_prompts = set()
        for level, prompt, answer, distractors, explanation in merged_bank[slug]:
            if level not in {"facil", "medio", "dificil"}:
                raise ValueError(f"Nível inválido no tema {slug}: {level}")
            options = [answer, *distractors]
            if len(options) != 4 or len(set(options)) != 4:
                raise ValueError(f"A questão de {slug}/{level} precisa de quatro alternativas únicas")
            if prompt in seen_prompts:
                raise ValueError(f"Enunciado duplicado no tema {slug}: {prompt}")
            seen_prompts.add(prompt)
            levels[level].append({
                "prompt": prompt,
                "answer": answer,
                "distractors": distractors,
                "explanation": explanation,
            })
            question_count += 1
        if any(not questions for questions in levels.values()):
            raise ValueError(f"O tema {slug} precisa ter ao menos uma questão em cada nível")
        destination = next(page for _, _, _, _, chapter_topics in chapters for topic_title, page, _ in chapter_topics if page.stem == slug)
        question_data[slug] = {
            "title": title,
            "href": relative_link(ROOT / "quiz.html", destination),
            "levels": levels,
        }

    serialized_data = json.dumps(question_data, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    app_markup = f"""<div class="quiz-app" id="quiz-app">
        <section class="quiz-intro" id="quiz-intro">
          <div class="quiz-rules">
            <h2>Como funciona</h2>
            <ul>
              <li>Cada rodada tem exatamente <strong>12 perguntas</strong>, com quatro alternativas.</li>
              <li>Os temas são sorteados sem repetição dentro da mesma rodada; cada assunto tem um conjunto de questões nos três níveis.</li>
              <li>A primeira pergunta sempre é difícil. Se errar, a próxima passa para médio; erros mantêm o nível médio até acertar.</li>
              <li>Acertar no médio leva a uma pergunta difícil. Acertar no difícil leva a uma fácil; acertar na fácil leva a uma difícil.</li>
              <li>Ao terminar, você pode iniciar outra rodada com novos sorteios.</li>
            </ul>
          </div>
          <p class="quiz-bank-count">{question_count} questões no banco · {len(topics)} temas · cada rodada é uma amostra de estudo, não uma medida definitiva de domínio.</p>
          <button class="quiz-button quiz-button-primary" id="quiz-start" type="button">Começar rodada</button>
        </section>
        <section class="quiz-play" id="quiz-play" hidden>
          <div class="quiz-progress-heading"><span id="quiz-count"></span><span id="quiz-score"></span></div>
          <progress id="quiz-progress" value="0" max="12" aria-label="Progresso da rodada"></progress>
          <div class="quiz-question-meta"><span class="quiz-level" id="quiz-level"></span><span id="quiz-topic"></span></div>
          <h2 id="quiz-question"></h2>
          <div class="quiz-options" id="quiz-options"></div>
          <section class="quiz-feedback" id="quiz-feedback" aria-live="polite" hidden></section>
          <button class="quiz-button quiz-button-primary" id="quiz-next" type="button" hidden>Próxima pergunta</button>
        </section>
        <section class="quiz-result" id="quiz-result" aria-live="polite" hidden>
          <p class="eyebrow-dark">RODADA CONCLUÍDA</p>
          <h2>Resultado: <span id="quiz-final-score"></span> de 12</h2>
          <p id="quiz-result-message"></p>
          <section class="quiz-review" id="quiz-review" aria-labelledby="quiz-review-title" hidden>
            <h3 id="quiz-review-title">Assuntos para revisar nesta rodada</h3>
            <ul id="quiz-review-list"></ul>
          </section>
          <button class="quiz-button quiz-button-primary" id="quiz-restart" type="button">Jogar outra rodada</button>
        </section>
      </div>
      <script type="application/json" id="quiz-data">{serialized_data}</script>
      <script>
      (() => {{
        "use strict";
        const bank = JSON.parse(document.getElementById("quiz-data").textContent);
        const totalQuestions = 12;
        const labels = {{ facil: "Fácil", medio: "Médio", dificil: "Difícil" }};
        const state = {{ usedTopics: new Set(), missedTopics: new Set(), number: 0, score: 0, level: "dificil", current: null, locked: false }};
        const intro = document.getElementById("quiz-intro");
        const play = document.getElementById("quiz-play");
        const result = document.getElementById("quiz-result");
        const optionsContainer = document.getElementById("quiz-options");
        const feedback = document.getElementById("quiz-feedback");
        const nextButton = document.getElementById("quiz-next");

        function shuffled(items) {{
          const copy = [...items];
          for (let index = copy.length - 1; index > 0; index -= 1) {{
            const swapIndex = Math.floor(Math.random() * (index + 1));
            [copy[index], copy[swapIndex]] = [copy[swapIndex], copy[index]];
          }}
          return copy;
        }}

        function appendInlineText(target, text) {{
          text.split(/(`[^`]+`)/g).forEach((part) => {{
            if (part.startsWith("`") && part.endsWith("`")) {{
              const code = document.createElement("code");
              code.textContent = part.slice(1, -1);
              target.append(code);
            }} else {{
              target.append(document.createTextNode(part));
            }}
          }});
        }}

        function startRound() {{
          state.usedTopics.clear();
          state.missedTopics.clear();
          state.number = 0;
          state.score = 0;
          state.level = "dificil";
          state.current = null;
          state.locked = false;
          intro.hidden = true;
          result.hidden = true;
          play.hidden = false;
          renderQuestion();
        }}

        function renderQuestion() {{
          const availableTopics = Object.keys(bank).filter((slug) => !state.usedTopics.has(slug));
          if (state.number >= totalQuestions || availableTopics.length === 0) {{
            finishRound();
            return;
          }}
          const topic = availableTopics[Math.floor(Math.random() * availableTopics.length)];
          const entry = bank[topic];
          const questionPool = entry.levels[state.level];
          const question = questionPool[Math.floor(Math.random() * questionPool.length)];
          state.usedTopics.add(topic);
          state.number += 1;
          state.current = {{ topic, question }};
          state.locked = false;

          document.getElementById("quiz-count").textContent = `Pergunta ${{state.number}} de ${{totalQuestions}}`;
          document.getElementById("quiz-score").textContent = `Acertos: ${{state.score}}`;
          document.getElementById("quiz-progress").value = state.number - 1;
          const levelBadge = document.getElementById("quiz-level");
          levelBadge.textContent = labels[state.level];
          levelBadge.className = `quiz-level quiz-level-${{state.level}}`;
          const topicLabel = document.getElementById("quiz-topic");
          topicLabel.replaceChildren();
          appendInlineText(topicLabel, entry.title);
          const questionHeading = document.getElementById("quiz-question");
          questionHeading.replaceChildren();
          appendInlineText(questionHeading, question.prompt);
          optionsContainer.replaceChildren();
          feedback.hidden = true;
          feedback.className = "quiz-feedback";
          nextButton.hidden = true;
          const choices = shuffled([question.answer, ...question.distractors]);
          choices.forEach((choice, index) => {{
            const button = document.createElement("button");
            button.className = "quiz-option";
            button.type = "button";
            button.append(document.createTextNode(`${{String.fromCharCode(65 + index)}}. `));
            appendInlineText(button, choice);
            button.dataset.answer = choice;
            button.addEventListener("click", () => selectAnswer(button));
            optionsContainer.append(button);
          }});
        }}

        function selectAnswer(selectedButton) {{
          if (state.locked) return;
          state.locked = true;
          const {{ question }} = state.current;
          const correct = selectedButton.dataset.answer === question.answer;
          if (correct) state.score += 1;
          else state.missedTopics.add(state.current.topic);
          optionsContainer.querySelectorAll("button").forEach((button) => {{
            button.disabled = true;
            if (button.dataset.answer === question.answer) button.classList.add("is-correct");
            else if (button === selectedButton) button.classList.add("is-wrong");
          }});

          const answeredLevel = state.level;
          if (!correct) state.level = "medio";
          else if (answeredLevel === "dificil") state.level = "facil";
          else state.level = "dificil";
          feedback.hidden = false;
          feedback.classList.add(correct ? "feedback-correct" : "feedback-wrong");
          const heading = document.createElement("strong");
          heading.textContent = correct ? "Resposta correta." : "Não foi dessa vez.";
          const explanation = document.createElement("p");
          appendInlineText(explanation, question.explanation);
          const transition = document.createElement("p");
          transition.className = "quiz-transition";
          transition.textContent = state.number < totalQuestions
            ? `A próxima será ${{labels[state.level].toLowerCase()}}.`
            : "Você completou as 12 perguntas.";
          feedback.replaceChildren(heading, explanation, transition);
          document.getElementById("quiz-score").textContent = `Acertos: ${{state.score}}`;
          document.getElementById("quiz-progress").value = state.number;
          nextButton.textContent = state.number < totalQuestions ? "Próxima pergunta" : "Ver resultado";
          nextButton.hidden = false;
        }}

        function finishRound() {{
          play.hidden = true;
          result.hidden = false;
          document.getElementById("quiz-final-score").textContent = state.score;
          document.getElementById("quiz-result-message").textContent =
            `Você acertou ${{state.score}} de ${{totalQuestions}}. Esta rodada avaliou uma amostra de 12 assuntos; use o resultado para escolher o próximo estudo, não como medida definitiva de domínio.`;
          const review = document.getElementById("quiz-review");
          const reviewList = document.getElementById("quiz-review-list");
          reviewList.replaceChildren();
          const missed = [...state.missedTopics];
          review.hidden = missed.length === 0;
          missed.forEach((slug) => {{
            const item = document.createElement("li");
            const link = document.createElement("a");
            link.href = bank[slug].href;
            appendInlineText(link, bank[slug].title);
            item.append(link);
            reviewList.append(item);
          }});
          if (missed.length === 0) {{
            document.getElementById("quiz-result-message").textContent +=
              " Nenhum assunto ficou marcado para revisão nesta amostra; continue praticando em novas rodadas.";
          }}
        }}

        document.getElementById("quiz-start").addEventListener("click", startRound);
        document.getElementById("quiz-restart").addEventListener("click", startRound);
        nextButton.addEventListener("click", () => {{
          if (state.number >= totalQuestions) finishRound();
          else renderQuestion();
        }});
      }})();
      </script>"""
    content = hero(
        "Quiz dinâmico de Java",
        "Pratique os assuntos do guia em rodadas de 12 perguntas com alternativas embaralhadas e dificuldade adaptativa.",
        "Prática interativa · Java SE 17",
        [f"{len(topics)} temas", f"{question_count} questões", "12 perguntas por rodada"],
    ) + "\n" + article(app_markup)
    page = ROOT / "quiz.html"
    write_html(
        page,
        page_shell(page, "Quiz dinâmico Java", content, "Quiz de Java com 12 perguntas, quatro alternativas, temas sem repetição e dificuldade adaptativa."),
    )


def generate_summary(chapters: list[tuple]) -> None:
    rows = []
    for number, title, description, destination, topics in chapters:
        rows.append(
            f'<tr><td><a href="{relative_link(ROOT / "resumo.html", destination)}">{number:02d}. {html.escape(title)}</a></td><td>{html.escape(description)}</td><td>{len(topics)}</td></tr>'
        )
    body = f"""<p>Este roteiro tem como base a <strong>1Z0-829</strong>, para Java SE 17 Developer. A comparação com a <strong>1Z0-808</strong> (Java 8 Programmer I) e a <strong>1Z0-830</strong> (Java SE 21 Developer Professional) ajuda a separar fundamentos, nível profissional e diferenças entre versões do Java.</p>
        <section class="exam-callout"><div><strong>Os códigos não representam apenas versões sucessivas da mesma prova.</strong><span>A 1Z0-808 tem perfil de fundamentos; 1Z0-829 e 1Z0-830 são exames de desenvolvedor profissional para versões distintas do Java.</span></div><a href="exames.html">Abrir comparação detalhada →</a></section>
        <h2>Visão geral do percurso</h2>
        <div class="table-wrap"><table><thead><tr><th>Capítulo</th><th>Escopo</th><th>Assuntos</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>
        <h2>Como usar o material</h2>
        <ol>
          <li>Se está começando, siga a <a href="trilha-iniciante.html">trilha progressiva</a> e use o glossário quando encontrar termos novos.</li>
          <li>Leia o objetivo e o exemplo do assunto, preveja o resultado, execute o programa e resolva a atividade prática.</li>
          <li>Pratique a recuperação ativa com o <a href="quiz.html">quiz dinâmico de 12 perguntas</a>; cada rodada sorteia temas sem repetição.</li>
          <li>Use os mapas mentais para revisar relações entre conceitos e consulte os exemplos de código disponíveis no repositório.</li>
          <li>Use os tópicos “Estude” e “Verifique se consegue” para aprofundar e revisar casos-limite para a prova.</li>
        </ol>
        <p><a href="glossario.html">Abrir glossário Java</a></p>
        <h2>Sobre o conteúdo</h2>
        <p>O material foi organizado como apoio independente de estudo. Ele não é conteúdo oficial da Oracle e não substitui a documentação da plataforma ou a página do exame.</p>
        <p><a href="exames.html">Comparação dos exames 1Z0-808, 1Z0-829 e 1Z0-830</a></p>
        <p><a href="https://education.oracle.com/java-se-17-developer/pexam_1Z0-829">Oracle: Java SE 17 Developer (1Z0-829)</a> · <a href="https://docs.oracle.com/en/java/javase/17/">Documentação Java 17</a></p>
        <p><a href="index.html">← Voltar ao índice</a></p>"""
    content = hero(
        "Visão geral do curso",
        "Uma visão integrada dos temas do exame e uma sugestão de percurso para orientar o estudo e a revisão.",
        "Resumo geral · OCJP",
        [f"{len(chapters)} domínios", "Java SE 17", "Exame 1Z0-829"],
    ) + "\n" + article(body)
    write_html(
        ROOT / "resumo.html",
        page_shell(ROOT / "resumo.html", "Resumo geral", content, "Visão geral dos domínios e do percurso de estudos Java SE 17 Developer."),
    )


def generate_exam_comparison() -> None:
    page = ROOT / "exames.html"
    exam_cards = [
        (
            "1Z0-808",
            "Java SE 8 Programmer I",
            "Java 8",
            "Programmer I · fundamentos",
            "Foco em linguagem e fundamentos: tipos, operadores, controle de fluxo, arrays, métodos, orientação a objetos, exceções e APIs selecionadas.",
            "É uma certificação de outro nível e geração. Não equivale à 1Z0-829 nem cobre, por si só, todo o escopo profissional.",
            "https://education.oracle.com/java-se-8-programmer-i/pexam_1Z0-808",
        ),
        (
            "1Z0-829",
            "Java SE 17 Developer",
            "Java 17",
            "Professional · desenvolvedor",
            "Abrange linguagem e APIs em contexto profissional: orientação a objetos, coleções e generics, lambdas e streams, módulos, concorrência, I/O, JDBC e localização.",
            "É a versão-base deste portal. Os capítulos e exemplos existentes foram organizados para apoiar esse exame.",
            "https://education.oracle.com/java-se-17-developer/pexam_1Z0-829",
        ),
        (
            "1Z0-830",
            "Java SE 21 Developer Professional",
            "Java 21",
            "Professional · desenvolvedor",
            "Mantém o perfil profissional com Java 21 como versão-alvo; além dos fundamentos, exige atenção às evoluções da linguagem e da plataforma desde Java 17.",
            "Não é apenas uma atualização automática do roteiro 1Z0-829. Confira os objetivos oficiais da prova e estude as funcionalidades de Java 21.",
            "https://education.oracle.com/java-se-21-developer-professional/pexam_1Z0-830",
        ),
    ]
    cards = []
    rows = []
    for exam_id, title, version, level, scope, relationship, url in exam_cards:
        cards.append(
            f"""<section class="exam-card" id="{exam_id.lower()}">
          <div class="exam-card-top"><span class="exam-code">{exam_id}</span><span class="exam-version">{version}</span></div>
          <h2>{html.escape(title)}</h2>
          <p class="exam-level">{html.escape(level)}</p>
          <h3>Perfil e escopo</h3><p>{html.escape(scope)}</p>
          <blockquote><p>{html.escape(relationship)}</p></blockquote>
          <a class="exam-source" href="{url}" target="_blank" rel="noopener noreferrer">Consultar a página do exame na Oracle ↗</a>
        </section>"""
        )
        rows.append(
            f"<tr><th scope=\"row\">{exam_id}</th><td>{version}</td><td>{html.escape(level)}</td><td>{html.escape(scope)}</td></tr>"
        )
    matrix_rows = []
    for directory in CHAPTER_DIRS:
        title, _, _ = chapter_data(directory)
        notes = CHAPTER_EXAM_NOTES[directory.name]
        chapter_link = relative_link(page, directory / "index.html")
        matrix_rows.append(
            f'<tr><th scope="row"><a href="{chapter_link}">{inline_markup(title)}</a></th>'
            + "".join(f"<td>{html.escape(note)}</td>" for note in notes)
            + "</tr>"
        )
    body = f"""<p>Os exames <strong>1Z0-808</strong>, <strong>1Z0-829</strong> e <strong>1Z0-830</strong> estão associados a versões diferentes do Java e a perfis diferentes. A relação entre eles é de evolução de plataforma e carreira — não de equivalência direta de conteúdo.</p>
        <div class="exam-grid">{"".join(cards)}</div>
        <h2>Comparação rápida</h2>
        <div class="table-wrap"><table><thead><tr><th>Exame</th><th>Versão Java</th><th>Perfil</th><th>Ênfase geral</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>
        <h2 id="matriz">Matriz de uso deste material</h2>
        <p>A tabela indica como aproveitar cada capítulo deste portal ao estudar para os exames. Ela distingue a base Java 17 dos pontos que precisam de validação ou atualização de versão.</p>
        <div class="table-wrap exam-matrix"><table><thead><tr><th>Capítulo deste portal</th><th>1Z0-808 · Java 8</th><th>1Z0-829 · Java 17</th><th>1Z0-830 · Java 21</th></tr></thead><tbody>{"".join(matrix_rows)}</tbody></table></div>
        <p class="matrix-note"><strong>Importante:</strong> esta é uma matriz editorial de compatibilidade e reaproveitamento, não um mapeamento oficial dos objetivos (exam objectives). Ela não declara itens cobrados, peso ou cobertura integral. Consulte o blueprint atual de cada exame antes de planejar a preparação.</p>
        <h2>O que muda de Java 17 para Java 21?</h2>
        <p>Ao usar este roteiro para a 1Z0-830, revise também as funcionalidades introduzidas após Java 17. Entre os destaques finalizados em Java 21 estão:</p>
        <ul>
          <li><strong>Pattern matching para <code>switch</code></strong>: padrões em rótulos e verificações de exaustividade.</li>
          <li><strong>Record patterns</strong>: decomposição de valores de records em padrões.</li>
          <li><strong>Virtual threads</strong>: threads leves para aplicações com muitas tarefas bloqueantes.</li>
          <li><strong>Sequenced Collections</strong>: interfaces de coleções com ordem de encontro definida e operações nas extremidades.</li>
        </ul>
        <p>Esta lista serve como orientação de versão, não como transcrição do blueprint do exame. Confirme no guia oficial quais objetivos e funcionalidades são cobrados, inclusive a disponibilidade de recursos em preview.</p>
        <h2>Como aproveitar este portal</h2>
        <ul>
          <li><strong>Preparação para 1Z0-829:</strong> use o índice e os capítulos existentes como roteiro principal.</li>
          <li><strong>Preparação para 1Z0-808:</strong> priorize fundamentos compatíveis com Java 8 e confira o escopo específico de Programmer I; este portal foi feito para um exame profissional posterior.</li>
          <li><strong>Preparação para 1Z0-830:</strong> aproveite os conceitos compartilhados, mas complemente o estudo com Java 21 e o blueprint atual. Não presuma cobertura completa deste exame pelo material 1Z0-829.</li>
        </ul>
        <blockquote><p>Os escopos acima são uma comparação editorial de alto nível, não uma matriz oficial de objetivos. Os nomes, requisitos, disponibilidade e conteúdo dos exames podem mudar; confirme os detalhes nas páginas da Oracle antes de se inscrever.</p></blockquote>
        <h2>Fontes oficiais</h2>
        <ul>
          <li><a href="https://education.oracle.com/java-se-8-programmer-i/pexam_1Z0-808" target="_blank" rel="noopener noreferrer">Oracle · Java SE 8 Programmer I (1Z0-808)</a></li>
          <li><a href="https://education.oracle.com/java-se-17-developer/pexam_1Z0-829" target="_blank" rel="noopener noreferrer">Oracle · Java SE 17 Developer (1Z0-829)</a></li>
          <li><a href="https://education.oracle.com/java-se-21-developer-professional/pexam_1Z0-830" target="_blank" rel="noopener noreferrer">Oracle · Java SE 21 Developer Professional (1Z0-830)</a></li>
          <li><a href="https://docs.oracle.com/en/java/javase/21/language/" target="_blank" rel="noopener noreferrer">Oracle · Java Language Updates, Java 21</a></li>
          <li><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html" target="_blank" rel="noopener noreferrer">Oracle · API SequencedCollection, Java 21</a></li>
        </ul>
        <p><a href="index.html">← Voltar ao índice</a></p>"""
    content = hero(
        "Três exames, três contextos",
        "Compare Java 8 Programmer I, Java 17 Developer e Java 21 Developer Professional por versão, perfil e foco de estudo.",
        "Comparativo de exames · Oracle Java",
        ["1Z0-808 · Java 8", "1Z0-829 · Java 17", "1Z0-830 · Java 21"],
    ) + "\n" + article(body)
    write_html(
        page,
        page_shell(page, "Comparativo 1Z0-808, 1Z0-829 e 1Z0-830", content, "Compare os exames Java 1Z0-808, 1Z0-829 e 1Z0-830 por versão Java, perfil e escopo."),
    )


def main() -> None:
    total, chapters = generate_topic_pages()
    generate_index(chapters)
    generate_beginner_guide(chapters)
    generate_glossary()
    generate_quiz(chapters)
    generate_summary(chapters)
    generate_exam_comparison()
    print(f"Geradas 6 páginas gerais, {len(chapters)} páginas de capítulo e {total} páginas de assunto.")


if __name__ == "__main__":
    main()
