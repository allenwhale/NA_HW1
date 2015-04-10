
class NormalHandler:
    MAP = {
        'numpad_8': 'up',
        'numpad_2': 'down',
        'numpad_6': 'right',
        'numpad_4': 'left',
        'enter': 'start',
        'backspace': 'select',
        'z': 'a',
        'x': 'b'}
    def __init__(self, ExecuteHandler):
        self.ExecuteHandler = ExecuteHandler
        self.name = 'Normal'

    def execute(self, message):
        cmd = []
        for m in message:
            cmd += m['cmd']
            #print('mmmm '+str(m['cmd']))      
            tmp = m['cmd']
            output = ''
            for t in tmp:
                output += self.MAP[t] + ' '
            f = open('log', 'a+')
            f.write('%s execute %s in %s mode\n'% (m['user'], output, m['mode']))
            f.close()
            #print('for: '+str(m['cmd']))
        #print('eee '+str(cmd))
        self._execute([cmd])

    def _execute(self, cmd):
        for c in cmd:
            #print('_execute '+str(c))
            self.ExecuteHandler.send(c)

