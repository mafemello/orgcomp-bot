import sys
import time
import telepot
from telepot.loop import MessageLoop
from bot import Bot
from settings import bot_key

bot = Bot(bot_key)

def handle_msg(msg):
    content_type, chat_type, user_id = telepot.glance(msg)
    user = bot.all_users[f'{user_id}']
    comando = msg['text']

    if user['current_quizz'] is not None and comando in bot.ANSWER_QUIZZ_MENU:
        answer = comando
        bot.answer_quizz(answer)

    elif comando in bot.MENU:
        bot.MENU[comando]['method'](user_id)

bot.BOT.message_loop(handle_msg)

while True:
    pass
