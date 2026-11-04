"""Question bank for the generated Java study quiz.

Each topic has at least one question per difficulty. The quiz randomizes topics,
question variants, and answer order; a topic can appear only once per attempt.
"""

QUIZ_BANK = {
    "tipos-primitivos-e-wrappers": [
        ("facil", "Qual destes tipos é primitivo em Java?", "int", ["Integer", "String", "ArrayList"], "int é um dos oito tipos primitivos; Integer é sua classe wrapper."),
        ("medio", "Qual é o resultado de `int total = 5 / 2;`?", "2", ["2.5", "2.0", "O código não compila"], "Como os dois operandos são inteiros, a divisão inteira descarta a parte fracionária."),
        ("dificil", "O que acontece ao executar `Integer n = null; int valor = n;`?", "É lançada NullPointerException durante o unboxing", ["valor recebe 0 automaticamente", "O código não compila porque Integer não pode ser atribuído a int", "valor recebe null"], "A atribuição faz unboxing; extrair um primitivo de uma referência null lança NullPointerException."),
    ],
    "operadores-expressoes-e-conversoes": [
        ("facil", "Qual operador lógico para a avaliação quando o primeiro operando de `&&` é false?", "`&&`", ["`&` em qualquer contexto", "`||`", "`^`"], "`&&` usa curto-circuito: se o primeiro operando é false, o segundo não é avaliado."),
        ("medio", "Qual é o tipo do resultado de `byte a = 1; byte b = 2; a + b`?", "`int`", ["`byte`", "`long`", "`Integer`"], "A promoção numérica converte byte para int em expressões aritméticas."),
        ("dificil", "Qual é o resultado de `int n = 2147483647; System.out.println(n + 1);`?", "-2147483648", ["2147483648", "Lança ArithmeticException", "O código não compila"], "Overflow de inteiro não lança exceção automaticamente; o valor dá a volta dentro do intervalo de int."),
    ],
    "texto-string-e-stringbuilder": [
        ("facil", "Qual afirmação sobre `String` está correta?", "É imutável; métodos como `concat` devolvem outra String", ["É mutável como StringBuilder", "Só pode guardar letras", "A comparação `==` sempre verifica o conteúdo"], "String é imutável. Para conservar o resultado de concat, atribua a nova String."),
        ("medio", "O que imprime `String s = \"Java\"; s.concat(\" 17\"); System.out.println(s);`?", "`Java`", ["`Java 17`", "`null`", "O código não compila"], "O valor retornado por concat não foi atribuído a s."),
        ("dificil", "Em `\"abcdef\".substring(2, 5)`, quais caracteres são retornados?", "`cde`", ["`bcd`", "`cdef`", "`bcde`"], "O início é inclusivo e o fim exclusivo: índices 2, 3 e 4."),
    ],
    "data-e-hora-java-time": [
        ("facil", "Qual tipo representa uma data civil sem horário?", "`LocalDate`", ["`Instant`", "`LocalTime`", "`Duration`"], "LocalDate representa ano, mês e dia, sem horário nem fuso."),
        ("medio", "O que ocorre com `LocalDate d = LocalDate.of(2024, 1, 1); d.plusDays(1);` se o retorno não for guardado?", "`d` continua em 2024-01-01", ["`d` passa a 2024-01-02", "`d` vira null", "O método altera o objeto original"], "Os tipos de java.time são imutáveis; plusDays devolve outro valor."),
        ("dificil", "Em um ano não bissexto, qual resultado tem `LocalDate.of(2023, 1, 31).plusMonths(1)`?", "2023-02-28", ["2023-03-03", "2023-03-31", "Lança DateTimeException"], "Ao ajustar um mês sem dia 31, LocalDate usa o último dia válido do mês de destino."),
    ],
    "condicionais-e-switch": [
        ("facil", "Qual estrutura executa um bloco quando uma condição booleana é verdadeira?", "`if`", ["`for`", "`import`", "`package`"], "`if` seleciona um caminho com base em uma expressão booleana."),
        ("medio", "Em um `switch` com rótulos `case ... ->`, ocorre fall-through para o próximo case?", "Não", ["Sim, sempre", "Só quando o seletor é String", "Apenas dentro de uma expressão"], "A forma com seta não continua automaticamente para o próximo rótulo."),
        ("dificil", "Dentro de um bloco `case` de uma expressão `switch`, como se devolve o valor?", "Com `yield`", ["Com `continue`", "Com `super`", "Com `break`"], "O bloco de uma expressão switch usa yield para produzir o valor; os caminhos precisam produzir resultado."),
    ],
    "lacos-e-desvios": [
        ("facil", "Qual laço testa a condição antes de executar o corpo?", "`while`", ["`do-while`", "`switch`", "`try`"], "while verifica a condição antes de cada execução do corpo."),
        ("medio", "Quantas vezes um `do { ... } while (false);` executa o corpo?", "Uma vez", ["Nenhuma", "Duas vezes", "Depende do compilador"], "O corpo do do-while é executado antes da primeira verificação da condição."),
        ("dificil", "Em laços aninhados, o que faz `continue externo;`?", "Pula para a próxima iteração do laço rotulado externo", ["Encerra todos os laços", "Encerra somente o laço interno", "Reinicia o programa"], "Um continue rotulado continua a próxima iteração do laço nomeado, encerrando o restante da iteração atual."),
    ],
    "metodos-sobrecarga-e-varargs": [
        ("facil", "Qual parte de um método indica o valor que ele devolve?", "O tipo de retorno", ["O nome do pacote", "O modificador de acesso", "O nome do arquivo"], "O tipo de retorno declara o tipo do valor devolvido; void indica ausência de valor."),
        ("medio", "Como os argumentos são passados para parâmetros de método em Java?", "Por valor, inclusive quando o valor é uma referência", ["Por referência em todos os casos", "Por cópia profunda do objeto", "Somente por nome"], "A variável do parâmetro recebe uma cópia do valor; para objetos, esse valor é uma referência."),
        ("dificil", "Uma variável declarada como `Animal a = new Gato()` é passada a métodos sobrecarregados `m(Animal)` e `m(Gato)`. Qual é escolhido?", "`m(Animal)`, conforme o tipo declarado da expressão", ["`m(Gato)`, conforme o objeto real", "O compilador sempre rejeita a chamada", "A escolha é aleatória"], "A sobrecarga é resolvida em compilação com os tipos declarados; isso difere do despacho dinâmico de métodos sobrescritos."),
    ],
    "classes-objetos-e-encapsulamento": [
        ("facil", "O que a expressão `new Tarefa()` faz?", "Cria uma instância de Tarefa", ["Declara um pacote", "Compila todos os arquivos", "Cria uma interface"], "`new` cria um objeto e invoca um construtor."),
        ("medio", "Se `Tarefa b = a;`, o que é copiado para b?", "O valor da referência; a e b podem apontar para o mesmo objeto", ["Uma cópia independente do objeto", "Somente os campos primitivos", "Nada: a atribuição não compila"], "A atribuição de referências não clona o objeto."),
        ("dificil", "Qual é a visibilidade de um membro sem modificador de acesso?", "Acesso de pacote", ["`public`", "`private`", "Acesso apenas por subclasses"], "Sem modificador, o membro tem acesso package-private: é acessível dentro do mesmo pacote."),
    ],
    "construtores-e-inicializacao": [
        ("facil", "Quando o compilador fornece um construtor padrão sem argumentos?", "Quando a classe não declara nenhum construtor", ["Sempre, mesmo que haja outros construtores", "Somente se a classe for public", "Nunca"], "A declaração de qualquer construtor impede que o compilador forneça o construtor padrão."),
        ("medio", "Onde deve aparecer a chamada explícita `this(...)` em um construtor?", "Como primeira instrução", ["Como última instrução", "Dentro de um bloco `finally`", "Em qualquer posição"], "Uma chamada a outro construtor da mesma classe deve ser a primeira instrução."),
        ("dificil", "Ao criar uma instância de uma subclasse, qual inicialização de instância ocorre primeiro?", "Inicializadores e construtor da superclasse antes dos inicializadores e construtor da subclasse", ["Construtor da subclasse e depois o da superclasse", "Todos os construtores antes dos inicializadores", "A ordem não é definida"], "A construção inicializa a parte da superclasse antes de concluir a inicialização da subclasse."),
    ],
    "heranca-sobrescrita-e-polimorfismo": [
        ("facil", "Qual palavra-chave declara herança de uma classe?", "`extends`", ["`implements`", "`instanceof`", "`package`"], "Uma classe estende outra usando extends."),
        ("medio", "Qual implementação é chamada quando um método de instância sobrescrito é invocado?", "A implementação correspondente à classe real do objeto", ["Sempre a da classe declarada na variável", "Sempre a primeira da hierarquia", "A implementação escolhida aleatoriamente"], "O despacho dinâmico escolhe a implementação sobrescrita pela classe real do objeto."),
        ("dificil", "Como é resolvido o acesso a um campo ocultado por uma subclasse?", "Pelo tipo declarado da referência usada no acesso", ["Pela classe real do objeto, como métodos sobrescritos", "Pelo modificador `final`", "Campos não podem ser ocultados"], "Campos não usam despacho dinâmico; o tipo da referência determina qual declaração é acessada."),
    ],
    "interfaces-e-enums": [
        ("facil", "Qual palavra-chave uma classe usa para implementar uma interface?", "`implements`", ["`extends`", "`permits`", "`exports`"], "Uma classe implementa uma ou mais interfaces com implements."),
        ("medio", "Uma classe implementa duas interfaces com o mesmo método `default`. O que deve fazer?", "Sobrescrever o método para resolver o conflito", ["Ignorar ambos os métodos", "Declarar a classe como enum", "O compilador escolhe a primeira interface"], "A classe deve fornecer uma implementação explícita para resolver o conflito entre defaults."),
        ("dificil", "O que `MeuEnum.values()` devolve?", "Um array com as constantes do enum na ordem declarada", ["Um Set ordenado por ordinal", "A constante de ordinal zero", "Um Map de nomes e valores"], "values() é um método gerado para enum que retorna as constantes em sua ordem de declaração."),
    ],
    "records-sealed-e-pattern-matching": [
        ("facil", "Para que um `record` é usado principalmente?", "Representar um conjunto conciso de componentes de dados", ["Criar uma thread", "Abrir um pacote para reflexão", "Substituir todos os arrays"], "Records são apropriados para modelar dados e geram componentes, acessores e métodos usuais."),
        ("medio", "Um record pode estender uma classe definida pelo usuário?", "Não; records estendem `java.lang.Record` e são implicitamente finais", ["Sim, qualquer classe", "Sim, se declarar `sealed`", "Somente se não tiver componentes"], "Records não podem estender outra classe e não podem ser herdados."),
        ("dificil", "Que modificador deve ter uma subclasse direta permitida de uma classe `sealed`?", "`final`, `sealed` ou `non-sealed`", ["Obrigatoriamente `abstract`", "Obrigatoriamente `public`", "Nenhum desses modificadores é permitido"], "Cada subtipo direto permitido precisa encerrar, restringir ou reabrir a hierarquia explicitamente."),
    ],
    "hierarquia-e-tipos-de-excecao": [
        ("facil", "Qual classe é a raiz comum de erros e exceções em Java?", "`Throwable`", ["`ObjectException`", "`RuntimeException`", "`Error`"], "Error e Exception são subclasses de Throwable."),
        ("medio", "O que se exige normalmente para uma exceção checked?", "Capturá-la ou declará-la com `throws`", ["Convertê-la sempre em `Error`", "Ignorá-la porque o compilador a captura", "Declarar `throws` somente em `main`"], "O compilador exige que exceções checked sejam tratadas ou declaradas."),
        ("dificil", "Por que um `catch (Exception e)` antes de `catch (IOException e)` não compila?", "O catch de IOException fica inalcançável após capturar Exception", ["IOException não é uma exceção", "Exception é uma subclasse de IOException", "Um método pode ter apenas um catch"], "O catch mais abrangente captura IOException; o bloco específico posterior torna-se inalcançável."),
    ],
    "try-catch-finally-e-multicatch": [
        ("facil", "Qual bloco trata uma exceção lançada no `try`?", "`catch`", ["`finally`", "`throws`", "`yield`"], "O bloco catch trata exceções compatíveis lançadas pelo bloco try."),
        ("medio", "Qual afirmação sobre `finally` é correta?", "Em fluxo normal de conclusão do try/catch, finally é executado", ["Só executa se houver exceção", "Executa antes do try", "Nunca executa se houver return"], "finally executa ao sair do try/catch em fluxos normais; terminação abrupta da JVM é uma exceção."),
        ("dificil", "No multi-catch `catch (IOException | Exception e)`, qual é o problema?", "Os tipos têm relação de subtipo; alternativas do multi-catch não podem se sobrepor assim", ["Multi-catch aceita apenas tipos primitivos", "O operador correto é `&&`", "Exception precisa vir primeiro"], "As alternativas de multi-catch não podem ter relação de subtipo entre si."),
    ],
    "try-with-resources": [
        ("facil", "Qual interface permite fechamento automático em try-with-resources?", "`AutoCloseable`", ["`Runnable`", "`Serializable`", "`Comparable`"], "Recursos precisam implementar AutoCloseable, diretamente ou por meio de Closeable."),
        ("medio", "Em que ordem dois recursos declarados no mesmo try são fechados?", "Na ordem inversa à declaração", ["Na mesma ordem da declaração", "Em ordem alfabética", "Não são fechados automaticamente"], "Os recursos são fechados na ordem inversa à que foram abertos/declarados."),
        ("dificil", "Se a operação no try e o fechamento do recurso falham, como a falha do fechamento é registrada?", "Como exceção suprimida da falha principal", ["Substitui sempre a falha principal", "É descartada sem possibilidade de consulta", "É convertida em Error"], "A exceção principal é preservada; falhas de close ficam acessíveis por getSuppressed()."),
    ],
    "arrays": [
        ("facil", "Qual propriedade informa o tamanho de um array `a`?", "`a.length`", ["`a.size()`", "`a.length()`", "`a.count`"], "Arrays têm o campo length; coleções, em geral, usam size()."),
        ("medio", "Qual é o índice do primeiro elemento de um array?", "0", ["1", "-1", "Depende do tipo"], "Os índices de arrays Java começam em zero."),
        ("dificil", "O que pode ocorrer ao armazenar um `Integer` em um `Number[]` que na verdade referencia um `Double[]`?", "`ArrayStoreException` durante a execução", ["Sempre compila e armazena normalmente", "`ClassCastException` durante a compilação", "O array cresce automaticamente"], "Arrays são covariantes, mas verificam o tipo real do array em runtime ao armazenar valores."),
    ],
    "generics": [
        ("facil", "O que `List<String>` informa?", "A lista é tipada para elementos String", ["A lista só pode ter um elemento", "A lista é imutável", "A lista converte automaticamente números em texto"], "O parâmetro de tipo restringe os elementos aceitos e define o tipo lido."),
        ("medio", "É possível atribuir diretamente um `List<Integer>` a uma variável `List<Number>`?", "Não; tipos genéricos são invariantes", ["Sim, porque Integer estende Number", "Sim, mas somente com `var`", "Não; List não pode guardar números"], "Mesmo com Integer sendo subtipo de Number, List<Integer> não é subtipo de List<Number>."),
        ("dificil", "Em `List<? extends Number> valores`, qual inserção é segura em geral?", "`null`", ["Um `Integer`", "Um `Double`", "Qualquer `Number`"], "O tipo específico da lista é desconhecido; null é aceito, mas não se pode inserir um Number específico com segurança."),
    ],
    "interfaces-e-colecoes": [
        ("facil", "Qual interface representa uma coleção que não mantém elementos duplicados?", "`Set`", ["`List`", "`Queue`", "`Map`"], "Set modela uma coleção sem duplicatas segundo seu critério de igualdade/ordenação."),
        ("medio", "Qual regra deve ser verdadeira para objetos usados em chaves de hash?", "Se `equals` retorna true, `hashCode` deve ser igual", ["`hashCode` deve sempre ser zero", "`equals` deve comparar referências", "O hash deve mudar a cada consulta"], "O contrato exige hashes iguais para objetos iguais; isso permite localizar buckets corretamente."),
        ("dificil", "Uma lista criada por `List.of(\"A\")` pode receber `add(\"B\")`?", "Não; a lista retornada é não modificável", ["Sim, sempre", "Sim, se o item não existir", "Só depois de chamar `sort`"], "As fábricas List.of/Set.of/Map.of retornam coleções não modificáveis."),
    ],
    "comparacao-e-ordenacao": [
        ("facil", "O que `compareTo` de `Comparable` define?", "Uma ordem natural para objetos do tipo", ["A igualdade por referência", "A ordem de criação de threads", "A conversão para String"], "Comparable permite que a própria classe defina sua ordem natural."),
        ("medio", "O que `compare(a, b) == 0` significa para `TreeSet`?", "Os elementos são equivalentes segundo a ordenação e não ficam ambos no conjunto", ["Os elementos são necessariamente a mesma referência", "O conjunto aceita ambos sempre", "O comparador lançou uma exceção"], "TreeSet usa o resultado da ordenação para determinar duplicatas."),
        ("dificil", "Qual é o requisito para `Arrays.binarySearch` funcionar corretamente?", "O array deve estar ordenado segundo a mesma ordem da busca", ["O array deve conter apenas objetos", "O array deve ser reverso", "A busca só funciona em arrays vazios"], "Busca binária pressupõe dados ordenados de acordo com a ordem usada pela busca."),
    ],
    "interfaces-funcionais-lambdas-e-referencias": [
        ("facil", "Quantos métodos abstratos uma interface funcional tem?", "Um", ["Nenhum", "Dois", "Um método para cada lambda"], "Ela possui um único método abstrato, embora possa ter outros métodos default ou static."),
        ("medio", "Uma lambda pode reatribuir uma variável local capturada?", "Não; a variável deve ser final ou efetivamente final", ["Sim, sempre", "Somente se for `static`", "Somente quando a lambda tem bloco"], "Variáveis locais capturadas não podem ser reatribuídas depois de capturadas."),
        ("dificil", "O que determina se uma method reference é compatível com um destino?", "O tipo funcional esperado e as assinaturas dos parâmetros e retorno", ["Somente o nome do método", "O nome do arquivo Java", "A ordem alfabética das classes"], "A method reference é validada pelo contexto funcional e pela compatibilidade de assinatura."),
    ],
    "streams-e-pipelines": [
        ("facil", "Qual operação normalmente inicia a execução de um pipeline de stream?", "Uma operação terminal", ["`filter`", "`map`", "`peek`"], "Operações intermediárias são lazy; uma operação terminal dispara a avaliação."),
        ("medio", "Quantas vezes um mesmo stream pode ser consumido por operações terminais?", "Uma vez", ["Ilimitadas", "Duas vezes", "Uma vez por elemento"], "Após consumo, um stream não pode ser reutilizado; crie outro a partir da fonte."),
        ("dificil", "Qual é a diferença entre `map` e `flatMap`?", "`map` transforma cada elemento; `flatMap` transforma e achata streams/estruturas resultantes", ["`map` ordena e `flatMap` filtra", "`map` é terminal e `flatMap` é intermediária", "Não há diferença"], "flatMap evita pipelines aninhados ao achatar os resultados de cada transformação."),
    ],
    "collectors-e-optional": [
        ("facil", "Qual collector agrupa elementos por uma chave?", "`Collectors.groupingBy`", ["`Collectors.joining`", "`Optional.empty`", "`Stream.sorted`"], "groupingBy classifica elementos em grupos conforme a função de chave."),
        ("medio", "Qual diferença existe entre `orElse` e `orElseGet`?", "`orElse` avalia o argumento; `orElseGet` chama o supplier apenas se vazio", ["`orElseGet` sempre lança exceção", "`orElse` só aceita lambdas", "São idênticos em avaliação"], "orElse recebe um valor já avaliado; orElseGet posterga a obtenção do valor alternativo."),
        ("dificil", "O que ocorre em `Collectors.toMap` se duas entradas gerarem a mesma chave e não houver função de merge?", "A coleta lança `IllegalStateException`", ["A segunda entrada sempre substitui a primeira", "A coleta cria uma lista automaticamente", "O mapa aceita chaves duplicadas"], "Sem função de merge, chaves duplicadas causam IllegalStateException."),
    ],
    "sistema-de-modulos-jpms": [
        ("facil", "Qual arquivo declara um módulo Java?", "`module-info.java`", ["`package-info.class`", "`pom.xml` obrigatoriamente", "`MANIFEST.JAR`"], "O descritor do módulo é escrito em module-info.java."),
        ("medio", "O que a diretiva `requires` declara?", "Uma dependência de módulo", ["Um pacote aberto para reflexão", "Um método de serviço", "Um arquivo de configuração"], "requires declara que o módulo depende de outro módulo."),
        ("dificil", "Qual é a diferença entre `exports` e `opens`?", "`exports` disponibiliza tipos públicos do pacote; `opens` permite acesso reflexivo profundo", ["`exports` fecha o pacote; `opens` compila módulos", "Ambas são sinônimos", "`opens` declara dependências"], "Exportar expõe API pública; abrir concede acesso reflexivo conforme as regras do JPMS."),
    ],
    "threads-e-executors": [
        ("facil", "Qual chamada inicia uma nova thread?", "`start()`", ["`run()` diretamente", "`sleep()`", "`join()`"], "start inicia uma thread independente e então executa seu método run."),
        ("medio", "O que `ExecutorService.submit(Callable<T>)` devolve?", "Um `Future<T>`", ["Um `Thread` já encerrado", "Um `Stream<T>`", "Um `Optional<T>`"], "Future permite acompanhar conclusão, cancelar e obter o resultado de uma tarefa."),
        ("dificil", "O que `shutdown()` faz em um ExecutorService?", "Recusa novas tarefas e permite que as já submetidas terminem", ["Interrompe imediatamente todas as tarefas", "Espera indefinidamente sem iniciar encerramento", "Reinicia o executor"], "shutdown inicia encerramento ordenado; tarefas submetidas podem concluir."),
    ],
    "sincronizacao-e-visibilidade": [
        ("facil", "Qual palavra-chave pode garantir visibilidade de uma variável compartilhada entre threads?", "`volatile`", ["`transient`", "`native`", "`strictfp`"], "volatile estabelece garantias de visibilidade e ordenação para leituras e escritas."),
        ("medio", "`volatile int contador; contador++;` é uma operação atômica?", "Não; incremento combina leitura, soma e escrita", ["Sim, qualquer operação com volatile é atômica", "Sim, mas apenas em uma thread", "Não compila"], "volatile não transforma uma sequência de leitura-modificação-escrita em operação atômica."),
        ("dificil", "Por que uma chamada a `wait()` costuma ficar dentro de um laço que verifica uma condição?", "A thread deve verificar novamente a condição ao acordar, inclusive por wakeups espúrios", ["Porque wait executa o corpo do laço", "Para impedir que outras threads notifiquem", "Porque wait só aceita laços infinitos"], "Ao acordar, a condição pode ainda não ser verdadeira; por isso, deve ser testada novamente sob o monitor."),
    ],
    "apis-concorrentes-e-colecoes": [
        ("facil", "Qual classe oferece operações atômicas para um contador inteiro?", "`AtomicInteger`", ["`StringBuilder`", "`ArrayList`", "`LocalDate`"], "AtomicInteger fornece operações atômicas como incrementAndGet."),
        ("medio", "Qual método de ConcurrentHashMap pode calcular e inserir um valor ausente em uma única operação por chave?", "`computeIfAbsent`", ["`get` seguido de `put`", "`size`", "`toString`"], "computeIfAbsent combina a verificação e cálculo do valor ausente para a chave."),
        ("dificil", "Uma coleção sincronizada garante que qualquer sequência de várias operações seja atômica?", "Não; a sequência precisa de sincronização externa ou de uma operação composta apropriada", ["Sim, sem exceções", "Sim, se for percorrida com for-each", "Não; coleções não podem ser sincronizadas"], "A sincronização de chamadas individuais não torna automaticamente uma sequência composta indivisível."),
    ],
    "streams-readers-e-writers": [
        ("facil", "Qual abstração é apropriada para ler texto como caracteres?", "`Reader`", ["`InputStream` apenas", "`Object`", "`Path`"], "Reader e Writer trabalham com caracteres; InputStream e OutputStream trabalham com bytes."),
        ("medio", "Que tipo de dado é melhor copiado com streams de bytes?", "Uma imagem", ["Uma frase decodificada", "Uma data localizada", "Um nome de classe"], "Dados binários, como imagens, devem ser tratados como bytes."),
        ("dificil", "Por que especificar um charset ao ler texto de arquivo?", "Para decodificar bytes de forma previsível, sem depender do charset padrão da máquina", ["Para comprimir o arquivo", "Para tornar o arquivo imutável", "Para evitar usar close"], "A codificação define a relação entre bytes e caracteres; explicitar o charset evita diferenças de ambiente."),
    ],
    "nio2-path-e-files": [
        ("facil", "O que um objeto `Path` representa?", "Um caminho de arquivo ou diretório", ["O conteúdo inteiro do arquivo", "Uma conexão de rede", "Um fluxo de caracteres"], "Path representa um caminho; não implica que o arquivo exista."),
        ("medio", "Criar um `Path` confirma que o arquivo existe?", "Não; verifique separadamente com Files", ["Sim, sempre", "Sim, mas apenas para caminhos relativos", "Não; Path só representa diretórios"], "Path é uma representação. Files.exists ou a própria operação de arquivo verifica o estado no sistema."),
        ("dificil", "O que deve ser feito com o stream devolvido por `Files.lines(path)`?", "Fechá-lo, por exemplo, com try-with-resources", ["Nada; ele fecha sempre após a primeira linha", "Convertê-lo em array antes de ler", "Chamar `shutdown()`"], "Files.lines devolve um stream associado a recurso de I/O, que deve ser fechado."),
    ],
    "serializacao": [
        ("facil", "Qual interface de marcação é usada na serialização padrão de objetos?", "`Serializable`", ["`AutoCloseable`", "`Runnable`", "`Comparable`"], "Serializable marca classes cujas instâncias podem participar da serialização padrão."),
        ("medio", "Um campo `transient` participa da serialização padrão?", "Não", ["Sim, sempre", "Somente quando é static", "Somente se for public"], "transient exclui o campo da serialização padrão."),
        ("dificil", "Por que não se deve desserializar dados de origem não confiável sem proteção?", "O processo pode construir grafos de objetos perigosos e acionar comportamentos inesperados", ["Porque Serializable não funciona em rede", "Porque a desserialização sempre apaga arquivos", "Porque ObjectInputStream só aceita primitivos"], "Desserialização de dados não confiáveis pode permitir ataques por objetos e gadgets; é preciso evitar ou filtrar entradas."),
    ],
    "conexoes-e-comandos": [
        ("facil", "Qual interface representa uma conexão JDBC?", "`Connection`", ["`ResultSet`", "`Locale`", "`ExecutorService`"], "Connection representa uma sessão/conexão com a fonte de dados JDBC."),
        ("medio", "A partir de que número começam os índices dos parâmetros de `PreparedStatement`?", "1", ["0", "-1", "O índice é o nome do parâmetro"], "Parâmetros posicionais JDBC começam no índice 1."),
        ("dificil", "Qual método executa uma consulta SQL que retorna um único ResultSet?", "`executeQuery()`", ["`executeUpdate()`", "`commit()`", "`closeQuery()`"], "executeQuery é usado para comandos que produzem um ResultSet, normalmente consultas."),
    ],
    "resultset-recursos-e-transacoes": [
        ("facil", "O que `ResultSet.next()` faz?", "Avança o cursor e informa se há uma linha", ["Fecha a conexão", "Confirma a transação", "Ordena as linhas"], "next move o cursor para a próxima linha e retorna false quando não há mais linhas."),
        ("medio", "Onde começa o cursor de um ResultSet recém-criado?", "Antes da primeira linha", ["Na primeira linha", "Depois da última linha", "Na linha de cabeçalho"], "É necessário chamar next() antes de ler a primeira linha."),
        ("dificil", "Com auto-commit desativado, qual chamada confirma as alterações da transação?", "`Connection.commit()`", ["`ResultSet.next()`", "`Statement.close()`", "`Connection.rollback()`"], "commit confirma a transação; rollback desfaz as alterações ainda não confirmadas."),
    ],
    "locale-e-bundles": [
        ("facil", "O que `Locale` representa?", "Uma configuração de idioma e, opcionalmente, região", ["Um fuso horário", "Uma conexão JDBC", "Um tipo numérico"], "Locale identifica convenções linguísticas/regionais, não um fuso horário."),
        ("medio", "Para que serve `ResourceBundle`?", "Carregar recursos localizados, como textos em arquivos de propriedades", ["Executar SQL", "Ordenar threads", "Serializar objetos"], "ResourceBundle seleciona conteúdo apropriado a uma configuração regional."),
        ("dificil", "O que ocorre se faltar um bundle para um locale específico?", "A busca pode recorrer a locales mais gerais e ao bundle base", ["A aplicação sempre encerra imediatamente", "O Java inventa a tradução", "O bundle base é ignorado"], "A resolução de ResourceBundle segue uma busca por candidatos mais gerais e pelo bundle base."),
    ],
    "formatacao-e-parsing": [
        ("facil", "Qual classe pode formatar números de acordo com um Locale?", "`NumberFormat`", ["`Thread`", "`Path`", "`ObjectInputStream`"], "NumberFormat fornece formatação e parsing numéricos localizados."),
        ("medio", "Por que é útil informar um `Locale` explicitamente ao formatar valores?", "Para que a saída não dependa das configurações regionais da máquina", ["Para impedir arredondamento", "Para converter a data em UTC", "Para fechar o formatter"], "Um locale explícito torna separadores e símbolos previsíveis entre ambientes."),
        ("dificil", "Qual afirmação sobre `DateTimeFormatter` é correta?", "É imutável e thread-safe", ["É mutável e não pode ser compartilhado", "Só formata datas em inglês", "Substitui `LocalDate`"], "DateTimeFormatter é imutável e thread-safe e pode ser compartilhado."),
    ],
}
