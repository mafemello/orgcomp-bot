from users import Users
class Commands(Users):
    def __init__(self, bot):
        self.bot = bot
        self.COMANDOS = {
            '/start': {
                'method': self.start_user,
                'description': 'Inicia o bot e Comandos Disponíveis'
            },
            '/help': {
                'method': self.get_help,
                'description': 'Comandos Disponíveis'
            },
            '/teoria': { 
                'method': self.get_teoria_help,
                'description': 'Aprenda a teoria!'
            },
            '/quizz': {
                'method': self.get_quizz_help,
                'description': 'Teste seus conhecimentos!'
            },
            '/gustavinho': {
                'method': self.send_gustavinho,
                'description': 'Manda foto do gustavinho'
            }
        }
        Users.__init__(self)

        self.playlist = ('https://www.youtube.com/watch?v=HgA-oXOV7kI&list=PLxI8Can9yAHdG-xUDj6i-HGB7IAsAU-t1')

    def get_help(self,user_id):
        msg = '------------- \n*Comandos Disponíveis:* \n'
        for comando in self.COMANDOS:
            msg  += f'{comando}: {self.COMANDOS[comando]["description"]}\n'
        msg += '------------- \n'
        self.bot.sendMessage(user_id,msg, parse_mode= 'Markdown')

    def start_user(self, user_id):
        was_user_created = self.create_user(user_id)
        self.get_help(user_id)

    def get_teoria_help(self, user_id):
        teoria_help_msg = '''
        Teorias disponíveis:
        /teoria_assembly
        /teoria_datapass
        /teoria_cache
        '''
        self.bot.sendMessage(user_id, teoria_help_msg)

    def get_quizz_help(self, user_id):
        quizz_help_msg = '''
        Quizzes disponíveis:
        /quizz_assembly
        /quizz_datapass
        /quizz_cache
        '''
        self.bot.sendMessage(user_id, quizz_help_msg)

    def send_gustavinho(self, user_id):
        gustavinho = 'https://avatars0.githubusercontent.com/u/37300626?s=64&v=4'
        self.bot.sendPhoto(user_id,gustavinho)

    