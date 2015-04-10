import socket
import sys
import re
import datetime
import select
import win32api
import win32con


class twitch_IRC:
    def __init__(self, username, key, buffer_size=2048):
        self.speed = 0
        self.HOST = 'irc.twitch.tv'
        self.PORT = 6667
        self.USER = username
        self.NICK = username
        self.IDENT = username
        self.REALNAME = username
        self.CHANNEL = '#' + username
        self.KEY = key
        self.BUFFER_SIZE = buffer_size
        self.start_time = datetime.datetime.now()
        err = self.connect()
        
        if err:
            print(err)
            exit(1)
        print('SUCCESSFULLY CONNECTED')

    def recv(self):
        return self.s.recv(self.BUFFER_SIZE).decode()

    def send(self, m):
        self.s.send(m.encode())


    def connect(self):
        print('START CONNECTING')
        self.s = socket.socket()
        try:
            self.s.connect((self.HOST, self.PORT))
        except:
            print('CONNECTION ERROR')
            return 'Econnect'
        print('OAUTH')
        self.s.settimeout(0.5)
        self.s.send(('PASS %s\r\n' % self.KEY).encode())
        self.s.send(('NICK %s\r\n' % self.NICK).encode())
        self.s.send(("USER %s %s bla :%s\r\n" % (self.IDENT, self.HOST, self.REALNAME)).encode())
        self.s.send(('JOIN %s\r\n' % self.CHANNEL).encode())
        tmp = self.recv()
        if tmp == ':tmi.twitch.tv NOTICE * :Login unsuccessful\r\n':
            return 'EAuth'
        print('OAUTH pass')
        return None

    def convert(self, m):
        m = m.split('\r\n')
        ret = []
        cmd = []
        for line in m:
            if line.find('PING') != -1:
                self.send('PONG %s\r\n' % line.split()[1])
            else:
                if line.find('PRIVMSG') != -1:
                    r = re.search(':(.*)!(.*)@(.*)\sPRIVMSG #(.*)\s:(.*)', line)
                    if r.group(5).find('\\') != -1 and r.group(5)[0] == '\\':
                        cmd.append(r.group(5)[1:].split())
                        continue
                    ret.append({'user': r.group(1),
                        'time': datetime.datetime.now(),
                        'past_time': datetime.datetime.now() - self.start_time,
                        'mode': self.CmdHandler.name,
                        'message': r.group(5)})
                
        return (ret, cmd)
        
    def command(self, cmd):
        for c in cmd:
            try:
                if c[0].lower() == 'change':
                    if c[1].lower() == 'mode':
                        if c[2].lower() == 'normal':
                            self.CmdHandler = self.CmdHandlerList[0]
                            print('change to normal')
                        elif c[2].lower() == 'democracy':
                            self.CmdHandler = self.CmdHandlerList[1]
                            self.CmdHandler.set_time_delta(int(c[3]))
                            print('change to democracy')
                        elif c[2].lower() == 'violence':
                            self.CmdHandler = self.CmdHandlerList[2]
                            self.CmdHandler.set_time_delta(int(c[3]))
                            print('change to violence')
                        elif c[2].lower() == 'reverse':
                            self.CmdHandler = self.CmdHandlerList[3]
                            print('change to Reverse')

                elif c[0].lower() == 'exit':
                    print('service close')
                    return 'exit'
                elif c[0].lower() == 'speed':
                    if self.speed == 0:
                        win32api.keybd_event(0x20, 0, 0, 0)
                        self.speed = 1;
                    else:
                        win32api.keybd_event(0x20,0 , win32con.KEYEVENTF_KEYUP, 0)
                        self.speed = 0
                
                    print('speed up')
            except:
                print('command error')
        return None
                    

    def run(self, CmdHandlerList, LogHandler, ParserHandler):
        self.CmdHandlerList = CmdHandlerList
        self.CmdHandler = self.CmdHandlerList[0]
        while True:
            try:
                message = self.recv()
                message, cmd = self.convert(message)
                LogHandler.log(message)
                if self.command(cmd) == 'exit':
                    return
                for m in message:
                    m['cmd'] = ParserHandler.parser(m['message'])
                    #print('parse:' + str(m['cmd']))
                self.CmdHandler.execute(message)
            except:
                self.CmdHandler.execute([])
                pass

