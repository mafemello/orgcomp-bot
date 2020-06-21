class Teorias():
    def __init__(self):
        self.messages_teoria_introducao = [
            {
                'type': 'text',
                'content': '''
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
                    Principais componentes do computador são: 
                        - CPU = unidade de controle + unidade lógica e aritmética
                        - E/S = comunicação com mundo exterior (inserção de dados e instruções)
                        - memória principal = fornece instruções e operandos para execução e armazena resultados fora da CPU

                '''
            }
        ]