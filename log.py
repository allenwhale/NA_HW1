class LogHandler:
    def __init__(self, filename='log'):
        self.FILENAME = filename

    def log(self, message):
        f = open(self.FILENAME, 'a+')
        for m in message:
            f.write('%s %s %s %s %s\n' % (m['time'], m['past_time'], m['user'], m['mode'], m['message']))
        f.close()
    
    def log_cmd(self, message):
        f = open(self.FILENAME, 'a+')
        for m in message:
            f.write(m['user']+'\n')
            for c in m['cmd']:
                f.write(c+' ')
            f.write('\n')
        f.close()
        
    def log_count(self, count):
        f = open(self.FILENAME, 'a+')
        f.write('--------------------------\n')
        for c in count:
            f.write('%s: %d\n'% (c, count[c]))
        f.write('--------------------------\n')
        f.close()

