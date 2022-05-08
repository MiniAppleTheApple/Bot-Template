import json

def jload(file, mode='r', *args, **kwargs):
    file = file if file[-5:] == '.json' else file + '.json'
    with open(file, mode, *args, **kwargs) as file:
        return json.load(file)