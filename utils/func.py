import json
from discord import Intents

def jload(file, mode='r', *args, **kwargs):
    file = file if file[-5:] == '.json' else file + '.json'
    with open(file, mode, *args, **kwargs) as file:
        return json.load(file)

def getIntents(items):
    _map = {'all': Intents.all(), 'default': Intents.default(), 'none': Intents.none()}
    intents = _map.get(items[0])
    if len(items) == 1:
        return intents
    _dict = intents.__dict__
    for i in items:
        _dict[i] = True
    return intents