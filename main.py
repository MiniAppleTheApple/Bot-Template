import os

from discord import Intents
from discord.ext import commands

import utils.func as utils

config = utils.jload(file='./config', mode='r', encoding='utf8')

def getIntents(items):
    _map = {'all': Intents.all(), 'default': Intents.default(), 'none': Intents.none()}
    intents = _map.get(items[0])
    if len(items) == 1:
        return intents
    _dict = intents.__dict__
    for i in items:
        _dict[i] = True
    return intents

bot = commands.Bot(
    command_prefix = config['commands.prefix'],
    Intents = getIntents(config['commands.intents'])
    )

@bot.event
async def on_ready():
    print('> Bot is Ready')
    for filename in os.listdir('./cogs'):
        if filename[-3:] == '.py':
            bot.load_extension(f'cogs.{filename}')

bot.run(utils.jload(file='./token'))