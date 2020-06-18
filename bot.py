import sys
import time
import telepot
from telepot.loop import MessageLoop
from commands import Commands
from settings import bot_key
bot = telepot.Bot(bot_key)

commands = Commands(bot)

def recebe_msg(msg):
    content_type, chat_type, user_id = telepot.glance(msg)
    text = msg['text']
    if text in commands.COMANDOS:
        commands.COMANDOS[text](user_id)

bot.message_loop(recebe_msg)

while True:
    pass
