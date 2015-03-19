class ParserHandler:
    AVAILABLE = ['up',
                'down',
                'right',
                'left',
                'a',
                'b',
                'start',
                'select']
    def __init__(self):
        pass

    def parser(self, message):
        ret = []
        while len(message) > 0:
            found = False
            for a in self.AVAILABLE:
                if message.find(a) == 0:
                    ret.append(a)
                    message = message[len(a):]
                    fount = True
            if not found:
                message = message[1:]
        return ret
