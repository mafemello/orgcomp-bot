import sys
import time
import telepot
from telepot.loop import MessageLoop
from users import all_users, create_user
bot = telepot.Bot("1238253599:AAHyxXSRoMxDL9cmBOFzW4jarOG3RJVPTTo")


def get_help(user_id):
    help_msg = '''
    Bem vindo ao @orgcomp_bot \n Comandos Disponíveis: 
    /help : Menu de comandos
    /teoria: Estude a teoria de Orgcomp
    /quizz: Teste seus conhecimentos
    '''
    bot.sendMessage(user_id, help_msg)

def start_user(user_id):
    was_user_created = create_user(all_users, user_id)
    bot.sendMessage(user_id, was_user_created)
    if was_user_created:
        bot.sendMessage(user_id, 'Criei seu usuario viu')
        bot.sendMessage(user_id, all_users)
    else:
        bot.sendMessage(user_id, 'Usuario ja existia')
    
def get_teoria_help(user_id):
    teoria_help_msg = '''
    Teorias disponíveis:
    /teoria_assembly
    /teoria_datapass
    /teoria_cache
    '''
    bot.sendMessage(user_id, teoria_help_msg)

def get_quizz_help(user_id):
    quizz_help_msg = '''
    Quizzes disponíveis:
    /quizz_assembly
    /quizz_datapass
    /quizz_cache
    '''
    bot.sendMessage(user_id, quizz_help_msg)


COMANDOS = {
    '/start': start_user,
    '/help': get_help,
    '/teoria': get_teoria_help,
    '/quizz': get_quizz_help
}

def recebe_msg(msg):
    content_type, chat_type, user_id = telepot.glance(msg)
    text = str.lower(msg['text'])
    if text in COMANDOS:
        COMANDOS[text](user_id)


bot.message_loop(recebe_msg)

while True:
    pass
