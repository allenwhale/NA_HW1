class ParserHandler:
    AVAILABLE = ['up',
                'down',
                'right',
                'left',
                'a',
                'b',
                'start',
                'select']
    MAP = {
        'up': 'numpad_8',
        'down': 'numpad_2',
        'right': 'numpad_6',
        'left': 'numpad_4',
        'start': 'enter',
        'select': 'backspace',
        'a': 'z',
        'b': 'x'
    }
    def __init__(self):
        pass

    def parser(self, message):
        ret = []
        while len(message) > 0:
            found = False
            for a in self.AVAILABLE:
                if message.find(a) == 0:
                    ret.append(self.MAP[a])
                    message = message[len(a):]
                    found = True
            if not found:
                message = message[1:]
        return ret
