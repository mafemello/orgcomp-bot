class Teorias():
    def __init__(self):
        self.messages_teoria_introducao = [
            {
                'type': 'text',
                'content':
'''
    O sistema computacional pode ser entendido pelo conjunto de Hardware e Software usado como ferramenta na solução de problemas. O hardware diz respeito aos objetos tangíveis, a parte física de um computador, as peças que o compõem. O monitor, impressora e o mouse são exemplos de hardware. O software diz respeito aos objetos não tangíveis, são os programas que fazem com que a máquina funcione, como os aplicativos e sistemas operacionais.
    Os limites entre eles não são claros e foram modificados conforme as tendências atuais. Eles são logicamente equivalentes.
    Arquitetura é o conjunto de atributos visíveis ao programador, como o conjunto de instruções, número de bits, mecanismos de entrada e saída, modos de endereçamento…. Já a organização diz respeito a como esses atributos são implementados, como os sinais de controle, interfaces e tecnologia de memória.
    Para estudar o computador, é preciso ter em mente o sistema hierárquico proposto por Tanenbaum na figura a seguir. As camadas superiores escondem detalhes das camadas inferiores.
'''
            },
            {
                'type': 'img',
                'content': 'https://slideplayer.com.br/slide/1260662/3/images/7/2-Organiza%C3%A7%C3%A3o+estruturada+de+computadores+%282%29.jpg'
            },
            {
                'type': 'text',
                'content': 'O compilador traduz uma linguagem de alto nível para um programa equivalente em linguagem de máquina ou Assembly. Essa execução segue o seguinte esquema:'
            },
            {
                'type': 'img',
                'content': 'https://imgur.com/a/rzEwCN2'
            },
            {
                'type': 'text',
                'content': 
'''
Três pontos importantes para o seu estudo: dados e instruções são representados na memória; a memória é endereçada pela posição e não pelo conteúdo; e a execução das instruções é sequencial! 
Os principais componentes do computador são: 
    - CPU = unidade de controle + unidade lógica e aritmética
    - E/S = comunicação com mundo exterior (inserção de dados e instruções)
    - memória principal = fornece instruções e operandos para execução e armazena resultados fora da CPU

'''
            }
        ]

        self.messages_teoria_instrucao = [
            {
                'type': 'text',
                'content': 
'''
    O ciclo de instrução é dividido em duas partes: ciclo de busca e ciclo de execução.
    No ciclo de busca o contator de programas (PC) guarda o endereço da próxima instrução a ser executada (lembrando que as instruções são executadas sequencialmente, exceto quando temos instruções de desvio). Ele funciona como um ponteiro para a próxima instrução.
    O processador faz a busca da instrução na posição de memória armazenado no PC. Daí o MAR (registrador de endereçamento de memória) recebe o conteúdo de PC, ou seja, contém o endereço de uma posição de memória, e o MBR (registrador de armazenamento temporário de dados) guarda os dados que estão no endereço de MAR, ou seja, uma palavra de dados a ser escrita na memória.
    Depois disso, o PC é incrementado: PC = PC + 1 (a não ser que exista instrução de desvio). A instrução é armazenada no registrador de instrução (IR = MBR). 
    No ciclo de execução, a Unidade de Controle decodifica a instrução e determina os sinais de controle para projetar as ações necessárias. A execução de instrução se resume às seguintes possibilidades:
    Processador-Memória: transferência de dados do processador para a memória ou da memória
    para o processador
        - Processador-E/S: transferência de dados entre o processador e um dispositivo de E/S
        - Processamento de dados: execução de operações aritméticas ou lógicas sobre os dados
        - Controle: especifica que a sequência de execução de instruções seja alterada
        - Combinação dessas 4 possibilidades
'''
            },
            {
                'type': 'img',
                'content': 'https://i.imgur.com/4Vyghs6.png'
            },
        ]

        self.messages_teoria_assembly = [
            {
                'type': 'text',
                'content': 
'''
    Assembly é uma linguagem de montagem, ou seja, é a representação simbólica da codificação binária / linguagem de máquina.
    Assembler é o programa montador que transforma o código escrito na linguagem Assembly em codificação binária / linguagem de máquina.

    As vantagens do Assembly podem ser catalogadas com as seguintes características: velocidade; controle da execução pelo, construção de partes de Sistemas Operacionais (SO). 
    As desvantagens do Assembly podem ser listadas em: programas gerados para arquiteturas (máquinas) específicas; dificuldade de ler e compreender o código (dar manutenção e corrigir bugs).

    Assembly MIPS ⇒ linguagem baseada na arquitetura MIPS, cuja construção é de 32 bits, contendo registradores de propósito geral e ponto flutuante, todos referenciados por $.
    Características da linguagem:
    Rótulos ⇒ Identificam uma linha no código para referência. Úteis para desvios condicionais, estruturas condicionais e de repetição, desvios incondicionais, chamadas a procedimentos. 
    Diretivas do Montador ⇒ Determinam configurações ao código sempre precedidas por ponto. (exemplo: .data, .main, etc).
    Syscall ⇒ chamada do sistema. Mecanismo programático pelo qual um programa de computador solicita um serviço do núcleo do sistema operacional sobre o qual ele está sendo executado.
    Serviços do sistema ⇒ a combinação de registrador com um determinado código pode executar tarefas quando existe a chamada do sistema. 
    Exemplo (li $v0, 10 	   #carrega o valor 10 (exit) em $v0
        syscall	   #executa a syscall para finalizar (exit) o programa).

    Existem 3 formatos de instrução: Tipo R, Tipo I e Tipo J. Todas as instruções possuem 32 bits de tamanho.

'''
            },
            {
                'type': 'img',
                'content': 'https://i.imgur.com/kiUtpRC.png'
            },
        ]