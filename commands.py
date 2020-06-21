class Commands():
    def __init__(self): 
        self.HELP_MENU = {
                '/start': {
                    'method': self.start_user,
                    'description': 'Inicia o bot e Comandos Disponíveis'
                },
                '/help': {
                    'method': self.help,
                    'description': 'Comandos Disponíveis'
                },
                '/teoria': {
                    'method': self.teoria_help,
                    'description': 'Aprenda a teoria!'
                },
                '/quizz': {
                    'method': self.quizz_help,
                    'description': 'Teste seus conhecimentos!'
                },
                '/gustavinho': {
                    'method': self.gustavinho,
                    'description': 'Manda foto do gustavinho'
                }
            }

        self.TEORIA_MENU = {
            '/teoria_introducao': {
                    'method': self.teoria_introducao,
                    'description': 'Aprenda a matéria introdutória'
                },
            '/teoria_ciclo_instrucao': {
                    'method': self.teoria_instrucao,
                    'description': 'Aprenda sobre ciclos de instrução'
                },
            '/teoria_assembly': {
                    'method': self.teoria_assembly,
                    'description': 'Aprenda sobre assembly'
                }
        }

        self.QUIZZ_MENU = {
            '/quizz_introducao': {
                    'method': self.quizz_introducao,
                    'description': 'Inicia o quizz de introdução'
                },
            '/quizz_ciclo_instrucao': {
                    'method': self.quizz_instrucao,
                    'description': 'Inicia o quizz sobre ciclos de instrução'
                },
            '/quizz_assembly': {
                    'method': self.quizz_assembly,
                    'description': 'Inicia o quizz sobre assembly'
                }
        }

        self.MENU = self.HELP_MENU.copy()
        self.MENU.update(self.TEORIA_MENU)
        self.MENU.update(self.QUIZZ_MENU)