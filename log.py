class LogHandler:
    def __init__(self, filename='log'):
        self.FILENAME = filename

    def log(self, message):
        f = open(self.FILENAME, 'a+')
        for m in message:
            f.write('%s %s %s\n' % (m['time'], m['user'], m['message']))
        f.close()

