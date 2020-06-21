from users import Users
from commands import Commands
import telepot

class Bot(Commands, Users):
    def __init__(self, bot_key):
        self.BOT = telepot.Bot(bot_key)
        Users.__init__(self)
        Commands.__init__(self)
        
    def help(self,user_id):
        self.print_command_list(self.HELP_MENU, user_id)

    def start_user(self, user_id):
        self.create_user(user_id)
        self.help(user_id)

    def teoria_help(self, user_id):
        self.print_command_list(self.TEORIA_MENU, user_id)

    def quizz_help(self, user_id):
        self.print_command_list(self.QUIZZ_MENU,user_id)

    def gustavinho(self, user_id):
        gustavinho = 'https://avatars0.githubusercontent.com/u/37300626?s=64&v=4'
        self.BOT.sendPhoto(user_id,gustavinho)

    def print_command_list(self, command_list, user_id):
        msg = '------------------------------------ \n'
        for comando in command_list:
            msg  += f'{comando}: {command_list[comando]["description"]}\n'
        msg += '------------------------------------ \n'
        self.BOT.sendMessage(user_id,msg)

    def teoria_introducao(user_id):
        self.BOT.sendMessage(user_id,'teoria introdução')
    
    def teoria_instrucao(self,user_id):
        self.BOT.sendMessage(user_id,'teoria instrução')

    def teoria_assembly(self,user_id):
        self.BOT.sendMessage(user_id,'teoria assembly')
    
    def quizz_introducao(self, user_id):
        self.BOT.sendMessage(user_id,'quizz introdução')
    
    def quizz_instrucao(self, user_id):
        self.BOT.sendMessage(user_id,'quizz instrução')

    def quizz_assembly(self, user_id):
        self.BOT.sendMessage(user_id,'quizz assembly')