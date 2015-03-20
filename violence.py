import datetime
class ViolenceHandler:
    def __init__(self, ExecuteHandler, delta):
        self.ExecuteHandler = ExecuteHandler
        self.last_time = datetime.datetime.now()
        self.time_delta = datetime.timedelta(seconds=delta)
        self.count = {'up': 0,
                    'down': 0,
                    'left': 0,
                    'right': 0,
                    'a': 0,
                    'b': 0,
                    'select': 0,
                    'start': 0,
                    'x': 0,
                    'y': 0,
                    'l': 0,
                    'r': 0}

    def set_time_delta(self, delta):
        self.time_delta = datetime.timedelta(seconds=delta)
        
    def clear_count(self):
        for i in self.count.keys():
            self.count[i] = 0

    def execute(self, message):
        for m in message:
            for c in self.count.keys():
                if m['cmd'].count(c) == len(m['cmd']):
                    self.count[c] = max(self.count[c], len(m['cmd']))
                    break
        print(datetime.datetime.now() - self.last_time , self.time_delta)
        if datetime.datetime.now() - self.last_time >= self.time_delta:
            self._execute()
            self.clear_count()
            self.last_time = datetime.datetime.now()

    def _execute(self):
        cmd = max(self.count.keys(), key=lambda x: self.count[x])
        print('test: '+cmd+str(self.count[cmd]))
        if self.count[cmd] == 0:
            return
        print(cmd)
        self.ExecuteHandler.send([cmd])
