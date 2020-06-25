from components.users import Users
from components.commands import Commands
from components.teorias import Teorias
from components.quizzes import Quizzes
import telepot


class Bot(Commands, Users, Teorias, Quizzes):
    def __init__(self, bot_key):
        self.BOT = telepot.Bot(bot_key)
        Users.__init__(self)
        Teorias.__init__(self)
        Commands.__init__(self)
        Quizzes.__init__(self)

    def help(self, user_id):
        self.print_command_list(self.HELP_MENU, user_id)

    def start_user(self, user_id):
        self.create_user(user_id)
        self.help(user_id)

    def teoria_help(self, user_id):
        self.print_command_list(self.TEORIA_MENU, user_id)

    def quizz_help(self, user_id):
        self.print_command_list(self.QUIZZ_MENU, user_id)

    def gustavinho(self, user_id):
        gustavinho = 'https://avatars0.githubusercontent.com/u/37300626?s=64&v=4'
        self.BOT.sendPhoto(user_id, gustavinho)

    def print_command_list(self, command_list, user_id):
        msg = '------------------------------------ \n'
        for comando in command_list:
            msg += f'{comando}: {command_list[comando]["description"]}\n'
        msg += '------------------------------------ \n'
        self.BOT.sendMessage(user_id, msg)

    def teoria_introducao(self, user_id):
        self.handle_and_send_messages(user_id, self.messages_teoria_introducao)

    def teoria_instrucao(self, user_id):
        self.handle_and_send_messages(user_id, self.messages_teoria_instrucao)

    def teoria_assembly(self, user_id):
        self.handle_and_send_messages(user_id, self.messages_teoria_assembly)

    def handle_and_send_messages(self, user_id, messages):
        for message in messages:
            if message['type'] == 'text':
                self.BOT.sendMessage(user_id, message['content'])
            elif message['type'] == 'img':
                self.BOT.sendPhoto(user_id, message['content'])

    def start_quizz_introducao(self, user_id):
        quizz = self.QUIZZES.get('quizz_introducao')
        self.start_quizz(user_id, quizz)
    
    def start_quizz_instrucao(self, user_id):
        quizz = self.QUIZZES.get('quizz_instrucao')
        self.start_quizz(user_id, quizz)
    
    def start_quizz_assembly(self, user_id):
        self.start_quizz(user_id, 'quizz_assembly')

    def start_quizz(self, user_id, new_quizz):
        quizz = self.QUIZZES.get('f{new_quizz}')
        print(quizz)
        user = self.all_users.get(f'{user_id}')
        if not user:
            no_user_error_msg = (
                'Você ainda não está cadastrado(a)! Utilize o comando /start para se cadastrar e poder utilizar o quizz.'
            )
            self.BOT.sendMessage(user_id, no_user_error_msg)
            return

        current_user_quizz = user.get('current_quizz')
        if current_user_quizz:
            on_quizz_error_msg = f'Você já está no {current_quizz}! Termine-o antes de tentar outro.'
            self.BOT.sendMessage(user_id, on_quizz_error_msg)

        else:
            user['current_user_quizz'] = new_quizz.keys()
            start_quizz_msg = f'bem vindo ao {new_quizz}!'
            self.BOT.sendMessage(user_id, start_quizz_msg)

            self.print_command_list(self.QUIZZ_MENU, user_id)

    def answer_quizz(self, choice, user_id):
        user = self.all_users[f'{user_id}']

        current_quizz = user.get('current_quizz')
        quizz_state = user.get('quizz_state')
