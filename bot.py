import sys
import time
import telepot
from telepot.loop import MessageLoop
from commands import Commands
from settings import bot_key
bot = telepot.Bot(bot_key)

bot_commands = Commands(bot).COMANDOS

def recebe_msg(msg):
    content_type, chat_type, user_id = telepot.glance(msg)
    comando = msg['text']
    if comando in bot_commands:
        print(bot_commands[comando]['method'](user_id))

bot.message_loop(recebe_msg)

while True:
    pass
