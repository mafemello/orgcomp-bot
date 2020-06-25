class Quizzes():
	def __init__(self):
		self.QUIZZES = {
			'quizz_introducao': [{
				'question': '''
			1. Quais destas descrevem uma das funções da CPU? Escreva apenas a, b, c ou d.
			I) buscar instruções da memória
			II) examinar ou decodificar a instrução
			III) executar a instrução
				a) todas estão certas
				b) apenas a II e a III estão certas
				c) apenas a I e III estão certas
				d) todas estão erradas
			''',
				'answer': "/a"
			}, {
				'question': '''
			Qual ou quais são as ações básicas que a unidade de controle executa?
			a) busca
			b) decodificação
			c) execução
			d) todas as anteriores.

			''',
				'answer': "/b"
			}],
			'quizz_instrucao': [{
				'question': '''
			1. Qual a principal diferença entre organização e arquitetura de um computador?
			a) não há diferença prática.
			b) organização é o conjunto de atributos visíveis ao programador e a arquitetura diz respeito a como estes são implementados.
			c) A arquitetura se refere a atributos que têm impactos diretos sobre a execução lógica de um programa. A organização refere-se às unidades operacionais e suas interconexões.
			d) Os limites entre eles não são claros pois são logicamente equivalentes.
			''',
				'answer': "/c"
			}, {
				'question': '''
			2. Qual a principal diferença entre organização e arquitetura de um computador?
			a) O software diz respeito aos objetos tangíveis, a parte física de um computador, as peças que o compõem. O hardware são os programas que fazem com que a máquina funcione, como os aplicativos e sistemas operacionais.
			b) não há diferença prática.
			c) O software se refere a atributos que têm impactos diretos sobre a execução lógica de um programa. O hardware refere-se às unidades operacionais e suas interconexões.
			d) O hardware diz respeito aos objetos tangíveis, a parte física de um computador, as peças que o compõem. O software são os programas que fazem com que a máquina funcione, como os aplicativos e sistemas operacionais.
			''',
				'answer': "/d"
			}],
			'quizz_assembly': [{
				'question': '''
			1. Escreva V para verdadeiro e F para falso a respeito da seguinte afirmação:
			As instruções abaixo são para empilhar e desempilhar uma informação:
			push: 	addi $sp, $sp, -4
					sw $t4, 0($sp)
			pop:	lw $t4, 0($sp)
					addi $sp, $sp, 4
			''',
				'answer': "/v"
			}, {
				'question': '''
			2. Escreva V para verdadeiro e F para falso a respeito da seguinte afirmação: (R: V).
			As instruções abaixo são para copiar uma string
			strcpy:
				addi $sp, $sp, -8
				sw $a0, 0($sp)
				sw $a1, 4($sp)
			loop:
				lb $s1, 0($a0)
				sb $s1, 0($a1)
				
				addi $a1, $a1, 1
				addi $a0, $a0, 1

				bne $s1, $zero, loop

				lw $a0, 0($sp)
				lw $a1, 4($sp)
				addi $sp, $sp, 8

				jr $ra
			''',
				'answer': "/v"
			}]
		}
