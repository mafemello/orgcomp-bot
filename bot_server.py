import sys
import time
import telepot
from telepot.loop import MessageLoop
from bot import Bot
from settings import bot_key

bot = Bot(bot_key)

def handle_msg(msg):
    content_type, chat_type, user_id = telepot.glance(msg)
    comando = msg['text']
    if comando in bot.MENU:
        print(bot.MENU[comando]['method'](user_id))

bot.BOT.message_loop(handle_msg)

while True:
    pass
