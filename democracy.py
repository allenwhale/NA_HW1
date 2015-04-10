import datetime
import time
class DemocracyHandler:
    MAP = {
        'numpad_8': 'up',
        'numpad_2': 'down',
        'numpad_6': 'right',
        'numpad_4': 'left',
        'enter': 'start',
        'backspace': 'select',
        'z': 'a',
        'x': 'b'}
    MAP2 = {
        'up': 'numpad_8',
        'down': 'numpad_2',
        'right': 'numpad_6',
        'left': 'numpad_4',
        'start': 'enter',
        'select': 'backspace',
        'a': 'z',
        'b': 'x'
    }
    def __init__(self, ExecuteHandler, delta):
        self.ExecuteHandler = ExecuteHandler
        self.last_time = datetime.datetime.now()
        self.time_delta = datetime.timedelta(seconds=delta)
        self.name = 'Democracy'
        self.count = {'up': 0,
                    'down': 0,
                    'left': 0,
                    'right': 0,
                    'a': 0,
                    'b': 0,
                    'select': 0,
                    'start': 0}

    def set_time_delta(self, delta):
        self.time_delta = datetime.timedelta(seconds=delta)
    
    def clear_count(self):
        for i in self.count.keys():
            self.count[i] = 0

    def execute(self, message):
        for m in message:
            for c in m['cmd']:
                #print('lala '+c)
                self.count[self.MAP[c]] += 1
        if datetime.datetime.now() - self.last_time >= self.time_delta:
            self.last_time = datetime.datetime.now()
            _max = self.count[max(self.count.keys(),key=lambda x: self.count[x])]
            #print('_max '+str(_max))
            #print([self.count[i]==_max for i in self.count].count(True))
            if [self.count[i]==_max for i in self.count].count(True) > 1:
                @print(time.time())
                print('----------------')
                print("vote: ")
                for i in self.count:
                    if self.count[i] != _max:
                        self.count[i] = -999999
                    else:
                        print(i)
                print('----------------')
                return
            self._execute()
            self.clear_count()

    def _execute(self):
        cmd = max(self.count.keys(), key=lambda x: self.count[x])
        if self.count[cmd] == 0:
            return
        self.ExecuteHandler.send([self.MAP2[cmd]])
