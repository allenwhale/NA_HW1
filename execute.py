class ExecuteHandler:
    def __init__(self, KeyboardHandler):
        self.KeyboardHandler = KeyboardHandler
        self.count = {}

    def send(self, cmd):
        self.KeyboardHandler.send(cmd)
