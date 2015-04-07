class NormalHandler:
    def __init__(self, ExecuteHandler):
        self.ExecuteHandler = ExecuteHandler
        self.name = 'Normal'

    def execute(self, message):
        cmd = []
        for m in message:
            cmd += m['cmd']
        self._execute([cmd])
        print(cmd)

    def _execute(self, cmd):
        for c in cmd:
            self.ExecuteHandler.send(c)

