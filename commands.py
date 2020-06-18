from users import Users
class Commands(Users):
    def __init__(self, bot):
        self.bot = bot
        self.COMANDOS = {
        '/start': self.start_user,
        '/help': self.get_help,
        '/teoria': self.get_teoria_help,
        '/quizz': self.get_quizz_help
        }
        Users.__init__(self)

        self.playlist = ('https://www.youtube.com/watch?v=HgA-oXOV7kI&list=PLxI8Can9yAHdG-xUDj6i-HGB7IAsAU-t1')

    def get_help(self,user_id):
        help_msg = '''
        Bem vindo ao @orgcomp_bot \n Comandos Disponíveis: 
        /help : Menu de comandos
        /teoria: Estude a teoria de Orgcomp
        /quizz: Teste seus conhecimentos
        '''
        self.bot.sendMessage(user_id, help_msg)

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


    