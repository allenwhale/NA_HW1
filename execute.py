import datetime
from log import LogHandler
class ExecuteHandler:
    MAP = {
    'numpad_8': 'up',
    'numpad_2': 'down',
    'numpad_6': 'right',
    'numpad_4': 'left',
    'enter': 'start',
    'backspace': 'select',
    'z': 'a',
    'x': 'b'}
    def __init__(self, KeyboardHandler, delta=10):
        self.KeyboardHandler = KeyboardHandler
        self.count = {'up': 0, 'down': 0, 'right': 0, 'left': 0, 'start': 0, 'select': 0, 'a': 0, 'b': 0}
        self.last_time = datetime.datetime.now()
        self.time_delta = datetime.timedelta(seconds=delta)
        self.LogHandler = LogHandler()

    def send(self, cmd):
        #print('cmd '+str(cmd))
        for c in cmd:
            #print('exe: '+str(c))
            self.count[self.MAP[c]] += 1
        self.KeyboardHandler.send(cmd)
        if datetime.datetime.now() - self.last_time >= self.time_delta:
            self.last_time = datetime.datetime.now()
            self.LogHandler.log_count(self.count)
            
