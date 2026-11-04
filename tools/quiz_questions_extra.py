"""Additional randomized question variants for the Java study quiz."""

QUIZ_QUESTION_VARIANTS = {
    "tipos-primitivos-e-wrappers": [
        ("facil", "Qual destes tipos guarda um valor lógico verdadeiro ou falso?", "`boolean`", ["`char`", "`int`", "`String`"], "`boolean` é o tipo primitivo usado para valores verdadeiros ou falsos."),
        ("medio", "Uma variável local declarada com `var` pode ficar sem inicializador?", "Não; o tipo é inferido a partir de uma expressão inicializadora", ["Sim; o tipo será `Object`", "Sim; receberá `null`", "Somente dentro de um método `static`"], "`var` exige uma expressão inicializadora para que o compilador possa inferir o tipo."),
        ("dificil", "O que ocorre ao ler uma variável local `int total;` antes de atribuir um valor?", "O código não compila por falta de inicialização", ["`total` recebe zero automaticamente", "`total` recebe `null`", "O programa lança `NullPointerException`"], "Variáveis locais não recebem valores padrão; devem ser inicializadas antes de serem lidas."),
    ],
    "operadores-expressoes-e-conversoes": [
        ("facil", "Qual operador calcula o resto de uma divisão inteira?", "`%`", ["`/`", "`*`", "`=`"], "O operador `%` devolve o resto da divisão."),
        ("medio", "Qual valor é atribuído a `double valor = 5 / 2;`?", "`2.0`", ["`2.5`", "`2` como tipo `int`", "O código não compila"], "A divisão é feita entre dois inteiros e resulta em `2`; depois esse valor é convertido para `double`."),
        ("dificil", "Qual valor `b` recebe em `int a = 3; int b = a++ + ++a;`?", "`8`", ["`7`", "`6`", "`9`"], "`a++` produz 3 e depois incrementa; `++a` incrementa para 5 e produz 5. A soma é 8."),
    ],
    "texto-string-e-stringbuilder": [
        ("facil", "Qual método compara o conteúdo de duas strings?", "`equals`", ["`==` em todos os casos", "`append`", "`length`"], "`equals` compara o conteúdo; `==` compara referências."),
        ("medio", "O que acontece com o mesmo objeto `StringBuilder` depois de `builder.append(\"!\")`?", "O conteúdo do `StringBuilder` é alterado", ["É criada uma nova `StringBuilder` e a original fica igual", "O método sempre retorna `null`", "O código não compila"], "`StringBuilder` é mutável; `append` altera seu conteúdo."),
        ("dificil", "Em `\"Java\".substring(4)`, qual string é retornada?", "A string vazia", ["`Java`", "O código lança exceção porque o índice final é exclusivo", "`a`"], "O índice inicial pode ser igual ao comprimento da string; nesse caso, o resultado é vazio."),
    ],
    "data-e-hora-java-time": [
        ("facil", "Qual tipo representa apenas um horário local, sem data?", "`LocalTime`", ["`LocalDate`", "`Instant`", "`Period`"], "`LocalTime` representa hora, minuto, segundo e frações, sem data ou fuso."),
        ("medio", "Qual tipo representa uma quantidade de dias, meses ou anos de calendário?", "`Period`", ["`Duration`", "`Instant`", "`ZoneId`"], "`Period` expressa unidades de calendário como dias, meses e anos."),
        ("dificil", "Qual afirmação sobre `ZonedDateTime` está correta?", "Ele combina data/hora local com uma região de fuso horário", ["Representa somente uma data, sem horário", "É sempre equivalente a `LocalDate`", "Não pode considerar regras de horário de verão"], "`ZonedDateTime` associa data e horário a um `ZoneId`, incluindo as regras daquele fuso."),
    ],
    "condicionais-e-switch": [
        ("facil", "Qual palavra introduz um caminho alternativo quando um `if` é falso?", "`else`", ["`case`", "`default`", "`continue`"], "`else` define o bloco alternativo de uma estrutura `if`."),
        ("medio", "Em um `switch` tradicional, para que serve `break` em um `case`?", "Para sair do `switch` e evitar continuar para o próximo `case`", ["Para devolver um valor de uma expressão", "Para repetir o mesmo `case`", "Para encerrar a JVM"], "`break` termina a execução do `switch` tradicional; não devolve valor de uma expressão `switch`."),
        ("dificil", "Uma expressão `switch` que atribui um valor precisa cobrir todas as possibilidades do seletor?", "Sim; seus caminhos precisam produzir um valor", ["Não; caminhos sem resultado recebem `null`", "Não; o compilador sempre adiciona `default`", "Somente se o seletor for um `int`"], "Uma expressão `switch` deve ser exaustiva para que o compilador possa garantir um valor em todos os caminhos."),
    ],
    "lacos-e-desvios": [
        ("facil", "Qual laço é apropriado quando se conhece a quantidade de repetições?", "`for`", ["`try`", "`switch`", "`catch`"], "`for` reúne inicialização, condição e atualização, sendo útil para repetições contadas."),
        ("medio", "Em laços aninhados, o que `break` sem rótulo encerra?", "O laço mais interno que o contém", ["Todos os laços", "Somente o programa", "A próxima iteração do laço externo"], "Sem rótulo, `break` encerra a estrutura de repetição ou `switch` mais próxima."),
        ("dificil", "Em `do { ... } while (condicao);`, quando a condição é testada?", "Depois da primeira execução do corpo", ["Antes da primeira execução", "Somente quando o corpo contém `continue`", "Nunca"], "O corpo do `do-while` executa ao menos uma vez antes do primeiro teste."),
    ],
    "metodos-sobrecarga-e-varargs": [
        ("facil", "O que indica o retorno de um método declarado com `void`?", "Que o método não devolve um valor", ["Que o método é privado", "Que o método não recebe parâmetros", "Que o método é executado uma única vez"], "`void` declara ausência de valor de retorno."),
        ("medio", "É possível sobrecarregar métodos mudando apenas o tipo de retorno?", "Não; a lista de parâmetros também precisa diferir", ["Sim, sempre", "Sim, se um dos métodos for `static`", "Somente com `void`"], "O tipo de retorno não faz parte da assinatura usada para distinguir overloads."),
        ("dificil", "Onde o parâmetro `...` de um método `varargs` deve aparecer?", "Como o último parâmetro do método", ["Sempre como o primeiro parâmetro", "Em qualquer posição", "Um método pode ter vários parâmetros `varargs`"], "Um método pode ter no máximo um parâmetro `varargs`, e ele deve ser o último."),
    ],
    "classes-objetos-e-encapsulamento": [
        ("facil", "Qual palavra-chave cria uma instância de uma classe comum?", "`new`", ["`this`", "`extends`", "`package`"], "`new` cria um objeto e invoca um construtor."),
        ("medio", "Qual valor padrão recebe um campo de instância do tipo `boolean`?", "`false`", ["`true`", "`null`", "O código não compila"], "Campos de instância recebem valores padrão; para `boolean`, o padrão é `false`."),
        ("dificil", "Uma classe de outro pacote pode acessar diretamente um campo `private`?", "Não; o modificador `private` restringe o acesso à classe que o declara", ["Sim, se criar a instância com `new`", "Sim, se o campo tiver valor", "Somente por uma variável `var`"], "`private` restringe o acesso ao corpo da classe que declara o membro."),
    ],
    "construtores-e-inicializacao": [
        ("facil", "Qual afirmação sobre o nome de um construtor está correta?", "Ele tem o mesmo nome da classe e não declara tipo de retorno", ["Ele sempre se chama `main`", "Ele precisa retornar o tipo da classe", "Ele tem o mesmo nome do pacote"], "Construtores usam o nome da classe e não têm tipo de retorno."),
        ("medio", "Onde uma chamada explícita a `this(...)` deve aparecer em um construtor?", "Como primeira instrução do construtor", ["Como última instrução", "Dentro de um bloco `finally`", "Em qualquer método da classe"], "Uma chamada a outro construtor da mesma classe com `this(...)` deve ser a primeira instrução."),
        ("dificil", "Uma classe que declara um construtor com parâmetros ainda recebe automaticamente um construtor sem argumentos?", "Não", ["Sim, sempre", "Sim, se o construtor for `public`", "Somente quando há um campo `static`"], "O compilador fornece um construtor padrão apenas quando nenhum construtor foi declarado."),
    ],
    "heranca-sobrescrita-e-polimorfismo": [
        ("facil", "Qual palavra-chave declara que uma classe herda de outra classe?", "`extends`", ["`implements`", "`inherits`", "`super`"], "Uma classe estende outra com `extends`."),
        ("medio", "Qual é uma vantagem da anotação `@Override`?", "O compilador verifica se o método realmente sobrescreve um método herdado", ["Ela torna o método `static`", "Ela permite reduzir a visibilidade do método", "Ela cria uma sobrecarga automaticamente"], "`@Override` ajuda a detectar erros de assinatura ao sobrescrever métodos."),
        ("dificil", "Uma chamada a método de instância sobrescrito é escolhida principalmente por qual tipo?", "Pela classe real do objeto em tempo de execução", ["Somente pelo tipo declarado da variável", "Pelo nome da variável", "Pelo tipo de retorno do método"], "A sobrescrita é dinâmica: a implementação da classe real do objeto é chamada."),
    ],
    "interfaces-e-enums": [
        ("facil", "O que um `enum` representa?", "Um conjunto fixo de constantes nomeadas", ["Uma classe que não pode ter instâncias", "Um tipo de exceção checked", "Uma coleção ordenada de objetos"], "Um enum declara um conjunto conhecido de constantes."),
        ("medio", "Qual é a natureza implícita de um campo declarado em uma interface?", "`public static final`", ["`private volatile`", "`protected transient`", "`final` de instância"], "Campos de interface são implicitamente constantes públicas, estáticas e finais."),
        ("dificil", "O que uma classe pode fazer se duas interfaces implementadas fornecerem o mesmo método `default`?", "Sobrescrever o método e escolher explicitamente o comportamento", ["O compilador escolhe sempre a primeira interface", "A classe herda os dois métodos ao mesmo tempo", "O método deixa de ser acessível"], "A classe deve resolver o conflito sobrescrevendo o método; pode chamar uma implementação com `Interface.super.metodo()`."),
    ],
    "records-sealed-e-pattern-matching": [
        ("facil", "Como se acessa um componente `nome` de um record `Pessoa`?", "Com o acessor `nome()`", ["Com o campo público `nome`", "Com `getNome()` sempre", "Com `component(0)`"], "Um record gera um acessor com o nome de cada componente, como `nome()`."),
        ("medio", "Uma classe declarada como `record` pode ser estendida por uma classe comum?", "Não; records são implicitamente finais", ["Sim, se o record não declarar construtor", "Sim, usando `extends Record`", "Somente por classes do mesmo pacote"], "Uma classe record é implicitamente `final` e não pode ser estendida."),
        ("dificil", "O que um construtor compacto de record pode fazer com um componente?", "Validar ou normalizar o parâmetro antes da atribuição automática", ["Atribuir diretamente a um campo de instância não declarado", "Declarar um tipo de retorno", "Estender outro record"], "No construtor compacto, os parâmetros podem ser validados ou ajustados; os componentes são atribuídos automaticamente ao final."),
    ],
    "hierarquia-e-tipos-de-excecao": [
        ("facil", "Uma exceção que estende `RuntimeException` é checked ou unchecked?", "Unchecked", ["Checked", "Não é uma exceção", "É um `Error`"], "`RuntimeException` e suas subclasses são exceções unchecked."),
        ("medio", "O que normalmente é necessário fazer com uma exceção checked?", "Capturá-la ou declará-la com `throws`", ["Convertê-la sempre em `Error`", "Ignorá-la no método `main`", "Torná-la `static`"],"O compilador exige tratamento ou declaração das exceções checked."),
        ("dificil", "Qual ordem de `catch` é válida ao tratar `FileNotFoundException` e depois `IOException`?", "Capturar `FileNotFoundException` antes de `IOException`", ["Capturar `IOException` antes de `FileNotFoundException`", "A ordem nunca importa", "Capturar somente `Throwable` é obrigatório"], "O tipo mais específico deve vir antes do tipo mais geral, senão o segundo bloco se torna inalcançável."),
    ],
    "try-catch-finally-e-multicatch": [
        ("facil", "Qual bloco trata uma exceção compatível lançada no `try`?", "`catch`", ["`finally`", "`throws`", "`case`"], "`catch` trata uma exceção compatível com o tipo declarado no bloco."),
        ("medio", "Em um multi-catch, as alternativas podem ter relação de subclasse entre si?", "Não; as alternativas não podem ser subtipos umas das outras", ["Sim, em qualquer ordem", "Somente se forem `RuntimeException`", "Sim, se o bloco for `finally`"], "As alternativas de multi-catch não podem ter relação de subclasse, pois um tipo mais geral já cobriria o específico."),
        ("dificil", "Se `finally` lança uma nova exceção enquanto outra já está sendo propagada, o que normalmente é observado pelo chamador?", "A exceção lançada em `finally` substitui a exceção anterior", ["As duas exceções são lançadas simultaneamente", "A exceção anterior sempre vence", "A JVM ignora a exceção de `finally`"], "Uma exceção lançada em `finally` pode substituir a exceção que estava em propagação; por isso esse padrão deve ser evitado."),
    ],
    "try-with-resources": [
        ("facil", "Qual interface é implementada por recursos que podem ser usados em try-with-resources?", "`AutoCloseable`", ["`Runnable`", "`Comparable`", "`Serializable`"], "Um recurso de try-with-resources implementa `AutoCloseable` (diretamente ou via `Closeable`)."),
        ("medio", "Em que ordem são fechados vários recursos declarados em um try-with-resources?", "Na ordem inversa à declaração", ["Na mesma ordem da declaração", "Em ordem alfabética", "Apenas o primeiro é fechado"], "Os recursos são fechados na ordem inversa, como uma pilha."),
        ("dificil", "O que ocorre com uma exceção lançada ao fechar um recurso quando outra já foi lançada no corpo do `try`?", "A exceção do fechamento pode ficar suprimida na exceção principal", ["A exceção do corpo é sempre descartada", "O fechamento não pode lançar exceção", "A JVM combina as duas em um `Error`"], "Try-with-resources preserva a exceção principal e registra falhas de fechamento como exceções suprimidas."),
    ],
    "arrays": [
        ("facil", "Depois de criado, o tamanho de um array Java pode ser alterado?", "Não; o tamanho é fixo", ["Sim, com `array.resize()`", "Sim, ao adicionar um elemento", "Somente se os elementos forem objetos"], "Arrays têm comprimento fixo definido na criação."),
        ("medio", "Qual é o primeiro índice válido de um array Java não vazio?", "`0`", ["`1`", "`-1`", "O índice do último elemento"], "Os índices de arrays Java começam em zero."),
        ("dificil", "Qual condição é importante antes de usar `Arrays.binarySearch` em um array?", "O array deve estar ordenado segundo a mesma ordem da busca", ["O array precisa conter apenas números", "O array deve estar vazio", "Os índices precisam começar em um"], "A busca binária requer que os elementos estejam ordenados conforme a ordem usada pela busca."),
    ],
    "generics": [
        ("facil", "O que `List<String>` informa ao compilador?", "A lista é declarada para trabalhar com valores do tipo `String`", ["A lista só pode ter um elemento", "A lista é imutável", "A lista guarda apenas objetos `Class`"], "O parâmetro de tipo informa que a coleção trabalha com strings e permite checagem de tipos em compilação."),
        ("medio", "Qual valor, além de `null`, pode ser inserido em uma `List<?>`?", "Nenhum valor com tipo específico conhecido", ["Qualquer `Object`", "Somente `String`", "Somente o primeiro tipo usado na aplicação"], "O tipo exato da lista é desconhecido; não é seguro inserir um valor específico (exceto `null`)."),
        ("dificil", "O que é seguro fazer com `List<? super Integer>`?", "Adicionar um `Integer` e ler elementos como `Object`", ["Adicionar `Double` e ler como `Integer`", "Ler todo elemento como `Number` sem cast", "Adicionar apenas `null`"], "Um wildcard `super Integer` aceita `Integer` para escrita, mas o tipo lido com segurança é `Object`."),
    ],
    "interfaces-e-colecoes": [
        ("facil", "Uma `ArrayList` permite elementos repetidos?", "Sim", ["Não; é um `Set`", "Somente se os elementos forem números", "Apenas uma vez por execução"], "`List`, incluindo `ArrayList`, permite elementos repetidos e mantém uma ordem de encontro."),
        ("medio", "Qual característica define um `Set`?", "Não mantém elementos duplicados segundo seu contrato de igualdade", ["Sempre ordena os elementos alfabeticamente", "Permite apenas valores numéricos", "Acessa elementos somente por índice"], "Um `Set` representa elementos sem duplicatas; a ordenação depende da implementação."),
        ("dificil", "Quais métodos são importantes para uma chave usada corretamente em `HashMap`?", "`equals` e `hashCode` consistentes", ["`toString` e `clone`", "`wait` e `notify`", "`compareTo` e `finalize`"], "`HashMap` usa `hashCode` para localizar grupos e `equals` para confirmar igualdade."),
    ],
    "comparacao-e-ordenacao": [
        ("facil", "Que interface uma classe pode implementar para definir sua ordem natural?", "`Comparable`", ["`Comparator`", "`Iterable`", "`Cloneable`"], "`Comparable` define a comparação natural por meio de `compareTo`."),
        ("medio", "Para que serve `Comparator.comparing`?", "Para criar um comparador baseado em uma chave extraída dos objetos", ["Para converter uma lista em array", "Para eliminar todos os duplicados", "Para comparar referências com `==`"], "`Comparator.comparing` cria uma ordenação com base em uma função que extrai a chave de comparação."),
        ("dificil", "Em um `TreeSet`, o que pode acontecer quando `compare(a, b)` retorna zero?", "O conjunto trata os elementos como equivalentes para ordenação e não mantém ambos como elementos distintos", ["Sempre mantém os dois porque `equals` prevalece", "Lança `NullPointerException` obrigatoriamente", "Ordena os dois pelo endereço de memória"], "Para estruturas ordenadas, o resultado zero indica equivalência na ordenação e pode impedir a inclusão do segundo elemento."),
    ],
    "collectors-e-optional": [
        ("facil", "O que representa `Optional.empty()`?", "Um `Optional` sem valor presente", ["Um `Optional` contendo `null`", "Uma lista vazia", "Uma exceção checked"], "`Optional.empty()` representa explicitamente a ausência de um valor."),
        ("medio", "O que ocorre ao chamar `Optional.of(null)`?", "É lançada `NullPointerException`", ["É criado `Optional.empty()`", "O código não compila", "É criado um Optional com null"], "`Optional.of` exige um valor não nulo; use `ofNullable` quando o argumento pode ser null."),
        ("dificil", "Quando o fornecedor passado a `orElseGet(supplier)` é executado?", "Somente quando o `Optional` está vazio", ["Sempre, antes de verificar o valor", "Somente quando o valor está presente", "Nunca"], "`orElseGet` chama o supplier apenas para obter um valor substituto quando o Optional está vazio."),
    ],
    "interfaces-funcionais-lambdas-e-referencias": [
        ("facil", "Qual é o resultado esperado de um `Predicate<String>`?", "Um valor `boolean`", ["Um `StringBuilder`", "Um `int` obrigatoriamente", "Um `void` em todos os casos"], "`Predicate<T>` representa uma condição que recebe um `T` e produz um boolean."),
        ("medio", "Em uma lambda com corpo em bloco que deve devolver um valor, como esse valor é produzido?", "Com `return` dentro do bloco", ["Com `yield` em qualquer lambda", "Com `break` no fim do bloco", "O corpo em bloco não pode devolver valor"], "Uma lambda com corpo em bloco que implementa um método com retorno deve usar `return` para produzir esse valor."),
        ("dificil", "Qual tipo funcional corresponde a `String::length`?", "`ToIntFunction<String>`", ["`Predicate<String>`", "`Consumer<String>`", "`Supplier<String>`"], "`String::length` recebe uma string e devolve um inteiro, correspondendo a `ToIntFunction<String>`."),
    ],
    "streams-e-pipelines": [
        ("facil", "Qual operação intermediária de stream seleciona elementos que passam em uma condição?", "`filter`", ["`count`", "`forEach`", "`collect`"], "`filter` é a operação intermediária usada para selecionar elementos."),
        ("medio", "Um stream pode ser consumido por mais de uma operação terminal?", "Não; depois de consumido, não deve ser reutilizado", ["Sim, qualquer número de vezes", "Somente se a operação terminal for `count`", "Apenas em streams paralelos"], "Um stream descreve uma única sequência de processamento e não pode ser reutilizado após uma operação terminal."),
        ("dificil", "O que normalmente inicia a avaliação de operações intermediárias lazy em um pipeline?", "Uma operação terminal", ["A criação do stream", "Uma chamada a `filter`", "A declaração de uma lambda"], "Operações intermediárias são lazy; a operação terminal inicia o processamento do pipeline."),
    ],
    "sistema-de-modulos-jpms": [
        ("facil", "Qual arquivo declara o módulo de um projeto JPMS?", "`module-info.java`", ["`package-info.class`", "`pom-module.xml`", "`module.properties`"], "O descritor de um módulo Java é escrito em `module-info.java`."),
        ("medio", "Qual diretiva disponibiliza tipos públicos de um pacote para outros módulos?", "`exports`", ["`opens`", "`uses`", "`provides`"], "`exports` expõe os tipos públicos de um pacote; `opens` está relacionado ao acesso reflexivo."),
        ("dificil", "O que `requires transitive outro.modulo;` comunica aos módulos que dependem do módulo atual?", "Que eles também leem `outro.modulo` como dependência transitiva", ["Que o módulo atual é opcional", "Que todos os pacotes serão abertos para reflexão", "Que o módulo deixa de depender de `outro.modulo`"], "`requires transitive` propaga a legibilidade dessa dependência para módulos que leem o módulo declarante."),
    ],
    "apis-concorrentes-e-colecoes": [
        ("facil", "Uma `ConcurrentHashMap` aceita `null` como chave ou valor?", "Não", ["Sim, como chave, mas não como valor", "Sim, apenas para um valor", "Somente quando há uma thread"], "`ConcurrentHashMap` não permite chaves nem valores nulos."),
        ("medio", "O que `putIfAbsent(chave, valor)` faz?", "Insere o valor somente se a chave ainda não tiver mapeamento", ["Remove a chave se já existir", "Substitui sempre o valor existente", "Bloqueia a aplicação até a chave sumir"], "`putIfAbsent` combina teste e inserção para a chave em uma única operação."),
        ("dificil", "A iteração sobre uma coleção concorrente garante que todos os elementos reflitam um único instante imutável?", "Não necessariamente; iteradores podem ser weakly consistent", ["Sim, sempre cria uma fotografia transacional", "Sim, bloqueia todas as escritas", "Não; a iteração sempre lança `ConcurrentModificationException`"], "Iteradores de várias coleções concorrentes são weakly consistent: toleram atualizações sem prometer uma fotografia atômica."),
    ],
    "sincronizacao-e-visibilidade": [
        ("facil", "Qual é um efeito de sincronizar blocos usando o mesmo monitor?", "Exclusão mútua entre as regiões sincronizadas nesse monitor", ["Executar sempre em paralelo", "Transformar todos os campos em `final`", "Impedir qualquer exceção"], "Somente uma thread por vez pode executar uma região sincronizada no mesmo monitor."),
        ("medio", "Uma variável `volatile int contador` torna `contador++` atômico?", "Não; o incremento continua sendo leitura, soma e escrita", ["Sim, qualquer incremento fica atômico", "Sim, se houver apenas duas threads", "Não; `volatile` impede a leitura do valor"], "`volatile` contribui para visibilidade, mas não torna atômica uma operação composta como `++`."),
        ("dificil", "Qual operação de `AtomicInteger` incrementa atomicamente e devolve o novo valor?", "`incrementAndGet()`", ["`get()`", "`set()`", "`toString()`"], "`incrementAndGet` realiza o incremento atomicamente e retorna o valor atualizado."),
    ],
    "threads-e-executors": [
        ("facil", "Qual método de `Runnable` descreve a tarefa a ser executada?", "`run()`", ["`start()`", "`submit()`", "`call()`"], "`Runnable` declara `run`; quem agenda a execução pode ser uma thread ou um executor."),
        ("medio", "Qual tipo pode ser retornado por `ExecutorService.submit` para acompanhar uma tarefa?", "`Future`", ["`Path`", "`Locale`", "`ThreadLocal`"], "`submit` devolve um `Future` que representa o resultado ou estado da tarefa."),
        ("dificil", "O que `ExecutorService.shutdown()` faz?", "Impede o recebimento de novas tarefas e permite concluir as já submetidas", ["Espera necessariamente todas as tarefas terminarem antes de retornar", "Interrompe sempre as tarefas em execução", "Reinicia o pool com novas threads"], "`shutdown` inicia encerramento ordenado, mas não espera sozinho a conclusão; use `awaitTermination` para aguardar."),
    ],
    "nio2-path-e-files": [
        ("facil", "Qual método pode criar um `Path` a partir de texto em Java moderno?", "`Path.of(...)`", ["`Files.path(...)`", "`File.read(...)`", "`Paths.createFile(...)`"], "`Path.of` cria uma representação de caminho a partir de uma string."),
        ("medio", "A existência verificada por `Files.exists(path)` garante que a próxima operação terá sucesso?", "Não; o estado ou as permissões podem mudar", ["Sim, a existência garante leitura e escrita", "Sim, desde que o caminho seja absoluto", "Não; `exists` sempre retorna `false`"], "Uma verificação de estado não torna a operação seguinte atômica nem garante permissões futuras."),
        ("dificil", "O que pode ocorrer ao pedir `StandardCopyOption.ATOMIC_MOVE` em um sistema de arquivos que não oferece a operação?", "A operação pode falhar com `AtomicMoveNotSupportedException`", ["Java sempre simula atomicidade sem exceção", "O arquivo é convertido para texto", "O caminho de origem é renomeado em memória"], "A opção de movimentação atômica depende do suporte do sistema de arquivos e pode não estar disponível."),
    ],
    "serializacao": [
        ("facil", "Qual modificador exclui um campo da serialização padrão?", "`transient`", ["`volatile`", "`synchronized`", "`native`"], "Campos `transient` são ignorados pela serialização padrão de objetos."),
        ("medio", "Um campo de instância `static` é serializado como parte do estado de cada objeto?", "Não; o campo pertence à classe, não a cada instância", ["Sim, sempre", "Somente se também for `transient`", "Somente quando não há construtor"], "Campos `static` pertencem à classe e não fazem parte do estado serializado de cada instância."),
        ("dificil", "Para que serve declarar explicitamente `serialVersionUID`?", "Controlar a compatibilidade de versão da classe serializável", ["Criptografar o objeto", "Evitar que um campo seja `transient`", "Garantir que dados não confiáveis sejam seguros"], "`serialVersionUID` participa da verificação de compatibilidade entre a classe serializada e a classe disponível."),
    ],
    "streams-readers-e-writers": [
        ("facil", "Qual par trabalha principalmente com caracteres?", "`Reader` e `Writer`", ["`InputStream` e `OutputStream`", "`Path` e `Files`", "`Thread` e `Runnable`"], "`Reader` e `Writer` são abstrações para caracteres; streams trabalham com bytes."),
        ("medio", "Por que indicar um charset ao ler texto?", "Para decodificar bytes de forma previsível", ["Para ordenar as linhas", "Para tornar o arquivo somente leitura", "Para evitar fechar o leitor"], "O charset determina como bytes representam caracteres; informá-lo evita depender do padrão da máquina."),
        ("dificil", "Qual afirmação sobre `BufferedReader` em try-with-resources é correta?", "Ele pode ser fechado automaticamente ao sair do bloco", ["Ele fecha a JVM ao terminar", "Ele só lê arquivos binários", "Ele não implementa recursos fecháveis"], "Um `BufferedReader` implementa `Closeable`/`AutoCloseable` e pode ser fechado automaticamente."),
    ],
    "conexoes-e-comandos": [
        ("facil", "Qual interface JDBC representa uma conexão com o banco?", "`Connection`", ["`ResultSet`", "`DriverManager`", "`PreparedStatement`"], "`Connection` representa uma sessão de conexão JDBC."),
        ("medio", "Qual método de `PreparedStatement` define o primeiro parâmetro posicional?", "`set...` com índice `1`", ["`set...` com índice `0`", "`bind` com índice `-1`", "Parâmetros JDBC não têm índice"], "Os índices de parâmetros posicionais em JDBC começam em 1."),
        ("dificil", "Qual método é apropriado para uma consulta que retorna um `ResultSet`?", "`executeQuery()`", ["`executeUpdate()`", "`commit()`", "`close()`"], "`executeQuery` executa uma consulta que retorna um `ResultSet`; `executeUpdate` é usado para comandos de alteração."),
    ],
    "resultset-recursos-e-transacoes": [
        ("facil", "O que `ResultSet.next()` retorna?", "Um `boolean` indicando se há uma linha atual", ["O número de todas as linhas", "Uma `Connection`", "Sempre `true`"], "`next()` avança o cursor e informa se encontrou uma linha."),
        ("medio", "Antes do primeiro `next()` de um `ResultSet`, onde está o cursor?", "Antes da primeira linha", ["Na primeira linha", "Depois da última linha", "Na linha selecionada automaticamente"], "O cursor começa antes da primeira linha; é preciso chamar `next()` para avançar."),
        ("dificil", "Com auto-commit desativado, qual ação desfaz alterações ainda não confirmadas?", "`Connection.rollback()`", ["`Connection.commit()`", "`ResultSet.close()`", "`Statement.executeQuery()`"], "`rollback` desfaz a transação não confirmada; `commit` a confirma."),
    ],
    "locale-e-bundles": [
        ("facil", "Um `Locale` representa principalmente quais informações?", "Idioma e, opcionalmente, região", ["Fuso horário e instante", "Nome de classe e pacote", "Charset e caminho"], "`Locale` identifica convenções linguísticas/regionais, não um fuso horário."),
        ("medio", "O que `ResourceBundle` ajuda a selecionar?", "Textos ou recursos adequados a um locale", ["Um executor para threads", "Uma conexão de banco", "O charset do compilador"], "`ResourceBundle` carrega recursos localizados, como mensagens."),
        ("dificil", "Se não houver bundle para um locale específico, o que pode ocorrer durante a busca?", "A resolução pode tentar locales mais gerais e o bundle base", ["Java inventa a tradução ausente", "A aplicação sempre ignora todos os bundles", "O bundle específico é criado automaticamente"], "`ResourceBundle` percorre candidatos de fallback segundo as regras de resolução."),
    ],
    "formatacao-e-parsing": [
        ("facil", "Qual classe pode formatar números conforme um `Locale`?", "`NumberFormat`", ["`Thread`", "`Path`", "`Optional`"], "`NumberFormat` formata e interpreta números segundo convenções regionais."),
        ("medio", "Qual afirmação sobre `DateTimeFormatter` está correta?", "É imutável e pode ser compartilhado entre threads", ["É mutável e não pode ser compartilhado", "Só funciona com `Locale.US`", "Representa uma data e substitui `LocalDate`"], "`DateTimeFormatter` é imutável e thread-safe."),
        ("dificil", "Em um padrão de `DateTimeFormatter`, o que `MM` representa?", "Mês", ["Minuto", "Milissegundo", "Dia do mês"], "No padrão de data/hora, `M` representa mês; `m` minúsculo representa minuto."),
    ],
}
